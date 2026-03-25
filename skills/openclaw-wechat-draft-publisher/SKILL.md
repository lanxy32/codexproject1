---
name: openclaw-wechat-draft-publisher
description: End-to-end AI article writing + WeChat Official Account draft publication. Generate viral-style articles with professional新媒体运营 best practices and publish directly to WeChat draft box.
---

# OpenClaw WeChat Draft Publisher

End-to-end workflow: **AI Article Generation (Viral Style) → Format Validation → Publish to WeChat Official Account Draft → Push to GitHub**.

Professional viral article writing follows 10-year experienced新媒体运营 best practices.

## Workflow Overview

Complete process from topic to published draft:

```
Topic Input → AI Viral Article Generation → Format Validation (Title + Content) → Publish to WeChat Draft → Push to GitHub
```

## Required Inputs

Collect these inputs from the user before starting:

1. `appid` and `appsecret` for the target Official Account.
2. Article requirements:
   - Topic/core viewpoint/brief copy from user
   - Author name (for the article)
3. Cover source:
   - Existing `thumb_media_id`, or
   - Local image file to upload as permanent image material.
4. Confirmation that the execution host outbound IP is added to WeChat backend API whitelist.

## Article Writing Best Practices

### System Prompt (Viral WeChat Article Generation)

```
你是一位拥有10年经验的资深新媒体运营官及爆款文案专家，深谙微信公众号的传播逻辑、用户心理及算法推荐机制。你擅长将复杂的行业知识转化为通俗易懂、具有高度传播力的深度干货文章，风格既专业又极具吸引力，能够引发读者强烈共鸣和转发欲望。

#Task（任务）：
根据用户提供的[选题/核心观点/简要文案]，撰写一篇完整的微信公众号文章。
你需要产出：
1. 5个极具点击欲望的"爆款标题"（包含情绪价值、悬念或利益点）。
2. 一篇结构完整、逻辑严密且干货满满的正文。

#Goal（目标）：
1. 吸引用户点击（高打开率）。
2. 提供实质性价值，确保读者读完有获得感（高完读率）。
3. 激发用户的情绪共鸣或收藏欲望，促使文章在朋友圈进行二次传播（高分享率）。

#Objective（操作要求）：
1. 【标题要求】：提供5个不同维度的标题供选择（如：痛点型、悬念型、反常识型、利益型、故事型），每个标题不超过25字。
2. 【正文结构】：
采用"金字塔原理"展开，分3-4个小标题，每个部分必须有理论/观点 + 案例/故事 + 具体可执行的方法论（干货），拒绝空洞说教。结尾：总结核心价值，金句升华，并设计一个强互动的结尾（如提问或行动呼吁）。文章总字数不低于1000字
3. 在不了解选题的具体方向的时候，优先联网收集资料后创作
```

## Complete Workflow

### Step 1: Article Generation (Viral Style)

1. Use the professional prompt above to generate article
2. Output includes: 5 different title options, one complete article
3. Let user confirm which title to use

### Step 2: Format Validation (Before Publishing)

**Mandatory check before pushing to WeChat:**

- [ ] **Title check**: Selected title ≤ 25 characters
- [ ] **Title check**: Contains emotion, suspense, or clear benefit
- [ ] **Structure check**: 3-4 clear subheadings (H2)
- [ ] **Content check**: Each section has: theory/viewpoint + case/story + actionable methodology
- [ ] **Word count**: ≥ 1000 words
- [ ] **Ending check**: Has summary + golden sentence + interactive CTA
- [ ] **Markdown format**: Correct heading levels (`#` `##`), proper spacing

Fix any issues found before proceeding.

### Step 3: Publish to WeChat Draft

1. Export credentials as environment variables:
   - `WECHAT_APPID`
   - `WECHAT_APPSECRET`
2. Save confirmed article as Markdown file in `generated_articles/`
3. Prepare cover:
   - Use `--thumb-media-id` if already in WeChat material library
   - Or use `--thumb-image` to upload local image
4. Run publish script
5. Validate output: get `media_id` and confirm success
6. If API returns `40164` (whitelist error), stop and guide user to whitelist host IP

