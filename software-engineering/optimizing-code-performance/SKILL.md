---
name: optimizing-code-performance
description: Make code faster and leaner the disciplined way — measure and profile first, find the real hotspot, fix algorithmic complexity before micro-optimizing, then verify the win with a benchmark. Use when the user says "this is slow", "optimize this", "reduce latency/memory", "why is it taking so long", or asks to speed up a function, endpoint, or job. Produces a profiled, benchmarked improvement, not guesswork.
---

# Optimizing Code Performance

## Scope
Improving the runtime, throughput, or memory of working code through measurement,
targeted change, and verification. Covers profiling, complexity, caching, batching,
and IO — not correctness bugs and not SQL query tuning.

## Purpose
Deliver a real, proven speedup where it matters: locate the actual hotspot with
data, fix the largest cost first (usually algorithmic), and prove the gain with a
before/after benchmark — instead of scattering micro-optimizations on cold code.

## When to use this skill
- "This is slow / optimize this / reduce latency or memory / why so slow?"
- A profiler, timeout, or load test flags a hotspot.
- Speeding up a function, endpoint, batch job, or startup path.

## When NOT to use this skill
- Wrong output, not slow output → [debugging-systematically](../debugging-systematically/SKILL.md).
- Query/index tuning → [authoring-sql-queries](../authoring-sql-queries/SKILL.md).
- Untangling structure with no perf goal → [refactoring-code](../refactoring-code/SKILL.md).

## Inputs
- The slow code path and a reproducible way to exercise it with realistic data.
- The target/budget (latency, throughput, memory) and current baseline.
- Constraints: platform, data size, acceptable trade-offs (memory for speed, etc.).

## Outputs
- A profiled diagnosis (where time/memory actually goes), the applied change, and a
  before/after benchmark on representative input, with correctness unchanged.

## Workflow
```
Progress:
- [ ] 1. Define the goal, budget, and a repeatable benchmark on realistic data
- [ ] 2. Measure the baseline; profile to find the true hotspot
- [ ] 3. Diagnose the cost — complexity, IO, allocation, or contention
- [ ] 4. Fix the biggest cost first (algorithm/data structure before micro-tuning)
- [ ] 5. Re-benchmark; confirm the win and that behavior is unchanged
- [ ] 6. Stop at "good enough"; document the trade-off
```

**Step 1 — benchmark before touching code.** Without a repeatable measurement on
representative data, you cannot prove a win. Tiny/uniform inputs mislead. **Step 2 —
profile, don't guess.** Intuition about hotspots is usually wrong; let the profiler
name the function. **Step 4 — complexity first:** an O(n²) loop or an N+1 call
dominates any constant-factor tweak. Cache repeated work, batch chattly IO, hoist
work out of loops, pick the right data structure (set/dict lookup vs. linear scan).
**Step 5 — verify:** re-run the same benchmark; a change without a measured
improvement is not an optimization.

## Principles
1. **Measure first, optimize second** — profile the real path, never the guess.
2. **Fix the dominant cost** — algorithmic complexity before micro-optimization.
3. **Chase the hotspot** — the slow 5% of code, not the whole file.
4. **Preserve correctness** — same outputs; optimization is not a rewrite license.
5. **Stop at good enough** — meet the budget; avoid premature optimization.

## Decision framework
- **Don't know where time goes?** Profile before changing anything.
- **Hot loop / large N?** Attack complexity and data structures first.
- **Repeated identical work?** Cache/memoize (mind invalidation and staleness).
- **Many small IO/DB/API calls?** Batch, paginate, or parallelize.
- **Memory-bound?** Stream/generate instead of materializing; cut copies.
- **Already meets budget?** Stop — further tuning adds risk, not value.

## Common mistakes
- **Optimizing before profiling** — speeding up code that was never the bottleneck.
- **Micro-tuning over an O(n²)** — polishing constants while the algorithm dominates.
- **No baseline/benchmark** — "feels faster" with no number.
- **Benchmarking toy data** — wins that vanish at production scale.
- **Trading readability for illusory gains** on cold paths.
- **Caching without invalidation** — fast but wrong.

## Validation checklist
- [ ] Goal/budget stated and a repeatable benchmark exists on realistic data.
- [ ] Baseline measured; hotspot identified by profiling, not guessing.
- [ ] Dominant cost (complexity/IO/allocation) addressed first.
- [ ] Before/after numbers show a real, meaningful improvement.
- [ ] Outputs unchanged; tests still pass.
- [ ] Trade-offs (memory, complexity, staleness) noted; stopped at good enough.

## Edge cases
- **Micro-benchmarks lie:** warm up, run many iterations, beware dead-code elimination.
- **Tail latency:** optimize p95/p99, not just the mean.
- **Concurrency:** contention/lock waits won't show in single-thread profiles.
- **Startup vs. steady state:** JIT/cache warmup skews early samples.

## Related skills
- [debugging-systematically](../debugging-systematically/SKILL.md), [refactoring-code](../refactoring-code/SKILL.md), [authoring-sql-queries](../authoring-sql-queries/SKILL.md).
- [writing-automated-tests](../writing-automated-tests/SKILL.md), [reviewing-code](../../review/reviewing-code/SKILL.md).

## Examples
**Input:** "This report endpoint takes 8s — make it faster."
**Output:** Profiled: 90% of time in a loop issuing one DB call per row (N+1).
Baseline 8.1s on 2k rows. Fix: batch into a single query + dict lookup — one query
instead of N round-trips (O(1) queries, O(n) in-memory lookup). Re-benchmark: 0.4s, same output, tests green. Left a note that
the response is now memoized for 60s; documented the staleness window. Stopped —
under the 1s budget.

## Automation opportunities
- Add a profiling harness and commit representative benchmark inputs.
- Track a perf budget in CI; fail the build on regressions past a threshold.
- Capture flame graphs on the hot path so future work targets data, not hunches.
