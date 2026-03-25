# China Contract Playbook

Use this file when the drafting task needs clause choices, risk controls, or PRC-specific business-legal defaults.

## 1. Intake Checklist

Normalize the business facts into this grid before writing:

| Field | What to capture |
| --- | --- |
| Transaction type | service, deployment, memo, framework, supplemental agreement |
| Parties | full names, entity type, role, contact person, registration / tax data if provided |
| Background | what the cooperation is for and whether a proposal or quote already exists |
| Scope | service items, deliverables, milestones, function modules, exclusions |
| Money | total fee, staged fee, tax status, invoice arrangement, variable pricing |
| Time | service term, implementation cycle, acceptance window, renewal / expiration |
| Risk | data, IP, account access, platform policy, customer assets, exclusivity, settlement |
| Dispute | governing venue or court clause if specified |

## 2. Contract-Type Decision Rules

### Use a service contract when:

- the core deal is operation support,陪跑, training, consulting, or software usage support
- the deliverable is ongoing service rather than a custom-built system

### Use a development / deployment contract when:

- the deal contains POC, testing, formal deployment, API integration, maintenance, or custom modules
- acceptance depends on milestone completion or system functionality

### Use a cooperation memo or framework agreement when:

- the parties need to confirm principles, channels, market coordination, or exclusivity first
- settlement, detailed pricing, or detailed execution rules will be fixed later

## 3. Clause Library

### Cooperation objective / background

Use this to connect the draft to the actual proposal. State:

- why the parties cooperate
- what the main solution or project is
- whether the service is based on a prior quote sheet, proposal, or discussed mechanism

### Scope and exclusions

Write the scope precisely enough to avoid later disputes. For module-heavy projects:

- list the module or service package by section
- identify included and excluded items
- state whether later additions require a supplemental agreement or new fee

Always state exclusions when the source context already includes them. Example categories:

- account unblocking not included
- optional module not included unless separately purchased
- traffic volume is a service workload standard, not a guaranteed conversion result
- third-party platform fees are borne separately unless explicitly included

### Fees and payment

Use the user's structure exactly when provided. Otherwise choose the pattern that best matches the deal:

- one-off service / simple tool authorization: sign + pay within a short fixed period
- POC + formal deployment: POC full payment first, then formal deployment prepayment and acceptance tail payment
- recurring operation service: sign + monthly / quarterly payment, with renewal handled separately
- variable usage: define base package, overage unit price, settlement timing, and trigger point

Do not merge distinct pricing logic into a vague total if the business deal has separate modules, optional items, or staged deployment.

### Acceptance

For implementation or system delivery, define:

- completion notice by乙方
- acceptance period by甲方
- written objection deadline
- remediation period
- deemed acceptance if no written objection is raised in time

For ongoing services, acceptance can be tied to period-end confirmation, monthly report acceptance, or delivery of agreed outputs.

### Confidentiality and data

If the project involves enterprise WeChat, CRM, chat archives, customer lists, or AI data:

- define the business data as confidential
- limit each side to contract-purpose use
- prohibit unauthorized disclosure or out-of-scope use
- require lawful handling of personal information and customer data
- separate platform restrictions from contractual obligations

Keep in mind PRC-style data compliance concerns, especially under practical business expectations related to the Civil Code, PIPL, Data Security Law, and Cybersecurity Law. Do not write expansive rights to reuse the other side's customer data unless the deal explicitly allows it.

### Intellectual property

Use the correct ownership model:

- pure service / operation support: each side retains pre-existing IP; service outputs are used per contract
- software tool authorization:乙方 retains platform / tool IP,甲方 gets agreed usage rights
- custom development / agent deployment:乙方 usually retains base platform, framework, and underlying algorithms;甲方 gets the agreed business-use rights to the project results unless exclusivity or transfer is expressly negotiated
- reports or client data generated in the cooperation: usually belong to the party paying for or originating them, subject to contract wording

### Breach liability

Keep breach liability proportional and tied to the nature of the breach:

- payment delay: small daily percentage, right to suspend service after a reasonable grace period
- service non-conformity: remediation first, then refund / reduction / termination if unfixable
- confidentiality or IP breach: higher liquidated damages may be justified, but avoid obviously detached numbers
- unilateral termination: set a fixed percentage only if it is commercially defensible

Avoid extremely one-sided terms that would collapse in negotiation or later become hard to enforce.

### Force majeure and third-party platform changes

Separate:

- true force majeure
- government action or major policy adjustment
- platform rule or API policy changes
- failure caused by the non-performing party's own conduct

For enterprise WeChat, ad platforms, AI model APIs, and other third-party systems, make clear that platform-side policy adjustments or technical changes are not automatically a breach by the service provider.

### Dispute resolution

If the user specifies a venue, use it. Otherwise use a practical court clause tied to one party's所在地, usually the service provider's location when drafting from乙方 perspective, or a negotiated neutral venue if the request is balanced.

## 4. Fair-But-Protective Defaults

Use these defaults when the source facts support them:

- unknown entity details: leave blanks
- invoice issuance: after payment receipt within a stated number of working days
- response obligations: commercially reasonable, not impossible SLA promises
- confidentiality survival: 3 years unless the deal requires longer
- acceptance window: 3 to 5 working days is common for commercial cooperation
- remediation period: 3 to 7 working days depending on project complexity

## 5. Business-Specific Flags

### Enterprise WeChat / SCRM / private-domain operation

- distinguish between tool authorization, implementation, and运营陪跑
- exclude illegal or non-compliant account unblocking unless separately contracted
- do not guarantee platform rule exemptions
- define customer asset, chat archive, and employee-operation boundaries

### AI / agent / software deployment

- split POC and formal deployment if the quote does
- tie payment to phase acceptance
- clarify model API, third-party services, and optional modules
- protect base technology and framework IP while granting usable business rights

### Channel / overseas / exclusivity cooperation

- define who can use the official title and in what scope
- define channel ownership or lead routing rules
- if settlement is not final, reserve it for a later written agreement
- avoid over-detailed execution obligations before pricing and legal structure are ready

## 6. Output Rule

When the user asks for a finished contract, output the contract directly in Chinese. Do not preface it with a long explanation. Only add a short assumption note if a missing fact materially changes payment, exclusivity, optional modules, or legal structure.
