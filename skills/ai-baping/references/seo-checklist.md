# AI霸屏审核清单

完整清单，用于审核和优化网站，同时适配传统AI霸屏和AI搜索可见性。

## 优先级

| 级别 | 含义 | 操作 |
|-------|---------|--------|
| **P0** | 严重 | 必须立即修复 - 会阻止索引或导致重大问题 |
| **P1** | 重要 | 应尽快修复 - 对排名有显著影响 |
| **P2** | 推荐 | 很好有 - 提升可见性和用户体验 |

---

## 技术AI霸屏

### P0 - 严重

- [ ] **P0** `robots.txt` 允许重要页面
- [ ] **P0** 网站可访问（没有 5xx 错误）
- [ ] **P0** 启用 HTTPS（有效 SSL 证书）
- [ ] **P0** 移动响应设计
- [ ] **P0** 没有重要页面被 `noindex` 阻止
- [ ] **P0** 网站已被 Google 收录（检查：`site:domain.com`）

### P1 - 重要

- [ ] **P1** `robots.txt` 允许 AI 机器人（GPTBot, PerplexityBot, ClaudeBot）
- [ ] **P1** XML 网站地图存在已提交
- [ ] **P1** 网站已被 Bing 收录（用于 Copilot 可见性）
- [ ] **P1** 规范标签正确实现
- [ ] **P1** 没有重复内容问题
- [ ] **P1** 页面加载时间 < 3 秒
- [ ] **P1** 最大内容绘制 (LCP) < 2.5s

### P2 - 推荐

- [ ] **P2** 首次输入延迟 (FID) < 100ms
- [ ] **P2** 累积布局偏移 (CLS) < 0.1
- [ ] **P2** 图片优化（WebP 格式，懒加载）
- [ ] **P2** CSS/JS 压缩
- [ ] **P2** 启用 GZIP/Brotli 压缩
- [ ] **P2** 配置 CDN
- [ ] **P2** 通过移动友好测试
- [ ] **P2** 没有混合内容警告
- [ ] **P2** 配置安全响应头

---

## 页面AI霸屏

### P0 - 严重

- [ ] **P0** 唯一 `<title>` 标签存在（50-60 字符）
- [ ] **P0** 标题包含核心关键词
- [ ] **P0** 唯一 `<meta description>` 存在（150-160 字符）
- [ ] **P0** 每个页面只有一个 H1 标签
- [ ] **P0** H1 包含核心关键词

### P1 - 重要

- [ ] **P1** 描述吸引人且包含关键词
- [ ] **P1** `<meta name="robots">` 正确设置
- [ ] **P1** 逻辑标题层级（H1 > H2 > H3）
- [ ] **P1** 所有图片都有 `alt` 属性
- [ ] **P1** 内部链接到相关内容
- [ ] **P1** 没有 broken 链接（404s）
- [ ] **P1** 锚文本描述清晰

### P2 - 推荐

- [ ] **P2** 设置 `og:title`
- [ ] **P2** 设置 `og:description`
- [ ] **P2** 设置 `og:image`（推荐 1200x630px）
- [ ] **P2** 设置 `og:url`（规范 URL）
- [ ] **P2** 设置 `og:type`（website/article）
- [ ] **P2** 设置 `twitter:card`（summary_large_image）
- [ ] **P2** 设置 `twitter:title`
- [ ] **P2** 设置 `twitter:description`
- [ ] **P2** 设置 `twitter:image`
- [ ] **P2** 段落简短（2-3 句话）
- [ ] **P2** 列表使用项目符号
- [ ] **P2** 对比使用表格
- [ ] **P2** 自然地在 alt 文本包含关键词
- [ ] **P2** 图片文件名描述清晰
- [ ] **P2** 外部链接使用 `rel="noopener noreferrer"`

---

## 结构数据标记（结构化数据）

### P1 - 重要

- [ ] **P1** 主页添加 Organization 结构
- [ ] **P1** 所有页面添加 WebPage 结构
- [ ] **P1** 博客文章添加 Article 结构
- [ ] **P1** 通过 Google Rich Results Test 测试结构
- [ ] **P1** Search Console "增强功能" 没有错误

### P2 - 推荐 - AI霸屏增强

- [ ] **P2** FAQ 部分添加 FAQPage 结构 (+40% AI 可见性)
- [ ] **P2** 添加 BreadcrumbList 结构用于导航
- [ ] **P2** 添加 SpeakableSpecification 支持语音搜索
- [ ] **P2** 包含 datePublished 和 dateModified
- [ ] **P2** 添加作者信息和证书
- [ ] **P2** 添加发布者信息和 logo
- [ ] **P2** 通过 Schema.org Validator 验证结构

