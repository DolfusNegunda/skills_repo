---
name: prioritizing-options
description: Order many competing items — features, bugs, bets, backlog — by value against effort using a fit-for-purpose method (RICE, WSJF, MoSCoW, Eisenhower, value/effort), then defend the ranking. Use when the user asks to "prioritize this backlog", "what should we do first", "rank these features", "sequence the roadmap", or has more work than capacity. Produces a transparent, sequenced list with the scoring method and its rationale, not a gut order.
---

# Prioritizing Options

## Scope
Sequencing many competing items by value and effort (or cost of delay) with a
method matched to the situation, and justifying the order. For ranking a list, not
scoring a few finalists against weighted criteria — that is
[building-decision-matrices](../../business/building-decision-matrices/SKILL.md).

## Purpose
Turn an overwhelming, contested list into a defensible sequence so the highest-value
work gets done first — making value, effort, and trade-offs explicit instead of
prioritizing by whoever argues loudest.

## When to use this skill
- "Prioritize the backlog / what do we do first / rank these features."
- More candidate work than capacity to deliver it.
- Sequencing a roadmap or triaging incoming requests.

## When NOT to use this skill
- Scoring a few finalists on weighted criteria → [building-decision-matrices](../../business/building-decision-matrices/SKILL.md).
- Setting the goals the work serves → [setting-okrs](../../business/setting-okrs/SKILL.md).
- Choosing under deep uncertainty with no data → [deciding-under-uncertainty](../deciding-under-uncertainty/SKILL.md).

## Inputs
- The full list of candidate items and the objective they serve.
- A sense of each item's value/impact, effort/cost, and any deadlines or dependencies.
- Capacity available and who owns the call.

## Outputs
- A ranked, sequenced list with each item's score (or tier), the method used, and a
  short rationale — plus what was cut and why.

## Workflow
```
Progress:
- [ ] 1. Frame the objective and gather the full candidate list
- [ ] 2. Pick a prioritization method that fits the goal and data
- [ ] 3. Estimate value and effort/cost per item on a consistent scale
- [ ] 4. Score and rank; surface dependencies and hard deadlines
- [ ] 5. Sanity-check the order against capacity and intuition
- [ ] 6. Record the method, ranking, and rationale; state what was cut
```

**Step 1 — Frame.** Name the objective the ranking serves; items are ranked *toward*
that goal, not in the abstract. Include everything competing for the same capacity.
**Step 2 — Pick a method.** Match it to the situation (see Decision framework); one
method, applied consistently, beats mixing several. **Step 3 — Estimate.** Score
value and effort on one anchored scale each; reuse [estimating-under-uncertainty](../estimating-under-uncertainty/SKILL.md)
when data is thin. **Step 4 — Rank.** Compute and order; pull out dependency chains
(a blocker outranks what it blocks) and fixed deadlines as overrides. **Step 5 —
Sanity-check.** Draw the capacity cut-line; if the top of the list is all huge bets
or the order defies obvious sense, revisit the estimates. **Step 6 — Record.** Keep
the scores and reasoning so the order can be challenged and re-run.

## Principles
1. **Rank toward an objective,** never in the abstract.
2. **Value against effort** — a high-value item that costs a year may lose to two quick wins.
3. **One consistent method,** applied to every item.
4. **Cost of delay matters** — time-sensitive value decays; WSJF captures it.
5. **Estimates are rough by design;** precision to two decimals is theatre.
6. **The score informs the sequence;** dependencies and deadlines can override it.

## Decision framework
- **Impact + confidence + reach, divided by effort?** RICE — good for feature backlogs.
- **Time-sensitive value / cost of delay?** WSJF — good for flow and economic sequencing.
- **Must / should / could / won't buckets?** MoSCoW — good for scope negotiation and releases.
- **Urgent vs important quadrants?** Eisenhower — good for personal or ops triage.
- **Quick, few items, rough data?** 2×2 value/effort grid — do the high-value/low-effort first.
- **Deep uncertainty, no comparables?** Stop scoring → [deciding-under-uncertainty](../deciding-under-uncertainty/SKILL.md).

## Common mistakes
- **False precision** — ranking on RICE scores to two decimals built on guessed inputs.
- **Ignoring effort** — sorting by value alone and drowning in expensive items.
- **Ignoring cost of delay** — treating a decaying opportunity like an evergreen one.
- **Mixing methods** mid-list so scores aren't comparable.
- **Prioritizing without an objective** — every item looks important in isolation.
- **No cut-line** — a ranked list nobody uses to say no.
- **Recency/loudest-voice bias** overriding the scores silently.

## Validation checklist
- [ ] Objective stated; full candidate list captured.
- [ ] One method chosen and justified for the situation.
- [ ] Value and effort estimated on consistent, anchored scales.
- [ ] Dependencies and hard deadlines identified as overrides.
- [ ] Capacity cut-line drawn; what's below the line named.
- [ ] Ranking sanity-checked against intuition; outliers investigated.
- [ ] Method, scores, and rationale recorded so the order is defensible.

## Edge cases
- **Everything is "priority one":** force a strict order or MoSCoW buckets; ties are a refusal to choose.
- **Dependencies dominate:** sequence by the dependency graph first, then prioritize within what's unblocked.
- **Incomparable units (revenue vs risk vs debt):** normalize to a common scale or run separate tracks.
- **Estimates wildly uncertain:** widen to tiers (T-shirt sizes) rather than fake point scores.
- **Political items:** score them anyway; make the override explicit if leadership reprioritizes.

## Related skills
- [building-decision-matrices](../../business/building-decision-matrices/SKILL.md) — scoring a few finalists on weighted criteria.
- [estimating-under-uncertainty](../estimating-under-uncertainty/SKILL.md), [analyzing-tradeoffs](../analyzing-tradeoffs/SKILL.md), [decomposing-problems](../decomposing-problems/SKILL.md).
- [setting-okrs](../../business/setting-okrs/SKILL.md), [planning-projects](../../business/planning-projects/SKILL.md), [deciding-under-uncertainty](../deciding-under-uncertainty/SKILL.md).

## Examples
**Input:** "We have 40 backlog items and one quarter — what ships?"
**Output:** Objective set (activation lift). RICE applied on a 1–5 reach/impact scale,
confidence as %, effort in person-weeks; list ranked; two dependency chains pulled
forward as blockers; capacity cut-line drawn at 12 items. Top tier: three
high-reach/low-effort wins plus one big bet justified by cost of delay. Below the
line named explicitly so stakeholders see what "no" means. Scores recorded for re-run.

## Automation opportunities
- Compute RICE/WSJF scores and re-rank automatically as inputs change.
- Flag items above the capacity cut-line vs below it in the tracker.
- Surface dependency violations (a blocked item ranked above its blocker) automatically.
