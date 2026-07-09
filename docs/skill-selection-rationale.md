# Why These Skills — Research & Selection Rationale

A defensible, evidence-backed justification for the first batch of skills. Use it
to explain the roadmap to stakeholders. Companion to
[skills-catalog.md](skills-catalog.md) (the full backlog) and
[branded-templates-design.md](branded-templates-design.md).

> **On sources:** figures below come from industry research (Microsoft, McKinsey,
> Deloitte, Asana, APQC) and vendor/analyst reports. Vendor numbers can be
> optimistic, but the direction is consistent across independent sources: office
> time is dominated by communication, reporting, searching, and reformatting —
> exactly the work these skills target.

## Selection method

Each candidate skill was scored on three axes, and the first batch is the set
that scores High on all three:

1. **Frequency** — how often the task recurs across roles. High-frequency tasks
   compound: a small per-use saving × thousands of uses = large impact.
2. **Impact** — time and quality gain per use, and whether it removes a
   recognized pain (not a nice-to-have).
3. **Feasibility** — can a *skill* deliver it **today** with no external
   integration? We split "🟢 works today" (pure procedure/knowledge) from
   "🔌 needs integration" (live email, calendar, ERP → requires MCP). The first
   batch is deliberately all 🟢.

Two structural filters (from earlier analysis) also applied:
- **Skill, not app.** We excluded telephony/scheduling/RPA use cases that are
  really SaaS products, not skills.
