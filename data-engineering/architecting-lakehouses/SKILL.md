---
name: architecting-lakehouses
description: Design a lakehouse on the medallion pattern — bronze/silver/gold layering, open table formats (Delta/Iceberg), ACID transactions and time travel, physical file layout and the small-file problem, and compaction with OPTIMIZE and Z-order/clustering. Use when the user says "design a lakehouse", "set up bronze/silver/gold", "Delta vs Iceberg", "too many small files", "my Spark reads are slow on the lake", or "how do I lay out these tables".
---

# Architecting Lakehouses

## Scope
Physical and structural design of a lakehouse: medallion layering, table-format
choice, transaction/time-travel guarantees, partitioning, and file compaction.
Not dimensional/star modeling ([modeling-dimensional-warehouses](../modeling-dimensional-warehouses/SKILL.md)),
not warehouse query tuning ([tuning-warehouse-performance](../tuning-warehouse-performance/SKILL.md)).

## Purpose
Produce a layered lakehouse where raw data is preserved immutably, cleaned data is
trustworthy, serving tables are fast, and the physical layout avoids the small-file
tax — using an open table format for ACID, schema enforcement, and time travel.

## When to use this skill
- "Design a lakehouse", "set up medallion / bronze-silver-gold layers".
- "Delta or Iceberg?", "do we need Hudi?", "how should these tables be laid out?".
- "Reads are slow / we have millions of tiny files", "how do I compact / Z-order?".

## When NOT to use this skill
- Star schemas, facts/dimensions, SCDs → [modeling-dimensional-warehouses](../modeling-dimensional-warehouses/SKILL.md).
- Tuning a slow warehouse query/engine → [tuning-warehouse-performance](../tuning-warehouse-performance/SKILL.md).
- Tuning the Spark job itself (shuffle, skew, memory) → [optimizing-spark-jobs](../optimizing-spark-jobs/SKILL.md).

## Inputs
- Sources feeding bronze, volumes, and file arrival sizes/counts.
- Query/serving patterns on gold (which columns filter, expected latency).
- Engine + catalog (Spark/Databricks/Trino, Unity/Glue/Hive) and format constraints.

