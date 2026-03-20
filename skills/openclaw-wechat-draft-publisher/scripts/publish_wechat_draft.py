#!/usr/bin/env python3
"""Publish articles to WeChat Official Account draft box."""

from __future__ import annotations

import argparse
import html
import json
import mimetypes
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path
from typing import Any

BASE_URL = "https://api.weixin.qq.com"


class WechatApiError(RuntimeError):
    """Represents a non-zero errcode response from WeChat API."""

    def __init__(self, endpoint: str, errcode: int, errmsg: str):
        super().__init__(f"WeChat API error at {endpoint}: {errcode} - {errmsg}")
        self.endpoint = endpoint
        self.errcode = errcode
        self.errmsg = errmsg


def _http_json(
    url: str,
    method: str = "GET",
    payload: dict[str, Any] | None = None,
    timeout: int = 30,
    headers: dict[str, str] | None = None,
) -> dict[str, Any]:
    data = None
    request_headers = {
        "User-Agent": "openclaw-wechat-draft-publisher/1.0",
    }

    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        request_headers["Content-Type"] = "application/json; charset=utf-8"

    if headers:
        request_headers.update(headers)

    req = urllib.request.Request(
        url=url, data=data, headers=request_headers, method=method.upper()
    )

    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code} for {url}: {body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Network error for {url}: {exc}") from exc

    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Non-JSON response from {url}: {raw}") from exc


def _http_upload_file(
    url: str, field_name: str, file_path: Path, timeout: int = 30
) -> dict[str, Any]:
    boundary = f"----OpenClawBoundary{uuid.uuid4().hex}"
    mime_type = mimetypes.guess_type(file_path.name)[0] or "application/octet-stream"
    file_bytes = file_path.read_bytes()

    body = b"".join(
        [
            f"--{boundary}\r\n".encode("utf-8"),
            (
                f'Content-Disposition: form-data; name="{field_name}"; '
                f'filename="{file_path.name}"\r\n'
            ).encode("utf-8"),
            f"Content-Type: {mime_type}\r\n\r\n".encode("utf-8"),
            file_bytes,
            b"\r\n",
            f"--{boundary}--\r\n".encode("utf-8"),
        ]
    )

    headers = {
        "User-Agent": "openclaw-wechat-draft-publisher/1.0",
        "Content-Type": f"multipart/form-data; boundary={boundary}",
    }
    req = urllib.request.Request(url=url, data=body, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code} for {url}: {body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Network error for {url}: {exc}") from exc

    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Non-JSON response from {url}: {raw}") from exc


def _raise_if_api_error(endpoint: str, data: dict[str, Any]) -> dict[str, Any]:
    errcode = data.get("errcode")
    if errcode in (None, 0):
        return data
    errmsg = str(data.get("errmsg", "unknown error"))
    raise WechatApiError(endpoint, int(errcode), errmsg)


def _strip_yaml_front_matter(text: str) -> str:
    if not text.startswith("---"):
        return text

    match = re.match(r"^---\s*\n.*?\n---\s*\n", text, flags=re.DOTALL)
    if match:
        return text[match.end() :]
    return text


def _normalize_markdown_for_wechat(markdown_text: str) -> str:
    normalized_lines: list[str] = []
    for line in markdown_text.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        normalized_line = re.sub(r"^\s*•\s+", "- ", line)
        normalized_lines.append(normalized_line)
    return "\n".join(normalized_lines)


def _derive_title_from_markdown(markdown_text: str) -> str | None:
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            title = stripped.lstrip("#").strip()
            if title:
                return title
    return None


def _remove_first_markdown_heading(markdown_text: str) -> str:
    lines = markdown_text.splitlines()
    for idx, line in enumerate(lines):
        if line.strip().startswith("#"):
            return "\n".join(lines[:idx] + lines[idx + 1 :]).strip()
    return markdown_text


def _markdown_to_html(markdown_text: str) -> str:
    try:
        import markdown as md  # type: ignore

        return md.markdown(markdown_text, extensions=["extra", "sane_lists"])
    except Exception:
        paragraphs = re.split(r"\n\s*\n", markdown_text.strip())
        html_paragraphs: list[str] = []
        for para in paragraphs:
            text = para.strip()
            if not text:
                continue
            if text.startswith("#"):
                heading = re.match(r"^(#{1,6})\s+(.+)$", text)
                if heading:
                    level = len(heading.group(1))
                    content = html.escape(heading.group(2).strip())
                    html_paragraphs.append(f"<h{level}>{content}</h{level}>")
                    continue
            clean = html.escape(text).replace("\n", "<br/>")
            html_paragraphs.append(f"<p>{clean}</p>")
        return "\n".join(html_paragraphs)


def _plain_text_from_html(value: str) -> str:
    no_tags = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", no_tags).strip()


def _build_digest(content_html: str, max_len: int) -> str:
    text = _plain_text_from_html(content_html)
    return text[:max_len].strip()


def _normalize_article(article: dict[str, Any], fallback_thumb_media_id: str | None) -> dict[str, Any]:
    normalized = dict(article)

    if not normalized.get("thumb_media_id") and fallback_thumb_media_id:
        normalized["thumb_media_id"] = fallback_thumb_media_id

    required = ["title", "content", "thumb_media_id"]
    missing = [name for name in required if not normalized.get(name)]
    if missing:
        raise ValueError(f"Article is missing required field(s): {', '.join(missing)}")

    normalized.setdefault("author", "OpenClaw")
    normalized.setdefault("content_source_url", "")
    normalized.setdefault("digest", _build_digest(str(normalized["content"]), 120))
    normalized.setdefault("need_open_comment", 0)
    normalized.setdefault("only_fans_can_comment", 0)
    return normalized


def _load_articles_from_json(path: Path) -> list[dict[str, Any]]:
    obj = json.loads(path.read_text(encoding="utf-8"))

    if isinstance(obj, dict) and isinstance(obj.get("articles"), list):
        return [dict(item) for item in obj["articles"]]
    if isinstance(obj, dict):
        return [dict(obj)]
    if isinstance(obj, list):
        return [dict(item) for item in obj]
    raise ValueError("JSON must be an object, an articles list, or {'articles': [...]} format.")


def _build_article_from_content(args: argparse.Namespace) -> dict[str, Any]:
    content_path = Path(args.content_file)
    if not content_path.exists():
        raise FileNotFoundError(f"Content file not found: {content_path}")

    raw = content_path.read_text(encoding="utf-8")

    if args.content_format == "markdown":
        markdown_text = _normalize_markdown_for_wechat(_strip_yaml_front_matter(raw))
        discovered_title = _derive_title_from_markdown(markdown_text)
        title = args.title or discovered_title
        if not title:
            title = f"OpenClaw Article {time.strftime('%Y-%m-%d %H:%M')}"
        if discovered_title and not args.title:
            markdown_text = _remove_first_markdown_heading(markdown_text)
        content_html = _markdown_to_html(markdown_text)
    else:
        title = args.title or f"OpenClaw Article {time.strftime('%Y-%m-%d %H:%M')}"
        content_html = raw

    digest = args.digest or _build_digest(content_html, args.digest_max_length)
    return {
        "title": title,
        "author": args.author,
        "digest": digest,
        "content": content_html,
        "content_source_url": args.content_source_url,
        "thumb_media_id": args.thumb_media_id,
        "need_open_comment": int(args.need_open_comment),
        "only_fans_can_comment": int(args.only_fans_can_comment),
    }


class WechatDraftPublisher:
    def __init__(self, appid: str, appsecret: str, timeout: int = 30):
        self.appid = appid
        self.appsecret = appsecret
        self.timeout = timeout

    def get_access_token(self) -> str:
        endpoint = "/cgi-bin/token"
        url = (
            f"{BASE_URL}{endpoint}?"
            + urllib.parse.urlencode(
                {
                    "grant_type": "client_credential",
                    "appid": self.appid,
                    "secret": self.appsecret,
                }
            )
        )
        data = _http_json(url, timeout=self.timeout)
        _raise_if_api_error(endpoint, data)
        token = data.get("access_token")
        if not token:
            raise RuntimeError("Missing access_token in token response.")
        return str(token)

    def upload_image_material(self, access_token: str, image_path: Path) -> str:
        endpoint = "/cgi-bin/material/add_material"
        url = (
            f"{BASE_URL}{endpoint}?"
            + urllib.parse.urlencode(
                {"access_token": access_token, "type": "image"}
            )
        )
        data = _http_upload_file(url, "media", image_path, timeout=self.timeout)
        _raise_if_api_error(endpoint, data)
        media_id = data.get("media_id")
        if not media_id:
            raise RuntimeError("Missing media_id in material upload response.")
        return str(media_id)

    def add_draft(self, access_token: str, articles: list[dict[str, Any]]) -> dict[str, Any]:
        endpoint = "/cgi-bin/draft/add"
        url = (
            f"{BASE_URL}{endpoint}?"
            + urllib.parse.urlencode({"access_token": access_token})
        )
        payload = {"articles": articles}
        data = _http_json(
            url,
            method="POST",
            payload=payload,
            timeout=self.timeout,
        )
        _raise_if_api_error(endpoint, data)
        return data


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Publish OpenClaw-generated content to WeChat Official Account drafts."
    )
    parser.add_argument("--appid", help="WeChat Official Account appid")
    parser.add_argument("--appsecret", help="WeChat Official Account appsecret")
    parser.add_argument(
        "--article-json",
        help="Path to article JSON. Supports object/list or {'articles': [...]}",
    )
    parser.add_argument("--content-file", help="Path to markdown/html content file")
    parser.add_argument(
        "--content-format",
        choices=["markdown", "html"],
        default="markdown",
        help="Format of --content-file",
    )
    parser.add_argument("--title", help="Article title (used with --content-file)")
    parser.add_argument("--author", default="OpenClaw", help="Article author")
    parser.add_argument("--digest", help="Article digest/summary")
    parser.add_argument(
        "--digest-max-length",
        type=int,
        default=120,
        help="Digest max length if digest is auto-generated",
    )
    parser.add_argument(
        "--content-source-url", default="", help="Original source URL for article"
    )
    parser.add_argument(
        "--thumb-media-id", help="Existing thumb_media_id in WeChat material library"
    )
    parser.add_argument(
        "--thumb-image",
        help="Image path to upload as permanent material when thumb_media_id is absent",
    )
    parser.add_argument(
        "--need-open-comment",
        type=int,
        choices=[0, 1],
        default=0,
        help="Whether comments are enabled",
    )
    parser.add_argument(
        "--only-fans-can-comment",
        type=int,
        choices=[0, 1],
        default=0,
        help="Whether only followers can comment",
    )
    parser.add_argument("--timeout", type=int, default=30, help="HTTP timeout seconds")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Build and print payload only; skip WeChat API calls",
    )
    return parser.parse_args()


