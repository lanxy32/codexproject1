# Department AI Map

Use this reference when the client is a multi-department e-commerce,直播,内容型 organization. Adapt it to the actual maturity and staffing level.

## Core rule

Do not recommend separate tool stacks for every team. Reuse a small common base, then add one specialist layer only where the department truly needs it.

## Suggested common base

- `文本与问答`: DeepSeek, Kimi, 豆包, 通义千问
- `智能体/流程`: 扣子 Coze, Dify
- `协作与知识沉淀`: 飞书文档, 企业微信, Notion, internal SOP docs
- `图片/设计`: Canva, 即梦, 稿定, Midjourney when suitable
- `视频/剪辑`: 剪映, 即梦, 可灵, Runway when suitable

Always note that final tool selection depends on compliance, budget, and the client's current software environment.

## Department playbook

### 设计部

- Typical work:
  banner, campaign KV, live-room visuals, product detail page ideas, ad creative drafts
- AI use:
  generate concept directions, draft copy-to-visual prompts, rapid poster variation, material整理
- Training exercise:
  create one campaign visual set from a real promotion brief
- Good outcomes:
  faster draft generation, more versions per campaign, reduced back-and-forth on first draft

### 客服部

- Typical work:
  repetitive inquiry handling, product FAQ, order issues, after-sales messaging, escalation summaries
- AI use:
  FAQ draft generation, standard reply optimization, emotion-aware rewriting, case summarization
- Training exercise:
  build a customer-service reply assistant from top 30 repeated questions
- Good outcomes:
  faster response prep, more consistent replies, better新人上手速度

### 直播运营部

- Typical work:
  session planning, product排期,话术准备,复盘总结,数据记录
- AI use:
  live-room SOP drafting, product selling-point extraction, session script generation, review summaries
- Training exercise:
  generate one full直播排班与话术包 for a real product campaign
- Good outcomes:
  shorter prep cycle, stronger standardized review, faster activity planning

### 推流部

- Typical work:
  live-room switching, material coordination, stream notes, troubleshooting checklists
- AI use:
  checklist generation, event logging templates, issue summary, standard operating guide refinement
- Training exercise:
  convert the current推流流程 into a reusable AI-assisted SOP
- Good outcomes:
  fewer missed steps, cleaner交接, faster incident复盘

### 直播切片部

- Typical work:
  highlight selection, title writing, clip planning, batch output management
- AI use:
  clip-angle ideation, title generation, highlight description, batch content planning
- Training exercise:
  turn one live replay into a clip plan with 10 publishable angles
- Good outcomes:
  higher material reuse, faster second-edit planning, better content consistency

### 文案策划部

- Typical work:
  campaign themes, product copy, social content, activity naming, selling-point packaging
- AI use:
  campaign ideation, angle expansion, long-to-short rewriting, platform adaptation
- Training exercise:
  generate one full campaign content pack for multiple channels
- Good outcomes:
  more angle output, faster first draft, better style consistency

### 拍摄剪辑部

- Typical work:
  shot lists, script-to-shot mapping, caption drafts, rough-cut planning, revision notes
- AI use:
  storyboard assistance, shot-list drafting, subtitle optimization, rough-cut commentary extraction
- Training exercise:
  create a script plus shot list plus edit notes from a real SKU
- Good outcomes:
  smoother前后端协作, reduced script ambiguity, faster rough-cut turnaround

### 采购部

- Typical work:
  vendor comparison, quote summaries, demand collection, order follow-up, exception communication
- AI use:
  supplier comparison tables, requirement summary, follow-up draft emails, meeting notes
- Training exercise:
  compare 3 suppliers and generate a standardized decision summary
- Good outcomes:
  faster information整理, clearer比价逻辑, less manual follow-up drafting

### 仓储部

- Typical work:
  inbound/outbound exception logging, inventory summaries, handover notes, process checklists
- AI use:
  exception classification, report drafting, SOP refinement, training material generation
- Training exercise:
  convert 1 week of exception records into an issue summary and SOP optimization list
- Good outcomes:
  stronger process standardization, faster report output, clearer异常复盘

### 人事部

- Typical work:
  JD drafting, interview question prep, onboarding docs, training notices,制度整理
- AI use:
  JD and interview outline generation, onboarding handbook drafting, training quiz support, policy summarization
- Training exercise:
  produce one岗位招聘包 plus one新人入职包
- Good outcomes:
  faster HR document drafting, more consistent onboarding, reduced repetitive editing

## Grouping hints for 3-day training

Use the smallest number of department clusters that still feel operationally natural:

- Cluster A: 设计部 + 文案策划部 + 拍摄剪辑部 + 直播切片部
- Cluster B: 直播运营部 + 推流部
- Cluster C: 客服部
- Cluster D: 采购部 + 仓储部 + 人事部

If time is tighter, merge Cluster B into Cluster A and keep Cluster C and D separate.
