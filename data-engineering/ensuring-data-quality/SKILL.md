---
name: ensuring-data-quality
description: Build data quality into pipelines — define expectations (row counts, nulls, uniqueness, referential integrity, ranges, freshness), test at pipeline boundaries, quarantine bad data, set data contracts, and decide fail-vs-warn per check. Use when the user says "add data quality checks", "validate this data", "Great Expectations / dbt tests", "set a data contract", "why did bad rows reach prod", or "the numbers look wrong".
---

# Ensuring Data Quality

## Scope
Making data correctness a built-in, enforced property of a pipeline: expectations
defined as tests, run at ingest and publish boundaries, with bad data quarantined
and contracts agreed with producers. Covers detecting and gating on bad data, not
managing schema changes or cataloging lineage.

## Purpose
Catch bad data at the boundary — before it corrupts downstream tables or dashboards —
with checks specific enough to be meaningful, a clear fail-vs-warn decision per check,
and a quarantine path so one bad batch never silently poisons the warehouse.

## When to use this skill
- "Add data quality checks / validate this data / set up Great Expectations or dbt tests."
- Setting a data contract with an upstream producer.
- Bad rows reached prod, numbers look wrong, or a load silently dropped rows.

## When NOT to use this skill
- Handling schema/column changes over time → [managing-schema-evolution](../managing-schema-evolution/SKILL.md).
- Lineage, catalog, ownership, and glossary → [governing-data-and-lineage](../governing-data-and-lineage/SKILL.md).
- Alerting/metrics infrastructure depth → [observing-data-pipelines](../observing-data-pipelines/SKILL.md).
- Orchestration/scheduling of the checks → [orchestrating-data-workflows](../orchestrating-data-workflows/SKILL.md).

## Inputs
- The dataset, its grain, and what "correct" means to consumers (their tolerances).
- Known keys, required fields, valid ranges/enums, referential relationships.
- Expected volume/cadence and freshness SLA; historical baselines for drift.
- Producer relationship: is a data contract possible, and who owns fixes.

## Outputs
- A suite of expectations (row count, null, uniqueness, RI, range/enum, freshness).
- Checks placed at ingest and publish boundaries, each tagged fail (block) or warn.
- A quarantine mechanism (bad rows/batches diverted, not dropped) and a triage path.
- A data contract per critical source: schema, semantics, SLA, and breach behavior.

## Workflow
```
Progress:
- [ ] 1. Define what "correct" means with consumers; pick the grain
- [ ] 2. Write expectations: counts, nulls, uniqueness, RI, ranges, freshness
- [ ] 3. Place checks at ingest and publish boundaries (validate early)
- [ ] 4. Classify each check fail-vs-warn; wire quarantine for failures
- [ ] 5. Set data contracts with producers; agree breach behavior
- [ ] 6. Baseline, run in pipeline, tune thresholds to cut false alarms
```

**Step 1 — Define correct.** Ask consumers what breaks their decisions and translate
it into measurable expectations at a stated grain. "High quality" is not a spec; "PK
unique, `amount` in [0, 1e6], < 0.1% null `customer_id`" is.

**Step 2 — Write expectations.** Cover the core families: row-count/volume vs.
baseline, null rate on required fields, uniqueness of keys, referential integrity to
dimensions, value ranges/enums, and freshness (max lag). Use Great Expectations- or
dbt-test-style declarative checks, not ad-hoc queries scattered in code.

**Step 3 — Test at boundaries.** Validate on ingest (reject bad input at the door)
and again before publish (guard consumers). Checking only at the end lets bad data
propagate through intermediate tables and wastes compute; checking only at ingest
misses transform-introduced errors.

**Step 4 — Fail vs. warn + quarantine.** Mark each check: **fail** stops the load
(uniqueness, RI, hard ranges — data would be wrong); **warn** logs and continues
(soft volume drift, rare nulls). On fail, divert offending rows/batch to a quarantine
table with the reason — never silently drop, never let them through.

**Step 5 — Contracts.** For critical sources, agree a data contract: schema, field
semantics, freshness SLA, allowed null/range, and what happens on breach (who's
paged, is the batch rejected). Version it; a contract change is a negotiated event.

**Step 6 — Baseline and tune.** Seed thresholds from historical distributions, run
the suite in the pipeline (see [writing-automated-tests](../../software-engineering/writing-automated-tests/SKILL.md)),
and tighten/loosen to kill false positives. A check people learn to ignore is worse
than none.

