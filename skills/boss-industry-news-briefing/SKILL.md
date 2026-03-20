---
name: boss-industry-news-briefing
description: Collect and synthesize the latest domestic and international industry news for bosses, founders, and executives. Use when Codex needs to browse the web, verify recency, and turn industry developments into a decision-oriented briefing, news digest, policy scan, competitor watch, board-style update, or executive summary for a specific sector, company, theme, or geography.
---

# Boss Industry News Briefing

## Overview

Use this skill to gather the newest industry information and convert it into an executive briefing that is short, reliable, and decision-oriented.

Prioritize what changed, why it matters, what the business impact is, and what action the boss should consider next.

## Workflow

### 1. Define the briefing scope

- Identify the industry or theme first: for example AI, robotics, energy storage, retail, consumer tech, SaaS, advanced manufacturing, biotech, or cross-border e-commerce.
- Identify the geography next: China only, overseas only, or both.
- Identify the decision lens: policy, market demand, pricing, supply chain, capital markets, regulation, competition, or technology roadmap.
- If the user did not specify an industry, infer from the surrounding project context when it is obvious. Ask one concise question only when the ambiguity would materially change the source set.

### 2. Gather the latest information

- Always browse the internet for latest-news requests. Do not answer from memory when recency matters.
- Search both Chinese and English so domestic and international developments are both covered.
- Prefer primary sources first: regulators, ministries, listed-company filings, company newsrooms, investor relations pages, earnings releases, exchange announcements, industry associations, and official statistics.
- Use reputable secondary sources to expand coverage and context after primary-source collection.
- Read [references/source-strategy.md](./references/source-strategy.md) when you need source tiers, search patterns, or verification rules.

### 3. Verify significance and recency

- Use exact publication dates in the final answer. Do not rely on relative wording like "today" or "recently" without anchoring it to an absolute date.
- Separate confirmed facts from inference. If you infer an implication, label it as an implication or likely impact.
- Cross-check major claims with at least two independent sources unless the claim comes directly from a primary source.
- De-prioritize commentary pieces, reposts, thin summaries, and undated pages.
- If a development cannot be verified, say so explicitly and exclude it from the top findings.

### 4. Filter for boss relevance

- Lead with only the handful of developments that could change revenue, cost, margin, market access, valuation, supply continuity, product timing, or strategic positioning.
- Favor developments with a clear executive implication:
  - policy or regulatory changes
  - competitor moves
  - large financing, M&A, or IPO activity
  - major partnerships or customer wins
  - pricing shifts
  - supply-chain bottlenecks
  - technology breakthroughs or commercialization milestones
- Cut low-signal items such as generic conference recaps, opinion columns, repeated rumors, and weakly sourced trend pieces.

### 5. Write for executive consumption

- Start with a one-screen summary.
- For each key development, answer four questions:
  - What happened?
  - Why does it matter?
  - What is the likely business impact?
  - What should leadership watch or do next?
- Keep the tone crisp and neutral. Avoid storytelling and avoid jargon unless it changes meaning.
- Prefer short bullets or a compact table over long paragraphs.
- Read [references/executive-brief-template.md](./references/executive-brief-template.md) when you need briefing formats.

## Output Modes

### Flash Alert

Use when the user needs a fast answer on a breaking event.

- Return the event, exact date, why it matters, and the immediate watchpoints.
- Keep it under 8 bullets unless the user asks for detail.

### Daily Brief

Use when the user wants the latest domestic and international updates for a sector.

- Cover the top 5 to 10 items only.
- Group them into China, global, and cross-border implications when helpful.

### Weekly Executive Scan

Use when the user wants a higher-level management view rather than raw headlines.

- Organize around themes, not chronology.
- Include a short "what changed vs last week" section when the comparison period is known.

### Competitor or Policy Watch

Use when the user asks about a named company, competitor set, or regulation-driven market.

- Focus on actions and consequences, not general market chatter.
- Highlight what is confirmed, what is emerging, and what remains uncertain.

## Non-Negotiable Rules

- Always use browsing for current-news tasks.
- Always include source links for factual claims that matter.
- Always include exact dates for major events.
- Always distinguish facts, interpretation, and recommendation.
- Always say when evidence is thin or conflicting.
- Never overload the user with a long undifferentiated news dump.
- Never treat a single media report as settled fact when the claim affects major decisions.

## Source Coverage Checklist

Before finalizing, make sure the briefing covers the most relevant parts of this checklist:

- domestic policy and regulation
- domestic market and competitors
- global policy and regulation
- global market and competitors
- capital markets and funding activity
- major customer, supply-chain, or pricing signals
- technology and product milestone shifts

## Example Requests

- "Use this skill to give me today's key AI industry updates in China and the US for a CEO."
- "Summarize the latest robotics developments that could affect manufacturing margins and supply chains."
- "Give me a board-style weekly scan of domestic and overseas energy-storage news."
- "Track policy, competition, and financing news for cross-border e-commerce this week."
