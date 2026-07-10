---
name: building-batch-transformations
description: Build reliable batch ETL/ELT transformations — stage raw data, transform in idempotent reprocessable steps (SQL/dbt/Spark), separate ELT (transform-in-warehouse) from ETL, test transforms, and make reruns safe. Use when the user asks to "build an ETL job", "write a dbt model", "transform this data in batch", "why did my rerun double the rows", or needs a scheduled batch pipeline that can be replayed without corruption.
---

# Building Batch Transformations

## Scope
Designing and building batch transformations that turn raw input into modeled
output on a schedule: staging, layered idempotent transforms, ELT-vs-ETL choice,
tests, and safe reruns/backfills. Not streaming, not CDC/incremental mechanics.

## Purpose
Produce a transformation that yields the same correct result whether run once or
five times, can be backfilled per partition without duplicates or drift, and fails
loudly instead of silently emitting bad rows.

## When to use this skill
- "Build an ETL/ELT job", "write a dbt model", "transform this table in batch".
- "My rerun doubled the rows / the backfill is wrong / how do I replay one day".
- Moving row-by-row or ad-hoc scripts into a repeatable, testable batch layer.

## When NOT to use this skill
- Real-time/event processing → [building-streaming-pipelines](../building-streaming-pipelines/SKILL.md).
- Loading only changed rows / CDC / MERGE upserts → [implementing-incremental-loading](../implementing-incremental-loading/SKILL.md).
- Query authoring/tuning only → [authoring-sql-queries](../../software-engineering/authoring-sql-queries/SKILL.md).

## Inputs
- Sources (files/tables/APIs), their grain, volumes, and refresh cadence.
- Target model + grain, SLA, and the warehouse/engine (Snowflake/BigQuery/Spark).
- Partition key (usually a date), backfill needs, and existing tests/contracts.

## Outputs
- Layered transforms (staging → intermediate → mart) that are idempotent per partition.
- A rerun/backfill procedure, transform tests, and freshness/row-count checks.

## Workflow
```
Progress:
- [ ] 1. Land raw immutably; pin the partition key and grain per layer
- [ ] 2. Stage: cast, rename, dedupe — one row per source grain, no business logic
- [ ] 3. Choose ELT (transform in warehouse) vs ETL (transform before load)
- [ ] 4. Transform in small deterministic steps; make each replaceable, not appended
- [ ] 5. Make writes idempotent: overwrite/replace the partition, never blind INSERT
- [ ] 6. Test transforms; add freshness + row-count checks; document backfill
```

**Step 1 — Land raw, fix grain.** Keep an immutable raw/landing copy so any
downstream logic can be replayed from source. State "one row per ___" for every
layer up front — most rerun bugs are grain surprises, not logic errors.

**Step 2 — Stage.** Staging does type casting, renaming, and dedup only (no joins,
no business rules). Dedupe with `ROW_NUMBER() OVER (PARTITION BY nk ORDER BY
loaded_at DESC)=1` so the layer is deterministic regardless of input duplicates.

**Step 3 — ELT vs ETL.** Prefer ELT: load raw, transform with set-based SQL/dbt in
the warehouse — cheaper, testable, replayable. Choose ETL (transform before load)
only when the target can't scale the compute, or PII must be masked pre-landing.

**Step 4 — Deterministic steps.** Build thin layers (dbt models / Spark stages)
each a pure function of its inputs. No `current_timestamp`/`random()`/`now()` inside
transform logic that changes output across reruns — pass the run/logical date in.

**Step 5 — Idempotent writes.** The core rule: reruns must not accumulate. Overwrite
by partition (`INSERT OVERWRITE`/dynamic partition, dbt `insert_overwrite`, or
delete-partition-then-insert in one transaction) or MERGE on the key. Never a bare
append — that is the #1 cause of doubled rows on retry.

