---
name: building-decision-matrices
description: Build a weighted decision matrix to choose among options objectively — defining criteria, weighting them, scoring each option, and computing a transparent ranked result. Use when the user asks to "compare these options", "make a decision matrix", "help me choose between", "weighted scoring", or evaluate alternatives against multiple criteria. Reduces bias and makes trade-offs explicit. Produces a defensible ranked recommendation with sensitivity, not a gut pick.
---

# Building Decision Matrices

## Scope
Structured multi-criteria decision-making: defining and weighting criteria, scoring
options, and computing a transparent ranking. For choosing among defined
alternatives. Financial-only comparison is
[analyzing-cost-benefit](../analyzing-cost-benefit/SKILL.md).

## Purpose
Replace a biased gut pick with a transparent, defensible comparison — making the
criteria, weights, and trade-offs explicit so the decision (and the reasoning) can
be scrutinized and trusted.

## When to use this skill
- "Compare these options / help me choose between / make a decision matrix."
- "Weighted scoring / evaluate alternatives against criteria."
- Vendor/tool/approach selection with multiple factors.

## When NOT to use this skill
- Purely financial choice → [analyzing-cost-benefit](../analyzing-cost-benefit/SKILL.md).
- Strategic positioning → [running-swot-analysis](../running-swot-analysis/SKILL.md).
- Only one real option / trivial choice → just decide.

## Inputs
- The options (2+) and the decision to make.
- The criteria that matter and their relative importance; who owns the decision.

## Outputs
- A weighted decision matrix: criteria × options with weights, scores, weighted
  totals, a ranked result, and a sensitivity check on the weights.

## Workflow
```
Progress:
- [ ] 1. Define the decision and list the real options (incl. do-nothing)
- [ ] 2. Choose criteria that discriminate between options
- [ ] 3. Weight criteria by importance (sum to 100%)
- [ ] 4. Score each option per criterion on a consistent scale
- [ ] 5. Compute weighted totals and rank
- [ ] 6. Sensitivity-check weights; sanity-check the winner
```

**Step 2 — criteria that discriminate.** Drop criteria all options score the same on
— they add noise, not signal. Include must-haves as gates (fail = eliminated) before
scoring. **Step 3 — weight before scoring** (and ideally before seeing scores) to
avoid rigging weights toward a favored option. **Step 4 — consistent scale** (e.g.
1–5) with defined anchors so scoring is repeatable. **Step 6 — sensitivity:** nudge
the weights; if the winner flips easily, the decision is close — say so rather than
implying false confidence.

## Principles
1. **Explicit criteria and weights** — the point is transparency.
2. **Weight before scoring** to avoid motivated reasoning.
3. **Criteria must discriminate;** gate must-haves separately.
4. **Consistent, anchored scoring scale.**
5. **Sensitivity-check** — know if the result is robust or a coin-flip.
6. **The matrix informs judgment;** it doesn't replace it — sanity-check the winner.

## Decision framework
- **Hard must-haves?** Gate them first (pass/fail), then score the survivors.
- **Cost is one of many factors?** Include it as a weighted criterion (or run CBA separately and feed it in).
- **Close result?** Report it as close + the deciding criteria; don't manufacture certainty.
- **Group decision?** Have members score independently, then reconcile divergence.

## Common mistakes
- **Choosing weights after seeing scores** to justify a preference.
- **Non-discriminating criteria** padding the matrix.
- **Inconsistent scoring** with no anchors.
- **Ignoring must-haves** — a high total on an option that fails a hard requirement.
- **No sensitivity** — presenting a near-tie as a clear winner.
- **Treating the number as the decision** rather than informing judgment.

## Validation checklist
- [ ] Options (incl. do-nothing) and the decision defined.
- [ ] Criteria discriminate; must-haves gated separately.
- [ ] Weights set before scoring and sum to 100%.
- [ ] Consistent, anchored scoring scale applied.
- [ ] Weighted totals computed and ranked.
- [ ] Sensitivity checked; winner sanity-checked against intuition.

## Edge cases
- **Highly subjective criteria:** define anchors; use multiple scorers to reduce bias.
- **Interacting criteria:** watch for double-counting the same underlying factor.
- **Near-tie:** surface it; the "soft" factors or a pilot may decide.
- **Manipulation risk:** lock weights with the decision-owner before scoring.

## Related skills
- [analyzing-cost-benefit](../analyzing-cost-benefit/SKILL.md), [running-swot-analysis](../running-swot-analysis/SKILL.md), [writing-business-cases](../writing-business-cases/SKILL.md).
- [evaluating-technology](../../research/evaluating-technology/SKILL.md) — tech selection input.

## Examples
**Input:** "Help us choose between three CRM vendors."
**Output:** Must-have gate (SOC 2, API) eliminates one; remaining two scored on
weighted criteria (functionality 30%, TCO 25%, support 20%, integration 15%, UX 10%)
on a 1–5 scale; weighted totals rank Vendor B ahead of A (3.9 vs 3.6); sensitivity
shows B stays ahead unless TCO weight rises above 40% — a robust result, recommended
with the deciding criteria noted.

## Templates
- [templates/decision-matrix.md](templates/decision-matrix.md) — weighted matrix with must-have gate and sensitivity.

## Automation opportunities
- Compute weighted totals and re-rank automatically as scores/weights change.
- Run weight sensitivity as a small what-if table.
