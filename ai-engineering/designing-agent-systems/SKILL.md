---
name: designing-agent-systems
description: Design LLM agent systems — choose a control loop (ReAct vs plan-execute), decide single vs multi-agent, set stopping conditions and step budgets, handle failures and loops, and keep the run observable. Use when the user asks to "design an agent", "build an agentic loop", pick ReAct vs plan-and-execute, decide whether to add more agents, or stop an agent that loops or runs forever.
---

# Designing Agent Systems

## Scope
The control architecture of an LLM agent: the loop that interleaves reasoning, tool
calls, and observations; single- vs multi-agent structure; termination and budgets;
failure and loop handling; and observability. Not the tool interface itself, not memory
design, not the prompts.

## Purpose
Produce an agent that makes progress toward a goal, stops deliberately, degrades safely
when tools or the model fail, and can be inspected after the fact — instead of a loop
that burns tokens, spins, or fails silently.

## When to use this skill
- "Design an agent / agentic loop / autonomous workflow."
- Choosing a control loop (ReAct, plan-execute, reflexion) or single vs multi-agent.
- An agent loops forever, never stops, or fails opaquely and needs guardrails.

## When NOT to use this skill
- Designing tool schemas / function calling → [integrating-tool-use](../integrating-tool-use/SKILL.md).
- Agent state and long-term memory → [managing-agent-memory](../managing-agent-memory/SKILL.md).
- No autonomy needed — a single prompt or chain suffices → [engineering-prompts](../engineering-prompts/SKILL.md).
- Whole product spanning many components → [designing-ai-systems](../designing-ai-systems/SKILL.md).

## Inputs
- The goal and success criteria; who or what consumes the result.
- Available tools, their cost/latency/risk, and which actions are irreversible.
- Budget limits (tokens, wall-clock, dollars, max steps) and autonomy tolerance.

## Outputs
- A chosen control loop with a written termination policy and step/token budget.
- Single- or multi-agent topology with responsibilities and handoffs named.
- Failure/loop handling rules and a trace/logging plan.

## Workflow
```
Progress:
- [ ] 1. State the goal, success test, and hard budget (steps/tokens/time)
- [ ] 2. Choose the control loop for the task shape
- [ ] 3. Decide single vs multi-agent; justify any extra agent
- [ ] 4. Define stopping conditions and the step budget
- [ ] 5. Add failure, retry, and loop-detection handling
- [ ] 6. Instrument the run; dry-run the happy path and two failure paths
```

**Step 1 — Frame the goal.** Write a machine-checkable success condition and a hard
ceiling on steps, tokens, and time before any loop design. An agent without a stop test
is a bug. Decide the autonomy level: propose-only, act-with-confirmation, or fully
autonomous.

**Step 2 — Choose the loop.** ReAct (reason→act→observe, repeat) for open-ended tasks
where each step depends on the last observation. Plan-execute (plan up front, then run
steps) for tasks with knowable structure — cheaper, more predictable, easier to audit.
Add a reflect/critique step only when quality gains beat the extra calls. Default to the
simplest loop that fits.

**Step 3 — Single vs multi-agent.** Default to one agent with a good tool set.
Split into multiple agents only for genuinely separable concerns (distinct tool sets,
context that would collide, independent parallelism) — each agent adds handoff cost,
error surface, and latency. Prefer a supervisor/worker shape over a free-for-all;
give each agent one clear responsibility and a defined handoff contract.

**Step 4 — Stopping conditions.** Terminate on ANY of: success test met, step/token/time
budget exhausted, repeated identical action/observation, or explicit give-up. Always cap
iterations with a hard `max_steps`; never rely on the model to decide it's done. Define
what happens at the ceiling — return best-effort partial with a reason, not silence.

**Step 5 — Failure and loops.** Tool errors return to the model as structured
observations, not exceptions that kill the run; bound retries per tool. Detect loops by
hashing recent (action, args, observation) tuples — if repeating, break, escalate, or
change strategy. Guard irreversible actions behind confirmation or a dry-run.

**Step 6 — Observability.** Log every step: thought, tool + args, observation, tokens,
latency. Emit a replayable trace and a run summary (steps, stop reason, cost). You cannot
debug an agent you cannot replay. Dry-run the happy path plus a tool-failure and a
loop scenario before shipping.

