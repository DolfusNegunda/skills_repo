---
name: optimizing-spark-jobs
description: Tune slow or failing Spark/PySpark jobs — diagnose skew, minimize and right-size shuffle, use broadcast joins, fix the small-file and partition-count problems, cache deliberately, exploit adaptive query execution, and stop driver-side collects. Use when the user says "my Spark job is slow", "reduce shuffle", "Spark OOM", "one task takes forever", or "why is this stage stuck".
---

# Optimizing Spark Jobs

## Scope
Performance tuning of Spark/PySpark batch and structured-streaming jobs on a
cluster: read the Spark UI, find the bottleneck stage, fix skew, shuffle, joins,
partitioning, file sizes, and caching. Not query logic correctness, not warehouse
SQL, not single-node app code.

## Purpose
Make a Spark job faster and cheaper *and* stop it OOM-ing, by measuring in the
Spark UI first, changing the one thing that governs the slow stage, and
re-measuring — not by blindly bumping executor memory.

## When to use this skill
- "My Spark/PySpark job is slow / stuck / keeps OOM-ing."
- "One task runs for an hour while the rest finish" (skew).
- "Reduce shuffle", "too many small files", "the join spills to disk".
- A stage has thousands of tiny tasks, or a `collect()`/`toPandas()` blows the driver.

## When NOT to use this skill
- Cloud warehouse query tuning (Snowflake/BigQuery/Synapse) → [tuning-warehouse-performance](../tuning-warehouse-performance/SKILL.md).
- General single-process app performance → [optimizing-code-performance](../../software-engineering/optimizing-code-performance/SKILL.md).
- Cutting spend across the platform, not one job → [optimizing-data-costs](../optimizing-data-costs/SKILL.md).

## Inputs
- The job/notebook, the Spark UI (or event log) for a representative run, and Spark version.
- Cluster shape: executor count, cores, memory; input/output formats and sizes.
- The slow symptom: wall time, failing stage, OOM location (driver vs executor), row/partition counts.

## Outputs
- The bottleneck named (stage + cause: skew / shuffle / spill / small files / driver collect).
- A minimal, measured change with before/after runtime and the config/code diff.

## Workflow
```
Progress:
- [ ] 1. Reproduce; capture the Spark UI for one representative run
- [ ] 2. Find the bottleneck stage (longest, most spill, or straggler task)
- [ ] 3. Classify the cause: skew / shuffle / join / partitioning / files / driver
- [ ] 4. Apply the one targeted fix for that cause
- [ ] 5. Re-run and compare; confirm AQE is on and doing its job
- [ ] 6. Right-size partitions and output files; remove needless caching
```

**Step 1 — Measure first.** Never tune from the code alone. Open the Spark UI:
Stages tab for task-time distribution, SQL tab for the plan and shuffle read/write,
Executors tab for spill and GC. Read the plan *before* changing anything.

**Step 2 — Find the stage.** The bottleneck is the stage with the longest task
max, the biggest shuffle spill, or a max task time far above the median (the
straggler signature of skew). Ignore fast stages.

**Step 3 — Classify.** Straggler + one huge partition = **skew**. Large shuffle
write feeding an exchange = **shuffle-bound**. `SortMergeJoin` where one side is
small = a **missed broadcast**. Thousands of tiny tasks or tiny output files =
**partition/file sizing**. OOM on the driver = a **collect**.

**Step 4 — Fix the cause.** Skew: enable AQE skew join, or **salt** the hot key
(add a random suffix, join, aggregate away). Missed broadcast: `broadcast(df)` the
small side (< ~10–100 MB) so the big side isn't shuffled. Shuffle-bound: filter and
project *before* the wide op, pre-aggregate, avoid re-shuffling on the same key.
Driver OOM: replace `collect()`/`toPandas()` with a write, `limit`, or aggregate.

**Step 5 — AQE.** Confirm `spark.sql.adaptive.enabled=true` — it coalesces
post-shuffle partitions, converts to broadcast, and splits skewed partitions at
runtime. Verify in the SQL plan that it actually fired.

