---
name: orchestrating-data-workflows
description: Orchestrate scheduled data workflows (Airflow/ADF/Dagster-style) — model dependencies as a DAG, make every task idempotent and retriable with backoff, support backfills, and set schedules and SLAs without hidden cross-task coupling. Use when the user says "schedule this pipeline", "build the DAG", "set up Airflow/Dagster/ADF", "add a backfill", "wire task dependencies", or "these jobs run in the wrong order".
---

# Orchestrating Data Workflows

## Scope
Turning a set of data jobs into a scheduled, dependency-aware workflow: a DAG of
idempotent, retriable tasks with defined schedules, SLAs, and backfill support.
Covers the orchestration layer (Airflow/ADF/Dagster-style), not the transform SQL
inside a task or the monitoring depth around it.

## Purpose
Run the right tasks in the right order at the right time, every time — recoverable
after failure, re-runnable without damage, and backfillable over history, with no
hidden coupling that breaks silently when one task moves.

## When to use this skill
- "Schedule this pipeline / build the DAG / set up Airflow/Dagster/ADF."
- Wiring task ordering, retries, or SLAs; adding a backfill over past dates.
- Jobs run in the wrong order, double-process, or can't recover after a failure.

## When NOT to use this skill
- The transform logic inside a task → [building-batch-transformations](../building-batch-transformations/SKILL.md).
- Alerting/metrics/dashboard depth → [observing-data-pipelines](../observing-data-pipelines/SKILL.md).
- Only-changed-rows load strategy → [implementing-incremental-loading](../implementing-incremental-loading/SKILL.md).
- Data-correctness checks between tasks → [ensuring-data-quality](../ensuring-data-quality/SKILL.md).

## Inputs
- The jobs to run, their true data dependencies, and cadence/business SLA.
- Source availability signals (arrival times, upstream partitions) and time zones.
- Orchestrator + executor, secrets/connection story, and compute the tasks call.
- Whether history must be backfilled and over what range/grain.

## Outputs
- A DAG: tasks, explicit dependencies, schedule, retries/backoff, timeouts, SLAs.
- Idempotent tasks keyed by the run's logical date/partition, safe to re-run.
- A working backfill path and a runbook for failed/late/stuck runs.

## Workflow
```
Progress:
- [ ] 1. Map real data dependencies; draw the DAG (no hidden edges)
- [ ] 2. Set schedule, partition/logical date, catchup, and time zone
- [ ] 3. Make each task idempotent, keyed by partition; define done
- [ ] 4. Add retries with backoff, timeouts, and SLAs per task
- [ ] 5. Wire backfill (parameterized by date range) and test one slice
- [ ] 6. Add failure handling/alerts hooks; dry-run then enable
```

**Step 1 — Map dependencies.** List each task's actual data inputs/outputs and draw
edges only where a real data dependency exists. Every ordering assumption becomes an
explicit edge — never rely on "it happens to run after". Keep it a DAG; break cycles.

**Step 2 — Schedule.** Set cadence, the logical/execution date, and partition grain.
Decide `catchup` deliberately (on for backfillable history, off to skip the gap).
Pin the time zone; account for DST and late-arriving source data with sensors, not
fixed sleeps.

**Step 3 — Idempotency.** Key every write to the run's partition and use
delete-then-insert / MERGE / overwrite-partition so a re-run replaces, never
duplicates. Define each task's "done" as a checkable output (partition exists, row
count nonzero), not "the code finished".

**Step 4 — Reliability.** Add bounded retries with exponential backoff for transient
faults, a task timeout so nothing hangs forever, and an SLA that fires when a task
misses its window. Don't retry non-idempotent or deterministic-failure tasks blindly.

**Step 5 — Backfill.** Parameterize the run by date range so one code path serves
schedule and backfill. Test a single historical slice end to end, then run the range
with bounded concurrency so you don't overwhelm sources or warehouse.

**Step 6 — Ship.** Wire failure/SLA-miss notifications to the alerting hook (see
[observing-data-pipelines](../observing-data-pipelines/SKILL.md)), dry-run the DAG,
then enable. Log per [handling-errors-and-logging](../../software-engineering/handling-errors-and-logging/SKILL.md).

