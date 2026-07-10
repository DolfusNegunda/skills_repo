---
name: analyzing-tradeoffs
description: Weigh competing options against criteria that matter, make the opportunity cost of each choice explicit, and recommend one with the reasoning shown. Use when a decision has two or more viable paths that pull against each other — speed vs quality, build vs buy, cost vs flexibility — and someone asks "which should we pick and why" or "what are the tradeoffs here".
---

# Analyzing Tradeoffs

## Scope
Comparing a small set of viable options against the criteria that actually
matter, surfacing what each choice gives up (opportunity cost), and landing on a
defensible recommendation with the reasoning laid bare. Covers informal-to-
structured judgment; stops short of a formal weighted scoring artifact.

## Purpose
Turn "it depends" into a clear, honest choice — one that names what is sacrificed,
not just what is gained, so the decision survives scrutiny and later hindsight.

## When to use this skill
- Two or more viable options genuinely pull against each other.
- Someone asks "which should we pick and why" or "what are the tradeoffs".
- A choice between speed/quality, build/buy, cost/flexibility, now/later.

## When NOT to use this skill
- A formal weighted scoring matrix is the deliverable → [building-decision-matrices](../../business/building-decision-matrices/SKILL.md).
- The decision hinges on financial ROI/NPV → [analyzing-cost-benefit](../../business/analyzing-cost-benefit/SKILL.md).
- The task is finding the single limiting factor → [identifying-constraints](../identifying-constraints/SKILL.md).
- Choosing under incomplete/probabilistic info → [deciding-under-uncertainty](../deciding-under-uncertainty/SKILL.md).
- Ordering a backlog by value → [prioritizing-options](../prioritizing-options/SKILL.md).

## Inputs
- The decision to be made and who owns it; the deadline and reversibility.
- The candidate options (2–5 real ones, not straw men).
- The criteria that matter and their relative weight; known constraints.

## Outputs
- A compact comparison of options against criteria.
- The opportunity cost of the recommended path stated explicitly.
- A recommendation with the reasoning and the discarded alternatives shown.

## Workflow
```
Progress:
- [ ] 1. Frame the decision, owner, deadline, and reversibility
- [ ] 2. List the real options (2–5); drop straw men
- [ ] 3. Name the criteria that matter and weight them
- [ ] 4. Score each option against criteria; note evidence, not vibes
- [ ] 5. Make opportunity cost explicit for the front-runners
- [ ] 6. Recommend one; show the reasoning and what it gives up
```

**Step 1 — Frame.** State the decision in one sentence, name its owner, its
deadline, and whether it is reversible. Reversibility changes how much rigor is
worth spending — see [deciding-under-uncertainty](../deciding-under-uncertainty/SKILL.md).

**Step 2 — Options.** List 2–5 genuinely viable options. Include "do nothing" when
it is real. Cut straw men — a rigged comparison fools only its author.

**Step 3 — Criteria.** Name the few criteria that decide this (not every
attribute). Weight them; an unweighted list hides which criteria actually govern.

**Step 4 — Assess.** Rate each option per criterion against evidence, not
preference. Flag where data is thin so the confidence is visible.

**Step 5 — Opportunity cost.** For the leading options, state what choosing it
sacrifices — the best foregone alternative, not just the sticker price. This is the
step most analyses skip and the one that makes the tradeoff honest.

**Step 6 — Recommend.** Pick one, justify it against the weighted criteria, and
show the runners-up and why they lost. A recommendation without the discarded
options is an assertion, not analysis.

## Principles
1. **Every choice has an opportunity cost** — name the best thing given up.
2. **Compare on the criteria that matter,** weighted, not on every attribute.
3. **Real options only** — no straw men to make the favorite look good.
4. **Match rigor to reversibility** — a two-way door deserves less analysis.
5. **Show the reasoning,** including the alternatives you rejected.
6. **Evidence over preference** — say where the data is thin.

## Decision framework
- **Options collapse to one dominant choice?** Say so and stop — no false balance.
- **Criteria conflict irreconcilably?** Surface the value judgment to the owner.
- **A criterion is actually a hard limit?** Treat it as a filter first → [identifying-constraints](../identifying-constraints/SKILL.md).
- **Money is the deciding axis?** Hand off to [analyzing-cost-benefit](../../business/analyzing-cost-benefit/SKILL.md).
- **Need an auditable weighted score?** Escalate to [building-decision-matrices](../../business/building-decision-matrices/SKILL.md).

## Common mistakes
- **Ignoring opportunity cost** — pricing what a choice costs, not what it forecloses.
- **Straw-man options** rigged so the preferred one wins.
- **Unweighted criteria** that let a minor factor swing the call.
- **Analysis paralysis** on a cheaply reversible decision.
- **Sunk-cost anchoring** — favoring an option because of past investment.
- **Hiding the reasoning** — a verdict with no visible trade.

## Validation checklist
- [ ] Decision, owner, deadline, and reversibility are stated.
- [ ] Options are real and viable; "do nothing" considered where relevant.
- [ ] Criteria are named, weighted, and tied to what matters.
- [ ] Each option is assessed against evidence, with thin spots flagged.
- [ ] Opportunity cost of the recommendation is explicit.
- [ ] Recommendation shows reasoning and the rejected alternatives.

## Edge cases
- **One option dominates:** state it plainly; do not manufacture balance.
- **Irreducible value conflict:** present the tradeoff and let the owner decide.
- **Too many options:** shortlist first with a coarse filter, then analyze deeply.
- **High stakes, thin data:** switch to [deciding-under-uncertainty](../deciding-under-uncertainty/SKILL.md).

## Related skills
- [identifying-constraints](../identifying-constraints/SKILL.md), [deciding-under-uncertainty](../deciding-under-uncertainty/SKILL.md), [prioritizing-options](../prioritizing-options/SKILL.md).
- [building-decision-matrices](../../business/building-decision-matrices/SKILL.md), [analyzing-cost-benefit](../../business/analyzing-cost-benefit/SKILL.md), [running-swot-analysis](../../business/running-swot-analysis/SKILL.md).

## Examples
**Input:** "Should we build our own auth or use a vendor?"
**Output:** Options: build, vendor, hybrid. Criteria (weighted): time-to-market
40%, control 25%, cost-at-scale 20%, compliance 15%. Vendor wins time and
compliance; build wins control and long-run cost. Opportunity cost of vendor:
forgoing deep customization and locking to their roadmap. Recommendation: vendor
now — reversible in ~1 quarter, and time-to-market dominates this year; revisit at
scale. Build rejected: control gains do not justify the delay today.

## Automation opportunities
- Template the option × weighted-criteria table for reuse across decisions.
- Standardize an opportunity-cost prompt so the sacrifice is never omitted.
- Log decisions and revisit them; compare outcomes to the reasoning shown.