## Principles
- **A stop condition is mandatory, not optional.** Every loop has a hard step budget.
- **Simplest loop that works.** ReAct or plan-execute before anything reflexive or multi-agent.
- **One agent until proven otherwise.** Add agents for separable concerns, not for tidiness.
- **Errors are observations.** Feed failures back into the loop; don't crash or swallow them.
- **Irreversible actions need a gate.** Confirm, dry-run, or sandbox before destructive calls.
- **If you can't replay it, you can't trust it.** Trace every step end to end.

## Decision framework
- **ReAct vs plan-execute?** Steps depend on prior observations → ReAct; structure known up front → plan-execute (cheaper, auditable).
- **Add a second agent?** Only if it owns a distinct tool set or context that would otherwise collide — else keep one.
- **Supervisor vs peer agents?** Almost always supervisor/worker; peer-to-peer only for truly independent parallel subtasks.
- **Retry vs escalate a failing tool?** Transient error → bounded retry with backoff; systematic error → escalate/stop.
- **Autonomous vs confirm?** Reversible + low cost → autonomous; irreversible or costly → require confirmation.

## Common mistakes
- **No step budget** — the loop runs until it hits a rate limit or the bill.
- **Letting the model self-declare done** with no external success test.
- **Multi-agent theater** — many agents where one with the right tools would do, multiplying latency and failure modes.
- **Swallowing tool errors** — exceptions kill the run or vanish instead of returning as observations.
- **No loop detection** — the agent repeats the same failing action indefinitely.
- **Unobservable runs** — no per-step trace, so failures can't be diagnosed or replayed.
- **Over-broad autonomy** — irreversible actions fire with no gate.

## Validation checklist
- [ ] A machine-checkable success condition is defined.
- [ ] Hard budgets on steps, tokens, and time; behavior at the ceiling is specified.
- [ ] Control loop chosen and justified for the task shape.
- [ ] Single vs multi-agent decision recorded; each agent has one responsibility.
- [ ] Tool errors return as observations with bounded retries; loop detection present.
- [ ] Irreversible actions are gated.
- [ ] Every step is traced; a run summary reports stop reason and cost.

## Edge cases
- **Parallel tool calls:** decide ordering and how partial failures merge before fanning out.
- **Human-in-the-loop:** define the pause/resume contract and how state survives the wait.
- **Long-running tasks:** checkpoint state so a crash resumes instead of restarting.
- **Nested agents:** propagate the parent's remaining budget down; don't let a child ignore the global ceiling.
- **Non-deterministic tools:** cache or pin results where replay requires it.

## Related skills
- [integrating-tool-use](../integrating-tool-use/SKILL.md) — the tool interface the loop calls.
- [managing-agent-memory](../managing-agent-memory/SKILL.md), [managing-context-windows](../managing-context-windows/SKILL.md).
- [applying-guardrails](../applying-guardrails/SKILL.md), [building-llm-evaluations](../building-llm-evaluations/SKILL.md), [designing-ai-systems](../designing-ai-systems/SKILL.md).
- [reviewing-architecture](../../review/reviewing-architecture/SKILL.md), [handling-errors-and-logging](../../software-engineering/handling-errors-and-logging/SKILL.md).

## Examples
**Input:** "Build an agent that triages incoming bug reports and files tickets."
**Output:** Single agent, ReAct loop (each step depends on what it reads). Tools:
`search_issues`, `read_report`, `create_ticket` (irreversible → confirm-before-create).
Success test: a ticket exists or the report is marked duplicate. `max_steps=12`, token
and time ceilings; stop on success, budget, or a repeated (search, same-query) loop.
Tool errors return as observations with two retries each. Per-step trace logged with a
run summary (steps, stop reason, tokens). Multi-agent rejected — one tool set, no
context collision.

## Automation opportunities
- Wrap the loop in a harness that enforces budgets and loop detection centrally, not per-agent.
- Emit traces to an eval/observability store; replay failed runs as regression cases.
- Auto-generate a run summary (cost, steps, stop reason) for every execution.
