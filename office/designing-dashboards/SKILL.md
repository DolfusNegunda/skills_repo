---
name: designing-dashboards
description: Design decision-oriented dashboards — choosing the right metrics, chart types, layout, and interactivity so a viewer grasps the state and knows what to do at a glance. Use when the user asks to "design/build a dashboard", "create a KPI/reporting view", "visualize these metrics", or improve a cluttered dashboard. Covers Excel, Power BI, Tableau, Looker, and Sheets. Produces a dashboard spec and layout focused on decisions, not decoration. For chart aesthetics, also load the dataviz skill.
---

# Designing Dashboards

## Scope
The design of dashboards: which metrics, which chart per metric, layout, hierarchy,
and interactivity — so the view drives decisions. Tool-agnostic (Excel, Power BI,
Tableau, Looker, Sheets). For chart color/mark aesthetics, pair with the
[dataviz](../generating-data-reports/SKILL.md) skill; for the data behind it,
the spreadsheet/data-engineering skills.

## Purpose
Let a viewer answer "how are we doing and what should I do?" in seconds — with the
right metrics, honest visuals, and a layout that leads the eye from headline to detail.

## When to use this skill
- "Design / build a dashboard / KPI view / reporting view."
- "Visualize these metrics" for ongoing monitoring.
- "Our dashboard is cluttered / nobody uses it."

## When NOT to use this skill
- A one-off chart or report → [dataviz](../generating-data-reports/SKILL.md) / [writing-reports](../writing-reports/SKILL.md).
- Pure aesthetics of a single chart → [dataviz](../generating-data-reports/SKILL.md).
- The data model itself → [engineering-spreadsheets](../engineering-spreadsheets/SKILL.md) / a data pipeline.

## Inputs
- The decision(s) the dashboard supports and its audience (exec / operational / analytical).
- The candidate metrics and their data sources and refresh cadence.
- Targets/benchmarks for the KPIs; device/context (wall screen, laptop, mobile).

## Outputs
- A dashboard spec: selected KPIs (with targets), chart type per metric, layout with
  a clear hierarchy, interactivity plan, and refresh/ownership notes.

## Workflow
```
Progress:
- [ ] 1. Define the decision and audience type
- [ ] 2. Select the few metrics that drive that decision
- [ ] 3. Choose the right visual for each metric
- [ ] 4. Lay out by hierarchy: headline → supporting → detail
- [ ] 5. Add context: targets, comparisons, trends
- [ ] 6. Plan interactivity (filters/drill-down) deliberately
- [ ] 7. Verify: glanceable, honest, and refreshed
```

**Step 1 — Decision & audience.** An exec dashboard (status at a glance) differs
from an operational one (act now) and an analytical one (explore). Design for one.

**Step 2 — Ruthless metric selection.** Pick the few KPIs that actually drive the
decision. A dashboard of everything communicates nothing. Prefer 5–9 focused metrics
over 30.

**Step 3 — Right visual per metric.** Trend → line; comparison → bar; single KPI vs
target → number + delta/bullet; composition → stacked bar (rarely pie); relationship
→ scatter. Match the chart to the question, not to variety.

**Step 4 — Layout by hierarchy.** Most important top-left (where eyes land); headline
KPIs first, supporting detail below, deep detail on drill-down. Group related metrics;
use whitespace to separate.

**Step 5 — Context makes numbers meaningful.** A number alone ("Revenue: $2M") is
useless — add target, prior period, and trend ("$2M, +12% vs. last month, 4% below
target"). Comparison and direction are the point.

**Step 6 — Deliberate interactivity.** Filters and drill-downs for the questions the
audience actually asks; don't add controls that clutter without purpose. Default
views should answer the main question with no clicking.

**Step 7 — Verify.** Can the target user get the headline in ~5 seconds? Are visuals
honest (zero baselines on bars, no dual-axis tricks, consistent scales)? Does it
refresh reliably? Fix all three.

## Principles
1. **Decision-first.** Every element serves a decision or is cut.
2. **Fewer metrics, chosen well.** Clutter is the enemy of insight.
3. **Right chart for the question;** no chartjunk, no 3-D, no gratuitous pies.
4. **Numbers need context** — target, comparison, trend.
5. **Layout guides the eye** from headline to detail.
6. **Honest visuals** — non-truncated axes, consistent scales, clear labels.

## Decision framework
- **Status at a glance (exec)?** Big KPIs + target/trend, minimal interactivity.
- **Act now (operational)?** Real-time, alerting/thresholds, drill to the item.
- **Explore (analytical)?** Rich filters, breakdowns, drill-downs.
- **Single KPI vs target?** Number + delta or bullet chart, not a gauge.
- **Many categories over time?** Line/small multiples, not a crowded stacked bar.

## Common mistakes
- **Too many metrics** — everything shown, nothing understood.
- **Wrong chart types** — pie for trends, gauges wasting space, 3-D distortion.
- **Numbers without context** — no target, comparison, or trend.
- **Truncated/dual axes** that mislead.
- **No visual hierarchy** — everything the same size, eye has no path.
- **Decorative clutter** — logos, gradients, backgrounds competing with data.
- **Stale data** with no refresh indicator.

## Validation checklist
- [ ] Supports a specific decision for a defined audience.
- [ ] Metrics limited to the few that matter; each earns its place.
- [ ] Each metric uses the right chart for its question.
- [ ] Layout hierarchy leads from headline KPIs to detail.
- [ ] Every number has target/comparison/trend context.
- [ ] Axes honest (zero baseline on bars), scales consistent, labels clear.
- [ ] Interactivity is purposeful; default view answers the main question.
- [ ] Refresh cadence and data owner defined; freshness shown.

## Edge cases
- **Mobile dashboards:** fewer metrics, vertical stack, touch-friendly.
- **Wall/TV displays:** large fonts, high contrast, no interactivity, auto-refresh.
- **Real-time ops:** thresholds/alerts and clear stale-data indicators.
- **Mixed audiences:** separate tabs/views per audience rather than one crowded view.
- **Sparse/uncertain data:** show confidence or "no data", never a misleading zero.

## Related skills
- [dataviz](../generating-data-reports/SKILL.md) — chart aesthetics, color, marks (load alongside).
- [engineering-excel-workbooks](../engineering-excel-workbooks/SKILL.md) / [engineering-google-sheets](../engineering-google-sheets/SKILL.md) — data layer.
- [engineering-spreadsheets](../engineering-spreadsheets/SKILL.md), [writing-reports](../writing-reports/SKILL.md).

## Examples
**Input:** "Build a sales leadership dashboard from our pipeline data."
**Output:** Spec with 6 KPIs (bookings vs target, pipeline coverage, win rate,
avg deal size, cycle time, forecast) — big number + delta for each headline metric
top-left, a trend line and a stage-funnel below, region/rep filters, monthly refresh
with a freshness stamp; excludes 20 vanity metrics that don't drive the forecast decision.

## Automation opportunities
- Connect live to the data source so KPIs refresh automatically.
- Threshold alerts that notify owners when a KPI breaches target.
- Templatize the layout so new dashboards start decision-first.