## Outputs
- A layer design (bronze/silver/gold with each layer's contract and write mode).
- Table-format choice, partition + clustering strategy, and a compaction/retention plan.

## Workflow
```
Progress:
- [ ] 1. Define the three layers and each layer's contract/guarantee
- [ ] 2. Pick an open table format (Delta/Iceberg) and a catalog
- [ ] 3. Design partitioning by real filter columns — coarse, low cardinality
- [ ] 4. Plan file sizing; schedule compaction (OPTIMIZE) + Z-order/clustering
- [ ] 5. Set retention: VACUUM / snapshot expiry vs time-travel needs
- [ ] 6. Enforce schema at layer boundaries; keep bronze immutable
```

**Step 1 — Layers.** Bronze = raw, append-only, immutable (replay source of truth).
Silver = cleaned, deduped, conformed, schema-enforced. Gold = business-level,
aggregated/serving. Each layer only reads from the one below.

**Step 2 — Format + catalog.** Use a format with ACID, schema enforcement, and time
travel (Delta or Iceberg) — never bare Parquet directories, which give no atomicity
and no safe concurrent writes. Register tables in a catalog so engines share metadata.

**Step 3 — Partition deliberately.** Partition by a low-cardinality column you
actually filter on (usually event date). Over-partitioning (e.g. by user_id, or
date+hour on small volume) is the #1 cause of the small-file problem.

**Step 4 — File sizing + clustering.** Target ~128MB–1GB files. Run `OPTIMIZE`
(bin-packing) to compact small files, and `Z-ORDER`/liquid clustering on high-selectivity
filter columns to enable data skipping. Many small files kill read throughput via
per-file overhead and metadata explosion.

**Step 5 — Retention.** Time travel keeps old files/snapshots; balance debuggability
against storage. Set `VACUUM` (Delta) / snapshot expiry (Iceberg) beyond your
longest time-travel need — vacuuming too aggressively breaks in-flight readers and replay.

**Step 6 — Enforce schema at boundaries.** Reject or quarantine non-conforming data
entering silver; let bronze absorb raw drift. Coordinate changes via [managing-schema-evolution](../managing-schema-evolution/SKILL.md).

## Principles
- Bronze is immutable and complete — it is your replay button; never edit it in place.
- Push quality/conformance work down into silver; keep gold cheap to serve.
- Partition coarsely, cluster/Z-order finely; more partitions is usually worse.
- Right-size files: compaction is maintenance, not an afterthought.
- Let the table format give you ACID and time travel — don't hand-roll it on Parquet.

## Decision framework
- **Delta vs Iceberg:** Databricks/Spark-centric → Delta; multi-engine/Trino/Flink neutrality → Iceberg; both give ACID + time travel — match your engine and catalog.
- **Partition column:** low-cardinality + frequently filtered (event date) → partition; high-cardinality filter → Z-order/cluster, don't partition.
- **OPTIMIZE cadence:** high-churn ingest → frequent compaction; append-then-read batch → after each load.
- **CoW vs MoR (Iceberg/Hudi):** read-heavy → copy-on-write; write/update-heavy with tolerable read merge → merge-on-read.
- **Full rebuild vs MERGE into silver:** small → rebuild; large incremental → `MERGE`.

## Common mistakes
- **Small-file problem** — streaming/over-partitioned writes create millions of tiny files; no compaction scheduled.
- **Over-partitioning** by high-cardinality or too many columns → tiny partitions, slow listing.
- **Bare Parquet** with no table format → no ACID, corrupt reads on concurrent writes.
- **Mutating bronze** — losing the immutable replay source.
- **No Z-order/clustering** on the real filter column → full scans despite partitions.
- **VACUUM window shorter than time-travel/reader needs** → broken queries and lost history.
- **Business logic in bronze** — coupling raw ingest to changing rules.

## Validation checklist
- [ ] Three layers defined; each reads only from the layer below.
- [ ] Bronze is append-only/immutable and sufficient to replay downstream.
- [ ] Open table format (Delta/Iceberg) with a shared catalog, not raw Parquet.
- [ ] Partitioning is low-cardinality and matches actual filter predicates.
- [ ] Target file size set; OPTIMIZE/compaction + Z-order/clustering scheduled.
- [ ] Retention (VACUUM/snapshot expiry) exceeds time-travel and reader needs.
- [ ] Schema enforced at the silver boundary; violations quarantined.

## Edge cases
- **Streaming ingest to bronze:** micro-batch and compact, or you flood the lake with small files.
- **GDPR/row deletes:** use format-native `DELETE`/`MERGE`; plain files can't erase rows.
- **Concurrent writers:** rely on format optimistic concurrency; design to avoid conflicting partition writes.
- **Backfill into partitioned tables:** `REPLACE`/overwrite by partition, then OPTIMIZE.
- **Schema evolution:** additive columns are safe; renames/type changes need a managed migration.

## Related skills
- [modeling-dimensional-warehouses](../modeling-dimensional-warehouses/SKILL.md) — the logical star model layered on gold.
- [optimizing-spark-jobs](../optimizing-spark-jobs/SKILL.md) — tuning the compute writing the tables.
- [optimizing-data-costs](../optimizing-data-costs/SKILL.md) — storage/compaction/retention cost tradeoffs.
- [reviewing-architecture](../../review/reviewing-architecture/SKILL.md) — reviewing the overall lakehouse design.

## Examples
**Input:** "Our streaming job writes Delta and reads got 10x slower; we have ~4M
files under the table."
**Output:** Classic small-file problem from per-micro-batch writes. Fix: partition
only by event date, schedule `OPTIMIZE ... ZORDER BY (customer_id)` post-batch to
bin-pack to ~256MB files and enable data skipping, enable auto-compaction/optimized
writes, and set VACUUM retention past the time-travel window before purging.

## Automation opportunities
- Schedule compaction (OPTIMIZE + Z-order/clustering) and VACUUM as maintenance jobs.
- Alert on file count / average file size per table to catch small-file drift early.
- Enforce silver schema contracts in CI; auto-quarantine non-conforming batches.
