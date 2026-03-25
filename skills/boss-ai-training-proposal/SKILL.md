---
name: boss-ai-training-proposal
description: Boss-facing AI internal-training proposal and departmental enablement planning for traditional companies, e-commerce teams, live-streaming organizations, and service businesses. Use when Codex needs to turn a boss's rough notes, chat screenshots, department lists, demand-survey notes, or customer requirements into a practical AI training proposal, 3-day to 7-day training outline, departmental AI tool map, intelligent-agent backlog, demand survey plan, or post-training support package. Trigger on requests like "给老板出一份AI内训方案", "把部门需求整理成培训提案", "根据聊天记录做AI培训大纲", "做客户AI赋能方案", "设计三天AI内训安排", or "turn this boss description into an AI adoption proposal".
---

# Boss AI Training Proposal

## Overview

Act like a practical AI enablement consultant writing for the boss, not a generic trainer. Convert vague demand into a sellable and deliverable方案: clear scope, realistic curriculum, department coverage, tool choices, pre-training调研, and post-training陪跑.

Default to concise executive Chinese when the user writes in Chinese. Lead with the recommendation and keep every module tied to business value, implementation difficulty, and adoption risk.

## Workflow

### 1. Reconstruct the engagement scope

Extract or infer the minimum information needed:

- Customer name and industry
- Company size or revenue band when available
- Channel mix such as traditional channels, e-commerce, live-streaming, private-domain, distributors, or offline stores
- Departments in scope and any excluded departments
- AI maturity: `0基础`, partial use, or already piloting
- Training duration and format: outline only, proposal, agenda, or full package
- Real goal: efficiency, quality, scale, standardization, or agent rollout
- Delivery preference: one-off培训, workshop, or training plus陪跑
- Constraints: compliance, budget, IT capability, tool sensitivity, leadership attention
- Need for cases or demos, especially industry-specific demo requests

Do not block on missing data unless it changes the proposal materially. State assumptions and continue.

Default assumptions when signals are weak:

- The company is early-stage in AI adoption
- Department tool usage is fragmented or near zero
- Finance and other highly sensitive teams are excluded unless explicitly requested
- The boss wants a方案 that can be sold, delivered, and expanded later

### 1A. Use the client-brief workflow the boss actually uses

In many requests, the boss will provide:

- 客户名称
- 客户行业
- 客户相关信息
- 培训天数或时间
- 参考图片或课程框架

Use that sequence as the working intake model.

Default to the built-in course reference library in this skill first. This library already summarizes the canonical AI course images and framework styles supplied earlier in this workspace.

When attachments or earlier images exist in the current thread, treat them as supplemental reference material. Reuse their structure and style without asking the user to resend them.

When the user provides a local proposal file such as `.docx`, treat it as a reference artifact to learn the expected sectioning, table density, and detail level. Extract the structure and reproduce it in the response rather than summarizing it vaguely.

Only ask the user to provide the images again if:

- the current thread does not contain them,
- the requested reference image is ambiguous,
- the user clearly points to a different attachment not present in context, or
- the user explicitly says `更新AI课程参考图片`, `按新的课程图来`, or equivalent.

If the user provides only customer name + industry + a short need statement, infer the likely training priorities and proceed with explicit assumptions.

### 2. Choose the right deliverable

Use the smallest useful output:

- `内训大纲`: when the user needs only day-by-day安排
- `客户提案`: when the user needs a sellable boss-facing方案
- `正式提案文案`: when the user wants a polished, client-facing training proposal with service flow, training outline, follow-up plan, and deliverables
- `部门AI机会清单`: when the user needs department use cases, tool ideas, and gains
- `调研到落地闭环方案`: when the user needs a full consulting path
- `智能体清单初稿`: when the user wants to connect training with later agent building
- `课程框架表`: when the user shares screenshots, tables, or says `参考这个格式`
- `AI+行业实战培训`: when the user wants the curriculum fused with a specific customer industry, business model, and channel structure

If the user asks for "只做大纲", still structure it so it can be expanded into a proposal later.

When the user provides screenshots or explicit format references, copy the structural logic first and only then fill in the content. Do not default to essay format if the user is clearly asking for a table-like课程架构.

If the user does not provide any fresh images, still use the built-in reference frameworks before inventing a new structure from scratch.

### 3. Build a practical delivery path

Prefer this best-practice sequence unless the user overrides it:

1. Sign the internal-training engagement and confirm scope
2. Run a real demand survey by department
3. Adjust the first draft based on survey findings
4. Deliver onsite or live training
5. Facilitate an on-the-spot `智能体/场景清单梳理`
6. Recommend tool paths only after the scenario inventory is clear
7. Add one month of online Q&A support
8. Add weekly online learning sessions, typically `每周1次，每次2小时`

