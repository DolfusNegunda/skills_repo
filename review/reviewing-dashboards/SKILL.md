---
name: reviewing-dashboards
description: Review dashboards and data reports for decision-fitness, correct chart choices, honest visuals, clarity, and context — producing severity-ranked findings with specific fixes. Use when the user asks to "review this dashboard/report", "is this chart right", "why is this dashboard confusing", or assess a data view before it ships. Inherits the shared severity/scoring model. Produces an actionable review that catches misleading visuals and clutter.
---

# Reviewing Dashboards

## Scope
Evaluation of dashboards and data reports for whether they drive the intended
decision with honest, clear visuals. Inherits method/severity/scoring from
[conducting-structured-reviews](../conducting-structured-reviews/SKILL.md). Building
them is [designing-dashboards](../../office/designing-dashboards/SKILL.md); chart
aesthetics come from the [dataviz](../../office/generating-data-reports/SKILL.md) principles.

## Purpose
Tell the author whether a viewer can answer "how are we doing and what should I do?"
at a glance — and catch the misleading axes, wrong chart types, and clutter that
quietly distort decisions.

## When to use this skill
- "Review this dashboard / data report / KPI view."
- "Is this the right chart? / why is this dashboard confusing?"
- A gate before a dashboard ships to decision-makers.

## When NOT to use this skill
- Building the dashboard → [designing-dashboards](../../office/designing-dashboards/SKILL.md).
- General UI/UX → [reviewing-designs](../reviewing-designs/SKILL.md).
- Underlying data correctness → [reviewing-sql](../reviewing-sql/SKILL.md).

## Inputs
- The dashboard/report, the decision it supports, and its audience (exec/ops/analytical).
- The metrics shown, their targets/benchmarks, and refresh cadence.

## Outputs
- A review: verdict + scores, severity-ranked findings (which chart/tile + issue +
  fix), and strengths.

## Evaluation rubric (dimensions)
1. **Decision-fit** — supports a specific decision for a defined audience; every element earns its place.
2. **Metric selection** — the few metrics that matter; no vanity clutter.
3. **Chart choice** — right visual for each question (trend→line, comparison→bar, etc.).
4. **Visual honesty** — zero-baseline bars, consistent scales, no dual-axis or truncation tricks.
5. **Context** — each number has target/comparison/trend; not bare figures.
6. **Hierarchy & clarity** — layout leads from headline to detail; labels clear; no chartjunk.
7. **Freshness & trust** — refresh cadence shown; stale/no-data states handled.

## Scoring & severity
Score 1–5; rank Blocker→Praise (see
[foundation reference](../conducting-structured-reviews/references/severity-and-scoring.md)).
Examples: **Blocker** = a truncated y-axis exaggerating a trend, misleading the
decision; **Major** = 30 metrics with no hierarchy so the key one is lost; **Minor**
= a pie chart better shown as a bar; **Nit** = inconsistent number formatting.

## Workflow
```
Progress:
- [ ] 1. Confirm the decision, audience, and key metrics
- [ ] 2. Glance test: can you get the headline in ~5 seconds?
- [ ] 3. Check each chart's type and visual honesty
- [ ] 4. Check context (targets/comparisons) and hierarchy/clutter
- [ ] 5. Check freshness and edge states
- [ ] 6. Severity-rank, score, verdict; fixes per finding
```

**Step 2 — the glance test.** If the target user can't get the main answer in a few
seconds, that's the top finding. **Step 3 — honesty first:** misleading visuals
(truncated axes, dual axes, inconsistent scales) are Blocker-level because they
corrupt the decision, even when they look polished.

## Recommended-improvements guidance
Give the fix: change the chart type to match the question, restore a zero baseline,
cut the vanity metrics, add the target/comparison, raise the key KPI in the
hierarchy, or add a freshness stamp and empty-state.

## Validation checklist
- [ ] Decision, audience, and key metrics confirmed.
- [ ] Glance test applied — headline obtainable fast.
- [ ] Each chart type fits its question; visuals are honest (baselines, scales).
- [ ] Every number carries context (target/comparison/trend).
- [ ] Hierarchy clear; clutter/chartjunk removed; labels clear.
- [ ] Freshness and no-data states handled.
- [ ] Findings carry location + severity + a fix; verdict + scores given.

## Common mistakes
- **Missing misleading axes/scales** while critiquing colors.
- **Not applying the glance test** — reviewing tiles, not the decision.
- **Accepting metric overload** — everything shown, nothing understood.
- **Ignoring context** — bare numbers with no target/comparison.
- **No audience frame** — judging an ops dashboard by exec criteria.

## Edge cases
- **Real-time/ops:** thresholds/alerts and stale-data indicators are must-haves.
- **Mobile/TV:** judge legibility and metric count for the medium.
- **Exploratory analytical tools:** more density/interactivity is acceptable; judge by explore-fit.
- **Data correctness suspected:** flag for a [reviewing-sql](../reviewing-sql/SKILL.md) pass; visuals can't fix wrong data.

## Related skills
- [conducting-structured-reviews](../conducting-structured-reviews/SKILL.md), [designing-dashboards](../../office/designing-dashboards/SKILL.md).
- [reviewing-designs](../reviewing-designs/SKILL.md), [reviewing-sql](../reviewing-sql/SKILL.md).

## Examples
**Input:** "Review our sales dashboard — leadership says it's confusing."
**Output:** Verdict: Request changes (Hierarchy 2/5, Honesty 2/5). **Blocker:** the
revenue chart's y-axis starts at $4M, exaggerating a 3% rise as if it doubled; fix:
zero baseline. **Major:** 24 tiles, no hierarchy — the forecast KPI is lost;
elevate 6 headline metrics. **Minor:** win-rate as a gauge; use a bar vs. target.
**Praise:** good use of color for status.

## Automation opportunities
- Reuse the rubric as a pre-publish dashboard gate.
- Flag truncated-axis and metric-count thresholds automatically for human check.
