---
name: optimizing-data-costs
description: Control cloud data-platform spend — separate storage from compute cost, auto-suspend and right-size compute, cut scanned bytes with partition pruning and column projection, apply lifecycle/retention policies, avoid needless reprocessing, and attribute cost back to owners. Use when the user says "our warehouse bill is too high", "why is this query so expensive", "we're paying for idle compute", "reduce Snowflake/BigQuery/Databricks cost", or "who owns this spend".
---

# Optimizing Data Costs

## Scope
Reducing the dollar cost of a cloud data platform: the storage/compute split,
compute sizing and idle time, bytes scanned per query, data retention, wasted
reprocessing, and cost attribution. Not query/job speed for its own sake, and not
organization-level budgeting.

## Purpose
Cut the bill without breaking SLAs: pay only for compute you use, scan only the
bytes you need, keep only the data that earns its keep, and make every dollar
traceable to an owner who can act on it.

## When to use this skill
- "The warehouse/lakehouse bill is too high", "cost spiked this month".
- "Why is this query/job so expensive?", "we're paying for idle compute".
- "Reduce Snowflake/BigQuery/Databricks/Redshift cost", "set up cost attribution".

## When NOT to use this skill
- Making a query or Spark job *faster* per se → [tuning-warehouse-performance](../tuning-warehouse-performance/SKILL.md) / [optimizing-spark-jobs](../optimizing-spark-jobs/SKILL.md).
- Org-level budgeting or spend-vs-value cases → [../../business/analyzing-cost-benefit/SKILL.md](../../business/analyzing-cost-benefit/SKILL.md).

## Inputs
- A cost/usage breakdown: compute vs storage, by warehouse/cluster/project, over time.
- The pricing model in play (per-second compute, bytes-scanned, storage tier, egress).
- Workload shape: query patterns, table sizes, partition columns, and SLAs to protect.
- Ownership metadata: tags/labels mapping spend to teams, pipelines, or datasets.

## Outputs
- A prioritized cost-reduction plan: compute sizing/auto-suspend, scan reduction,
  retention/lifecycle rules, and reprocessing fixes — each with an estimated saving.
- A cost-attribution scheme (tags/labels/resource monitors) so spend has an owner.

## Workflow
```
Progress:
- [ ] 1. Split the bill into storage vs compute vs egress; find the top drivers
- [ ] 2. Auto-suspend idle compute and right-size warehouses/clusters to the load
- [ ] 3. Cut bytes scanned: partition pruning, clustering, column projection
- [ ] 4. Apply lifecycle/retention: tier or expire cold data; drop dead tables
- [ ] 5. Eliminate needless reprocessing: incremental loads, materialize once
- [ ] 6. Attribute cost to owners with tags/labels; set monitors and alerts
```

**Step 1 — Split the bill.** Separate storage, compute, and egress before touching
anything; on most platforms compute dominates. Rank drivers by cost, not by row
count — one hourly full-scan job can outweigh a petabyte of cold storage.

**Step 2 — Idle and size.** Idle running compute is pure waste: set aggressive
auto-suspend (seconds-to-minutes) and auto-resume. Right-size to the workload —
scaling *up* a warehouse can be cheaper per-query if it finishes proportionally
faster (same credits, less wall-clock); scale *out* only for concurrency. Kill
always-on clusters serving bursty load.

**Step 3 — Scan less.** On bytes-scanned pricing, cost is bytes read, not rows
returned. Partition/cluster on the common filter column so the engine prunes
partitions; never `SELECT *` — project only needed columns (columnar formats skip
the rest). Replace repeated expensive scans with a materialized view or a summary
table. `SELECT *` on a wide table with no predicate is the classic money leak.

**Step 4 — Retention and lifecycle.** Data kept forever is billed forever. Set
retention per table by real access need; tier cold data to cheap storage, expire raw
staging after landing, and drop tables nothing reads. Time-travel/fail-safe windows
and orphaned snapshots quietly inflate storage — bound them.

**Step 5 — Stop reprocessing.** Recomputing unchanged history every run is the
biggest silent cost. Load incrementally ([implementing-incremental-loading](../implementing-incremental-loading/SKILL.md)),
materialize a result once and read it many times, and cache/reuse rather than
re-derive. Full daily rebuilds of an append-only table are almost always waste.