### Step 4: Push to GitHub (Recommended for Version Control)

After publishing, push the generated article source files to GitHub:
```bash
git add generated_articles/*.md
git commit -m "Add new article: {selected-title}"
git push
```

## Command Patterns

### End-to-End Example (AI Generation + Validation + Publish + GitHub Push)

```bash
# 1. Set credentials
export WECHAT_APPID=your_appid
export WECHAT_APPSECRET=your_appsecret

# 2. AI generates article with viral prompt (5 titles + 1 full article)
# User selects title, content is saved to generated_articles/your-article.md

# 3. Format validation check (manual inspection required)
# ✅ Title ≤ 25 chars ✅ 3-4 subheadings ✅ Each section: theory + case + method
# ✅ Word count ≥ 1000 ✅ Ending has summary + golden sentence + CTA

# 4. Publish from Markdown to WeChat draft
python scripts/publish_wechat_draft.py \
  --content-file generated_articles/your-article.md \
  --content-format markdown \
  --title "Selected Title Here" \
  --author "Your Author Name" \
  --thumb-image path/to/cover.jpg

# 5. Push to GitHub for version control
git add generated_articles/your-article.md
git commit -m "Add new article: Selected Title Here"
git push
```

### 1) Publish from Markdown (Standalone)

```bash
export WECHAT_APPID=your_appid
export WECHAT_APPSECRET=your_appsecret
python scripts/publish_wechat_draft.py \
  --content-file generated_articles/article.md \
  --content-format markdown \
  --title "OpenClaw Article Title" \
  --author "OpenClaw" \
  --thumb-image path/to/cover.jpg
```

### 2) Publish from WeChat-style JSON

```bash
python scripts/publish_wechat_draft.py \
  --article-json payload.json \
  --thumb-media-id your_existing_media_id
```

### 3) Validate payload locally without API calls

```bash
python scripts/publish_wechat_draft.py \
  --content-file generated_articles/article.md \
  --content-format markdown \
  --title "Dry Run Sample" \
  --thumb-media-id REPLACE_ME \
  --dry-run
```

## Article Management

After publishing, it's recommended to manage all articles in a Feishu Bitable with these fields:

| Field Name | Feishu Field Type | Description |
|------------|-------------------|-------------|
| **Article Title** | Single Text | Final selected title |
| **5 Candidate Titles** | Multi-line Text | All 5 candidate titles |
| **WeChat Draft ID** | Single Text | media_id from publish response |
| **Publish URL** | Link | Published article URL |
| **Created Date** | Date | Generation date |
| **Author** | Single Text | Article author |
| **Topic/Keyword** | Single Text | Core topic |
| **Status** | Single Select | Draft / Published |

## Failure Handling Rules

1. Interpret WeChat API `errcode` from script output.
2. Handle `40164` as IP whitelist issue first, before retrying credentials.
3. Handle `40001`/`40125` as invalid app credential issues.
4. Handle `41001` as missing required API field.
5. Avoid blind retries; fix root cause then retry once.

## Security Rules

1. Keep `appsecret` only in environment variables or secret manager.
2. Never commit credentials, access tokens, or raw API responses containing sensitive values.
3. Rotate `appsecret` immediately if exposed.
4. Avoid printing full secrets in logs or terminal screenshots.

## Pre-Publish Validation Checklist

Always go through this checklist before publishing:

- [ ] 标题是否在25字以内？
- [ ] 5个标题是否覆盖不同维度（痛点/悬念/反常识/利益/故事）？
- [ ] 正文是否分为3-4个小标题？
- [ ] 每个部分是否都有：理论观点 + 案例故事 + 可执行方法？
- [ ] 字数是否≥1000字？
- [ ] 结尾是否包含：总结核心价值 + 金句升华 + 互动提问/行动呼吁？
- [ ] Markdown格式是否正确（标题层级、空行分隔）？
- [ ] 是否没有过度营销和绝对化用语？

Only publish after ALL checks pass.

## Resources

- `scripts/publish_wechat_draft.py`: end-to-end draft publish script.
- `references/wechat-mp-draft-api.md`: endpoint and troubleshooting notes.