- **Thin layer, not reimplementation.** Document skills ride on top of built-in
  document generation and company templates — they don't re-solve file internals
  (which is also a licensing boundary with Anthropic's source-available doc skills).

## The macro evidence (why *office/document* skills at all)

- Office workers spend **~57% of time communicating** and **~43% creating**
  documents; the average worker gets **117 emails/day**.
  ([Microsoft Work Trend Index](https://www.microsoft.com/en-us/worklab/work-trend-index/breaking-down-infinite-workday))
- The average knowledge worker spends **~60% of time on "work about work"** —
  status updates, searching, coordinating — not the actual job.
  ([Asana Anatomy of Work](https://asana.com/resources/why-work-about-work-is-bad))
- **~25% of knowledge workers' time is lost** to productivity drains.
  ([APQC](https://www.apqc.org/about-apqc/news-press-release/apqc-survey-finds-one-quarter-knowledge-workers-time-lost-due))

Communication, reporting, searching, and reformatting are the biggest sinks — and
each maps directly to a first-batch skill.

---

## Per-skill rationale (first batch)

### 1. `summarizing-meeting-notes` 🟢
**Pain:** meetings are constant, and their output evaporates. Capturing notes +
action items while listening exceeds working memory, and **~70% of new
information is forgotten within 24 hours** without reinforcement; action items
never written down are almost never completed.
([Auto Interview AI](https://www.autointerviewai.com/blog/ai-meeting-notes-action-items-accountability-gap-2026))
**Impact:** poorly-run meetings cost U.S. businesses **>$399B/year**, and **71%
of attendees** call meetings unproductive — largely due to weak follow-through.
([Fellow](https://fellow.ai/blog/how-to-manage-meeting-tasks-and-action-items/))
**Why first:** highest frequency (every role, most days), zero integration, and it
attacks a quantified, universally-felt failure. It also feeds every other skill
(action items → status reports).

### 2. `drafting-business-email` 🟢
**Pain:** email is the single largest recurring communication load — **117
emails/day**, and the heaviest quartile spends **8.8 hours/week** on email; workers
spend **11+ hours/week** reading, writing, and sorting messages.
([Microsoft](https://www.microsoft.com/en-us/worklab/work-trend-index/breaking-down-infinite-workday),
[Asana](https://asana.com/resources/why-work-about-work-is-bad))
**Impact:** drafting/replying/rewriting to house tone cuts the per-message cost of
the biggest daily task; quality and consistency improve for client-facing mail.
**Why first:** maximum frequency, universal across roles, no integration for the
drafting itself (sending can be added later via MCP).

### 3. `writing-status-reports` 🟢
**Pain:** status reporting is the core of "work about work." Workers lose **1.7
hrs/week repeating the same updates** and **~352 hrs/year "talking about work."**
In finance specifically, **variance analysis + management reporting are rated the
highest-effort, lowest-value** use of team time.
([Asana](https://asana.com/resources/why-work-about-work-is-bad),
[Deloitte CFO Signals via Tellius](https://www.tellius.com/resources/blog/14-best-ai-tools-for-finance-teams-in-2026))
**Impact:** turns scattered updates into a consistent weekly report in minutes;
directly targets the largest single category of wasted time.
**Why first:** high frequency for PMs, leads, and finance; no integration; and it
is the content engine for `producing-branded-documents`.

### 4. `summarizing-long-documents` 🟢
**Pain:** people can't find or absorb what they need. Employees spend **~50% of
their time looking for information and only 5–15% reading/reviewing it**; searching
alone eats **~20–30% of the workweek** (McKinsey: ~1.8 hrs/day).
([Cottrill Research](https://cottrillresearch.com/various-survey-statistics-workers-spend-too-much-time-searching-for-information/))
**Impact:** condensing contracts/reports/policies to an exec summary + risks
collapses hours of reading into minutes and improves decisions.
**Why first:** universal, no integration, and a clean showcase of what a skill
does better than manual effort.

### 5. `formatting-to-brand` / `producing-branded-documents` 🟢
**Pain:** teams waste time reformatting and recreating branded assets. Employees
spend **~2.5 hrs/week searching for brand assets**, teams lose **~16% of time to
revisions/rework**, and teams recreate assets because they can't find or trust
existing ones.
([Ironmark](https://ironmarkusa.com/inconsistent-branding/),
[PaletteCheck](https://palettecheck.ai/blog/why-most-creative-teams-struggle-with-consistency-and-how-to-fix-it))
**Impact:** centralizing templates and brand assets cuts asset recreation **~40%**
and search time **~60%**; digital, maintained templates yield **~40% faster asset
creation** — and brand consistency correlates with **~23% growth**.
([Ironmark](https://ironmarkusa.com/inconsistent-branding/))
**Why first:** it's the rendering layer that makes the other skills produce
*shippable* deliverables, and it enforces one standard across every team — the
governance win, not just a time win. (Built and validated end-to-end; see the
`producing-branded-documents` skill.)

---

## Why the rest are deferred (not dropped)

The backlog skills are valuable but score lower on **feasibility** or **reach**
right now:

- **Integration-dependent (🔌):** finance reconciliation, calendar management,
  and PM task-sync need MCP connectors to live systems. High impact, but not
  deliverable as a pure skill today — promote once connectors are approved.
- **Role-narrow:** HR (`writing-job-descriptions` — 65% of HR already use AI here,
  per [AIHR](https://www.aihr.com/blog/generative-ai-in-hr/)) and sales
  (`responding-to-rfps` — 30–60% time savings, per
  [Loopio](https://loopio.com/blog/best-ai-software-rfp-responses/)) are strong
  but serve one department, so they rank behind cross-cutting skills that serve
  everyone.
- **Reception:** mostly telephony/scheduling = apps, not skills. The
  skill-appropriate slice is thin, so it's low priority.

Sequencing rule: **ship cross-cutting 🟢 skills first** (widest reuse, no
dependencies), then role-specific 🟢, then 🔌 as integrations land.

## How we'll know it worked (measure, don't assume)

For each shipped skill, track a simple before/after:
- **Adoption:** uses per week (does it trigger on real requests?).
- **Time saved:** self-reported minutes per use × frequency.
- **Quality/consistency:** for branded docs, % of deliverables passing the
  validation gate on first try; fewer reformatting rounds.
- **Coverage gaps:** requests where the skill *should* have fired but didn't →
  feed back into the description (the top driver of skill discovery).

This mirrors the evaluation-first approach in the skill-authoring guidance:
measure the gap, ship the minimal skill, iterate on observed behavior.
