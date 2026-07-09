---
name: defining-kpis
description: Define meaningful key performance indicators that measure what matters, resist gaming, and drive the right behavior — with clear definitions, targets, and data sources. Use when the user asks to "define KPIs", "what metrics should we track", "set up performance measures", or fix vanity/gameable metrics. Distinguishes KPIs from vanity metrics and pairs leading with lagging indicators. Produces a defensible metric set, not a dashboard of everything countable.
---

# Defining KPIs

## Scope
Selecting and defining performance indicators that genuinely reflect success,
resist gaming, and drive intended behavior — with precise definitions, targets, and
data sources. Not dashboard layout ([designing-dashboards](../../office/designing-dashboards/SKILL.md))
or goal-setting frameworks ([setting-okrs](../setting-okrs/SKILL.md)).

## Purpose
Ensure an organization measures what actually matters — a few meaningful, hard-to-
game indicators tied to outcomes — instead of tracking everything countable and
optimizing vanity numbers.

## When to use this skill
- "Define KPIs / what metrics should we track / set up performance measures."
- Fixing vanity or gameable metrics.
- Establishing measurement for a team, product, or process.

## When NOT to use this skill
- Objective/goal framework → [setting-okrs](../setting-okrs/SKILL.md).
- Visualizing metrics → [designing-dashboards](../../office/designing-dashboards/SKILL.md).
- Deep data analysis → a data-science skill.

## Inputs
- The goal/outcome to measure and who acts on the metric.
- Available data sources and reporting cadence.

## Outputs
- A KPI set: each with a plain definition, formula, target, data source, cadence,
  and owner — balancing leading and lagging indicators.

## Workflow
```
Progress:
- [ ] 1. Start from the outcome — what does success mean?
- [ ] 2. Choose few KPIs that truly reflect that outcome
- [ ] 3. Balance leading (predictive) with lagging (result) indicators
- [ ] 4. Define each precisely: formula, source, cadence, owner
- [ ] 5. Set realistic, evidence-based targets
- [ ] 6. Pressure-test for gaming and perverse incentives
```

**Step 1–2 — outcome first, few metrics.** A KPI must connect to a real outcome; if
improving it doesn't mean success, it's a vanity metric. Pick a handful, not dozens.
**Step 3 — leading + lagging:** lagging metrics (revenue, churn) confirm results but
too late to act; leading metrics (pipeline, engagement) predict them. Pair them.
**Step 6 — anti-gaming:** for each KPI ask "how would someone hit this number without
achieving the goal?" and add a guardrail/counter-metric (e.g. speed + quality).

## Principles
1. **Measure outcomes, not activity.** Busy ≠ successful.
2. **Few and meaningful** beats many and noisy.
3. **Leading + lagging** — predict and confirm.
4. **Define precisely** — same number every time, one owner.
5. **Design against gaming** — pair with counter-metrics.

## Decision framework
- **Metric can be hit while the goal is missed?** It's gameable — add a counter-metric or replace it.
- **Only lagging metrics?** Add a leading predictor you can act on.
- **Can't define the formula/source unambiguously?** It's not ready to be a KPI.
- **More than ~5–7 per team?** Cut — focus is the point.

## Common mistakes
- **Vanity metrics** (page views, activity counts) that don't reflect success.
- **Measuring what's easy** rather than what matters.
- **Only lagging indicators** — no time to react.
- **Ambiguous definitions** — the number means different things to different people.
- **Ignoring gaming** — the metric improves, the outcome doesn't.
- **Too many KPIs** — no focus.

## Validation checklist
- [ ] Each KPI ties to a real outcome (improving it = success).
- [ ] The set is small and focused.
- [ ] Leading and lagging indicators both present.
- [ ] Each has a precise formula, data source, cadence, and owner.
- [ ] Targets are realistic and evidence-based.
- [ ] Gaming risk assessed; counter-metrics added where needed.

## Edge cases
- **Early-stage/no baseline:** track the metric first, set targets once you have data.
- **Qualitative outcomes:** use proxy metrics + qualitative signals; state the proxy's limits.
- **Cross-team shared KPIs:** clarify ownership and contribution to avoid diffusion.
- **Regulated metrics:** align definitions with the mandated methodology.

## Related skills
- [setting-okrs](../setting-okrs/SKILL.md), [designing-dashboards](../../office/designing-dashboards/SKILL.md).
- [performing-business-analysis](../performing-business-analysis/SKILL.md).

## Examples
**Input:** "Define KPIs for our customer support team."
**Output:** Set: CSAT (lagging outcome), first-response time (leading), resolution
rate (outcome), each with formula/source/cadence/owner and evidence-based targets;
first-response time paired with a quality counter-metric (reopen rate) so agents
can't game speed by closing tickets prematurely; capped at 5 KPIs.

## Automation opportunities
- Pull KPI values automatically from source systems into a dashboard.
- Alert owners on target breaches and on counter-metric divergence (gaming signal).
