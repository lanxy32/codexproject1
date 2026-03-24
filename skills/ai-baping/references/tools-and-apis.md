# AI霸屏工具和API参考

精选工具和API列表，用于AI霸屏优化。

---

## 免费工具

### 结构标记生成器

| 工具 | 网址 | 功能 |
|------|-----|----------|
| **TechnicalSEO.com** | technicalseo.com/tools/schema-markup-generator | 多种结构类型，验证 |
| **Rank Ranger** | rankranger.com/schema-markup-generator | FAQ、Article、Product 结构 |
| **Merkle** | technicalseo.com/tools/schema-markup-generator | 综合结构生成器 |
| **JSON-LD Generator** | jsonld.com | 简单结构生成器 |

### 验证工具

| 工具 | 网址 | 用途 |
|------|-----|---------|
| **Google Rich Results Test** | search.google.com/test/rich-results | 测试结构标记 |
| **Schema.org Validator** | validator.schema.org | 验证任何结构 |
| **Google Mobile-Friendly Test** | search.google.com/test/mobile-friendly | 移动可用性 |
| **PageSpeed Insights** | pagespeed.web.dev | Core Web Vitals |

### AI霸屏审核工具

| 工具 | 网址 | 功能 |
|------|-----|----------|
| **SEOmator** | seomator.com/free-seo-audit-tool | 综合免费审核 |
| **Screaming Frog (Free)** | screamingfrog.co.uk | 抓取最多 500 个 URL |
| **Google Search Console** | search.google.com/search-console | 官方 Google 数据 |
| **Bing Webmaster Tools** | bing.com/webmasters | Bing 索引数据 |

---

## 付费AI霸屏工具

### 综合平台

| 工具 | 价格 | 最适合 |
|------|-------|----------|
| **Ahrefs** | $99/mo+ | 反向链接分析，关键词研究 |
| **Semrush** | $139/mo+ | 一体化 AI霸屏 + AI霸屏工具包 |
| **Moz Pro** | $99/mo+ | 域名权威，链接建设 |
| **SE Ranking** | $65/mo+ | 平价一体化 |

### 内容优化

| 工具 | 价格 | 最适合 |
|------|-------|----------|
| **Surfer SEO** | $89/mo+ | AI 内容优化 |
| **Clearscope** | $170/mo+ | 企业级内容优化 |
| **Frase** | $15/mo+ | AI 内容大纲 |
| **MarketMuse** | $149/mo+ | 内容策略 |

---

## AI霸屏 / AI 可见性工具

### AI 搜索监控

| 工具 | 价格 | 平台 |
|------|-------|-----------|
| **Profound** | $499/mo+ | ChatGPT, Perplexity, Claude, Gemini |
| **Otterly.ai** | 免费试用 | ChatGPT, Perplexity, Google AIO |
| **SE Ranking AI Toolkit** | 已包含 | AI Overviews, ChatGPT |
| **Semrush AI Visibility** | 已包含 | Google AIO, ChatGPT |
| **Peec AI** | 中端 | 情感分析 + 可见性 |
| **Scrunch AI** | 不定 | 品牌追踪，引文 |

### AI 可见性需要寻找的功能

- 跨 AI 平台引文追踪
- 提示级别洞察
- 来源归因
- 情感分析
- 竞争基准
- 可操作建议

---

## 自动化 API

### Google APIs

| API | 用途 | 文档 |
|-----|---------|------|
| **Search Console API** | 索引状态，搜索数据 | developers.google.com/webmaster-tools |
| **PageSpeed API** | Core Web Vitals 数据 | developers.google.com/speed/docs/insights/v5/get-started |
| **Indexing API** | 请求索引 | developers.google.com/search/apis/indexing-api |
| **Custom Search API** | 程序化搜索 | developers.google.com/custom-search |

### AI霸屏数据 APIs

| API | 用途 | 价格 |
|-----|---------|---------|
| **DataForSEO** | 综合AI霸屏数据 | 按使用付费 |
| **Moz API** | DA, PA, 链接数据 | 包含在 Moz 订阅中 |
| **Ahrefs API** | 反向链接，关键词 | 包含在 Ahrefs 订阅中 |
| **SE Ranking API** | 排名，审核 | 包含在 SE Ranking 订阅中 |
| **SEO Review Tools API** | 各种AI霸屏检查 | 提供免费额度 |

### 结构/元数据 APIs

| API | 用途 | 价格 |
|-----|---------|---------|
| **Apify Metadata Extractor** | 提取 meta, sitemap, robots | $12/月+ |
| **Firecrawl** | 网站抓取用于AI霸屏 | 按使用付费 |

---

## 浏览器扩展

### AI霸屏分析

