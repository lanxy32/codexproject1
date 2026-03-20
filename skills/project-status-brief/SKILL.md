---
name: project-status-brief
description: Draft executive-ready project status briefs / 项目状态简报, compact project progress reports, and multi-project progress trackers for bosses, leadership, steering committees, and senior stakeholders. Use when Codex needs to turn project notes, standups, milestone updates, risks, blockers, decisions, timelines, or delivery signals into a concise boss-facing status update, weekly brief, milestone review, leadership memo, short table-based progress report, or a portfolio-style tracker covering multiple projects. Trigger on requests like "给老板写项目状态简报", "写项目周报高层版", "写精简项目进度报告", "按截图风格整理项目进展", "记录不同项目进度", "整理多个项目状态", "summarize project health for leadership", "turn this into an executive status brief", or "what should I tell my boss about these projects?"
---

# Project Status Brief

## Overview

Write for decision-makers rather than implementers. Lead with delivery confidence, business impact, timeline, risk, and required support instead of execution detail.

Default to a one-screen brief unless the user asks for more depth. Preserve the user's language; when the request is in Chinese, write concise business Chinese rather than literal engineering translation.

## Workflow

### 1. Reconstruct the operating picture

Extract or infer the minimum facts needed to brief a boss:

- Project objective or committed outcome
- Current phase or milestone
- Delivery confidence against date, scope, and quality
- Material changes since the last update
- Top risks, blockers, and dependencies
- Decisions, support, or escalation needed from leadership

If the source material is fragmented, synthesize it first. Avoid blocking on missing minor details; state assumptions briefly when needed.

### 2. Normalize each project into trackable fields

For each project, normalize the update into a stable record:

- Project name
- Status
- Report date
- Deadline or next milestone date
- Remaining time, if date is known
- Current situation
- Next step
- Top risk or blocker
- Leadership support needed

When multiple projects are provided, keep one record per project and preserve consistent naming across updates. If a field is unknown, mark it as `待确认` instead of hiding the gap.

### 3. Decide the status honestly

Use simple executive health labels:

- `Green`: commitment is on track and no material management action is required now.
- `Amber`: outcome is still recoverable, but timing, scope, dependency, or quality is at risk and needs active mitigation.
- `Red`: committed outcome or date is not achievable without reset, decision, or intervention.

Avoid false-green reporting. If the narrative contains meaningful schedule slip, unresolved critical dependencies, or missing owners for major risks, do not label it `Green`.

### 4. Write in boss-first order

Prefer this order unless the user asks for a different format:

1. Overall status and one-line conclusion
2. What changed since last update
3. Delivery outlook and milestones
4. Top risks or blockers with impact
5. Mitigation, owner, and next checkpoint
6. Leadership ask, if any

Keep each item short. The boss should understand the situation in under 30 seconds.

### 5. Separate facts, judgment, and asks

Make the brief easy to scan:

- Facts: milestone reached, date changed, defect count, dependency delay, budget variance
- Judgment: on track, recoverable, likely slip, confidence improving, confidence decreasing
- Ask: approve scope tradeoff, escalate dependency, add reviewer, confirm deadline reset

Do not bury the ask inside a risk paragraph. If support is needed, call it out explicitly.

### 6. Use executive language

Write with precision and restraint:

- Prefer "impact + response + ask" over implementation diary
- Prefer quantified statements over vague adjectives
- Prefer direct language over hedging
- Prefer outcome language over task language

Replace weak phrases:

- Replace "基本完成" with "% complete plus remaining gating items"
- Replace "有点风险" with the specific risk, impact, and trigger date
- Replace "正在推进" with what moved and what remains
- Replace "问题不大" with the actual confidence statement

### 7. Calibrate the detail level

Choose the smallest format that solves the request:

- `Flash update`: 3-5 lines for IM or chat
- `Compact progress report`: title + date + deadline + remaining time + current situation + pending items table
- `Portfolio tracker`: a multi-project summary table with one row per project
- `Standard brief`: one-screen update for boss or weekly report
- `Decision brief`: brief plus explicit options and recommendation
- `Recovery brief`: explain miss, impact, recovery plan, and decisions needed

Use `Compact progress report` by default when the user asks for:

- 精简一些
- 像截图那样
- 项目进度报告
- 给老板快速看
- 表格式待办 / 状态跟踪