Make the proposal feel implementable. Separate:

- `培训阶段`: what happens during the 3 days
- `落地阶段`: what happens after training
- `升级阶段`: what can be built next, such as knowledge bases, workflows, or agents

### 4. Design the curriculum around workflows, not isolated departments

For multi-department companies, group departments by adjacent workflows so all teams can be covered in limited time.

For a 3-day program, use this logic by default:

- Day 1: shared foundation for all participating departments
- Day 2: front-office growth workflows
- Day 3: support and operational workflows

When there are too many departments for one-by-one teaching, cluster them into 3 or 4 blocks:

- `内容生产链路`: design, copywriting/planning, filming/editing, clip-editing
- `直播增长链路`: live-stream operations, stream-control, content analysis
- `客户转化链路`: customer service, FAQ handling, SOP response, after-sales handoff
- `经营支持链路`: procurement, warehousing, HR, admin, internal coordination

If the user must cover all non-finance departments in only 3 days, prioritize shared tool habits plus department exercises, not long theory.

### 4B. Turn generic AI training into `AI + 客户行业实战培训`

When the user gives an industry, do not output a generic AI class with the industry name pasted on top.

Instead, adapt all of these layers:

- `场景`: use the customer's real work chain
- `案例`: choose same-industry or adjacent-industry examples
- `Demo`: demonstrate with the customer's likely product, channel, or service flow
- `合规`: reflect industry-specific content boundaries
- `动作`: end with a realistic rollout or execution list

Typical adaptation dimensions:

- If the client is e-commerce: content, traffic, conversion, customer service, repurchase, SKU communication
- If the client is traditional + new media mixed: bridge channel coordination and material reuse
- If the client is regulated or sensitive, such as health, supplements, food, finance, legal, or medical-adjacent: explicitly include compliance wording and claim boundaries
- If the client asks for `案例demo`, ensure each major module has a demo idea, not just one demo for the whole day

For one-day industry training, compress but do not flatten. Keep:

1. 行业认知 and AI value
2. 提示词 and industry-safe expression
3. 内容 or workflow production
4. Customer-facing or service-facing use
5. End-to-end practical chain
6. Short implementation plan

### 4A. Match the image-style framework before writing content

When the user references attached images, course posters, or spreadsheet-like samples, prefer one of these output frames:

- `课程清单大纲表`: columns such as `天数 / 级别 / 模块 / 培训内容 / 课程详细内容 / 费用`
- `专题课包表`: columns such as `序号 / 课程主题 / 授课时长`
- `实训排期表`: columns such as `序号 / 天 / 时间 / 实训模块 / 实训内容 / 备注`
- `服务方案表`: columns such as `阶段 / 服务内容 / 输出成果 / 周期`

If the user gives only rough screenshots, infer the closest frame and state it implicitly through the output. Do not mention that the table is inferred unless necessary.

If a section is naturally tabular, render it as a markdown table. Never say `表格暂时无法展示此内容`.
Never output placeholders like `表格`, `点击图片可查看完整电子表格`, `见附件表格`, or similar when the response itself can materialize the table.

When writing course schedules, prefer exact time slots such as `09:30-10:20`, `10:20-11:10`, `14:00-14:50`, `15:50-16:40`. Avoid vague labels like `上午`, `下午`, `全天` unless the user explicitly wants a coarse outline.

Before inventing a new frame, check the built-in image-derived references:

- `课程专题菜单框架`
- `培训课程清单大纲框架`
- `7天AI实训排期框架`
- `线上月课 + 线下季课混合培训框架`

### 5. Recommend tools by scenario depth

Choose tools by category first and vendor second. Avoid dumping long tool lists.

Use a layered recommendation model:

- `通用对话与写作`: 1 primary model and 1 backup model
- `知识库与协作`: document systems, internal SOPs, shared prompt libraries
- `智能体/流程编排`: for later-stage automation, not for day-1 tool overload
- `设计/图片/视频`: only for departments with real media workloads
- `数据/表格/报表`: only when teams already depend on Excel or BI

Recommend `1-3` core tools per department cluster. Explain:

- What work the tool helps with
- What output it can generate
- Why the department can adopt it quickly
- What governance or review is still needed

For sensitive functions, prefer compliant enterprise-approved tools or local deployment paths. Never assume public tools are acceptable for confidential data.

### 6. Map each department to work, tools, and gains

For each department or workflow block, answer five questions:

1. What is the current repetitive work?
2. Where does AI save time or reduce errors?
3. Which tools or agent patterns fit?
4. What sample exercise should be taught in training?
5. What measurable improvement is realistic in 30 days?

Keep gains credible. Prefer phrases like:

- `缩短初稿产出时间`
- `提升标准化和一致性`
- `减少重复沟通`
- `提高素材复用率`
- `降低新人上手难度`

