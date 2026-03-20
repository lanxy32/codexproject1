---
name: boss-daily-agenda
description: Executive-oriented daily agenda management and reminder skill for bosses, founders, CEOs, general managers, and senior leaders. Use when Codex needs to turn calendars, meetings, approvals, deadlines, travel plans, follow-ups, assistant notes, or task lists into a concise daily priority brief, boss-facing reminder list, morning agenda, pre-meeting prompt, or end-of-day carryover plan. Trigger on requests like "remind the boss about today's critical items", "organize my executive agenda", "prepare a daily brief for the CEO", "what must I not miss tomorrow?", "what should the boss focus on today?", "make my executive daily brief", or "turn this schedule into a priority agenda".
---

# Boss Daily Agenda

## Overview

Write like a strong chief of staff. Help the user see what matters today, what cannot be missed, what should be delegated, and what needs preparation before a high-stakes conversation or decision.

Default to concise business language. When the request is in Chinese, write natural executive Chinese rather than literal translation or project-manager jargon.

Treat the task as context fusion, not simple formatting. Build the reminder from historical conversation records, the user's latest input, and any other available signals such as deadlines, meeting times, pending approvals, assistant notes, or carryover items from prior days.

## Operating Principle

Use this fixed formula:

`final reminder = historical conversation records + latest user input + other available context + unfinished carryover items`

Interpret each part precisely:

- `historical conversation records`: prior promises, discussed meetings, deadlines, approvals, unresolved risks, and already-mentioned priorities
- `latest user input`: fresh changes, newly added meetings, corrections, temporary priorities, and same-day updates
- `other available context`: task lists, notes, reminder fragments, assistant summaries, schedules, travel, approvals, and supporting material
- `unfinished carryover items`: items from prior days that remain incomplete and still matter today

Never reduce the task to "rewrite the latest message nicely." The value of the skill is correct context fusion and priority judgment.

## Workflow

### 1. Collect source inputs first

Before writing the brief, gather and merge the available sources in this priority order:

1. Historical conversation records: previously discussed meetings, promises, deadlines, follow-ups, risks, and decisions
2. Latest user input: new meetings, temporary changes, ad hoc priorities, travel, or special reminders
3. Other available context: task lists, notes, reminders, approvals, calendar-like schedules, or carryover items from yesterday

Do not treat the latest user message as the only truth. Check whether it updates, overrides, or adds to the longer-running context.

Normalize the source inputs into this internal checklist before ranking anything:

- Date and timezone
- Meetings with start and end times
- Hard deadlines
- Decisions or approvals waiting on the boss
- Follow-ups and promised actions
- Risks, blockers, and dependencies
- Items that can be delegated
- Carryover items from previous days

### 2. Reconstruct today's operating picture

Extract or infer the minimum information needed to brief a boss for the day:

- Current date, timezone, and any hard time constraints
- Fixed commitments: board meetings, investor calls, client meetings, internal reviews, travel, family commitments
- Decision items: approvals, sign-offs, hiring calls, vendor choices, budget calls, escalations
- Business-critical follow-ups: revenue, cash flow, deliveries, incidents, legal/compliance, payroll
- Relationship-critical touchpoints: VIP customers, key candidates, partners, senior direct reports
- Preparation needs: files to read, numbers to confirm, people to align with before a meeting

If the source material is incomplete, avoid blocking on minor gaps. State short assumptions and continue.

When sources conflict, use this rule:

- Latest explicit time or date updates override older ones
- Explicit user corrections override inferred history
- Hard deadlines and confirmed meetings outrank soft intentions
- If two items still conflict materially, surface the conflict instead of guessing

If the time horizon is ambiguous, default to the user's requested day. If the user says "tomorrow", translate it into an absolute date in the current timezone before writing the brief.

### 3. Triage with an executive lens

Prioritize by consequence, not by volume. Sort items into these buckets:

- `Must not miss today`: time-bound or high-consequence items that create real downside if missed
- `High leverage today`: items that materially improve revenue, hiring, product, partnerships, or team alignment
- `Delegate or defer`: tasks that do not require the boss personally today
- `Watch list`: items that are not due now but could become a same-day escalation

Use these decision rules:

- Promote any item with a hard external deadline or executive-only approval into `Must not miss today`
- Promote any item involving cash, compliance, major customers, board or investor communication, or key personnel decisions
- Downgrade internal low-impact updates if they can be delegated
- If the day is overloaded, explicitly recommend canceling, delegating, shortening, or moving lower-value items

Apply this ranking sequence:

1. Time-locked and externally committed items
2. Executive-only decisions or approvals
3. Revenue, cash, legal, compliance, and key relationship items
4. Items that unlock multiple downstream actions
5. Internal work that can be delegated or delayed

If there are more than 3 serious items, keep the top 3 in the main section and push the rest into `Watch list` or `Delegate or defer`.

### 4. Build the reminder in boss-first order

Prefer this order unless the user asks for another format:

1. Today's one-line focus
2. Top 3 priorities
3. Hard schedule in chronological order
4. Decisions or approvals waiting for the boss
5. Prep reminders before key meetings
6. Risks if something is missed
7. End-of-day carryover or delegation suggestions

