# Worked Example: Messy Standup Notes → Structured Summary

Demonstrates the full transformation on realistic raw input, in all three formats. Meeting date is Monday 2026-07-06, so "wed" resolves to 2026-07-08 and "eod fri" to 2026-07-10.

## Input (raw notes, as pasted by the user)

```
platform standup mon 7/6
here: priya, tom, alejandra, sam (rob ooo)

priya - search reindex finished over weekend, 0 dropped docs 🎉
  she'll post perf numbers to #platform by wed
tom - still fighting the flaky checkout e2e test... says its the payment sandbox
  timing out, NOT our code. maybe we should just skip that test?? priya pushed back
  alejandra: lets not decide til we see the sandbox logs. tom pulling logs eod tomorrow
DECIDED: we're going with pg 16 upgrade during the aug 1 maintenance window
  (tom wanted sept but capacity planning says aug)
alejandra - vendor api contract renewal due end of month, legal hasn't responded
  to her 2 emails. escalating?? she'll ping legal director if nothing by fri
sam - onboarding doc rewrite half done, no eta yet
somebody needs to own the oncall handoff checklist before rob is back 7/20 - crickets
```

## Output — canonical (default)

```markdown
# Meeting Summary — Platform Standup
**Date:** 2026-07-06 | **Attendees:** Priya, Tom, Alejandra, Sam (Rob OOO)

## Decisions
- Postgres 16 upgrade will run during the August 1 maintenance window (September was considered but ruled out by capacity planning).

## Action Items
| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | Post search-reindex performance numbers to #platform | Priya | 2026-07-08 |
| 2 | Pull payment-sandbox logs for the flaky checkout e2e test | Tom | 2026-07-07 |
| 3 | Escalate vendor API contract renewal to the legal director if legal has not responded | Alejandra | 2026-07-10 |
| 4 | Finish onboarding doc rewrite | Sam | TBD — no ETA given |
| 5 | Own the on-call handoff checklist before Rob returns (2026-07-20) | UNASSIGNED — no volunteer | 2026-07-20 |

## Risks & Blockers
- Vendor API contract renewal is due end of July and legal is unresponsive (two emails ignored); renewal could slip.
- Flaky checkout e2e test is reducing CI signal; suspected cause is payment-sandbox timeouts, not application code (unconfirmed).

## Open Questions
- Should the flaky checkout e2e test be skipped? Deferred until Tom's sandbox logs are reviewed (Priya opposed skipping).
```

Notes on the transformation:
- "we're going with pg 16 upgrade" is the only settled outcome → the sole decision. "maybe we should just skip that test??" was explicitly deferred → open question, not a decision.
- "eod tomorrow" and "by fri" converted to absolute dates from the 2026-07-06 meeting date.
- "somebody needs to own..." got no volunteer → captured with `UNASSIGNED` rather than dropped or guessed.
- Sam's item has no date in the source → `TBD`, with the source's own wording ("no ETA") preserved.
- Priya's reindex success is context/good news, not an action or decision; it survives only via her follow-up action (item 1).

## Output — quick recap variant

```markdown
**Platform Standup recap (2026-07-06)**
Decided: PG 16 upgrade goes in the Aug 1 maintenance window.
To do: Priya — reindex perf numbers to #platform (due 07-08); Tom — pull payment-sandbox logs for flaky checkout e2e (due 07-07); Alejandra — escalate vendor contract to legal director if no reply (due 07-10); UNASSIGNED — on-call handoff checklist before Rob returns (due 07-20).
Watch: legal unresponsive on vendor renewal (due end of July); skip-the-flaky-test question deferred pending Tom's logs.
```

## Output — formal minutes variant (excerpt)

```markdown
# Minutes — Platform Standup
**Date:** 2026-07-06 | **Time:** — | **Location/Call:** —
**Present:** Priya, Tom, Alejandra, Sam | **Absent/Apologies:** Rob (OOO)
**Chair:** — | **Minutes by:** Prepared from notes

## 1. Agenda Items Discussed
### 1.1 Search reindex
Priya reported the search reindex completed over the weekend with zero dropped documents. Performance numbers will follow in #platform.

### 1.2 Flaky checkout e2e test
Tom attributed ongoing failures to payment-sandbox timeouts rather than application code and proposed skipping the test; Priya objected. Alejandra proposed deferring the decision until sandbox logs are reviewed.

### 1.3 Postgres upgrade scheduling
It was agreed to run the Postgres 16 upgrade during the August 1 maintenance window; a September window was considered and rejected on capacity-planning grounds.

## 2. Decisions
- D1: Postgres 16 upgrade scheduled for the 2026-08-01 maintenance window.

## 3. Action Items
| # | Action | Owner | Due | Raised in |
|---|--------|-------|-----|-----------|
| A1 | Post reindex performance numbers to #platform | Priya | 2026-07-08 | 1.1 |
| A2 | Pull payment-sandbox logs for flaky checkout e2e | Tom | 2026-07-07 | 1.2 |
| A3 | Escalate vendor contract renewal to legal director if no response | Alejandra | 2026-07-10 | — |
| A4 | Finish onboarding doc rewrite | Sam | TBD | — |
| A5 | Own on-call handoff checklist before Rob returns | UNASSIGNED | 2026-07-20 | — |

## 5. Open Questions / Deferred Items
- Skip the flaky checkout e2e test? Deferred pending review of sandbox logs (A2).

## 6. Next Meeting
Not scheduled.
```

## Downstream use

The Action Items table above (task, owner, due, plus the Risks & Blockers list) can be fed directly into the **writing-status-reports** skill to produce a weekly status update without re-reading the raw notes.