## Principles
1. **Dependencies are data, not timing** — an edge means "needs this output", never "runs later".
2. **Every task idempotent** — re-running a partition yields the same result, no dupes.
3. **Retry the transient, fail the deterministic** — backoff for flakes; surface real bugs fast.
4. **One code path for schedule and backfill** — parameterize by date, don't fork logic.
5. **No hidden coupling** — no shared mutable state, no ordering by luck, no side effects across tasks.
6. **Small idempotent tasks** over one monolith — restartable at the point of failure.

## Decision framework
- **Task depends on external data landing?** Use a sensor/data-availability check, not a fixed offset.
- **Re-run would double-count?** Not idempotent — rewrite to overwrite-by-partition before scheduling.
- **Failure is deterministic (bad code/schema)?** Don't retry; fail loud and alert.
- **Need history loaded?** Enable catchup/backfill with bounded concurrency; else set catchup off.
- **Two tasks fight over the same table/file?** Make outputs partition-disjoint or serialize the edge.
- **DAG getting huge?** Split into per-domain DAGs linked by dataset/sensor triggers.

## Common mistakes
- **Non-idempotent tasks** — append-only writes that duplicate on every re-run.
- **No retry/backoff** (or infinite retries) — one blip fails the pipeline, or a bad task hammers a source.
- **Hidden cross-task coupling** — relying on run order, shared temp files, or global state instead of edges.
- **Fixed sleeps instead of sensors** for late data — brittle and time-zone-fragile.
- **No backfill path** — history requires hand-run scripts that diverge from prod logic.
- **catchup misconfigured** — a paused DAG resumes and floods hundreds of past runs unintentionally.
- **No timeout** — a stuck task blocks the slot forever.

## Validation checklist
- [ ] DAG has no cycles; every edge is a real data dependency, none implicit.
- [ ] Each task is idempotent — re-running a partition produces no duplicates or drift.
- [ ] Retries bounded with backoff; deterministic failures are not retried.
- [ ] Every task has a timeout and an SLA on the critical path.
- [ ] Schedule pins time zone; catchup set intentionally; late data handled by sensors.
- [ ] Backfill runs the same code path, parameterized by date, with bounded concurrency.
- [ ] Failure and SLA-miss notifications wired; runbook exists for stuck/late runs.

## Edge cases
- **Late-arriving source data:** sensor with timeout + SLA; decide skip vs. wait vs. alert.
- **Cross-DAG dependency:** trigger via dataset/data-aware scheduling, not a guessed time gap.
- **Long backfill:** cap parallelism; checkpoint progress so a mid-range failure resumes.
- **Partial failure mid-DAG:** design tasks so a retry from the failed node is safe and sufficient.
- **DST / midnight boundaries:** use UTC internally; verify the logical date maps to the right partition.

## Related skills
- [designing-data-pipelines](../designing-data-pipelines/SKILL.md), [building-batch-transformations](../building-batch-transformations/SKILL.md), [implementing-incremental-loading](../implementing-incremental-loading/SKILL.md).
- [ensuring-data-quality](../ensuring-data-quality/SKILL.md), [observing-data-pipelines](../observing-data-pipelines/SKILL.md).
- [handling-errors-and-logging](../../software-engineering/handling-errors-and-logging/SKILL.md).

## Examples
**Input:** "Our nightly sales pipeline sometimes double-counts and can't recover
after a failed step. Set it up properly in Airflow."
**Output:** Mapped four tasks (extract → stage → transform → publish) with explicit
edges; a sensor waits for the source partition instead of a 2am guess. Made
`stage`/`transform` overwrite by execution-date partition (MERGE), killing the
double-count. Added 3 retries with exponential backoff, a 30-min timeout, and an SLA
alert. Parameterized by `ds` so the same DAG backfills Q1 at concurrency 4. Re-run of
any date now replaces cleanly; a failure resumes from the failed task.

## Automation opportunities
- Lint DAGs in CI: cycle check, every task has retries/timeout/owner, no top-level side effects.
- Template a standard task (idempotent write + retry/backoff + SLA) so new tasks inherit the defaults.
- Auto-alert on SLA miss and on retry exhaustion; page only on critical-path failure.
- Generate a backfill command from the DAG's date parameter so history reruns are one line.