def _validate_inputs(args: argparse.Namespace) -> None:
    if not args.article_json and not args.content_file:
        raise ValueError("Pass either --article-json or --content-file.")

    if args.article_json and args.content_file:
        raise ValueError("Use only one of --article-json or --content-file.")

    if args.thumb_image and not Path(args.thumb_image).exists():
        raise FileNotFoundError(f"Cover image file not found: {args.thumb_image}")

    if not args.dry_run and not args.thumb_media_id and not args.thumb_image:
        raise ValueError(
            "WeChat draft requires thumb_media_id. Pass --thumb-media-id or --thumb-image."
        )


def _build_articles(args: argparse.Namespace) -> list[dict[str, Any]]:
    if args.article_json:
        source_articles = _load_articles_from_json(Path(args.article_json))
    else:
        source_articles = [_build_article_from_content(args)]

    if args.thumb_media_id:
        return [
            _normalize_article(article, fallback_thumb_media_id=args.thumb_media_id)
            for article in source_articles
        ]
    return [dict(article) for article in source_articles]


def _emit_error(err: Exception) -> int:
    if isinstance(err, WechatApiError):
        details = {
            "ok": False,
            "error_type": "wechat_api_error",
            "endpoint": err.endpoint,
            "errcode": err.errcode,
            "errmsg": err.errmsg,
        }
        if err.errcode == 40164:
            details["hint"] = (
                "IP whitelist mismatch. Add this host outbound public IP in "
                "WeChat MP backend: Development -> Basic Configuration -> IP whitelist."
            )
        elif err.errcode in (40001, 40125):
            details["hint"] = "Invalid appid/appsecret. Verify credentials and account type."
        elif err.errcode == 41001:
            details["hint"] = "Missing required parameter. Check title/content/thumb_media_id."
        _print_json(details, stream=sys.stderr)
        return 2

    _print_json(
        {
            "ok": False,
            "error_type": err.__class__.__name__,
            "message": str(err),
        },
        stream=sys.stderr,
    )
    return 1


