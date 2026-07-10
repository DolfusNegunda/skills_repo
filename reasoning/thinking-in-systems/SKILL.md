---
name: thinking-in-systems
description: Reason about a system's structure — its stocks, flows, feedback loops, delays, and the second-order effects and unintended consequences those produce — instead of treating a problem as one isolated cause. Use when someone says "why does this keep coming back", "what are the ripple effects", "map the feedback loops", "what happens downstream if we change X", or a fix in one place keeps breaking another. Produces a structural map and the leverage points and side effects it reveals.
---

# Thinking in Systems

## Scope
Reasoning about how a system's *structure* drives its behavior: the stocks that
accumulate, the flows that change them, the feedback loops that amplify or dampen,
the delays that hide cause from effect, and the second-order effects a change sets
off elsewhere. Used when behavior recurs, resists fixes, or produces surprises a
one-cause analysis can't explain.

## Purpose
See why a system behaves as it does — and where a change will actually help versus
where it will be absorbed, delayed, or backfire — before intervening.

## When to use this skill
- "Why does this problem keep coming back after we fix it?"
- "What are the ripple effects / downstream consequences of changing X?"
- Fixing one area keeps breaking another (policy resistance).
- Interventions produce the opposite of the intended effect over time.
- Mapping incentives, capacity, or a process where parts interact.

## When NOT to use this skill
- A single, linear, one-cause problem → [analyzing-root-causes](../analyzing-root-causes/SKILL.md).
- Choosing between defined options → [analyzing-tradeoffs](../analyzing-tradeoffs/SKILL.md) or [prioritizing-options](../prioritizing-options/SKILL.md).
- Breaking a task into parts to execute → [decomposing-problems](../decomposing-problems/SKILL.md).
- Forecasting one quantity → [estimating-under-uncertainty](../estimating-under-uncertainty/SKILL.md).

## Inputs
- The behavior of concern over time (not a single snapshot) and its history.
- The elements involved: actors, resources, metrics, and how they connect.
- The proposed change or decision whose effects need tracing.

## Outputs
- A structural map: key stocks, flows, feedback loops (reinforcing/balancing), and delays.
- Identified leverage points — where a small change moves the system most.
- Predicted second-order effects and plausible unintended consequences.

## Workflow
```
Progress:
- [ ] 1. Describe the behavior over time, not as a snapshot
- [ ] 2. Identify stocks and the flows that fill and drain them
- [ ] 3. Trace the feedback loops: reinforcing and balancing
- [ ] 4. Locate the delays between cause and effect
- [ ] 5. Find leverage points and simulate second-order effects
- [ ] 6. Name likely unintended consequences; recommend where to intervene
```

**Step 1 — Behavior over time.** Sketch how the metric has moved (growing, oscillating,
plateauing, collapsing). The *shape* points to the structure: oscillation implies a
delayed balancing loop; explosive growth implies a reinforcing one.

**Step 2 — Stocks and flows.** Name what accumulates (the stock: headcount, backlog,
trust, cash) and the flows that raise and lower it. Stocks create inertia and delay;
they can't change instantly, only through their flows.

**Step 3 — Feedback loops.** Trace loops back to their start. **Reinforcing** loops
amplify (growth, collapse, vicious/virtuous cycles); **balancing** loops seek a goal
and resist change. Most surprising behavior is a loop no one drew.

**Step 4 — Delays.** Mark the lag between an action and its visible effect. Delays
cause overshoot, oscillation, and over-correction — people push harder because the
first push hasn't landed yet.

**Step 5 — Leverage and second-order effects.** For the proposed change, follow the
chain past the first effect: X changes Y, which changes Z, which loops back to X.
Leverage is rarely at the obvious symptom — often it's a loop's goal, a delay, or an
information flow, not the parameter everyone wants to tune.

**Step 6 — Consequences and recommendation.** List what could backfire (policy
resistance, shifting the burden, eroding goals) and where to intervene for durable
effect.