Use `Portfolio tracker` by default when the user asks for:

- 记录不同项目进度
- 整理多个项目状态
- 做项目总表
- 汇总各项目进展
- 一个表看所有项目

## Output rules

- Open with the answer, not the background.
- Include only the 1-3 most material risks.
- Give every serious risk a mitigation owner or next checkpoint.
- Name date changes explicitly.
- When a deadline is known, show `报告日期`、`截止日期`、`剩余时间`.
- If there is no ask, say that no leadership action is needed now.
- If information is incomplete, include a short assumptions line instead of inventing certainty.
- Avoid jargon unless the user clearly wants a technical audience.
- For compact reports, prefer `当前情况` or `问题` over long narrative paragraphs.
- For compact reports, convert action items into a 2-column table: `待办事项 | 状态`.
- For multi-project reports, lead with a summary table and expand only the projects with risk, delay, or decisions needed.

## Multi-project tracking rules

- Use one row per project.
- Keep project names stable across updates; do not rename casually.
- Use consistent short status labels: `未开始`、`进行中`、`已完成`、`待确认`、`有风险`.
- If deadlines are known, include them for every tracked project.
- Sort projects by urgency when helpful: overdue or risky items first.
- If the user provides a previous tracker, preserve unchanged rows and update only changed fields.
- If several projects share the same blocker, say so once in a short note instead of repeating full paragraphs for each row.

## Default structure

Use this default structure for a standard boss-facing brief:

```md
项目：<名称>
状态：绿 / 黄 / 红

一句话结论：<老板先看这一句就能明白项目是否稳、哪里有风险、是否需要支持>

关键进展：
- <已完成或已确认的关键事项>
- <对交付有意义的推进>

交付展望：
- <关键里程碑、预计日期、是否变化>

主要风险 / 阻塞：
- <风险>；影响：<影响>；应对：<动作/负责人/时间点>

需要领导支持：
- <需要拍板、协调、升级的事项>
```

## Compact progress report structure

Use this structure when the user wants a shorter progress report:

```md
**<项目名称>项目进度报告**
**报告日期**：<YYYY年M月D日（周X）>
**截止日期**：<YYYY年M月D日（周X）>
**剩余时间**：<N天>

**当前情况**
<1-2 句说明当前进展、是否存在风险、是否需要领导关注>

**待确认事项**

| 待办事项 | 状态 |
|---|---|
| 1. <事项> | <未开始 / 进行中 / 已完成 / 待确认> |
| 2. <事项> | <状态> |

**需要支持**
<一句话说明是否需要老板拍板、协调或提供资源；如果没有，写“当前无需额外支持”>
```

Compact progress report rules:

- Keep the whole report within one screen when possible.
- Use only 3-5 pending items unless the user asks for more.
- Status labels should be short and operational: `未开始`、`进行中`、`已完成`、`待确认`、`有风险`.
- If the main issue is uncertainty, say that directly in `当前情况` instead of pretending progress is clear.
- If source information is incomplete, use `待确认事项` to surface the gap.

## Portfolio tracker structure

Use this structure when the user wants to track multiple projects together:

```md
**项目进度总表**
**报告日期**：<YYYY年M月D日（周X）>

| 项目 | 状态 | 截止日期 | 剩余时间 | 当前情况 | 下一步 | 需要支持 |
|---|---|---|---|---|---|---|
| <项目A> | <进行中> | <日期 / 待确认> | <N天 / 待确认> | <一句话现状> | <下一动作> | <暂无 / 支持项> |
| <项目B> | <有风险> | <日期 / 待确认> | <N天 / 待确认> | <一句话现状> | <下一动作> | <支持项> |
```

Portfolio tracker rules:

- Keep each cell short and scannable.
- `当前情况` should focus on the latest meaningful signal, not a task diary.
- `下一步` should be a concrete action, not a vague intention.
- `需要支持` can be `暂无`.
- If one or two projects need more context, add a short exception note under the table instead of expanding every row.

## Resources

Read [references/executive-brief-patterns.md](references/executive-brief-patterns.md) when you need:

- Chinese templates for different leadership scenarios
- Better status wording for green / amber / red cases
- Example phrasing for risks, asks, recovery plans, compact progress reports, and multi-project trackers