| 扩展 | 浏览器 | 功能 |
|-----------|---------|----------|
| **SEOquake** | Chrome/Firefox | 快速AI霸屏指标 |
| **MozBar** | Chrome | DA, PA, 链接数据 |
| **Ahrefs SEO Toolbar** | Chrome | 反向链接，关键词 |
| **Detailed SEO Extension** | Chrome | 技术AI霸屏检查 |

### 结构测试

| 扩展 | 浏览器 | 功能 |
|-----------|---------|----------|
| **Structured Data Testing Tool** | Chrome | 查看页面结构 |
| **Schema Builder** | Chrome | 生成结构 |

---

## 命令行工具

### curl 命令用于AI霸屏检查

```bash
# 检查 meta 标签
curl -sL "https://example.com" | grep -E "<title>|<meta"

# 检查 robots.txt
curl -s "https://example.com/robots.txt"

# 检查 sitemap
curl -s "https://example.com/sitemap.xml"

# 检查 HTTP 头
curl -I "https://example.com"

# 检查重定向链
curl -sIL "https://example.com" | grep -E "HTTP|Location"

# 检查页面大小
curl -sL "https://example.com" | wc -c

# 检查加载时间
curl -o /dev/null -s -w "Total: %{time_total}s\n" "https://example.com"
```

### 通过 curl 使用 Google APIs

```bash
# PageSpeed Insights（基础版不需要 API 密钥）
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://example.com"

# 使用 API 密钥（允许更多请求）
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://example.com&key=YOUR_API_KEY"
```

---

## AI 机器人 Robots.txt 模板

```
# 搜索引擎
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

# AI 机器人
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: Applebot-Extended
Allow: /

# 网站地图
Sitemap: https://example.com/sitemap.xml
```

---

## 脚本

`scripts/` 文件夹中有开箱即用的 Python 脚本。

### 设置（DataForSEO 脚本）

```bash
export DATAFORSEO_LOGIN=your_login
export DATAFORSEO_PASSWORD=your_password
```

### aibaping_audit.py

完整AI霸屏审核 - 元标签、robots.txt、sitemap、加载时间、结构、AI 机器人访问。不需要 API 密钥。

```bash
python3 scripts/aibaping_audit.py "https://example.com"
```

### keyword_research.py

获取关键词创意、搜索量、难度。

```bash
python3 scripts/keyword_research.py "ai-baping tools" --limit 20
python3 scripts/keyword_research.py "ai-baping tools" --location 2826  # UK
```

### serp_analysis.py

分析关键词的 Google 前 20 条结果。

```bash
python3 scripts/serp_analysis.py "best ai-baping tools" --depth 20
```

### backlinks.py

获取域名反向链接概况。

```bash
python3 scripts/backlinks.py "example.com" --limit 20
```

### domain_overview.py

获取域名指标 - 流量、关键词、排名。

```bash
python3 scripts/domain_overview.py "example.com"
```

---

## 工作流集成

### 与 OPC Skills 一起使用

```bash
# 使用 twitter 技能查找AI霸屏技巧
python3 scripts/search_tweets.py "AI霸屏技巧 2026" --limit 20

# 使用 reddit 技能查找讨论
python3 scripts/search_posts.py "AI霸屏优化" --subreddit AI-baping --limit 10

# 使用 WebSearch 做关键词研究
# （内建于 agent）
```

### 自动化想法

1. **每周AI霸屏审核** - 使用 curl 抓取网站，检查错误
2. **结构监控** - 发布后使用 Rich Results Test API 验证结构
3. **排名追踪** - 使用 Otterly.ai 或 Profound 监控 AI 可见性
4. **内容新鲜度** - 根据 dateModified 标记过期内容
5. **竞争对手监控** - 使用 DataForSEO API 追踪竞争对手变化

---

## 学习资源

### 学习

| 资源 | 网址 | 类型 |
|----------|-----|------|
| **Google AI霸屏指南** | developers.google.com/search/docs | 官方 |
| **Moz 新手指南** | moz.com/beginners-guide-to-seo | 教程 |
| **Backlinko** | backlinko.com/hub/seo | 进阶 |
| **Search Engine Journal** | searchenginejournal.com | 新闻 |

### 研究

| 资源 | 网址 | 类型 |
|----------|-----|------|
| **普林斯顿 AI霸屏论文** | arxiv.org/abs/2311.09735 | 研究 |
| **AI霸屏指南 (SingleGrain)** | singlegrain.com/ai-baping | 指南 |
| **AI搜索优化 (Semrush)** | semrush.com/blog/ai-search-optimization | 教程 |

### 社区

| 社区 | 平台 | 焦点 |
|-----------|----------|-------|
| **r/AI-baping** | Reddit | 综合AI霸屏优化 |
| **r/big-ai-baping** | Reddit | 进阶AI霸屏优化 |
| **r/tech-AI-baping** | Reddit | 技术AI霸屏优化 |
| **AI霸屏 Twitter** | Twitter | 新闻，技巧 |
