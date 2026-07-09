# Office Skills Catalog & Research

A research-backed backlog of skills to build for everyday office users. Use it to
decide what to build and in what order. Every entry follows the house style in
[../skill-builder/SKILL.md](../skill-builder/SKILL.md).

## What the research says

- Office workers spend **~57% of their time communicating** (email, meetings,
  chat) and **~43% creating** (docs, spreadsheets, slides). The average worker
  gets **117 emails/day** and struggles with focus and information-finding.
  ([Microsoft Work Trend Index](https://www.microsoft.com/en-us/worklab/work-trend-index/breaking-down-infinite-workday))
- **Administrative work consumes up to 40%** of a knowledge worker's time; the
  most-automatable tasks are email, data entry, reporting, scheduling, invoice
  handling, and document filing.
  ([Jotform](https://www.jotform.com/blog/administrative-automation/))
- Finance teams spend **up to 60% of their time on data gathering and
  reconciliation**, and **variance analysis + management reporting are rated the
  highest-effort, lowest-value** use of their time.
  ([Deloitte CFO Signals via Tellius](https://www.tellius.com/resources/blog/14-best-ai-tools-for-finance-teams-in-2026))
- **65% of HR professionals** already use AI to draft job descriptions; policy
  Q&A, onboarding kits, and offer letters are top document use cases.
  ([AIHR](https://www.aihr.com/blog/generative-ai-in-hr/))
- Project managers get the most value from **meeting-notes → action-items** and
  **auto-generated status reports**.
  ([The Digital Project Manager](https://thedigitalprojectmanager.com/tools/best-ai-project-management-tools/))
- Sales/BD teams cut proposal and RFP drafting time **30–60%** with AI first
  drafts from past-approved content.
  ([Loopio](https://loopio.com/blog/best-ai-software-rfp-responses/))

**Takeaway:** communication and document work dominate every office role, and
they are exactly what a skill does well.

## The framing filter (read before proposing any skill)

A **skill** is a reusable procedure + knowledge that Claude follows. It is *not*
a SaaS app. Two rules that shape this whole catalog:

1. **Skill vs. app.** Skills excel at drafting, transforming, extracting,
   summarizing, formatting, and analyzing *content you give Claude*. They do
   **not** natively place phone calls, send live email, read your calendar, or
   query an ERP. Those need an **MCP integration**. Each skill below is tagged:
   - 🟢 **Works today** — pure procedure/knowledge, no integration needed.
   - 🔌 **Needs integration** — requires an MCP connector for live email,
     calendar, or a business system to reach full value (the drafting half still
     works today).

2. **Thin layer, not reimplementation.** Claude Code / claude.ai already generate
   Word, PDF, PowerPoint, and Excel files. Anthropic's `docx/pdf/pptx/xlsx`
   skills that power this are **source-available (no copying/derivatives)**. So
   our document skills must be **thin house-style layers** — "produce a deck with
   *these sections, our brand, our tone, this review checklist*" — that ride on
   top of the built-in document capability. **Never re-solve OOXML/PDF
   internals.** This respects the license and puts effort where the value is:
   company conventions, not file-format plumbing.

## Priority scoring

Each skill is scored **Frequency × Impact × Feasibility** (each High/Med/Low).
"Feasibility" drops when a skill needs integration or heavy company-specific
templates. Start where all three are High.

---

## Tier 0 — Start here (cross-cutting, every role)

These serve everyone, so they get reused far more than any role-specific skill.
Build these first.

| Skill | What it does | Tag | F×I×Feas |
|---|---|---|---|
| **`summarizing-meeting-notes`** | Turn raw notes/transcripts into a structured summary with decisions, action items (owner + due date), and open questions, in a house format. | 🟢 | H·H·H |
| **`drafting-business-email`** | Draft/reply/rewrite emails in company tone, with variants (formal, brief, escalation). Paste the thread; get the draft. | 🟢 | H·H·H |
| **`formatting-to-brand`** | Apply company colors, fonts, headings, and boilerplate to any doc/deck/report the user is producing. A house-style layer over built-in generation. | 🟢 | H·H·M |
| **`summarizing-long-documents`** | Condense contracts, reports, or policies into an exec summary + key points + risks, at a chosen length. | 🟢 | H·H·H |
| **`writing-change-notes`** | Turn a set of changes (release, process, policy) into structured change notes / release notes in the company template. | 🟢 | M·H·H |

## Tier 1 — Finance

| Skill | What it does | Tag | F×I×Feas |
|---|---|---|---|
| **`explaining-budget-variances`** | Given actuals-vs-budget data, write clear P/V/M variance narratives ("revenue up 8% driven by…"). Targets the highest-effort/lowest-value finance task. | 🟢 | H·H·M |
| **`building-financial-reports`** | Assemble a monthly/quarterly report (commentary + tables) to the finance template, from provided figures. Thin layer over spreadsheet/doc generation. | 🟢 | H·H·M |
| **`drafting-cfo-narratives`** | Turn a numbers pack into a board/CFO-ready narrative with consistent framing. | 🟢 | M·H·M |
| **`reconciling-transactions`** | Match transactions across statements/ledgers and flag exceptions. Full value needs a data/ERP connector. | 🔌 | M·H·L |

## Tier 1 — Project Management

| Skill | What it does | Tag | F×I×Feas |
|---|---|---|---|
| **`writing-status-reports`** | Turn task updates/notes into a weekly status report: done, in-progress, blockers, upcoming, RAG status. | 🟢 | H·H·H |
| **`extracting-action-items`** | Pull owners, deadlines, and next steps from meeting notes into a tracked list. (Pairs with Tier-0 meeting notes.) | 🟢 | H·H·H |
| **`drafting-project-plans`** | Generate a project charter / plan (scope, milestones, risks, RACI) from a brief, in the PMO template. | 🟢 | M·H·M |
| **`syncing-project-tasks`** | Create/update tasks in Jira/Asana/Planner from notes. Needs an MCP connector. | 🔌 | M·M·L |

## Tier 2 — HR

| Skill | What it does | Tag | F×I×Feas |
|---|---|---|---|
| **`writing-job-descriptions`** | Draft consistent, inclusive JDs from a role brief, in the company format. Highest-adopted HR use case. | 🟢 | H·H·H |
| **`drafting-hr-documents`** | Offer letters, onboarding kits, and policy docs from templates + inputs. | 🟢 | M·H·M |
| **`answering-policy-questions`** | Answer employee questions from the company handbook (grounded in provided policy docs). | 🟢 | M·H·M |

## Tier 2 — Sales / Business Development

| Skill | What it does | Tag | F×I×Feas |
|---|---|---|---|
| **`drafting-proposals`** | First-draft proposals/SOWs from a brief + reusable content blocks, in the company template. | 🟢 | M·H·M |
| **`responding-to-rfps`** | Draft RFP/questionnaire answers from an approved answer library you provide. | 🟢 | M·H·M |
| **`writing-sales-followups`** | Post-meeting recap + tailored follow-up emails. | 🟢 | M·M·H |

## Tier 3 — Reception / Front Office (deliberately thin)

Most receptionist AI is telephony/scheduling — that's **apps, not skills**. The
skill-appropriate slice is narrow; don't pad it.

| Skill | What it does | Tag | F×I×Feas |
|---|---|---|---|
| **`drafting-front-office-comms`** | Visitor notices, internal announcements, room-booking confirmations, standard reply templates. | 🟢 | M·M·H |
| **`coordinating-meetings`** | Draft agendas, invites, and logistics docs (not live calendar booking). | 🟢 | M·M·H |
| **`managing-calendar`** | Read/schedule/reschedule on a real calendar. Needs an MCP connector. | 🔌 | M·M·L |

---

## Recommended first batch (build these 5)

Ranked by frequency × impact × feasibility, and chosen so the first releases
serve the widest audience:

1. **`summarizing-meeting-notes`** — every role, every day, zero integration.
2. **`drafting-business-email`** — the single biggest time sink (117 emails/day).
3. **`writing-status-reports`** — high value for PMs and anyone reporting upward.
4. **`summarizing-long-documents`** — universal, and a clean showcase of the format.
5. **`formatting-to-brand`** — the house-style layer the others can reuse.

These five are all 🟢 works-today, need only company templates as input, and
together cover the communication + document work that dominates every role.

## Backlog

Everything in Tiers 1–3 not in the first batch. Revisit after the first batch
ships and you've gathered feedback. Promote **🔌 needs-integration** skills
(finance reconciliation, calendar, task sync) only once the relevant MCP
connectors are available and approved.

## How to build each one

For every skill: `Using skill-builder, create a skill for <name>`. It will run
the scope → name → description → draft → split → checklist → test workflow. Feed
it your company's real templates and tone examples so the output matches house
style — that domain input is what turns a generic draft into a valuable skill.
