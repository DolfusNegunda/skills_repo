---
name: tuning-warehouse-performance
description: Tune slow or expensive cloud data-warehouse queries (Snowflake/BigQuery/Synapse-style) — enable partition pruning and clustering/sort keys, use materialized views and result caching, kill full scans, right-size the warehouse/compute, and read the query profile. Use when the user says "why is this warehouse query slow", "cut our compute cost", "it's scanning the whole table", or "our Snowflake/BigQuery bill is too high".
---

# Tuning Warehouse Performance

## Scope
Performance and cost tuning of queries on a columnar cloud warehouse
(Snowflake, BigQuery, Synapse, Redshift-style): read the query profile, enable
pruning and clustering, exploit caching and materialized views, avoid full scans,
and right-size compute. Not query logic/correctness, not Spark jobs.

## Purpose
Make a warehouse query faster and cheaper by reading the query profile first,
attacking the largest scan or spill, and cutting bytes scanned and compute time —
not by throwing a bigger warehouse at a query that scans everything.

## When to use this skill
- "Why is this warehouse query slow / expensive?"
- "It's doing a full table scan", "no partition pruning", "cut our compute cost".
- "Our Snowflake/BigQuery/Synapse bill is too high", "queries queue for a warehouse".
- Deciding on clustering/sort keys, materialized views, or warehouse size.

## When NOT to use this skill
- Spark/PySpark job tuning → [optimizing-spark-jobs](../optimizing-spark-jobs/SKILL.md).
- Writing the query logic itself → [authoring-sql-queries](../../software-engineering/authoring-sql-queries/SKILL.md).
- Auditing existing SQL for correctness → [reviewing-sql](../../review/reviewing-sql/SKILL.md).

## Inputs
- The query, its query profile/execution plan, and the warehouse platform + dialect.
- Table sizes, partition/clustering keys, and how tables are partitioned.
- The symptom: wall time, bytes/partitions scanned, cost, spill, or queueing.

## Outputs
- The bottleneck named (full scan / no pruning / spill / bad cluster key / oversized or contended warehouse).
- A measured change with before/after runtime, bytes scanned, and cost/credits.

## Workflow
```
Progress:
- [ ] 1. Run once; open the query profile / execution plan
- [ ] 2. Find the dominant operator: largest scan, spill, or exchange
- [ ] 3. Check pruning — bytes/partitions scanned vs table size
- [ ] 4. Apply the targeted fix: pruning, clustering, caching, or MV
- [ ] 5. Re-run; compare runtime, bytes scanned, and cost
- [ ] 6. Right-size the warehouse and check caching last, not first
```

**Step 1 — Read the profile first.** Never tune from the SQL text alone. Open the
query profile (Snowflake), execution details / bytes-billed (BigQuery), or plan
(Synapse/Redshift). Find where time and bytes actually go.

**Step 2 — Find the dominant operator.** Usually the biggest table scan, a spill to
local/remote disk, or an exchange/broadcast. Everything else is noise until that's
fixed.

**Step 3 — Check pruning.** Compare partitions/bytes scanned to total size. A full
scan means the predicate isn't pruning: filter on the partition/cluster column
directly (`event_date >= @d`, not `func(event_date)`), avoid wrapping it in
functions or implicit casts, and don't `SELECT *` from a wide columnar table.