Keep the output short enough to scan in under one minute unless the user asks for a deeper plan.

When the user asks for a "finished version", output the reminder directly instead of explaining the process.

### 5. Write like a chief of staff, not a task app

Use language that is direct, calm, and decision-oriented:

- Emphasize consequence: what happens if this slips
- Emphasize readiness: what to review, whom to call, what number to confirm
- Emphasize ownership: what the boss must do versus what can be delegated
- Emphasize leverage: why this meeting or decision matters today

Avoid noisy reminders such as:

- Long generic to-do lists
- Equal weighting of trivial and strategic items
- Detailed implementation notes unless requested
- Empty urgency words like "important" without saying why

Prefer wording that ties every item to one of these:

- consequence
- decision
- deadline
- leverage
- preparation

### 6. Adapt to the user's actual scenario

Choose the smallest useful format:

- `Morning brief`: first message of the day, focused on priorities and time blocks
- `Meeting prep reminder`: sent before a key meeting, focused on objective, stakes, and prep
- `Travel day brief`: focus on movement constraints, buffers, remote approvals, and essential calls
- `Evening rollover`: summarize unfinished items, delegation, and tomorrow's first priority
- `Assistant mode`: if the input comes from an EA or assistant, turn raw notes into a polished boss-facing agenda

If the user provides only one meeting and one task, still produce a complete executive brief rather than a bare two-line restatement.

### 7. Handle missing or messy inputs gracefully

If the user provides fragmented chat notes, mixed schedules, or partial tasks:

- Consolidate duplicates
- Normalize dates and times
- Surface conflicts or overbooking
- Point out missing preparation information
- Make lightweight assumptions instead of stopping unless the ambiguity changes the priority order materially

Use explicit assumption lines only when needed, for example:

- `Assumption: the meeting is confirmed and happens in the user's local timezone.`
- `Assumption: the unfinished task still remains open because no completion signal was provided.`

### 8. Preserve continuity across days

Look for unfinished items from earlier discussions and decide whether they should appear today.

Carry an item forward when:

- It was promised earlier and is still unfinished
- It has business, legal, financial, or relationship consequences if forgotten
- It is a dependency for today's meetings or decisions

Do not carry an item forward when:

- It was already clearly completed
- It is low leverage and can be safely deferred
- It only adds noise without changing today's decisions

## Output Contract

Every final reminder should answer these questions clearly:

1. What is the boss's main focus today?
2. What are the top priorities?
3. Which schedule items are fixed?
4. What must the boss personally decide, approve, or prepare?
5. What can be delegated, deferred, or dropped?

If any of these answers are missing from the source context, infer cautiously and label the assumption only if it materially affects the recommendation.

## Output Rules

- Open with the answer, not the background.
- Limit the top priorities to 3 unless the user explicitly asks for a longer list.
- Call out any item that has a hard external consequence if missed.
- Separate "must do personally" from "can delegate".
- When there are conflicts, recommend a decision instead of listing everything neutrally.
- If there is unused buffer time, suggest one strategic use for it.
- If the schedule is unrealistic, say so plainly and propose a lighter version.
- If historical context changes the priority ranking, reflect that explicitly.
- If the user provides only a small update, merge it into the existing context instead of rewriting the day from scratch.
- Prefer absolute dates when the user uses relative dates such as "today" or "tomorrow" and the exact day matters.
- If the user asks for reminders in Chinese, output polished Chinese even if the skill instructions are stored in English.

## Default Structure

Use this structure for a standard daily boss-facing reminder. If answering in Chinese, localize the labels naturally.

```md
Main focus:
<One sentence on what the boss must really protect today>

Top 3 priorities:
- <Item 1>; why today: <reason>
- <Item 2>; why today: <business / relationship / risk impact>
- <Item 3>; why today: <business / relationship / risk impact>

Hard schedule:
- <time> <event>; goal: <core outcome>
- <time> <event>; prep: <what to review, confirm, or align>

Approvals or decisions:
- <item>; deadline: <time>; consequence of delay: <impact>

Reminders:
- <easy-to-miss but expensive item>
- <item that needs 15-30 minutes of prep>

Delegate or defer:
- <what can be delegated, to whom, or until when>
```

## Fast Examples

Input pattern:

- Historical record: tomorrow needs a CEO review on pending work
- Latest input: meeting from 10:00 to 11:00 tomorrow
- Latest input: finish organizing skills tomorrow

Expected behavior:

- Convert `tomorrow` into an absolute date using the user's timezone
- Keep the 10:00-11:00 meeting as a hard schedule item
- Keep `organize skills` as a main task
- Mention meeting prep if the meeting outcome affects the task ordering
- Produce a boss-facing reminder rather than a neutral to-do list

## Resources

Read [references/executive-reminder-patterns.md](references/executive-reminder-patterns.md) when you need:

- Boss-facing wording patterns
- More templates for morning, meeting-prep, travel-day, and evening-rollover formats
- Triage guidance for overloaded executive calendars
