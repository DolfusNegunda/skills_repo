---
name: building-streaming-pipelines
description: Build real-time streaming pipelines — reason about event time vs processing time, set watermarks, choose windows, handle late/out-of-order data, manage Kafka offsets and checkpoints, and pick the right delivery guarantee. Use when the user asks to "build a streaming pipeline", "process Kafka events", "set a watermark", "handle late data", "why is my streaming state growing", or "how do I get exactly-once".
---

# Building Streaming Pipelines

## Scope
Designing and building continuous stream processing (Kafka + Spark Structured
Streaming / Flink): time semantics, watermarks, windowing, late/out-of-order data,
offset/checkpoint management, and delivery guarantees. Not batch, not job scheduling.

## Purpose
Produce a streaming job with correct event-time results, bounded state, no lost or
silently duplicated records, and a delivery guarantee that matches the downstream —
one that resumes cleanly from a checkpoint after a crash.

## When to use this skill
- "Build a streaming pipeline", "process Kafka/Kinesis events in real time".
- "Set a watermark", "choose a window", "handle late / out-of-order events".
- "Why does my streaming state keep growing", "how do I get exactly-once".

## When NOT to use this skill
- Scheduled/replayable table transforms → [building-batch-transformations](../building-batch-transformations/SKILL.md).
- Scheduling/dependency orchestration of jobs → [orchestrating-data-workflows](../orchestrating-data-workflows/SKILL.md).
- Changed-row extract from databases → [implementing-incremental-loading](../implementing-incremental-loading/SKILL.md).

## Inputs
- Source (topic, partitions, key, throughput) and the event schema + timestamp field.
- Required latency, correctness bar, and downstream sink (its idempotency/txn support).
- Expected lateness/skew, out-of-order degree, and the acceptable delivery guarantee.

## Outputs
- A job with explicit event-time extraction, watermark, window, and checkpoint config.
- A documented delivery guarantee (source→sink), offset-commit strategy, and late-data policy.

## Workflow
```
Progress:
- [ ] 1. Pin event time vs processing time; extract the event timestamp
- [ ] 2. Set a watermark = max lateness you'll wait for
- [ ] 3. Choose the window (tumbling/sliding/session) to match the question
- [ ] 4. Decide late/out-of-order policy: drop, side-output, or allowed lateness
- [ ] 5. Manage offsets + checkpoints; commit only after the sink write
- [ ] 6. Choose the delivery guarantee end-to-end; make the sink idempotent/txn
```

**Step 1 — Time semantics.** Aggregate on **event time** (when it happened), not
processing time (when it arrived) — processing time gives wrong counts under delay
or replay. Extract the timestamp from the payload, not the ingestion clock.

**Step 2 — Watermark.** A watermark tells the engine "no more events older than T
will come," letting it emit windows and drop old state. **Missing watermark on a
keyed/windowed aggregation → unbounded state growth → OOM.** Set it to the largest
lateness you're willing to wait (e.g. `withWatermark("ts","10 minutes")`); larger =
more completeness, more latency and state.

**Step 3 — Window.** Tumbling (fixed, non-overlapping) for periodic buckets;
sliding (overlapping) for moving averages; session (gap-based) for user activity.
Match the window to the business question, not the arrival rate.

**Step 4 — Late/out-of-order.** Events past the watermark are late. Decide
explicitly: drop (default), route to a side-output/dead-letter for reprocessing, or
allow bounded lateness and update the window. Never assume in-order arrival across
partitions — order holds only within a Kafka partition/key.

**Step 5 — Offsets & checkpoints.** Let the framework checkpoint offsets + state
together; commit source offsets only after the sink write succeeds. Committing
before the write loses data on crash; committing without checkpointed state
double-counts. Never auto-commit offsets independently of the checkpoint.

**Step 6 — Delivery guarantee.** at-most-once (may lose), at-least-once (may
duplicate), exactly-once (needs replayable source + transactional/idempotent sink +
checkpointed state). At-least-once is the common default — make it effectively-once
by writing to an idempotent/keyed sink so duplicates collapse.