**Step 4 — Fix the cause.** No pruning on a hot filter column → **cluster/sort**
(Snowflake clustering key, BigQuery partition + cluster, Synapse distribution/index)
on that column. Repeated expensive aggregation → a **materialized view** or a
pre-aggregated table. Identical repeated reads → let **result cache** serve them
(don't defeat it with `current_timestamp()` or nondeterministic functions). Spill →
reduce data scanned or bump size only for that job.

**Step 5 — Re-measure.** Confirm bytes scanned and runtime dropped. Cost tracks
bytes scanned (BigQuery) or credits = size × time (Snowflake) — both should fall.

**Step 6 — Right-size compute last.** A bigger warehouse speeds a well-pruned query
but only multiplies the cost of a full scan. Match warehouse size to the workload,
use auto-suspend, and separate/queue workloads instead of oversizing one warehouse.

## Principles
- Read the profile before you touch the query; fix the dominant operator only.
- Bytes scanned is the cost lever — prune first, size compute last.
- Cluster/partition on how the data is actually filtered, not on the primary key.
- Precompute repeated work (MV, summary table); let the result cache serve repeats.
- A bigger warehouse hides a full scan; it never fixes one.

## Decision framework
- **Prune vs cluster:** predicate exists but doesn't prune → make it sargable first; well-formed predicate still scanning → add/adjust clustering.
- **Materialized view vs summary table:** engine can auto-maintain and query is common → MV; complex/multi-source rollup → scheduled summary table.
- **Result cache vs MV:** identical repeated query → result cache (free); same aggregation over changing filters → MV.
- **Scale up vs scale out:** single heavy query spilling → scale up (bigger); many concurrent queries queueing → scale out / add a warehouse.
- **Cluster key choice:** pick the column(s) most filtered/joined with high pruning value; avoid very high-cardinality keys that never co-filter.

## Common mistakes
- **Tuning without the profile** — guessing instead of reading bytes scanned.
- **Non-sargable filter** (`WHERE DATE(ts)=…`, cast on the partition column) → no pruning, full scan.
- **`SELECT *`** on a wide columnar table — reads every column's storage.
- **Oversizing the warehouse** to mask a full scan, multiplying cost.
- **Clustering on the wrong column** (a key never filtered) — pays maintenance for no pruning.
- **Defeating result cache** with `current_timestamp()`/nondeterministic functions or trivial text changes.
- **Materializing everything** — MV storage and refresh cost exceeding the savings.
- **No auto-suspend** — an idle warehouse burning credits.
- **One warehouse for all workloads** — ETL and BI contending, everything queues.

## Validation checklist
- [ ] Query profile read; dominant operator identified.
- [ ] Bytes/partitions scanned is a small fraction of the table (pruning works).
- [ ] Filters on partition/cluster columns are sargable (no functions/casts).
- [ ] Explicit columns, not `SELECT *`.
- [ ] Clustering/partitioning matches the real filter/join pattern.
- [ ] Result cache or MV serving repeated work where applicable.
- [ ] Warehouse size fits the workload; auto-suspend on.
- [ ] Before/after runtime, bytes scanned, and cost recorded.

## Edge cases
- **High-cardinality cluster candidates:** cluster on a coarser derived column (date, bucket) instead.
- **Frequently mutated tables:** clustering re-cluster cost may exceed benefit; weigh maintenance.
- **Cross-region / cross-warehouse reads:** egress and no local cache — colocate.
- **Small tables:** don't cluster or materialize; overhead outweighs any gain.
- **Skewed distribution keys (Synapse/Redshift):** cause hot nodes — pick an even key.

## Related skills
- [optimizing-spark-jobs](../optimizing-spark-jobs/SKILL.md) — the Spark-engine counterpart.
- [authoring-sql-queries](../../software-engineering/authoring-sql-queries/SKILL.md) — writing the query logic.
- [reviewing-sql](../../review/reviewing-sql/SKILL.md) — auditing SQL for correctness.
- [modeling-dimensional-warehouses](../modeling-dimensional-warehouses/SKILL.md) — the model being queried.
- [optimizing-data-costs](../optimizing-data-costs/SKILL.md) — platform-wide spend.

## Examples
**Input:** "This dashboard query scans the whole 2 TB events table every time."
**Output:** Profile shows a full scan — the filter is `WHERE DATE(event_ts) = @d`,
which wraps the partition column and defeats pruning. Rewrite to a half-open range
on the raw column (`event_ts >= @d AND event_ts < @d + 1`), confirm the table is
partitioned/clustered on `event_ts`, and back the repeated rollup with a
materialized view. Bytes scanned drops from 2 TB to ~8 GB; cost falls with it.

## Automation opportunities
- Alert on queries exceeding a bytes-scanned / credit threshold; track full scans over time.
- Set auto-suspend and default warehouse sizes per workload in provisioning.
- Add plan/bytes-scanned capture in CI for hot queries to catch pruning regressions.