**Step 6 — Test & backfill.** Add not-null/unique/relationship/accepted-values
tests and a freshness + expected-row-count check. Document how to replay a single
partition; verify a replay produces byte-identical output.

## Principles
- Idempotent by construction: run N times, get the same table.
- Raw is immutable; all derived layers are rebuildable from it.
- Think in sets and partitions, not rows or files.
- Determinism: same inputs + same logical date → same output, always.
- Small, tested, named layers beat one giant query.

## Decision framework
- **ELT vs ETL:** warehouse can scale it and no pre-land masking needed → ELT; else ETL.
- **Full refresh vs partition overwrite:** small/dimension table → full refresh; large date-partitioned fact → overwrite the affected partitions.
- **Overwrite vs MERGE:** partition fully rebuildable from source → overwrite; sparse/keyed updates → MERGE (see [implementing-incremental-loading](../implementing-incremental-loading/SKILL.md)).
- **View vs table vs incremental model:** cheap/small → view; expensive+reused → table; large+append-mostly → incremental.
- **Snapshot vs recompute for history:** need point-in-time truth → snapshot; else recompute.

## Common mistakes
- **Blind `INSERT ... SELECT`** on rerun → duplicated rows; overwrite the partition or MERGE.
- **Non-deterministic logic** (`now()`, `rand()`, unordered `LIMIT`) → different output each run.
- **Business logic in staging** → untestable, non-reusable layers; keep staging mechanical.
- **No partition key** → can't replay one day without a full rebuild.
- **Transforming mutable raw in place** → nothing to replay from when logic changes.
- **Truncate-then-load without a transaction** → empty table visible on failure.
- **Skipping tests** → silent grain/fan-out drift ships to marts.

## Validation checklist
- [ ] Rerunning a partition produces identical output (no accumulation).
- [ ] Raw/landing is immutable; all derived layers rebuild from it.
- [ ] Grain stated and enforced (unique key) per layer.
- [ ] No non-deterministic functions altering results across reruns.
- [ ] Writes overwrite-by-partition or MERGE; no blind appends.
- [ ] Transform tests + freshness/row-count checks pass on realistic volume.
- [ ] Single-partition backfill procedure documented and verified.

## Edge cases
- **Late-arriving source data:** re-run affected partitions; don't only process "today".
- **Schema drift in source:** contract-check columns/types; see [managing-schema-evolution](../managing-schema-evolution/SKILL.md).
- **Full historical backfill:** parallelize by partition, cap concurrency, verify counts against source.
- **Cross-partition aggregates:** rebuild the whole aggregate, or window carefully so a partial rerun stays correct.
- **Time zones:** transform on a single logical/UTC date; avoid `DATE(col)` on local time.

## Related skills
- [implementing-incremental-loading](../implementing-incremental-loading/SKILL.md) — load only changed rows, MERGE/upsert.
- [designing-data-pipelines](../designing-data-pipelines/SKILL.md), [orchestrating-data-workflows](../orchestrating-data-workflows/SKILL.md), [ensuring-data-quality](../ensuring-data-quality/SKILL.md).
- [authoring-sql-queries](../../software-engineering/authoring-sql-queries/SKILL.md), [writing-automated-tests](../../software-engineering/writing-automated-tests/SKILL.md).

## Examples
**Input:** "Our nightly job appends orders, but retries after a failure double
yesterday's rows."
**Output:** Partition the fact by order date; replace the append with a partition
overwrite (`INSERT OVERWRITE ... WHERE order_date = @run_date` or dbt
`insert_overwrite`) so a retry rebuilds only that day. Move dedup into staging via
`ROW_NUMBER`, pin logic to the passed run_date instead of `now()`, and add a
unique test on `order_id` plus an expected-row-count check.

## Automation opportunities
- Run transform tests (dbt test / Great Expectations) and freshness checks in CI and post-run.
- Parameterize every model by logical date so any partition is replayable by config.
- Alert on row-count deltas and failed idempotency (rerun-diff) checks.