## Principles
1. **Quality is built in, not inspected later** — checks live in the pipeline, at boundaries.
2. **Validate early** — reject at ingest before bad data spreads and burns compute.
3. **Expectations are specific and measurable** — thresholds and keys, not "looks fine".
4. **Quarantine, never silently drop** — bad rows are diverted with a reason and triaged.
5. **Fail on wrong, warn on drift** — block what corrupts; surface what merely shifts.
6. **Contracts push quality upstream** — the producer owns their data's shape and SLA.

## Decision framework
- **Would this row make a downstream number wrong?** Fail and quarantine. Otherwise warn.
- **Check at ingest or publish?** Input-shape checks at ingest; business-rule/aggregate checks before publish. Critical ones at both.
- **Threshold too noisy?** Baseline from history and widen; a muted alarm protects nothing.
- **Producer keeps sending bad data?** Escalate to a data contract with breach consequences.
- **Bad batch blocks a deadline?** Quarantine the bad rows, publish the good, backfill the fixed batch.
- **New source, no baseline?** Start warn-only, observe a few cycles, then promote to fail.

## Common mistakes
- **Checking quality too late** — only on the final table, after bad data already spread.
- **Silent row loss** — an inner join or filter drops rows and nobody counts before/after.
- **No quarantine** — failures either crash the run or vanish; no way to inspect or replay.
- **Vague expectations** — "reasonable values" with no thresholds, so nothing actually fails.
- **Everything fails (or nothing does)** — no fail-vs-warn triage, so the pipeline is brittle or blind.
- **No freshness check** — stale data looks fine structurally and quietly misleads.
- **Alert fatigue** — untuned thresholds fire constantly until everyone ignores them.

## Validation checklist
- [ ] Expectations cover counts, nulls, uniqueness, referential integrity, ranges/enums, freshness.
- [ ] Checks run at ingest and before publish, not only at the end.
- [ ] Each check is classified fail vs. warn on an explicit rationale.
- [ ] Failing rows/batches are quarantined with a reason, never silently dropped.
- [ ] Row counts reconciled across each transform boundary (no unexplained loss).
- [ ] Data contracts exist for critical sources with SLA and breach behavior.
- [ ] Thresholds baselined from history; false-positive rate is low.

## Edge cases
- **Late/partial arrivals:** freshness + volume checks with a grace window before failing.
- **Legitimate spikes (promotions, seasonality):** use relative/seasonal baselines, not fixed absolutes.
- **Nulls that are valid:** distinguish "missing but allowed" from "required and missing" per field.
- **Referential integrity with late dimensions:** check after the dimension loads, or allow a bounded gap.
- **First run / no history:** warn-only until a baseline exists, then promote checks to fail.

## Related skills
- [orchestrating-data-workflows](../orchestrating-data-workflows/SKILL.md), [implementing-incremental-loading](../implementing-incremental-loading/SKILL.md), [building-batch-transformations](../building-batch-transformations/SKILL.md).
- [managing-schema-evolution](../managing-schema-evolution/SKILL.md), [governing-data-and-lineage](../governing-data-and-lineage/SKILL.md), [observing-data-pipelines](../observing-data-pipelines/SKILL.md).
- [writing-automated-tests](../../software-engineering/writing-automated-tests/SKILL.md), [reviewing-sql](../../review/reviewing-sql/SKILL.md), [maintaining-risk-registers](../../business/maintaining-risk-registers/SKILL.md).

## Examples
**Input:** "Bad orders keep reaching the dashboard — negative amounts and duplicate
IDs. Add data quality checks."
**Output:** Defined expectations with finance: `order_id` unique, `amount` in
[0, 1e6], `customer_id` < 0.1% null, RI to `dim_customer`, freshness < 6h. Placed
uniqueness/range/RI as **fail** at ingest and revenue-total sanity as **warn** before
publish. Failures route to `orders_quarantine` with a reason column; good rows still
publish. Added a row-count reconciliation across the join that had been silently
dropping unmatched rows. Baselined thresholds on 90 days; drafted a data contract with
the orders team. Duplicates and negatives now stop at the door.

## Automation opportunities
- Generate baseline expectations from profiling (distributions, null rates, cardinality), then curate.
- Run the suite as a gate in the DAG; block publish on any fail-level check.
- Auto-quarantine failing rows and open a triage ticket with the failed expectation.
- Track quality metrics over time; alert on trend degradation, not just single-run breaches.
- Validate incoming data against the contract in CI so producer changes surface before prod.