Avoid promising full replacement of human judgment.

### 7. Write the proposal in boss language

Use short, persuasive sections with clear business logic:

- Project background and objective
- Why AI internal training now
- Scope and excluded scope
- Training method and phases
- 3-day outline
- Department scenario coverage
- Deliverables
- Post-training support
- Preconditions and cooperation requirements

If the user provides chat screenshots or rough notes, translate them into clean proposal language instead of echoing the raw wording.

### 7A. Raise the scheme quality above a generic outline

When the user needs a stronger proposal or教案, upgrade the content quality in these ways:

- Start with `培训主题 / 培训对象 / 培训时长 / 核心目标`
- Make `核心目标` concrete and numbered, usually 3-5 items
- Show actual training intensity, such as `每天6小时` or `实操模块占比65%`, when the schedule supports it
- Break each day into time-based modules instead of only listing topics
- Give every module:
  - `核心目标`
  - `主要内容`
  - `互动形式`
  - `关键产出`
- Prefer business diagnosis and local adaptation over abstract theory
- If the request involves platform transformation, include:
  - business pain points
  - benchmark teardown
  - local adaptation path
  - operating SOP
  - risk control
  - phased rollout plan

For stronger方案 generation, think like this:

1. `为什么要做`
2. `标杆为什么成立`
3. `客户为什么能做`
4. `应该怎么做`
5. `先从哪里试点`
6. `如何控制风险和保证落地`

When the user wants a one-day curriculum, aim for `90分方案` by adding these quality signals:

- clear customer fit, not generic cross-industry language
- concrete demo examples tied to the customer's products or services
- visible practical ratio or practice-heavy module design
- exact time slots
- module-level outputs or assignments
- industry compliance reminders when needed
- a short post-training action list
- complete inline tables with row data, not omitted or deferred table content

### 8. Default output structure

Use this structure as a strong reference when the user wants a formal proposal and has not specified another format:

```md
<客户名称> AI内训方案
服务模式：<按需求组合，可包含集中内训 / 线上深化 / 咨询陪跑>

一、项目概述
<用1段话说明客户现状、覆盖部门、AI基础与项目目标>

二、项目目标
- <统一认知>
- <梳理部门场景>
- <沉淀智能体清单>
- <推动后续落地>

三、整体服务流程
| 阶段 | 服务内容 | 目标 |
|---|---|---|
| 需求调研阶段 | <问卷 + 访谈 + 场景摸底> | <明确培训重点> |
| 集中内训阶段 | <3天现场培训> | <完成认知与首轮实操> |
| 持续学习阶段 | <按需设置周度深化学习> | <帮助员工从会用到做熟> |
| 后续服务阶段 | <按需设置线上咨询或陪跑> | <确保落地> |

四、3天集中内训大纲
| 天数 | 培训对象 | 培训模块 | 培训内容 | 关键产出 |
|---|---|---|---|---|
| 第一天 | <全部门> | <AI认知统一 + 需求梳理> | <工具认知、提示词基础、场景盘点、智能体清单梳理> | <部门应用清单初稿> |
| 第二天 | <内容/直播/设计相关部门> | <专项实操> | <文案、设计、直播、切片、拍剪等场景训练> | <内容链路模板与候选智能体> |
| 第三天 | <客服/采购/仓储/人事等部门> | <专项实操 + 落地复盘> | <客服、供应链、人事场景训练与复盘> | <支持链路应用清单与后续优先级> |

五、线上深化学习大纲（可选）
| 周次 | 学习主题 | 重点部门 | 学习目标 | 作业/产出 |
|---|---|---|---|---|
| 第1周 | <提示词强化与统一规范> | <全部门> | <巩固基础> | <模板/作业> |
| 第2-6周 | <按部门深化> | <分部门> | <深化工具与场景> | <部门成果> |
| 第7周 | <智能体清单细化> | <重点部门负责人> | <明确优先级> | <智能体清单> |
| 第8周 | <复盘与下一阶段规划> | <关键岗位> | <形成后续动作> | <阶段复盘> |

六、配套服务建议
1. <智能体清单交付>
2. <按需设置线上学习>
3. <按需设置专属线上咨询>
4. <学习资料包交付>

七、项目交付成果
- <3天课程大纲>
- <部门AI应用场景清单>
- <智能体需求清单初稿>
- <8周学习安排表>
- <资料包>

八、客户配合事项
- <参训名单>
- <调研配合>
- <案例/素材提供>
- <内部对接人>

九、方案价值总结
<用1段话说明为什么该方案适合当前客户，以及后续可如何递进落地>
```

## Output Rules

