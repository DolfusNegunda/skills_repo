---
name: designing-data-pipelines
description: Architect a data pipeline end-to-end — choose batch vs streaming, define sources/sinks and data contracts, make loads idempotent and replayable, plan backfills and failure recovery, and reason about delivery guarantees (at-least-once vs exactly-once). Use when the user says "design a data pipeline", "batch or streaming?", "how do I make this reload safe", "how do I backfill", or "we get duplicate/missing rows".
---

# Designing Data Pipelines

## Scope
End-to-end pipeline architecture: source/sink selection, contracts, idempotency,
replay/backfill, and delivery semantics. Not the transform logic itself
([building-batch-transformations](../building-batch-transformations/SKILL.md)),
not scheduler wiring ([orchestrating-data-workflows](../orchestrating-data-workflows/SKILL.md)).

## Purpose
Produce a design where any run can be safely re-run, late/duplicate/out-of-order
data lands correctly, backfills use the same code path as production, and the
delivery guarantee is a deliberate choice — not an accident discovered in prod.

## When to use this skill
- "Design a pipeline from X to Y", "should this be batch or streaming?".
- "Make this load idempotent / safe to re-run", "we saw duplicate rows after a retry".
- "How do we backfill history?", "what happens when a run fails halfway?".

## When NOT to use this skill
- The SQL/Spark transform inside a step → [building-batch-transformations](../building-batch-transformations/SKILL.md).
- Scheduling, retries, DAG dependencies → [orchestrating-data-workflows](../orchestrating-data-workflows/SKILL.md).
- Incremental capture mechanics (CDC, watermarks) → [implementing-incremental-loading](../implementing-incremental-loading/SKILL.md).

## Inputs
- Sources and sinks: systems, formats, volume, arrival pattern, and their grain.
- Freshness/SLA target, and whether consumers need exactly-once correctness.
- Schema + ownership of each source (who can change it), and expected late/dup data.

## Outputs
- A pipeline design: batch/stream decision, contract per edge, load strategy
  (idempotent key + write mode), backfill plan, and stated delivery guarantee.
- A failure-recovery story: what a retry does, and what a full replay does.

## Workflow
```
Progress:
- [ ] 1. Map sources → sinks; pin the grain and freshness SLA of each
- [ ] 2. Decide batch vs streaming from the SLA, not from novelty
- [ ] 3. Define a data contract on every edge (schema, semantics, ownership)
- [ ] 4. Make each load idempotent: natural key + MERGE/overwrite-by-partition
- [ ] 5. Plan backfill and replay through the SAME code path
- [ ] 6. Choose and enforce a delivery guarantee; handle late/dup/out-of-order
```

**Step 1 — Map and pin grain.** For every source and sink write "one row per ___"
and its freshness need. Mismatched grain between an edge's two ends is the root of
most double-counting downstream.

**Step 2 — Batch vs streaming.** Drive off the SLA: minutes-to-hours → batch (or
micro-batch); sub-second/continuous → streaming. Streaming multiplies operational
cost and state-management burden — do not pick it for a daily report.

**Step 3 — Contracts.** Pin schema, types, nullability, semantic meaning, and the
owner for each edge. A contract makes schema drift a caught error, not silent
corruption; enforce it with a schema check on read (see [managing-schema-evolution](../managing-schema-evolution/SKILL.md)).

**Step 4 — Idempotent loads.** Never blind-`INSERT` in a retryable step. Use a
natural/business key with `MERGE` (upsert), or `INSERT OVERWRITE` of a whole
partition. Re-running the step must converge to the same table state — this is what
makes at-least-once delivery safe.

**Step 5 — Backfill = production path.** Parameterize by date/partition so a
backfill is the same job over an older range. A separate one-off backfill script
drifts from prod logic and reintroduces bugs.

**Step 6 — Delivery guarantee.** State it explicitly and design to it (Principles below).

## Principles
- Idempotency is the foundation: if a step is idempotent, retries and replays are free.
- Everything fails; design the retry and the full replay before the happy path.
- A contract on every edge turns silent corruption into a loud, early error.
- Partition by the dimension you reload by (usually event date) so overwrites are surgical.
- Prefer at-least-once + idempotent sink over chasing true exactly-once plumbing.

## Decision framework
- **Batch vs streaming:** SLA in minutes/hours and bounded data → batch; continuous low-latency → streaming; "near-real-time" that tolerates minutes → micro-batch.
- **Idempotency mechanism:** stable business key → `MERGE`; append-only events → dedupe key + partition overwrite; full small table → truncate-and-load.
- **At-least-once vs exactly-once:** at-least-once + idempotent write ≈ effectively-once and far simpler; reserve exactly-once transactional sinks for non-idempotent side effects.
- **Full vs incremental refresh:** small/volatile → full; large/append → incremental ([implementing-incremental-loading](../implementing-incremental-loading/SKILL.md)).

## Common mistakes
- **Non-idempotent load** (blind INSERT) → duplicates on every retry.
- **Believing the queue gives exactly-once** — most give at-least-once; the sink must dedupe.
- **Backfill via a bespoke script** that diverges from the production transform.
- **No data contract** → an upstream column rename silently nulls a downstream field.
- **Streaming chosen for a daily report** — needless state, cost, and on-call load.
- **Ignoring late/out-of-order events** — fixed windows drop stragglers silently.
- **Partitioning by load date, not event date** — makes replay overwrite the wrong slice.

## Validation checklist
- [ ] Grain and freshness SLA stated for every source and sink.
- [ ] Batch/stream choice justified by the SLA, not preference.
- [ ] Each edge has a schema+semantics contract with a named owner.
- [ ] Every load is idempotent (MERGE / partition overwrite); re-run converges.
- [ ] Backfill reuses the production code path, parameterized by range.
- [ ] Delivery guarantee stated; late/duplicate/out-of-order handling defined.
- [ ] Failure recovery documented for both single-step retry and full replay.

## Edge cases
- **Late-arriving data:** use watermarks + allowed lateness; reprocess the affected partition.
- **Poison records:** route to a dead-letter path; never let one bad row wedge the run.
- **Non-idempotent sinks** (emails, payments): use a transactional outbox or dedup ledger.
- **Source without a stable key:** derive a deterministic hash key for MERGE.
- **Schema drift mid-stream:** fail closed on contract violation, alert, quarantine.

## Related skills
- [implementing-incremental-loading](../implementing-incremental-loading/SKILL.md) — CDC, watermarks, incremental keys.
- [orchestrating-data-workflows](../orchestrating-data-workflows/SKILL.md) — scheduling, retries, dependencies.
- [building-streaming-pipelines](../building-streaming-pipelines/SKILL.md) — the streaming path in depth.
- [reviewing-architecture](../../review/reviewing-architecture/SKILL.md) — design review of the overall system.

## Examples
**Input:** "We ingest orders from Kafka into a warehouse table and see duplicate
rows whenever a consumer restarts."
**Output:** Diagnose at-least-once delivery + a non-idempotent INSERT sink. Redesign:
dedupe on `order_id` via `MERGE` into an event-date-partitioned table, checkpoint
offsets, and treat the pipeline as at-least-once + idempotent (effectively-once).
Backfill = replay offsets over a date range through the same MERGE job.

## Automation opportunities
- Enforce data contracts in CI with a schema-diff/validation gate on each source.
- Make idempotency a test: run each load twice in CI, assert identical table state.
- Generate backfill runs from the same parameterized job the scheduler invokes.
