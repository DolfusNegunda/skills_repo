---
name: analyzing-cost-benefit
description: Perform a cost-benefit analysis that quantifies all costs and benefits over time and computes NPV, ROI, and payback — including intangibles, risk, and sensitivity. Use when the user asks to "do a cost-benefit analysis", "is this worth it", "calculate ROI/NPV/payback", or compare the economics of options. Captures full lifecycle costs and time value of money. Produces a defensible economic analysis, not a one-year back-of-envelope.
---

# Analyzing Cost-Benefit

## Scope
Quantifying the full economics of a decision over its lifecycle — all costs and
benefits, discounted for time value, expressed as NPV, ROI, and payback, with
sensitivity on the key assumptions. Feeds business cases and decisions.

## Purpose
Answer "is this worth it?" rigorously: capture total cost (not just upfront),
quantify benefits honestly (including intangibles as proxies), account for the time
value of money, and show how robust the answer is to its assumptions.

## When to use this skill
- "Do a cost-benefit analysis / is this worth it / calculate ROI, NPV, payback."
- Comparing the economics of options or investments.
- The financial core of a business case.

## When NOT to use this skill
- The full narrative case → [writing-business-cases](../writing-business-cases/SKILL.md).
- Multi-criteria (non-financial) comparison → [building-decision-matrices](../building-decision-matrices/SKILL.md).
- Building the model in a tool → [engineering-spreadsheets](../../office/engineering-spreadsheets/SKILL.md).

## Inputs
- The option(s) and time horizon; upfront and ongoing costs; expected benefits.
- The discount rate/hurdle rate and key uncertain assumptions.

## Outputs
- A CBA: itemized costs and benefits over time, NPV/ROI/payback, treatment of
  intangibles and risk, and a sensitivity analysis on the critical drivers.

## Workflow
```
Progress:
- [ ] 1. Define scope, option(s), and time horizon
- [ ] 2. Itemize ALL costs (upfront + ongoing/lifecycle)
- [ ] 3. Quantify benefits (tangible + proxied intangibles)
- [ ] 4. Discount to present value; compute NPV, ROI, payback
- [ ] 5. Adjust for risk; run sensitivity on key assumptions
- [ ] 6. Compare against do-nothing; state the verdict
```

**Step 2 — total cost, not upfront.** Include run/maintenance, training, migration,
opportunity, and decommission costs. Understated ongoing cost is the classic CBA
error. **Step 4 — time value:** discount future cash flows to present value; a dollar
next year is worth less than today. NPV > 0 (above the hurdle rate) means value-
creating. **Step 5 — sensitivity is mandatory:** identify the one or two assumptions
the result hinges on and show the answer across a plausible range. A single-point ROI
hides fragility.

## Principles
1. **Full lifecycle cost,** not just the sticker price.
2. **Quantify benefits honestly;** proxy intangibles, don't inflate them.
3. **Discount for time value** — NPV, not undiscounted sums.
4. **Always compare to do-nothing.**
5. **Sensitivity, not false precision** — show the range and the drivers.

## Decision framework
- **Long horizon / large sums?** NPV with a proper discount rate is essential.
- **Quick screen?** Payback period, but note it ignores time value and later cash flows.
- **Comparing similar-cost options?** ROI ranking + sensitivity.
- **Big intangible component?** Proxy-measure it and flag it as a key uncertainty.

## Common mistakes
- **Counting upfront cost only** — ignoring ongoing/lifecycle.
- **No discounting** — treating future and present money as equal.
- **Inflated or hand-waved intangible benefits.**
- **No do-nothing baseline.**
- **Single-point estimate, no sensitivity** — fragile case looks solid.
- **Double-counting benefits** across categories.

## Validation checklist
- [ ] Scope, options, and horizon defined.
- [ ] All costs (upfront + ongoing/lifecycle) itemized.
- [ ] Benefits quantified; intangibles proxied and flagged.
- [ ] Cash flows discounted; NPV, ROI, payback computed correctly.
- [ ] Risk considered; sensitivity run on key drivers.
- [ ] Compared to do-nothing; clear verdict.

## Edge cases
- **High uncertainty:** use scenarios (best/base/worst), not one number.
- **Non-financial value dominant:** pair with [building-decision-matrices](../building-decision-matrices/SKILL.md).
- **Sunk costs:** exclude — only forward cash flows matter.
- **Inflation/currency:** be consistent (real vs. nominal; single currency).

## Related skills
- [writing-business-cases](../writing-business-cases/SKILL.md), [building-decision-matrices](../building-decision-matrices/SKILL.md), [maintaining-risk-registers](../maintaining-risk-registers/SKILL.md).
- [engineering-spreadsheets](../../office/engineering-spreadsheets/SKILL.md), [reviewing-business-cases](../../review/reviewing-business-cases/SKILL.md).

## Examples
**Input:** "Is buying this $80k automation tool worth it?"
**Output:** Costs over 3 yrs: $80k license + $15k/yr support + $20k implementation +
training = ~$155k. Benefits: 2 FTE-equivalents of time saved ≈ $180k/3yr (proxied,
flagged). Discounted at 10%: NPV +$18k, ROI 12%, payback ~2.1 yrs. Sensitivity: if
time-saved is 30% lower, NPV turns negative — the decisive assumption. Verdict:
marginal; proceed only if the adoption/time-saving target is credible.

## Automation opportunities
- Build the model with [engineering-spreadsheets](../../office/engineering-spreadsheets/SKILL.md); parameterize assumptions for sensitivity.
- Feed the result into a business case and a decision matrix.
