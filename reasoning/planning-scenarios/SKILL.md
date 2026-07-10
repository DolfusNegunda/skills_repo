---
name: planning-scenarios
description: Prepare for an uncertain future by building several plausible scenarios, running a pre-mortem, defining leading indicators, and setting contingency triggers — so a change in the world meets a ready response, not a scramble. Use when the user asks to "plan for different scenarios", "what if X happens", "stress-test the plan", "best/worst case", or faces a decision whose outcome hinges on unknowns outside their control. Produces scenarios with signposts and pre-committed contingencies, not a single forecast.
---

# Planning Scenarios

## Scope
Preparing for multiple plausible futures around a decision or plan: scenario
construction, a pre-mortem, leading indicators, and contingency triggers. For
readiness across branches — not committing to one path, which is
[planning-projects](../../business/planning-projects/SKILL.md).

## Purpose
Replace a single fragile forecast with a set of prepared responses — so when the
future resolves one way or another, the reaction is already thought through and the
signals that it's happening are already being watched.

## When to use this skill
- "Plan for different scenarios / what if X happens / best and worst case."
- "Stress-test / pressure-test this plan against how it could go wrong."
- A decision whose payoff hinges on unknowns outside your control.

## When NOT to use this skill
- Executing one agreed path → [planning-projects](../../business/planning-projects/SKILL.md).
- Cataloguing and rating discrete risks → [maintaining-risk-registers](../../business/maintaining-risk-registers/SKILL.md).
- Making the go/no-go call itself → [deciding-under-uncertainty](../deciding-under-uncertainty/SKILL.md).

## Inputs
- The decision or plan and its time horizon.
- The critical uncertainties — the unknowns that would most change the outcome.
- The organisation's tolerance for risk and its ability to react.

## Outputs
- A small set of named, plausible scenarios; a pre-mortem of the base plan; leading
  indicators per scenario; and pre-committed contingency triggers with owners.

## Workflow
```
Progress:
- [ ] 1. Frame the decision, horizon, and what "being wrong" would cost
- [ ] 2. Identify the two or three critical uncertainties that drive the outcome
- [ ] 3. Build 3–4 distinct, plausible scenarios across those axes
- [ ] 4. Run a pre-mortem: assume the plan failed — why?
- [ ] 5. Define leading indicators and contingency triggers per scenario
- [ ] 6. Assign owners and review cadence; keep the watch live
```

**Step 1 — Frame.** State the decision and horizon, and what a wrong bet costs — this
sets how much scenario work is warranted. **Step 2 — Critical uncertainties.** Find
the few unknowns that are both high-impact and genuinely uncertain; ignore what's
certain or trivial. **Step 3 — Build scenarios.** Cross two key axes to get 3–4
distinct worlds (not just good/bad/medium on one axis); each must be plausible and
force different actions. **Step 4 — Pre-mortem.** Imagine it's a year out and the plan
failed; list the causes — this surfaces blind spots optimism hides. **Step 5 —
Indicators + triggers.** For each scenario name the *leading* signals it's arriving
and pre-decide the action + threshold ("if churn > 5% two months running, cut scope").
**Step 6 — Own it.** Assign an owner to each indicator and a review cadence; a plan
nobody watches is a document, not preparedness.

## Principles
1. **Plan for several futures,** not the one you expect.
2. **Scenarios must diverge** — three flavours of the same forecast teach nothing.
3. **Each scenario must be plausible and actionable** — no strawmen, no fantasies.
4. **Pre-mortem beats optimism** — assume failure to find what you'd otherwise miss.
5. **Leading indicators, not lagging** — watch signals early enough to still act.
6. **Pre-commit the trigger** — decide the response now, when calm, not mid-crisis.
7. **Preparedness is maintained,** not authored once and shelved.

## Decision framework
- **One dominant uncertainty?** Build scenarios along that single axis (e.g. demand high/low).
- **Two independent drivers?** Cross them into a 2×2 of four worlds.
- **Which scenarios to resource?** The plausible-and-costly ones; note but don't over-invest in tail cases.
- **Trigger threshold unclear?** Set it where acting is still cheap and reversible — earlier than feels necessary.
- **Too many scenarios?** Collapse to 3–4; more dilutes attention and none get watched.
- **Discrete risks emerging?** Log them → [maintaining-risk-registers](../../business/maintaining-risk-registers/SKILL.md).

## Common mistakes
- **Planning for only one future** — a single forecast dressed as a plan.
- **Skipping the pre-mortem** — no structured search for how it fails.
- **Non-divergent scenarios** — best/base/worst on one variable, all needing the same response.
- **Implausible scenarios** that get dismissed, discrediting the exercise.
- **Lagging indicators** — noticing the shift only after it's too late to react.
- **No pre-committed trigger** — spotting the signal but debating the response from scratch.
- **Author once, never revisit** — the world moves, the scenarios don't.

## Validation checklist
- [ ] Decision, horizon, and cost-of-being-wrong stated.
- [ ] Critical uncertainties (high-impact, genuinely uncertain) identified.
- [ ] 3–4 distinct, plausible scenarios that demand different responses.
- [ ] Pre-mortem run; failure causes captured and addressed.
- [ ] Leading indicators defined per scenario — early enough to act on.
- [ ] Contingency triggers pre-committed with thresholds and owners.
- [ ] Review cadence set so the watch stays live.

## Edge cases
- **Very short horizon:** compress to two scenarios and a single trigger; don't over-produce.
- **Deep, irreducible uncertainty:** favour robust/no-regret moves that work across all scenarios.
- **Black-swan tails:** you can't enumerate them — build general resilience and reserves instead.
- **Fast-moving domain:** shorten the review cadence so indicators stay current.
- **Scenario paralysis:** cap at four and force each into a concrete action, or nothing gets done.

## Related skills
- [planning-projects](../../business/planning-projects/SKILL.md) — executing the chosen path.
- [maintaining-risk-registers](../../business/maintaining-risk-registers/SKILL.md) — tracking discrete risks.
- [deciding-under-uncertainty](../deciding-under-uncertainty/SKILL.md), [estimating-under-uncertainty](../estimating-under-uncertainty/SKILL.md), [thinking-in-systems](../thinking-in-systems/SKILL.md), [identifying-constraints](../identifying-constraints/SKILL.md).

## Examples
**Input:** "We're betting the year on one big product launch — what if it goes wrong?"
**Output:** Framed (12-month horizon, cost of miss = runway). Critical uncertainties:
adoption speed and competitor response. Crossed into four scenarios (fast/slow ×
quiet/aggressive competitor). Pre-mortem surfaced a support-capacity failure mode.
Leading indicators set (week-4 activation rate, competitor pricing moves); triggers
pre-committed ("activation < 20% by week 6 → pivot messaging and delay paid spend").
Owners and a fortnightly review assigned so signals are actually watched.

## Automation opportunities
- Dashboard the leading indicators so threshold breaches alert automatically.
- Wire trigger thresholds to notifications routed to the named owner.
- Re-run the scenario set on a cadence as new data shifts the probabilities.