**Step 6 — Right-size.** Target ~128–256 MB per partition and per output file.
`repartition`/`coalesce` before writing; partition output columns with sane
cardinality. Cache only a dataset reused ≥2× and that fits — then `unpersist`.

## Principles
- Measure in the UI before changing code; tune the one governing stage, not everything.
- The fastest shuffle is the one you don't do; the cheapest data is the data you filter early.
- Broadcast the small side instead of shuffling the big side.
- Keep data on the executors; the driver is not a data plane.
- Partition and file size are a Goldilocks problem — not too many, not too few.
- Cache is a deliberate trade (memory + eviction risk), not a default.

## Decision framework
- **Broadcast vs shuffle join:** one side under the broadcast threshold → broadcast; both large → sort-merge, and attack skew.
- **repartition vs coalesce:** need more/even partitions or a key layout → repartition (shuffles); only shrinking partition count → coalesce (no shuffle).
- **Salting vs AQE skew join:** AQE handles most skew for free; salt when a few keys still dominate or on pre-AQE Spark.
- **cache vs recompute:** reused ≥2× and fits in memory/disk → cache; used once → recompute.
- **collect vs write:** need all rows downstream → write to storage; need a scalar/sample → aggregate or `limit` then collect.

## Common mistakes
- **Tuning without the UI** — bumping executor memory instead of finding the skewed stage.
- **`collect()`/`toPandas()`** on a large frame → driver OOM.
- **Missed broadcast** — a small dimension shuffled through a sort-merge join.
- **Skew ignored** — one straggler task defines the whole job's runtime.
- **Small-file explosion** — thousands of tiny output files from over-partitioned writes.
- **`repartition(1)`** to get one file, forcing all data through one task.
- **Caching everything**, evicting the useful blocks and inflating GC.
- **UDFs / Python `for` loops** where a built-in column expression would stay in the JVM/vectorized path.
- **Re-shuffling** on the same key across steps instead of keeping the partitioning.

## Validation checklist
- [ ] Bottleneck stage identified in the UI, not guessed.
- [ ] Task-time distribution is even (no straggler) after the fix.
- [ ] Shuffle read/write and spill dropped versus the baseline run.
- [ ] Small side broadcast where applicable; big side not needlessly shuffled.
- [ ] AQE enabled and confirmed active in the plan.
- [ ] Partitions and output files ~128–256 MB; no tiny-file explosion.
- [ ] No `collect`/`toPandas` on large data; driver memory stable.
- [ ] Before/after runtime recorded.

## Edge cases
- **Streaming:** watch state-store size and per-batch shuffle; use watermarks; keep partitions stable across micro-batches.
- **Highly skewed keys (nulls, defaults):** filter/handle them separately, or salt.
- **Many small input files:** coalesce reads or compact upstream before processing.
- **Wide schemas / nested data:** project needed columns early; prune before the shuffle.
- **Broadcast that OOMs executors:** the "small" side grew — lower the threshold or switch to sort-merge.

## Related skills
- [tuning-warehouse-performance](../tuning-warehouse-performance/SKILL.md) — the warehouse-SQL counterpart.
- [building-batch-transformations](../building-batch-transformations/SKILL.md) — the transformations you're tuning.
- [optimizing-data-costs](../optimizing-data-costs/SKILL.md) — platform-wide spend.
- [observing-data-pipelines](../observing-data-pipelines/SKILL.md) — catching regressions in production.
- [optimizing-code-performance](../../software-engineering/optimizing-code-performance/SKILL.md) — general performance method.

## Examples
**Input:** "My join takes an hour; one task runs long after the others finish."
**Output:** Straggler in the UI = skew on the join key. First confirm AQE skew
join is on; if a few hot keys still dominate, salt them (append a random 0–N suffix
to the key on both sides, join, then drop the suffix). Also broadcast the small
dimension so the big fact isn't shuffled. Re-run: task times even, wall time from
60 min to 8.

## Automation opportunities
- Persist Spark event logs and alert on shuffle spill, straggler ratio, and output-file counts per job.
- Set AQE and sane shuffle-partition defaults in the cluster/session template.
- Add a CI guard that fails a job introducing `collect()`/`toPandas()` on unbounded data.