def _print_json(data: dict[str, Any], stream: Any = sys.stdout) -> None:
    try:
        print(json.dumps(data, ensure_ascii=False, indent=2), file=stream)
    except UnicodeEncodeError:
        # Fallback for Windows terminals using legacy encodings.
        print(json.dumps(data, ensure_ascii=True, indent=2), file=stream)


def main() -> int:
    args = parse_args()
    try:
        _validate_inputs(args)

        appid = args.appid or os.getenv("WECHAT_APPID")
        appsecret = args.appsecret or os.getenv("WECHAT_APPSECRET")

        articles = _build_articles(args)

        if args.dry_run:
            _print_json(
                {
                    "ok": True,
                    "dry_run": True,
                    "articles_count": len(articles),
                    "payload": {"articles": articles},
                }
            )
            return 0

        if not appid or not appsecret:
            raise ValueError(
                "Missing app credentials. Pass --appid/--appsecret or set "
                "WECHAT_APPID/WECHAT_APPSECRET."
            )

        publisher = WechatDraftPublisher(
            appid=appid, appsecret=appsecret, timeout=args.timeout
        )
        token = publisher.get_access_token()

        fallback_media_id = args.thumb_media_id
        if not fallback_media_id and args.thumb_image:
            fallback_media_id = publisher.upload_image_material(token, Path(args.thumb_image))
            for article in articles:
                if not article.get("thumb_media_id"):
                    article["thumb_media_id"] = fallback_media_id

        articles = [
            _normalize_article(article, fallback_thumb_media_id=fallback_media_id)
            for article in articles
        ]

        draft_resp = publisher.add_draft(token, articles)
        _print_json(
            {
                "ok": True,
                "media_id": draft_resp.get("media_id"),
                "created_at": draft_resp.get("created_at"),
                "articles_count": len(articles),
                "used_thumb_media_id": fallback_media_id,
            }
        )
        return 0
    except Exception as err:  # noqa: BLE001
        return _emit_error(err)


if __name__ == "__main__":
    raise SystemExit(main())
