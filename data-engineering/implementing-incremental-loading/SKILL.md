---
name: implementing-incremental-loading
description: Load only what changed — high-watermark incremental extracts, change data capture (log-based vs query-based), idempotent MERGE/upsert, handling deletes and late-arriving rows, and watermark bookkeeping. Use when the user asks to "load only new rows", "set up CDC", "write an incremental model", "do an upsert/MERGE", "capture deletes", or "why did my incremental load miss rows".
---

# Implementing Incremental Loading

## Scope
Loading only changed data since the last run: high-watermark extraction, CDC
(log-based vs query-based), idempotent MERGE/upsert, delete capture, late-arriving
rows, and durable watermark bookkeeping. Not full-refresh design, not streaming.

## Purpose
Move only the rows that changed, apply them so the target is identical whether the
load runs once or retries, and lose nothing — no missed updates, deletes, or
late-arriving rows, and no watermark that skips the boundary.

## When to use this skill
- "Load only new/changed rows", "incremental model", "don't full-refresh this".
- "Set up CDC", "capture deletes", "do a MERGE/upsert into the warehouse".
- "My incremental load missed rows / dropped updates / didn't catch deletes".

## When NOT to use this skill
- Designing full-refresh/partition-overwrite batch → [building-batch-transformations](../building-batch-transformations/SKILL.md).
- Real-time event streams → [building-streaming-pipelines](../building-streaming-pipelines/SKILL.md).
- Handling source column/type changes → [managing-schema-evolution](../managing-schema-evolution/SKILL.md).

## Inputs
- Source + a reliable change signal: an updated_at column, a monotonic id, or a CDC log.
- Target table, business/natural key, and whether hard deletes occur.
- Last-watermark storage, expected lateness/out-of-order, and update vs append-only nature.

## Outputs
- An incremental extract keyed to a persisted high-watermark (with overlap for lateness).
- An idempotent MERGE/upsert with delete handling, plus watermark bookkeeping updated only on success.

## Workflow
```
Progress:
- [ ] 1. Pick the change signal: log-based CDC vs query-based watermark
- [ ] 2. Read the last watermark; extract changes with a safe overlap window
- [ ] 3. Dedupe the delta to one row per key (latest wins)
- [ ] 4. Apply idempotently via MERGE/upsert on the natural key
- [ ] 5. Handle deletes: tombstones (log) or reconciliation (query-based)
- [ ] 6. Persist the new watermark only after the load commits
```

**Step 1 — Change signal.** Log-based CDC (Debezium/binlog/WAL) captures every
insert/update/delete in order — use it when deletes and intermediate updates
matter. Query-based (`WHERE updated_at > @wm`) is simpler but **misses hard deletes
and any change without a bumped timestamp** — that's the classic CDC gap.

**Step 2 — Extract with overlap.** Read the persisted watermark and pull `updated_at
>= @wm` (not `>`) with a small lookback (e.g. `@wm - 5 min`). A strict `>` on a
non-unique or clock-skewed timestamp silently drops boundary and late-committed
rows. Overlap re-pulls a few rows — safe, because the apply step is idempotent.

**Step 3 — Dedupe the delta.** A window may contain several versions of a key.
Collapse to the latest per key with `ROW_NUMBER() OVER (PARTITION BY nk ORDER BY
updated_at DESC, id DESC)=1` before applying, so MERGE has one row per key.

**Step 4 — Idempotent apply.** MERGE on the natural key: update on match, insert on
miss. This makes reruns safe — re-applying the same delta is a no-op. Never
`INSERT`-append a delta (retries duplicate) and never MERGE an un-deduped delta
(non-deterministic "which version won").

**Step 5 — Deletes.** Log-based: apply delete tombstones (hard-delete or set
`is_deleted`/valid-to for soft delete). Query-based has no delete signal —
reconcile periodically (anti-join source keys vs target, or full key-set compare)
or switch to CDC. Silently missing deletes leaves orphaned rows forever.

**Step 6 — Watermark bookkeeping.** Compute the new watermark from the **data
loaded** (max `updated_at`/committed LSN), and persist it in the **same
transaction** as the load, or only after commit. Advancing it before the load
commits means a crash skips that range permanently.