- Lead with the recommendation, not the history of reasoning.
- Cover every requested department explicitly, or explain grouping clearly.
- Keep day-level agendas realistic for the available hours.
- Distinguish `能立即落地` from `后续建设项`.
- Challenge over-scoping when the requested time is too short.
- If finance is excluded, keep it excluded and do not force it back in.
- Use examples to make AI feel concrete, but keep the proposal vendor-neutral enough to survive tool changes.
- For stronger教案, include `培训主题 / 培训对象 / 培训时长 / 核心目标` before the schedule table.
- Prefer `模块一 / 模块二` style progression when the user wants a more professional training scheme.
- In detailed module descriptions, include `核心目标`, `主要内容`, `互动形式`, and optionally `关键产出`.
- Add `培训保障与后续支持` when the proposal would benefit from课前、课中、课后安排.
- If the proposal involves commercialization or transformation, include `风险控制` and `分阶段落地计划`.
- If the request is for `AI+行业实战培训`, every major module should contain industry-specific examples or demos.
- If the customer has both traditional and new-media channels, explicitly connect the two instead of focusing on only one side.
- If the customer is in supplements, food, health, or other compliance-sensitive categories, include compliant wording rules and prohibited-claim awareness.
- If the proposal contains tables, fully materialize the rows and columns in the answer. Do not collapse table sections into placeholders or references to attachments.
- When an attached case document shows a good table style, imitate the table density and completeness in the new output.

## Resources

Read [references/department-ai-map.md](references/department-ai-map.md) when the company resembles an e-commerce, live-streaming, content, or customer-service organization with multiple operational departments.

Read [references/proposal-patterns.md](references/proposal-patterns.md) when you need proposal wording, scope boundaries, phased delivery design, or a ready-to-adapt 3-day training framework.

Read [references/curriculum-frameworks.md](references/curriculum-frameworks.md) when the user wants the output to resemble a course framework image, table, training matrix, 7-day bootcamp sheet, or package-style curriculum menu.

Read [references/course-image-framework-library.md](references/course-image-framework-library.md) when you need the built-in summary of the previously supplied AI course images. This is the default structural reference library and should usually be consulted before asking the user for course-reference images again.

Read [references/formal-proposal-template.md](references/formal-proposal-template.md) when the user wants a direct-to-client formal proposal and would benefit from a strong commercial reference structure. Treat that file as a template library, not a mandatory fixed format.

Read [references/high-quality-scheme-patterns.md](references/high-quality-scheme-patterns.md) when the user wants a stronger, more executive-ready教案 or a scheme that feels closer to `75分以上` quality: clearer goals, richer modules, stronger interaction design, and a more actionable rollout path.

Read [references/industry-ai-training-patterns.md](references/industry-ai-training-patterns.md) when the user gives a customer industry and wants `AI + 行业实战培训`, especially for one-day or two-day business training with cases and demos.

Read [references/blended-training-program-patterns.md](references/blended-training-program-patterns.md) when the request is about recurring online learning plus periodic onsite workshops, such as `每月一期线上课 + 每季度一期线下课`.

Read [references/complete-table-output-patterns.md](references/complete-table-output-patterns.md) when the user cares about fully expanded tables, attachment-derived table styles, or the previous方案 quality suffered from placeholder tables instead of real rows.

## Framework Rules

- Prefer markdown tables over long paragraphs when the user asks for `框架`, `课程清单`, `大纲表`, `按这个格式`, or references images.
- Keep proposals commercial and deliverable: show `阶段`, `对象`, `模块`, `输出`, and `后续服务`.
- For 3-day plans, combine `通识基础 + 部门专项 + 落地复盘`.
- For formal proposals, prefer a clear business sequence such as `项目概述 -> 项目目标 -> 服务流程 -> 培训大纲 -> 配套服务 -> 交付成果 -> 配合事项 -> 价值总结`, but adapt freely to user intent.
- For 7-day plans, ladder the design from `AI认知` to `文案/视频` to `流量经营` to `AI数字员工` to `实操复盘`.
- For package menus, group themes like the image samples do: `AI+客服`, `AI+办公`, `AI+提示词`, `AI+企业智能体`, `AI+私有化`, `AI+API`.
- Keep `费用` optional. Include it only when the user asks or when writing a commercial package menu.
- When using `级别`, default to `初阶科普 / 中阶岗位实操 / 高阶智能体研修`.
- When the client is 0基础, spend less space on model theory and more space on concrete岗位任务与练习产出.
- If the user says `作为模板`, borrow the useful structure and tone from the supplied template, but do not freeze the output into that exact section order unless explicitly requested.
- For course tables, default to a `时间` column with exact session ranges instead of `上午/下午`.
- Treat the built-in image-derived framework library as the default sample bank. Do not ask the boss to resend old course-reference images unless they explicitly want to update them.
- Tables are first-class output, not optional decoration. If a proposal logically needs a table, render the full table with populated rows.
