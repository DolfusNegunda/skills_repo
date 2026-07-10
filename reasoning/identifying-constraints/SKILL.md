---
name: identifying-constraints
description: Find the one binding constraint that actually limits the outcome (Theory of Constraints), separate hard from soft and real from assumed constraints, and focus effort where it moves the result. Use when progress is capped despite effort, when a plan feels blocked, or when someone asks "what's really holding this back" or "where is the bottleneck".
---

# Identifying Constraints

## Scope
Locating the single factor that currently caps the outcome, classifying every
candidate constraint as hard/soft and real/assumed, and directing effort to the
binding one. Grounded in the Theory of Constraints: a system's throughput is set
by its bottleneck, so improving anything else is motion without progress.

## Purpose
Stop scattered effort. Find the one thing that, relaxed, moves the result — and
expose the "constraints" that are merely assumptions dressed as walls.

## When to use this skill
- Progress is capped despite adding effort or resources.
- A plan feels blocked and it is unclear by what.
- Someone asks "what's really holding this back" or "where is the bottleneck".

## When NOT to use this skill
- Enumerating what a solution must do → [gathering-requirements](../../business/gathering-requirements/SKILL.md).
- Explaining why a failure happened → [analyzing-root-causes](../analyzing-root-causes/SKILL.md).
- Weighing options against criteria → [analyzing-tradeoffs](../analyzing-tradeoffs/SKILL.md).
- Seeing feedback loops across the whole system → [thinking-in-systems](../thinking-in-systems/SKILL.md).

## Inputs
- The outcome or throughput being limited, and its target.
- The end-to-end flow or system that produces it.
- Candidate limits: resources, policies, dependencies, skills, time.

## Outputs
- The binding constraint named, with evidence that it is the limiter.
- Each candidate classified hard/soft and real/assumed.
- A focused plan to exploit or relax the binding constraint.

## Workflow
```
Progress:
- [ ] 1. Define the outcome and its target throughput
- [ ] 2. Map the end-to-end flow; find where work piles up
- [ ] 3. List candidate constraints across the flow
- [ ] 4. Classify each: hard vs soft, real vs assumed
- [ ] 5. Identify the one binding constraint with evidence
- [ ] 6. Exploit/relax it; re-check what binds next
```

**Step 1 — Define.** State the outcome and the target. Without a target, no factor
can be called limiting.

**Step 2 — Map the flow.** Trace the process end to end. The constraint usually
shows itself where work queues up, idle time appears downstream, or a resource runs
at 100%. For loop effects, use [thinking-in-systems](../thinking-in-systems/SKILL.md).

**Step 3 — List candidates.** Gather every plausible limit: capacity, policy, a
dependency, a skill gap, budget, time.

**Step 4 — Classify.** Mark each **hard** (immovable — physics, law, contract) vs
**soft** (movable with effort/money/permission), and **real** (evidenced) vs
**assumed** (believed, untested). Most "hard" constraints are soft policies no one
has challenged.

**Step 5 — Find the binding one.** Only one constraint governs throughput at a
time. Confirm it with evidence: relaxing it would raise the outcome; relaxing
others would not. That test separates the bottleneck from the noise.

**Step 6 — Act, then re-check.** Exploit the constraint (get more from it) or relax
it (add capacity, change the policy). Once it stops binding, the constraint moves —
re-run the search rather than keep optimizing the old one.

## Principles
1. **One constraint binds at a time** — find it before acting.
2. **Optimizing a non-binding constraint yields nothing** — it just builds inventory.
3. **Challenge every "hard" constraint** — most are soft policies or assumptions.
4. **Assumed until evidenced** — treat unverified limits as hypotheses to test.
5. **The constraint moves** — after relieving one, the bottleneck shifts.
6. **Exploit before you expand** — wring the current constraint dry before buying more.

## Decision framework
- **Claimed constraint has no evidence?** Mark it assumed and test it.
- **A "hard" limit is really a policy?** Reclassify as soft and negotiate it.
- **Two candidates seem to bind?** One is downstream of the other — trace which.
- **Effort aimed off the constraint?** Redirect; gains there are illusory.
- **Constraint relieved and progress still capped?** Restart at Step 2 — it moved.

## Common mistakes
- **Treating a soft constraint as hard** — accepting a movable policy as a law.
- **Optimizing a non-binding constraint** — local efficiency, zero throughput gain.
- **Assumed constraints unchallenged** — a "can't" that no one ever tested.
- **Fixing symptoms** instead of the limiter → [analyzing-root-causes](../analyzing-root-causes/SKILL.md).
- **Chasing many constraints at once** rather than the one that binds.
- **Forgetting the constraint moves** after it is relieved.

## Validation checklist
- [ ] Outcome and target throughput are defined.
- [ ] The flow is mapped end to end; pile-up point located.
- [ ] Candidates are classified hard/soft and real/assumed.
- [ ] The binding constraint is named with evidence it is the limiter.
- [ ] At least one "hard" constraint was pressure-tested for softness.
- [ ] Effort is directed at the constraint, with a re-check planned.

## Edge cases
- **Multiple plants/parallel flows:** each stream may have its own constraint.
- **Constraint is external** (a vendor, a regulator): exploit internally, negotiate outward.
- **The constraint is a policy:** the fix is a decision, not a resource.
- **No single constraint binds:** the system has slack — the real issue may be requirements, not limits ([gathering-requirements](../../business/gathering-requirements/SKILL.md)).

## Related skills
- [analyzing-tradeoffs](../analyzing-tradeoffs/SKILL.md), [thinking-in-systems](../thinking-in-systems/SKILL.md), [analyzing-root-causes](../analyzing-root-causes/SKILL.md), [decomposing-problems](../decomposing-problems/SKILL.md).
- [gathering-requirements](../../business/gathering-requirements/SKILL.md), [maintaining-risk-registers](../../business/maintaining-risk-registers/SKILL.md).

## Examples
**Input:** "We added three engineers but shipping isn't any faster."
**Output:** Flow mapped: dev → single QA reviewer → release. Work piles up at QA;
engineers idle waiting on review. Candidates: dev capacity (soft, not binding), QA
capacity (soft, binding), release policy (assumed weekly — actually soft). Binding
constraint: QA review, at 100%. Adding engineers optimized a non-binding step.
Exploit: batch reviews, add a second reviewer; relax the weekly-release assumption.
Re-check: constraint likely moves to release automation next.

## Automation opportunities
- Instrument the flow to surface queues and utilization automatically.
- Alert when any stage sustains ~100% utilization — the bottleneck signal.
- Keep a log of past constraints to spot where the bottleneck recurs.
