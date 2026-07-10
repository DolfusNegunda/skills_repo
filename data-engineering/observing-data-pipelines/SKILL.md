---
name: observing-data-pipelines
description: Make data pipelines observable — monitor freshness, volume, and schema; define data SLAs/SLOs; alert on data downtime without alert fatigue; use column-level lineage for root-cause; and track the golden signals of pipeline health. Use when the user says "our data is stale and nobody noticed", "set up data monitoring/observability", "define an SLA for this table", "we got alert fatigue", or "trace what broke this dashboard".
---

# Observing Data Pipelines

## Scope
Continuous observability of running pipelines: freshness/volume/schema monitors,
data SLAs/SLOs, downtime alerting, and lineage-driven root-cause. Not one-off data
validation, and not application-level logging.

## Purpose
Detect data downtime before consumers do, alert the right owner with enough context
to act, and trace any incident to its source fast — so trust in the data holds and
mean-time-to-detect/resolve stays low.

## When to use this skill
- "Our data was stale/wrong and nobody noticed", "set up data observability".
- "Define an SLA/SLO for this table/pipeline", "alert us when a feed breaks".
- "We have alert fatigue", "trace what upstream change broke this dashboard".

## When NOT to use this skill
- One-off validation rules / test assertions on a dataset → [ensuring-data-quality](../ensuring-data-quality/SKILL.md).
- Application/service logs, exceptions, correlation IDs → [../../software-engineering/handling-errors-and-logging/SKILL.md](../../software-engineering/handling-errors-and-logging/SKILL.md).

## Inputs
- The pipelines/tables to observe, their consumers, and each one's freshness need.
- Expected volume ranges and schema/contract per table; normal load cadence.
- Existing monitoring/lineage tooling and the on-call/ownership routing.
- What "broken" means to consumers (stale, incomplete, wrong shape).

## Outputs
- Freshness, volume, and schema monitors per critical table, tuned to real patterns.
- Data SLAs/SLOs with error budgets, and downtime alerts routed to named owners.
- A lineage map (ideally column-level) usable for root-cause and impact analysis.

## Workflow
```
Progress:
- [ ] 1. Pick critical tables by consumer impact; define "healthy" for each
- [ ] 2. Instrument the golden signals: freshness, volume, schema (+ quality/lineage)
- [ ] 3. Set SLAs/SLOs with error budgets from real consumer needs
- [ ] 4. Alert on downtime — actionable, deduped, routed to an owner
- [ ] 5. Wire lineage for root-cause and downstream impact analysis
- [ ] 6. Run incident review; tune thresholds; track MTTD/MTTR over time
```

**Step 1 — Scope by impact.** You cannot watch everything equally; rank tables by
who breaks if they break. For each critical one write what "healthy" means: fresh by
X, roughly N rows, this schema. Everything downstream inherits from these.

**Step 2 — Golden signals.** Instrument the four pillars: **freshness** (time since
last successful update vs SLA), **volume** (row/byte count within an expected band),
**schema** (columns/types/nullability vs contract), and **distribution/quality** for
key fields. Baseline from history so thresholds reflect real seasonality, not a guess.
No freshness monitor is the number-one blind spot — stale data looks fine until a
consumer notices.