**Step 6 — Attribute.** Tag/label every warehouse, job, and dataset with an owner
and cost center so spend rolls up to a team. Set resource monitors/budget alerts
with hard or soft caps. Unattributed cost never gets fixed — nobody owns it.

## Principles
- Compute is rented by time; storage is rented by volume — optimize them separately.
- Idle compute has zero value; suspend it by default, resume on demand.
- On scan-priced engines, cost = bytes read; prune partitions and project columns.
- Data has a carrying cost: keep it only while it earns more than it costs to store.
- The cheapest reprocessing is the one you skip — compute once, read many.
- Unowned spend is unfixable; every dollar needs a name.

## Decision framework
- **Compute idle between runs?** Auto-suspend + auto-resume beats keeping it warm, unless resume latency breaks an SLA.
- **Query too expensive?** Bytes-scanned high → prune/project/cluster; wall-clock high but bytes low → performance skill, not this one.
- **Scale up vs out?** Up (bigger warehouse) for a single heavy query that speeds up linearly; out (more clusters) only for concurrency.
- **Keep vs expire data?** No reads in N days and reproducible from source → tier or drop; regulatory hold → tier, don't delete.
- **Rebuild vs incremental?** Append-only or slowly-changing → incremental; small/volatile table → full rebuild is fine.

## Common mistakes
- **Paying for idle compute** — no auto-suspend, always-on clusters for bursty work.
- **`SELECT *` / full scans** — reading every column and partition on scan-priced engines.
- **No partition pruning** — filtering on a non-partitioned column forces a full scan.
- **Unbounded retention** — infinite history, huge time-travel windows, orphaned snapshots.
- **Reprocessing unchanged data** — full daily rebuilds instead of incremental loads.
- **Oversized compute "to be safe"** — a giant warehouse idling on tiny queries.
- **No cost attribution** — untagged spend nobody owns, so nothing gets cut.

## Validation checklist
- [ ] Bill split into storage vs compute vs egress; top drivers ranked by cost.
- [ ] Auto-suspend enabled; compute right-sized to actual load, not peak fear.
- [ ] Hot queries prune partitions and project columns; no needless `SELECT *`.
- [ ] Retention/lifecycle set per table; cold data tiered, dead tables dropped.
- [ ] Reprocessing removed where inputs are unchanged (incremental / materialized).
- [ ] Every warehouse/job/dataset tagged to an owner; budget monitors + alerts set.
- [ ] Each change has an estimated saving and a check that the SLA still holds.

## Edge cases
- **Resume latency vs SLA:** interactive dashboards may justify a small always-on warehouse; batch never does.
- **Regulatory retention:** must-keep data goes to the cheapest compliant tier, not deletion.
- **Small tables:** micro-partitioning/clustering overhead can exceed the saving — leave them alone.
- **Egress-heavy workloads:** cross-region reads and exports can dwarf compute; co-locate storage and compute.
- **Reserved vs on-demand:** commit to reserved capacity only for stable, predictable baseline load.

## Related skills
- [tuning-warehouse-performance](../tuning-warehouse-performance/SKILL.md), [optimizing-spark-jobs](../optimizing-spark-jobs/SKILL.md) — speed tuning that often also cuts cost.
- [implementing-incremental-loading](../implementing-incremental-loading/SKILL.md) — the main lever against reprocessing spend.
- [governing-data-and-lineage](../governing-data-and-lineage/SKILL.md) — ownership/tagging that powers attribution.
- [observing-data-pipelines](../observing-data-pipelines/SKILL.md) — catch cost-spiking volume changes early.

## Examples
**Input:** "Our Snowflake bill doubled and we don't know why."
**Output:** Split the bill — compute up 3x, storage flat. Found a warehouse with no
auto-suspend idling 20h/day and an hourly job doing `SELECT *` over an unpartitioned
events table. Fix: auto-suspend at 60s, cluster events by event_date so the job
prunes to one day, project the 8 needed columns, and switch it to incremental.
Tagged each warehouse to a team and set a monthly resource monitor. Projected ~55%
compute reduction with SLAs intact.

## Automation opportunities
- Alert on cost anomalies (day-over-day spend, bytes-scanned per query) in monitoring.
- Enforce auto-suspend and required cost-owner tags via policy/IaC on every warehouse.
- Auto-expire staging and apply lifecycle tiering rules as scheduled maintenance jobs.
- Lint queries in CI for `SELECT *` and missing partition predicates on large tables.
