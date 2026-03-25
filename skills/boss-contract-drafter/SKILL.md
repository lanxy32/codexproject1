---
name: boss-contract-drafter
description: China-focused business contract drafting skill for bosses, founders, and commercial teams. Use when Codex needs to draft, redraft, or structure a Chinese cooperation contract, service agreement, deployment contract, memorandum, supplemental agreement, NDA, or other commercial legal document from chat context, prior proposals, quotations, customer names, cooperation scope, fees, payment terms, participants, party information, attachments, or screenshots. Especially useful when earlier conversation already contains a plan or proposal that must be merged into the contract, and when the output should balance transaction protection, enforceability, commercial fairness, and practical PRC legal risk control.
---

# Boss Contract Drafter

## Overview

Draft like a senior PRC commercial counsel serving a boss who wants a usable contract fast. Convert messy business chat, prior proposals, quote sheets, screenshots, and attachment details into a complete Chinese contract that is commercially practical, structurally clear, and fair enough to hold up in negotiation.

Default to polished Chinese legal-business writing. If the user clearly asks from the perspective of `甲方` or `乙方`, protect that side without making the contract obviously one-sided or legally brittle. If no side preference is stated, default to a balanced contract.

## Core Workflow

### 1. Mine the full context before drafting

Treat the contract request as a context-fusion task, not a formatting task. Read and merge:

- the latest user request
- earlier conversation context
- any proposal, plan, pricing sheet, or scope already discussed above
- attached images, tables, or document excerpts
- party names, fee amounts, participants, payment nodes, exclusions, and deadlines

If earlier messages already contain a `方案`, `报价清单`, `合作机制`, `功能模块`, `POC范围`, or other scope definition, use that material as the service baseline and reflect it in the contract text.

### 2. Normalize the intake into a drafting checklist

Extract or infer these fields before writing:

- contract type
- project / cooperation name
- contract role preference: balanced, `甲方` counsel, or `乙方` counsel
- party names and whether each side is a company, partnership, or individual
- contacts / participants
- cooperation scope and exclusions
- deliverables / deployment items / service modules
- service term or project milestones
- fee amount, tax / invoice arrangement, and payment schedule
- acceptance or testing rules
- confidentiality, data, IP, and account / system usage boundaries
- dispute venue if given

If key business data is missing, do not block unless the missing point changes the commercial structure. Use blanks such as `________________` for unknown identity, address, bank, tax, or representative fields. Never invent registration numbers, addresses, bank accounts, official approvals, or promised outcomes.

### 3. Choose the right document form

Use the business substance to choose the instrument:

- `合作合同` / `服务合同`: recurring service,运营陪跑,营销服务,软件工具授权,培训,私域运营
- `开发及部署合作合同`: AI agent, software development, interface build, deployment, testing, maintenance
- `合作备忘录` / `框架合作备忘录`: channel cooperation, market exclusivity, overseas business coordination, settlement principles not fully fixed
- `补充协议`: only when a main contract already exists and the request is clearly incremental

When the commercial points are still preliminary and settlement is not final, prefer a memo or framework agreement over forcing a detailed execution contract.

### 4. Draft the contract around enforceable business facts

Always make the main body match the real deal:

- tie service scope to the prior proposal, quote sheet, or feature list
- convert pricing lines into payment clauses or an annex
- convert staged delivery into staged acceptance and staged payment
- state exclusions explicitly, especially when the user already mentioned them
- distinguish between `服务动作`, `交付物`, `运营支持`, and `商业结果`

Do not casually guarantee sales growth, account unblocking, financing success, policy approval, or other result-based outcomes unless the user explicitly insists and the clause is clearly framed as a commercial commitment.

### 5. Run a PRC legal-risk sanity check

Before finalizing, check whether the draft is commercially fair and legally usable:

- rights and obligations should correspond to actual consideration
- breach clauses should be proportional, not obviously punitive
- acceptance should have a process, deadline, and deemed-acceptance fallback
- payment clauses should match milestones and invoice logic
- confidentiality should survive termination
- data, customer information, and conversation records should have lawful-use boundaries
- IP ownership and usage rights should reflect the deal type
- force majeure, termination, and dispute clauses should be complete

If the deal involves customer data, chat records, enterprise WeChat, CRM, AI models, or cross-border business, apply the extra checks in [references/china-contract-playbook.md](references/china-contract-playbook.md).

## Drafting Rules

### Writing posture

- Write the final contract directly unless the user explicitly asks for analysis first.
- Use Chinese legal-business prose, not literal machine translation.
- Prefer numbered clauses and subclauses.
- Keep titles specific to the transaction.
- Use placeholders for unknown hard facts instead of making them up.

### Fairness and protection

Protect enforceability first, then commercial leverage. Use these rules:

- lean toward the user's side if the role is explicit
- keep payment, acceptance, confidentiality, IP, and termination rights workable for both sides
- avoid unlimited or undefined liability unless the source deal clearly requires it
- separate direct breach liability from platform policy changes, third-party systems, and force majeure
- if the contract excludes a service item, say so plainly

### Missing information

If information is incomplete:

- draft with blanks for registration, address, account, representative, or tax details
- use neutral but practical defaults only when the business pattern is obvious
- mark optional modules, optional features, or variable charges clearly
- if one unresolved point materially changes the money or risk allocation, state a short assumption before the contract

### Prior-context rule

If the conversation above already contains a plan, quote, or solution:

- align the contract name and cooperation objective with that plan
- map scope items into the service content clause
- map milestones into acceptance and payment nodes
- map exclusions and caveats into exclusion or disclaimer clauses
- do not ignore earlier context just because the latest message is brief

## Output Contract

Default structure:

1. contract title and optional contract number
2. party information
3. recitals / cooperation objective if useful
4. definitions or project background when needed
5. service / cooperation content and standards
6. term, milestones, and acceptance
7. fees, tax / invoice, and payment method
8.双方权利义务
9. confidentiality, data compliance, and IP
10. change control, suspension, termination
11. breach liability
12. force majeure
13. dispute resolution
14. miscellaneous
15. signature blocks and `（以下无正文）`

For quote-based or module-based projects, add a table or annex if that makes the scope clearer.

## Scenario Selection

Read [references/example-patterns.md](references/example-patterns.md) when the request resembles one of these patterns:

- enterprise WeChat professional edition, SCRM,陪跑,账号 protection, operation service
- software tools with interface quotas, user caps, install fees, or monthly traffic service
- overseas market, channel exclusivity, official partner naming, Korea / World-OKTA type cooperation
- AI, software, agent, POC, deployment, maintenance, API integration, or optional modules

Read [references/china-contract-playbook.md](references/china-contract-playbook.md) when you need:

- clause selection guidance
- PRC commercial legal-risk checks
- data / IP / invoice / acceptance handling
- fair but protective drafting defaults

## Final Checks

Before sending the contract:

- confirm the contract type matches the business stage
- confirm all fees and payment nodes match the user input
- confirm exclusions are written where needed
- confirm unknown statutory / registration details are left blank, not fabricated
- confirm breach, termination, and dispute clauses are present
- confirm the draft uses the earlier proposal if one existed in context