**Step 3 — SLAs/SLOs.** Turn consumer need into a measurable target ("orders fresh
within 30 min, 99.5% of days") with an error budget. The SLO decides what is worth
paging for; without it every blip feels equally urgent.

**Step 4 — Alert on downtime, not noise.** Page only on SLO-breaching, actionable
conditions; group/dedupe related alerts, suppress during known maintenance, and route
each to the owning team with context (which table, expected vs actual, likely blast
radius). Alert fatigue is a failure mode — a firehose of non-actionable alerts trains
people to ignore the real one. Warn vs page deliberately.

**Step 5 — Lineage for RCA.** Maintain lineage, ideally **column-level**, so when a
metric breaks you trace upstream to the source table/column that changed and forward
to every affected dashboard. Without lineage, root-cause is manual archaeology under
time pressure ([governing-data-and-lineage](../governing-data-and-lineage/SKILL.md)).

**Step 6 — Close the loop.** After each incident, review detection gaps, tune noisy
or missed thresholds, and track MTTD/MTTR as the scoreboard. Observability that
never gets tuned decays into either silence or noise.

## Principles
- Detect before the consumer does — freshness is the earliest, cheapest signal.
- Monitor the golden signals continuously; don't rely on one-off checks.
- An alert without an owner and an action is noise; every page must be both.
- Baseline from history so thresholds respect seasonality, not a static magic number.
- Lineage turns root-cause from hours of guessing into minutes of tracing.
- Tune relentlessly: measure MTTD/MTTR and let incidents drive threshold changes.

## Decision framework
- **What to monitor first?** Highest-consumer-impact tables get freshness + volume + schema before anything else.
- **Threshold source?** Derive from historical distribution + SLO; hard-coded constants drift and misfire.
- **Page vs warn?** SLO-breach and actionable now → page; degraded but within budget → warn/ticket.
- **Anomaly detection vs fixed rules?** Volatile/seasonal metrics → learned baselines; stable contracts → fixed rules.
- **Column vs table lineage?** Metric-level RCA and impact analysis need column-level; coarse dependency mapping can be table-level.

## Common mistakes
- **No freshness monitor** — stale data ships silently until a consumer complains.
- **Alert fatigue** — non-actionable, un-deduped alerts, so the real one is ignored.
- **Static thresholds** — fixed row counts that break on every seasonal swing.
- **No lineage for RCA** — every incident becomes manual, slow archaeology.
- **Monitoring the job, not the data** — green DAG run while the output is wrong or empty.
- **Alerts with no owner** — fire into a shared channel nobody acts on.
- **Watching everything equally** — noise on trivial tables drowns critical ones.

## Validation checklist
- [ ] Critical tables ranked by consumer impact; "healthy" defined for each.
- [ ] Freshness, volume, and schema monitored on every critical table.
- [ ] Thresholds baselined from history, not hard-coded guesses.
- [ ] SLAs/SLOs with error budgets tied to real consumer needs.
- [ ] Alerts actionable, deduped, and routed to a named owner.
- [ ] Lineage (column-level where metrics matter) available for root-cause.
- [ ] MTTD/MTTR tracked; thresholds tuned after each incident.

## Edge cases
- **Irregular cadence:** derive freshness SLA from the schedule (allow for weekends/holidays), not a flat interval.
- **Expected volume swings:** promotions/backfills need seasonality-aware or suppressible thresholds.
- **Backfills/replays:** suppress volume alerts during known reloads to avoid false pages.
- **New tables:** no baseline yet — start with contract/schema checks, add statistical monitors as history accrues.
- **Third-party feeds you can't fix:** monitor at the boundary and alert; quarantine bad loads downstream.

## Related skills
- [ensuring-data-quality](../ensuring-data-quality/SKILL.md) — the validation rules the monitors watch over time.
- [governing-data-and-lineage](../governing-data-and-lineage/SKILL.md) — the lineage graph that powers RCA and impact analysis.
- [orchestrating-data-workflows](../orchestrating-data-workflows/SKILL.md) — where run-level retries and job signals live.
- [../../software-engineering/handling-errors-and-logging/SKILL.md](../../software-engineering/handling-errors-and-logging/SKILL.md) — app-level logging that complements data signals.
- [../../business/defining-kpis/SKILL.md](../../business/defining-kpis/SKILL.md) — the business metrics whose health these signals protect.

## Examples
**Input:** "A key dashboard showed yesterday's numbers for three days and nobody
caught it."
**Output:** Root cause: no freshness monitor — the load job succeeded but read a
stale upstream partition. Added a freshness SLO (fresh within 2h, 99% of days) with a
page to the owning team, a volume monitor baselined on 90 days, and a schema check on
the contract. Wired column-level lineage so the dashboard traces to its source table;
suppressed alerts during nightly backfill windows. MTTD dropped from ~3 days to
minutes.

## Automation opportunities
- Auto-generate freshness/volume monitors for every table in the catalog from metadata.
- Learn volume/distribution baselines automatically and refresh them on a schedule.
- Auto-capture lineage from query logs / orchestration DAGs rather than hand-drawing it.
- Post incident context (expected vs actual, upstream owner, impacted consumers) into the alert.
