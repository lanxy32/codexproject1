# WeChat MP Draft API Notes

## Core Endpoints

1. Get access token  
   `GET /cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET`

2. Upload permanent image material (for `thumb_media_id`)  
   `POST /cgi-bin/material/add_material?access_token=ACCESS_TOKEN&type=image`  
   Multipart form field: `media=@cover.jpg`

3. Add draft  
   `POST /cgi-bin/draft/add?access_token=ACCESS_TOKEN`  
   JSON body:

```json
{
  "articles": [
    {
      "title": "Sample Title",
      "author": "OpenClaw",
      "digest": "Summary",
      "content": "<p>HTML content</p>",
      "content_source_url": "",
      "thumb_media_id": "MEDIA_ID",
      "need_open_comment": 0,
      "only_fans_can_comment": 0
    }
  ]
}
```

## High-Frequency Error Codes

1. `40164`: API call source IP is not in whitelist.
2. `40001`: Invalid credential (token or app credential mismatch).
3. `40125`: Invalid appsecret.
4. `41001`: Missing required parameter.
5. `45009`: API call limit reached.

## IP Whitelist Checklist

1. Open WeChat Official Account backend.
2. Go to `Development -> Basic Configuration`.
3. Add current execution host outbound public IP to API whitelist.
4. Wait for propagation, then retry draft publish.

Tip: If running in cloud or containerized environments, whitelist the NAT egress IP instead of private host IP.

## Security Checklist

1. Keep `appid`/`appsecret` in environment variables or a secret manager.
2. Avoid storing access tokens in source control.
3. Rotate secrets if leaked.
4. Log minimal API response content in production pipelines.