## Principles
- Event time is truth; processing time is an accident of arrival.
- Every windowed/stateful aggregation needs a watermark, or state grows forever.
- Ordering is per-partition only; design for out-of-order across the topic.
- Offsets and state must advance atomically with the output write.
- Pick the weakest guarantee the downstream can tolerate, then make the sink absorb duplicates.

## Decision framework
- **Event vs processing time:** correctness under delay/replay matters → event time; pure "rate now" dashboards → processing time ok.
- **Watermark size:** high completeness need → longer; low latency need → shorter (accept more drops).
- **Window type:** fixed buckets → tumbling; smoothed metric → sliding; per-session activity → session.
- **Guarantee:** money/dedup-critical → exactly-once; analytics-tolerant → at-least-once + idempotent sink; lossy telemetry → at-most-once.
- **State store:** large keyed state → RocksDB/state backend; small → in-memory.

## Common mistakes
- **Windowing on processing time** → wrong counts when data is delayed or replayed.
- **No watermark** on a stateful aggregation → unbounded state, eventual OOM.
- **Auto-committing offsets** before/independently of the sink write → data loss or double-count.
- **Assuming global order** → wrong sessionization; order is per partition only.
- **Treating at-least-once as exactly-once** → duplicate rows in the sink.
- **Tiny checkpoint interval** → throughput collapse; **huge** → long recovery/replay.
- **Ignoring late data** → silently dropped events with no dead-letter trail.
- **Key skew** → one partition/task hot; state and lag pile up on it.

## Validation checklist
- [ ] Aggregations use event time from the payload, not processing time.
- [ ] Every stateful/windowed op has a watermark sized to real lateness.
- [ ] State stays bounded under sustained load (verified, not assumed).
- [ ] Offsets commit only after successful sink write; state is checkpointed.
- [ ] Delivery guarantee stated source→sink; sink is idempotent or transactional.
- [ ] Late/out-of-order policy is explicit (drop/side-output/allowed lateness).
- [ ] Job resumes correctly from checkpoint after a forced kill.

## Edge cases
- **Reprocessing/replay:** event-time logic + idempotent sink lets you replay from an offset safely.
- **Schema evolution on the topic:** use a registry + compatibility rules → [managing-schema-evolution](../managing-schema-evolution/SKILL.md).
- **Stream-stream joins:** both sides need watermarks + a time bound, or join state is unbounded.
- **Partition rebalance/scaling:** ensure state redistributes by key; avoid non-key-local state.
- **Burst/backpressure:** cap ingest rate (`maxOffsetsPerTrigger`) so recovery doesn't OOM.
- **Time skew across producers:** watermark on the slowest reasonable source, not one clock.

## Related skills
- [building-batch-transformations](../building-batch-transformations/SKILL.md) — the scheduled/replayable counterpart.
- [orchestrating-data-workflows](../orchestrating-data-workflows/SKILL.md), [observing-data-pipelines](../observing-data-pipelines/SKILL.md), [optimizing-spark-jobs](../optimizing-spark-jobs/SKILL.md).
- [handling-errors-and-logging](../../software-engineering/handling-errors-and-logging/SKILL.md) — dead-letter and failure handling.

## Examples
**Input:** "My Spark Structured Streaming job counts events per minute but the
counts are wrong and the executors keep running out of memory."
**Output:** Switch the window to event time and add `withWatermark("event_ts",
"10 minutes")` before the `window(...)` groupBy — the missing watermark is why old
state never drops (the OOM) and processing-time windows are why counts are wrong.
Route past-watermark events to a dead-letter topic, checkpoint to durable storage,
and write to an idempotent keyed sink so at-least-once retries don't double-count.

## Automation opportunities
- Alert on consumer lag, watermark lag, and state-store size growth.
- Chaos-test recovery: kill the job and assert it resumes from checkpoint with no loss/dup.
- Enforce a schema registry with compatibility checks in CI for topic contracts.