## Principles
- Move deltas, apply idempotently: MERGE, never blind append.
- Overlap and re-dedupe rather than trusting a razor-edge `>` boundary.
- A missing delete signal is missing data — plan for deletes explicitly.
- The watermark advances only on confirmed, committed load.
- Log-based CDC is complete and ordered; query-based is cheap but lossy — choose deliberately.

## Decision framework
- **Log-based vs query-based CDC:** need deletes/every update/exact order → log-based; append-mostly with a trustworthy timestamp → query-based.
- **Watermark column:** monotonic surrogate id (append-only) > `updated_at` (must be reliably set) > none (fall back to full compare).
- **MERGE vs delete+insert:** row-level keyed change → MERGE; whole-partition rebuild → overwrite ([building-batch-transformations](../building-batch-transformations/SKILL.md)).
- **Soft vs hard delete:** need history/audit → soft (valid-from/to, SCD2); else hard delete via tombstone.
- **Incremental vs periodic full refresh:** large + truly incremental → incremental; small or drift-prone → occasional full reconcile.

## Common mistakes
- **Strict `>` watermark** on non-unique/skewed timestamps → dropped boundary rows.
- **Query-based CDC ignoring deletes** → orphaned rows that never disappear.
- **Appending the delta** instead of MERGE → duplicates on retry.
- **MERGE on an un-deduped delta** → nondeterministic winner, wrong final state.
- **Advancing the watermark before commit** → a crash permanently skips a range.
- **Timestamp not set on every update** → missed changes; **no index on it** → full scans.
- **Late-arriving rows past the window** → never picked up without lookback/reconcile.
- **Ignoring out-of-order commit (LSN vs wall clock)** → gaps under concurrency.

## Validation checklist
- [ ] Change signal chosen deliberately; deletes are captured or reconciled.
- [ ] Extract uses `>=` + a lookback overlap, not a bare `>` boundary.
- [ ] Delta deduped to one row per key before apply.
- [ ] Apply is a MERGE/upsert on the natural key; reruns are no-ops.
- [ ] Watermark persisted only after (or within) the committed load.
- [ ] Deletes handled (tombstone or reconcile); no orphaned rows.
- [ ] Reconciliation vs full source proves no missed rows on realistic data.

## Edge cases
- **First load / no watermark:** seed with a full backfill, then set the initial watermark from it.
- **Late-arriving dimensions:** widen the lookback or reconcile a trailing window daily.
- **Schema change mid-stream:** version the delta contract → [managing-schema-evolution](../managing-schema-evolution/SKILL.md).
- **Multiple updates per key per window:** dedup by `updated_at`/LSN, not by arrival order.
- **Clock skew / non-monotonic timestamps:** prefer LSN/commit-order from log-based CDC.
- **Hard truncate at source:** query-based won't notice; needs full reconcile or CDC DDL events.

## Related skills
- [building-batch-transformations](../building-batch-transformations/SKILL.md) — full-refresh and partition-overwrite design.
- [managing-schema-evolution](../managing-schema-evolution/SKILL.md), [ensuring-data-quality](../ensuring-data-quality/SKILL.md), [modeling-dimensional-warehouses](../modeling-dimensional-warehouses/SKILL.md).
- [authoring-sql-queries](../../software-engineering/authoring-sql-queries/SKILL.md) — MERGE/upsert and sargable watermark predicates.

## Examples
**Input:** "We load rows where `updated_at > last_run` and MERGE them, but the
target is missing some updates and still has rows that were deleted at source."
**Output:** Two gaps. Missed updates: switch `>` to `>=` with a small lookback and
re-dedupe (latest per key) — a strict boundary on a coarse/skewed timestamp drops
rows; the idempotent MERGE makes the re-pull harmless. Missing deletes: query-based
extraction has no delete signal, so add a periodic key anti-join reconcile or move
to log-based CDC with tombstones. Persist the new watermark inside the load
transaction so a crash can't skip a range.

## Automation opportunities
- Schedule a periodic full reconcile (source vs target key/row counts) to catch drift and missed deletes.
- Track watermark lag and delta row counts; alert on zero-delta or sudden spikes.
- Test MERGE idempotency in CI: apply the same delta twice, assert the table is unchanged.