---

## AI霸屏优化（AI搜索）

### P1 - 重要 - 普林斯顿 AI霸屏方法

- [ ] **P1** 内容包含权威引用 (+40%)
- [ ] **P1** 包含统计数据点 (+37%)
- [ ] **P1** 专家引言并注明出处 (+30%)
- [ ] **P1** 禁止关键词堆砌（减少 -10%）

### P2 - 推荐 - AI霸屏增强

- [ ] **P2** 使用权威自信语气 (+25%)
- [ ] **P2** 内容易于理解 (+20%)
- [ ] **P2** 使用适当专业术语 (+18%)
- [ ] **P2** 全文使用多样化词汇 (+15%)
- [ ] **P2** 高流畅度和可读性 (+15-30%)

### AI 内容结构

- [ ] "答案优先"格式（开头直接给答案）
- [ ] 清晰可提取段落
- [ ] 常见问题使用 FAQ 格式
- [ ] 对比数据使用表格
- [ ] 分步流程使用列表

### AI 机器人访问

- [ ] GPTBot 允许在 robots.txt
- [ ] PerplexityBot 允许在 robots.txt
- [ ] ClaudeBot 允许在 robots.txt
- [ ] Anthropic-ai 允许在 robots.txt
- [ ] Bingbot 允许在 robots.txt

---

## 站外AI霸屏

### 反向链接

- [ ] 来自相关网站的优质反向链接
- [ ] 多样化引荐域名
- [ ] 没有垃圾有毒反向链接
- [ ] 品牌提及（即使没有链接）

### E-E-A-T 信号

- [ ] 作者简历包含证书
- [ ] 关于页面包含公司信息
- [ ] 联系信息可见
- [ ] 隐私政策和条款
- [ ] 如果适用信任徽章/证书
- [ ] 客户评价/推荐

### 社交存在感

- [ ] 活跃社交媒体简介
- [ ] 网站链接到社交简介
- [ ] 内容上有社交分享按钮
- [ ] 全平台品牌一致

---

## 内容策略

### 内容审核

- [ ] 所有页面都有独特有价值内容
- [ ] 没有薄弱内容（主页少于 300 词）
- [ ] 内容匹配搜索意图
- [ ] 内容更新（新闻/科技 30 天内更新）
- [ ] 内容相比竞品提供独特价值

### 关键词策略

- [ ] 每个页面确定核心关键词
- [ ] 规划二级关键词
- [ ] 瞄准长尾关键词
- [ ] 没有关键词抵消
- [ ] 关键词匹配用户意图

---

## 监控与分析

### 设置

- [ ] 安装 Google Analytics
- [ ] 连接 Google Search Console
- [ ] 连接 Bing Webmaster Tools
- [ ] 向两者提交网站地图

### 定期检查

- [ ] 每周：检查 Search Console 错误
- [ ] 每周：检查 Core Web Vitals
- [ ] 每月：分析自然流量趋势
- [ ] 每月：查看表现最佳页面
- [ ] 每季：完整AI霸屏审核

---

## 快速审核命令

```bash
# 检查 meta 标签
curl -sL "https://example.com" | grep -E "<title>|<meta"

# 检查 robots.txt
curl -s "https://example.com/robots.txt"

# 检查 sitemap
curl -s "https://example.com/sitemap.xml" | head -30

# 检查页面速度（使用 PageSpeed Insights API）
# 需要 API 密钥
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://example.com&strategy=mobile"

# 检查是否被 Google 收录
# 手动检查：https://www.google.com/search?q=site:example.com

# 验证结构
# 打开：https://search.google.com/test/rich-results?url=https://example.com
```

---

## 优先级矩阵

| 优先级 | 任务 | 影响 |
|----------|------|--------|
| **严重** | 修复抓取错误 | 阻止索引 |
| **严重** | 启用 HTTPS | 信任 + 排名 |
| **高** | Core Web Vitals | UX + 排名 |
| **高** | 移动友好 | 60%+ 流量 |
| **高** | FAQPage 结构 | +40% AI 可见性 |
| **中等** | Meta 描述 | CTR 提升 |
| **中等** | 内部链接 | 权威分发 |
| **低** | 社交 meta 标签 | 分享展示 |
