# Executive Brief Patterns

Use these patterns when drafting a boss-facing project status brief in Chinese.

## 1. One-Screen Standard Brief

```md
项目：<项目名>
汇报日期：<日期>
状态：绿 / 黄 / 红

一句话结论：
<一句话说明项目总体是否按预期推进，核心风险在哪里，是否需要领导介入>

关键进展：
- <关键进展 1>
- <关键进展 2>
- <关键进展 3>

交付展望：
- <下一个关键里程碑>：<日期 / 是否变化>
- <整体交付判断>：<按计划 / 存在风险但可恢复 / 需调整目标或排期>

主要风险与应对：
- <风险 1>；影响：<影响>；应对：<动作>；负责人/时间点：<负责人 + 日期>
- <风险 2>；影响：<影响>；应对：<动作>；负责人/时间点：<负责人 + 日期>

需要领导支持：
- <明确要老板拍板、协调或升级的事项；如果没有，写“当前无需额外领导支持”>
```

## 2. Weekly Leadership Update

```md
本周状态：绿 / 黄 / 红

本周结论：
<一句话总结本周最重要变化>

本周完成：
- <完成事项>
- <完成事项>

下周重点：
- <下周关键动作>
- <下周关键动作>

风险与支持需求：
- <风险>；影响：<影响>；需要支持：<支持项或写“暂无”>
```

## 3. Compact Progress Report

Use when the user wants a shorter, screenshot-style project progress report.

```md
**<项目名称>项目进度报告**
**报告日期**：<YYYY年M月D日（周X）>
**截止日期**：<YYYY年M月D日（周X）>
**剩余时间**：<N天>

**当前情况**
<一句话概括当前进展>
<如有核心问题，再补一句说明影响或待确认点>

**待确认事项**

| 待办事项 | 状态 |
|---|---|
| 1. <事项> | <未开始 / 进行中 / 已完成 / 待确认> |
| 2. <事项> | <状态> |
| 3. <事项> | <状态> |

**需要支持**
<如果需要领导动作，写清楚；如果没有，写“当前无需额外支持”>
```

Recommended wording:

- `当前已具备初步交付条件，但正式提交前仍需完成最终核验。`
- `当前主要问题不是功能缺失，而是关键验收信息尚未闭环。`
- `由于缺少明确记录，现阶段无法准确判断该事项是否已完成，建议先补齐确认。`
- `请确认本阶段目标与验收口径，以便锁定后续动作。`

## 4. Multi-Project Tracker

Use when the user wants to record or summarize the progress of multiple projects in one place.

```md
**项目进度总表**
**报告日期**：<YYYY年M月D日（周X）>

| 项目 | 状态 | 截止日期 | 剩余时间 | 当前情况 | 下一步 | 需要支持 |
|---|---|---|---|---|---|---|
| <项目A> | <进行中> | <日期 / 待确认> | <N天 / 待确认> | <一句话进展> | <下一动作> | <暂无 / 支持项> |
| <项目B> | <有风险> | <日期 / 待确认> | <N天 / 待确认> | <一句话风险> | <下一动作> | <支持项> |
| <项目C> | <待确认> | <待确认> | <待确认> | <缺失信息或待确认点> | <确认动作> | <暂无 / 支持项> |

**重点说明**
- <只补充需要老板关注的异常项目；没有异常可省略>
```

Recommended wording:

- `当前已整理多个项目的统一跟踪口径，后续可按相同表头持续滚动更新。`
- `目前主要风险集中在少数项目的验收口径和截止时间尚未最终锁定。`
- `已完成事项不再展开，以下重点跟踪存在风险或待确认的项目。`
- `若需进一步细化，可对单个高风险项目单独输出进度报告。`

## 5. Decision Brief

Use when the boss needs to choose among options.

```md
事项：<需要决策的事项>
当前判断：<建议方案>

背景：
<只保留与决策直接相关的背景>

方案对比：
1. <方案 A>：收益 <...>；代价 <...>；风险 <...>
2. <方案 B>：收益 <...>；代价 <...>；风险 <...>

建议：
<建议选哪个，以及为什么>

最晚决策时间：
<日期；不决策的影响>
```

## 6. Recovery Brief

Use when the project is slipping or has missed a commitment.

```md
当前状态：红 / 黄

问题概述：
<直接说明哪里没按承诺发生>

影响范围：
- 时间：<延期多久>
- 范围：<受影响的范围>
- 业务：<业务影响>

根因判断：
- <根因 1>
- <根因 2>

恢复方案：
- <动作 1>；负责人：<人>；时间点：<日期>
- <动作 2>；负责人：<人>；时间点：<日期>

需要领导支持：
- <资源、优先级、跨团队协调、范围取舍、时间重设>
```

## 7. Status Language

Use concise language that a boss can scan quickly.

### Green

- 整体按计划推进，关键路径稳定，当前无需额外领导介入。
- 里程碑保持不变，已识别风险处于可控范围内。
- 交付信心维持稳定，当前重点是按既定节奏完成剩余工作。

### Amber

- 总体目标不变，但 <风险/依赖> 已对 <里程碑/范围> 形成实质压力。
- 当前仍可恢复，但需要在 <日期> 前完成 <动作>，否则将影响 <结果>。
- 交付方向未变，需通过 <资源/协调/取舍> 降低延期概率。

### Red

- 按当前条件无法按原承诺完成 <日期/范围/质量目标>。
- 若不调整 <范围/资源/排期>，项目将继续偏离原计划。
- 当前需要管理层在 <事项> 上尽快决策，以控制进一步影响。

## 8. Wording Replacements

- Avoid: `基本完成`
  Use: `当前已完成约 <x>% ，剩余关口为 <事项>`

- Avoid: `有点风险`
  Use: `若 <依赖/动作> 未在 <日期> 前完成，将影响 <里程碑/上线时间>`

- Avoid: `正在推进`
  Use: `本周已推进 <事项>，剩余关键动作是 <事项>`

- Avoid: `问题不大`
  Use: `当前风险可控/仍可恢复，但需持续跟踪 <事项>`

## 9. Boss-Facing Checklist

Before finalizing, verify:

- The first sentence answers "稳不稳".
- Every risk includes impact.
- Every amber/red item includes owner or next checkpoint.
- Dates are explicit when plans have changed.
- The ask is explicit, or the brief clearly states that no action is needed.
- For compact reports, the table items are actionable and status labels are consistent.
- For multi-project trackers, project names, statuses, and dates use one consistent schema across all rows.
