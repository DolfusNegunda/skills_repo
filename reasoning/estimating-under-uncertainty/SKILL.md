---
name: estimating-under-uncertainty
description: Produce a defensible estimate with limited data — decompose the unknown (Fermi), give a range with a confidence level, state assumptions explicitly, and sanity-check against independent anchors. Use when the user asks "roughly how much/many/long", "ballpark this", "we don't have exact numbers but", "order of magnitude", or needs a number to decide with before full data exists. Produces a reasoned range with assumptions and checks, not a false-precision point value.
---

# Estimating Under Uncertainty

## Scope
Reaching a good-enough number when full data is absent: decomposition, ranges with
confidence, explicit assumptions, and cross-checks. For rough sizing to decide with —
not precise costing with real figures, which is
[analyzing-cost-benefit](../../business/analyzing-cost-benefit/SKILL.md).

## Purpose
Give a decision-maker a number they can act on *and* trust the shape of — bounded,
assumption-tagged, and sanity-checked — instead of either a confident-but-wrong point
figure or a paralysed "we can't know."

## When to use this skill
- "Roughly how much / many / long? / ballpark / order of magnitude."
- A number is needed to decide before full data can be gathered.
- Sizing a market, cost, effort, or load with only partial inputs.

## When NOT to use this skill
- Precise costing with full data → [analyzing-cost-benefit](../../business/analyzing-cost-benefit/SKILL.md).
- Turning estimates into a schedule → [planning-projects](../../business/planning-projects/SKILL.md).
- Choosing among options once sized → [building-decision-matrices](../../business/building-decision-matrices/SKILL.md).

## Inputs
- The quantity to estimate and the decision it feeds (which sets the precision needed).
- Whatever anchors exist: known sub-quantities, comparables, benchmarks, prior data.
- The acceptable error band and time available to estimate.

## Outputs
- A range (low–high) with a stated confidence level, the decomposition behind it, the
  key assumptions, and at least one independent sanity check.

## Workflow
```
Progress:
- [ ] 1. Define the quantity precisely and the decision it must serve
- [ ] 2. Decompose the unknown into estimable sub-quantities (Fermi)
- [ ] 3. Estimate each piece as a range; state every assumption
- [ ] 4. Combine into a low/expected/high with a confidence level
- [ ] 5. Sanity-check against an independent anchor or comparable
- [ ] 6. Report the range, assumptions, checks, and what would tighten it
```

**Step 1 — Define.** Nail units, scope, and timeframe; "cost" and "users" are
ambiguous until pinned. The decision sets how tight the estimate must be. **Step 2 —
Decompose.** Break the unknown into factors you can each guess within ~an order of
magnitude (Fermi): quantity × rate × price, etc. Errors in independent factors partly
cancel. **Step 3 — Range each piece.** Give low/high, not a point; write the
assumption beside each so it can be challenged. **Step 4 — Combine.** Multiply/add
through; carry a range end-to-end and state confidence (e.g. "80% it's £2–5M"). **Step
5 — Sanity-check.** Reach the number a second, independent way (top-down vs bottom-up,
a comparable, a benchmark); if the two disagree by 10×, find out why before reporting.
**Step 6 — Report.** Lead with the range and confidence, list assumptions, and name
the one input that would most narrow it.

## Principles
1. **A range beats a point** — a single number hides the uncertainty that matters.
2. **Decompose the unknown** into knowable parts; guess factors, not the whole.
3. **State every assumption** — an estimate is only as defensible as its inputs.
4. **Confidence must be explicit** — "80% between X and Y", not bare numbers.
5. **Cross-check independently** — two methods agreeing is worth more than one refined.
6. **Match precision to the decision** — order-of-magnitude is often enough; don't over-work it.
7. **Beware anchoring** — the first number spoken (or a round figure) drags the rest.

## Decision framework
- **No direct data but knowable sub-parts?** Fermi decomposition.
- **A close comparable exists?** Analogy/reference-class — adjust from the base rate.
- **A trend to extend?** Extrapolate — but flag where linearity likely breaks.
- **Range feels arbitrary?** Set the 90% low and high *first*, then the middle (reduces overconfidence).
- **Two methods disagree wildly?** Don't average blindly — reconcile the gap, it reveals a bad assumption.
- **Estimate drives a big irreversible bet?** Widen the band and buy more data first.

## Common mistakes
- **False precision** — "£4,271,900" from inputs guessed to one significant figure.
- **No confidence range** — a point estimate presented as fact.
- **Anchoring** — snapping to the first or a round number and adjusting too little.
- **Overconfidence** — 90% ranges that are actually right 50% of the time; widen them.
- **Hidden assumptions** the reader can't see or challenge.
- **No sanity check** — one derivation, never cross-validated.
- **Double-counting or unit errors** in the decomposition (mixing monthly and annual).

## Validation checklist
- [ ] Quantity, units, scope, and timeframe defined; decision it serves named.
- [ ] Broken into sub-quantities each estimable within an order of magnitude.
- [ ] Every piece given as a range with its assumption written down.
- [ ] Combined into low/expected/high with an explicit confidence level.
- [ ] Cross-checked a second, independent way; large gaps reconciled.
- [ ] Precision matched to the decision; not over- or under-worked.
- [ ] The highest-leverage input to tighten next is named.

## Edge cases
- **Fat-tailed quantities (outages, viral demand):** the mean misleads; report scenarios or percentiles, not one range.
- **Deeply novel, no comparables:** widen bands hard; treat as a bet → [deciding-under-uncertainty](../deciding-under-uncertainty/SKILL.md).
- **Correlated factors:** errors compound instead of cancelling — widen the combined range.
- **Political estimates:** anchor to method, not to the number someone wants to hear.
- **Estimate will be quoted as a commitment:** label it clearly as an estimate with its confidence band.

## Related skills
- [analyzing-cost-benefit](../../business/analyzing-cost-benefit/SKILL.md) — precise costing once data exists.
- [decomposing-problems](../decomposing-problems/SKILL.md), [prioritizing-options](../prioritizing-options/SKILL.md), [testing-hypotheses](../testing-hypotheses/SKILL.md).
- [deciding-under-uncertainty](../deciding-under-uncertainty/SKILL.md), [planning-scenarios](../planning-scenarios/SKILL.md), [planning-projects](../../business/planning-projects/SKILL.md).

## Examples
**Input:** "Roughly how many support agents will we need next year?"
**Output:** Defined as concurrent agents at peak. Fermi: forecast tickets/month (range)
× minutes/ticket (range) ÷ productive minutes/agent/month, with assumptions listed
(deflection %, growth rate). Combined to "9–14 agents, ~11 expected, 80% confidence."
Cross-checked bottom-up (current 6 agents × projected volume growth) — agrees within
range. Named the biggest lever: self-serve deflection, which could halve the top end.

## Automation opportunities
- Build the Fermi model in a sheet so ranges propagate to the output automatically.
- Run a Monte Carlo over the input ranges to get an output distribution, not one band.
- Track estimate vs actual over time to calibrate future confidence intervals.