## Principles
1. **Structure drives behavior** — blame the loops, not the people in them.
2. **Stocks change slowly** — expect inertia and plan for the delay.
3. **Delays cause overshoot** — the effect not yet visible is still on its way.
4. **The obvious fix is often the symptom** — leverage sits upstream in a loop.
5. **Every intervention has a second-order effect** — trace at least one hop further.
6. **The system pushes back** — durable change alters a loop, not just a number.

## Decision framework
- **Behavior oscillates?** Suspect a balancing loop with a delay; slow the response, don't amplify it.
- **Problem recurs after every fix?** You're treating a symptom; find the loop regenerating it.
- **Fix here breaks there?** Shifting-the-burden or a shared stock — map the coupling.
- **Growth looks unstoppable?** A reinforcing loop; find the balancing loop that will eventually bind (a limit).
- **Change had no effect?** A balancing loop absorbed it; find and address the loop's goal.
- **Effect went the wrong way?** Trace the second-order loop that reversed it.

## Common mistakes
- **Ignoring feedback delays** — judging an intervention before its effect arrives, then over-correcting.
- **Missing second-order effects** — stopping at the first, intended consequence.
- **Treating symptoms** — tuning the visible number instead of the loop that sets it.
- **Linear thinking** — assuming one cause, one effect, no loop-back.
- **Drawing only the loops that confirm the plan;** omitting the balancing loop that will resist it.
- **Optimizing one stock** at the expense of the whole system.

## Validation checklist
- [ ] Behavior is described over time, not as a single snapshot.
- [ ] Key stocks and their in/out flows are named.
- [ ] Reinforcing and balancing loops are both traced (not just the convenient ones).
- [ ] Delays between cause and effect are marked.
- [ ] Second-order effects are followed at least one hop past the intended one.
- [ ] Plausible unintended consequences and policy resistance are named.
- [ ] Leverage points are identified, not just the obvious symptom.

## Edge cases
- **Genuinely simple, linear problem:** don't over-model — use [analyzing-root-causes](../analyzing-root-causes/SKILL.md).
- **No time-series data:** reconstruct behavior qualitatively from history and interviews.
- **Human systems:** incentives are loops too — people optimize for what's measured.
- **Deep delays (years):** current stability may be borrowed; the loop hasn't closed yet.
- **Model uncertainty:** map loops as hypotheses and test them → [testing-hypotheses](../testing-hypotheses/SKILL.md).

## Related skills
- [analyzing-root-causes](../analyzing-root-causes/SKILL.md), [decomposing-problems](../decomposing-problems/SKILL.md), [analyzing-tradeoffs](../analyzing-tradeoffs/SKILL.md).
- [planning-scenarios](../planning-scenarios/SKILL.md), [deciding-under-uncertainty](../deciding-under-uncertainty/SKILL.md), [testing-hypotheses](../testing-hypotheses/SKILL.md).
- [identifying-constraints](../identifying-constraints/SKILL.md), [prioritizing-options](../prioritizing-options/SKILL.md).

## Examples
**Input:** "We added more support staff but ticket backlog is worse. Why?"
**Output:** Stock: open tickets. Flows: arrivals in, resolutions out. Structure found:
faster resolution → shorter waits → users file *more* tickets (a reinforcing loop on
demand), while new staff take weeks to ramp (a delay). Second-order effect: the visible
"fix" raised demand faster than capacity, so backlog grew. Leverage is not more staff
(the obvious symptom) but the arrival flow — deflect repeat tickets with self-service
and fix the top recurring causes. Unintended consequence to watch: cutting arrivals too
hard hides real demand signals. Recommend: address the demand loop; expect a lag before
backlog turns.

## Automation opportunities
- Chart key stocks over time so loop signatures (oscillation, exponential) are visible.
- Add a "second-order effects" section to change proposals so ripple effects are forced.
- Instrument the flows into/out of critical stocks, not just the stock level itself.
