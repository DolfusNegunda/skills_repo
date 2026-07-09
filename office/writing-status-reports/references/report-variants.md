# Report Variants and RAG Definitions

## Contents
- Choosing a variant
- Variant 1: Individual
- Variant 2: Team roll-up
- Variant 3: Executive
- Variant 4: Client
- RAG status definitions
- RAG edge cases

## Choosing a variant

| Variant      | Reader                          | Length    | Detail level |
| ------------ | ------------------------------- | --------- | ------------ |
| Individual   | Your direct manager             | 1/2 page  | Task-level |
| Team roll-up | Department head / PMO           | 1 page    | Workstream-level, attributed |
| Executive    | Leadership / steering committee | 1/3 page  | Outcome + risk only |
| Client       | External stakeholder            | 1 page    | Outcome-level, externally safe |

If the reader is unknown, ask. If the report will be rendered by
`producing-branded-documents`, it is almost always the **client** variant.

## Variant 1: Individual

One person reporting up. The reader knows the project context, so skip
background and get to specifics.

- Include task-level detail, ticket references, and effort notes if useful.
- Blockers may name colleagues directly ("waiting on review from Sam").
- Honest about struggles — this is the variant where "this took longer than
  expected because X" belongs.
- The upcoming section doubles as a commitment list for next period.

## Variant 2: Team roll-up

Several individual updates merged into one report for a department head or PMO.

- Organize by **workstream**, not by person; attribute within each line
  ("Dashboard rebuild 3/8 complete (Priya)").
- Deduplicate: two people reporting the same milestone is one line.
- Surface cross-team dependencies as blockers even if no individual flagged
  them as such.
- The roll-up's RAG is the **worst** credible workstream status, not an
  average (see RAG edge cases below).

## Variant 3: Executive

Leadership wants trajectory and decisions, not activity.

- The summary carries the whole report: status, trend since last period, the
  one biggest risk, and any decision needed — in 3-4 sentences.
- Cap each list at 3 items; merge or cut the rest.
- Every blocker ends with the ask: what decision or intervention is needed,
  from whom, by when.
- No names below director level, no ticket numbers, no tool jargon.

## Variant 4: Client

External-facing. This is the variant whose JSON feeds
`producing-branded-documents` for the branded Word/PDF deliverable.

- Outcomes and value, never internal process ("validated data across all 12
  source systems", not "closed 14 Jira tickets").
- Blockers that require **client action** are stated plainly and dated — this
  is the report's most important job.
- Internal-only problems (staffing churn, tooling pain) are omitted or recast
  as their delivery impact; never air internal laundry.
- No internal staff surnames unless the client already works with them; no
  internal system names.
- Tone: confident and factual. Amber/Red is fine — surprise is what damages
  trust, not color.

## RAG status definitions

`overall_status` must be exactly one of these three values.

**Green** — On track. Deliverables and dates hold. Any open issues have a
known fix inside the current plan and need nothing from the reader.

**Amber** — At risk. A specific, named threat to scope, schedule, or quality
exists, with a credible recovery path. Amber is a request for attention: the
report must say what would return the project to Green and who acts.

**Red** — Off track. A commitment (date, scope, or quality bar) will be
missed, or already has been, without intervention beyond the team's control.
Red is a request for a decision: replan, add resource, cut scope, or accept
the slip. Name the options.

## RAG edge cases

- **Blocker on the critical path, unresolved for more than one reporting
  period** → at least Amber, regardless of everything else going well.
- **Roll-ups**: overall status is the worst workstream status unless that
  workstream is genuinely non-critical — say so explicitly if you hold Green.
- **Recovered this period**: if last period was Amber/Red and the risk is
  cleared, report Green and say what cleared it. Don't silently snap back.
- **No data**: if updates are too thin to judge, that is itself Amber — you
  cannot certify Green on missing information.
- **Never use intermediate values** ("Green/Amber", "trending Red"). Pick
  one; put the trend in the summary.
