---
name: reviewing-business-cases
description: Review a business case or investment proposal for the soundness of its problem, assumptions, financials, alternatives, risks, and benefits realization — producing severity-ranked findings and a fund/revise/reject recommendation. Use when the user asks to "review this business case", "assess this investment/proposal", "sanity-check these numbers", or evaluate a funding ask. Inherits the shared severity/scoring model. Produces a rigorous, actionable review.
---

# Reviewing Business Cases

## Scope
Critical evaluation of a business case or investment ask — whether the problem is
real, the numbers hold, alternatives were considered, and benefits are realizable.
Inherits method/severity/scoring from
[conducting-structured-reviews](../conducting-structured-reviews/SKILL.md). Writing
one is [writing-business-cases](../../business/writing-business-cases/SKILL.md).

## Purpose
Protect the decision-maker from a plausible-but-flawed case: expose optimistic
assumptions, missing alternatives, unquantified risk, and benefits that won't
materialize — before money is committed.

## When to use this skill
- "Review this business case / investment proposal / funding ask."
- "Sanity-check these numbers / this ROI."
- A finance or governance gate before approval.

## When NOT to use this skill
- Writing the case → [writing-business-cases](../../business/writing-business-cases/SKILL.md).
- Technical design → [reviewing-architecture](../reviewing-architecture/SKILL.md).
- The financial model mechanics → [engineering-spreadsheets](../../office/engineering-spreadsheets/SKILL.md).

## Inputs
- The business case (problem, options, costs, benefits, risks, timeline).
- The underlying model/assumptions if available; the decision and its threshold
  (e.g. hurdle rate, payback target).

## Outputs
- A review: recommendation (fund / revise / reject) + scores, severity-ranked
  findings, tested assumptions, and strengths.

## Evaluation rubric (dimensions)
1. **Problem/opportunity** — real, evidenced, and worth solving; not a solution in search of a problem.
2. **Assumptions** — explicit, sourced, and realistic (not best-case-only).
3. **Financials** — costs complete (incl. run/ongoing), benefits quantified, method sound (NPV/ROI/payback), math correct.
4. **Alternatives** — genuine options considered, including do-nothing.
5. **Risk** — key risks identified, sized, and mitigated; sensitivity shown.
6. **Benefits realization** — measurable, owned, with a plan to actually capture them.
7. **Strategic fit** — aligns with priorities and capacity.

## Scoring & severity
Score 1–5; rank Blocker→Praise (see
[foundation reference](../conducting-structured-reviews/references/severity-and-scoring.md)).
Examples: **Blocker** = benefits rest on an unsupported assumption that, if wrong,
flips the ROI negative; **Major** = ongoing run costs omitted; **Minor** = no
sensitivity analysis; **Nit** = inconsistent rounding.

## Workflow
```
Progress:
- [ ] 1. Confirm the decision, threshold, and what the case claims
- [ ] 2. Test the problem: is it real and evidenced?
- [ ] 3. Stress the assumptions and financials (recompute key figures)
- [ ] 4. Check alternatives (incl. do-nothing) and risks/sensitivity
- [ ] 5. Assess benefits realization and strategic fit
- [ ] 6. Severity-rank, score, recommendation; fixes per finding
```

**Step 3 — follow the money.** Re-derive the headline number; check that costs
include run/maintenance, benefits are quantified and not double-counted, and the
method matches the decision. **The assumptions are where cases fail** — identify the
one or two that the whole result hinges on and test them hardest.

## Recommended-improvements guidance
Name the fix: source or revise the shaky assumption, add the omitted cost, run a
sensitivity on the key driver, add the missing alternative, or assign a benefit
owner with a measurement plan.

## Validation checklist
- [ ] Decision and approval threshold known.
- [ ] Problem tested for reality and evidence.
- [ ] Key assumptions identified and stress-tested; headline figure re-derived.
- [ ] Costs complete (incl. ongoing); benefits quantified and singly-counted.
- [ ] Alternatives (incl. do-nothing) and risk/sensitivity assessed.
- [ ] Benefits realization owned and measurable.
- [ ] Findings carry severity + a fix; recommendation + scores given.

## Common mistakes
- **Accepting assumptions at face value** — the #1 way bad cases pass.
- **Reviewing benefits, ignoring run costs** — TCO understated.
- **No do-nothing baseline** — everything looks worth doing.
- **Ignoring sensitivity** — a fragile case looks robust.
- **Confusing strategic fit with financial soundness** — both required.

## Edge cases
- **Intangible/strategic benefits:** require a rationale and proxy measures, not hand-waving.
- **High uncertainty:** demand ranges and scenarios, not false precision.
- **Sunk-cost framing:** ignore money already spent; judge forward economics.
- **Optimism bias:** compare estimates to comparable past projects.

## Related skills
- [conducting-structured-reviews](../conducting-structured-reviews/SKILL.md), [writing-business-cases](../../business/writing-business-cases/SKILL.md).
- [analyzing-cost-benefit](../../business/analyzing-cost-benefit/SKILL.md), [maintaining-risk-registers](../../business/maintaining-risk-registers/SKILL.md).

## Examples
**Input:** "Review this $2M automation business case."
**Output:** Recommendation: Revise (Financials 2/5, Risk 2/5). **Blocker:** the 3-yr
ROI depends on 40% headcount reduction with no evidence it's achievable — at 20% the
NPV is negative; fix: evidence the target or model a conservative case. **Major:**
$300k/yr platform run cost omitted. **Minor:** no sensitivity on adoption rate.
**Praise:** clear problem quantification.

## Automation opportunities
- Reuse the rubric as a standing investment-committee gate.
- Require a sensitivity table and benefit owner before review.
- Pair with [analyzing-cost-benefit](../../business/analyzing-cost-benefit/SKILL.md) to rebuild weak financials.
