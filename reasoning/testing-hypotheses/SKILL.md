---
name: testing-hypotheses
description: Turn a belief or hunch into a falsifiable hypothesis, define in advance what evidence would confirm or disconfirm it, gather that evidence, and update honestly on the result. Use when someone says "I think X is happening", "let's test whether", "is this actually true", "prove/disprove this theory", or wants to check an assumption before betting on it. Produces a stated hypothesis, its predictions, the evidence, and a revised belief.
---

# Testing Hypotheses

## Scope
Taking a belief, hunch, or claim about how something works and subjecting it to a
fair test: making it falsifiable, predicting what should be observed if it were
true (and if it were false), collecting that evidence, and updating. Covers the
discipline of pre-committing to what would change the mind before looking.

## Purpose
Replace "I'm pretty sure" with an answer earned from evidence — and guard against
fooling oneself, so the conclusion survives a skeptic.

## When to use this skill
- "I think X causes Y / X is happening — let's confirm before acting."
- Validating an assumption behind a plan, estimate, or design.
- Competing explanations exist and one must be chosen on evidence.
- A metric moved and the reason is being guessed at.

## When NOT to use this skill
- Verifying a factual claim against authoritative sources → [verifying-facts](../../research/verifying-facts/SKILL.md).
- Tracing a defect to its single cause → [analyzing-root-causes](../analyzing-root-causes/SKILL.md).
- Deciding among options under irreducible uncertainty → [deciding-under-uncertainty](../deciding-under-uncertainty/SKILL.md).
- Pure forecasting of a quantity → [estimating-under-uncertainty](../estimating-under-uncertainty/SKILL.md).

## Inputs
- The belief or claim, stated as plainly as possible, and why it matters.
- Available data, ability to run an experiment, and what's cheap to observe.
- The current confidence and what decision hinges on the answer.

## Outputs
- A falsifiable hypothesis with a stated null/alternative.
- Predictions written *before* looking: what confirms, what disconfirms.
- The evidence gathered and how it maps to those predictions.
- A revised belief with new confidence, and residual uncertainty named.

## Workflow
```
Progress:
- [ ] 1. State the belief and sharpen it into a falsifiable hypothesis
- [ ] 2. Write the predictions: what should be seen if true, and if false
- [ ] 3. Choose the cheapest test that could disconfirm it
- [ ] 4. Gather the evidence without peeking-and-adjusting
- [ ] 5. Compare evidence to predictions; update the belief
- [ ] 6. State the revised confidence and what's still unknown
```

**Step 1 — Sharpen.** Rewrite the belief so it could be wrong. "The site is slow"
is untestable; "p95 latency exceeds 2s during peak hours" is. If no observation
could contradict it, it is not yet a hypothesis — narrow it until one could.

**Step 2 — Predict.** Before gathering anything, write what a true hypothesis
predicts *and* what a false one predicts. A test that fits any outcome proves
nothing. Name the null (no effect) explicitly.

**Step 3 — Design the test.** Pick the observation most likely to *disconfirm* if
the belief is wrong — a disconfirming test is worth more than ten confirmations.
Prefer the cheapest one that discriminates between the competing explanations.

**Step 4 — Gather.** Collect the evidence as designed. Do not move the goalposts or
stop the moment the data looks favorable. Decide the sample/duration up front.

**Step 5 — Compare and update.** Map evidence to the Step-2 predictions. Update
proportionally: strong disconfirming evidence should move the belief a lot; a weak
confirmation, little. Consider whether another hypothesis explains the data better.

**Step 6 — Report.** State the revised belief, the new confidence, and what remains
uncertain or untested.

## Principles
1. **Falsifiable or it's not a hypothesis** — name the observation that would kill it.
2. **Predict before you peek** — commit to what confirms/disconfirms in advance.
3. **Seek disconfirmation** — try hardest to break your own belief.
4. **Hold the null** — "no effect" must be a live possibility, not a formality.
5. **Update in proportion to evidence strength**, not to how much the belief is liked.
6. **One variable at a time** where possible, so the result is attributable.

## Decision framework
- **Can't state a disconfirming observation?** It's a value or definition, not a hypothesis — reframe.
- **Evidence is ambiguous?** The test didn't discriminate; design a sharper one, don't force a verdict.
- **Result confirms the belief?** Ask what else predicts the same data before celebrating.
- **Result surprises you?** Suspect the test before the world, but do update — don't explain it away.
- **Test is expensive?** Find a cheaper proxy that still could disconfirm.

## Common mistakes
- **Unfalsifiable hypotheses** — worded so no outcome could ever contradict them.
- **Confirmation bias** — collecting only supporting evidence, dismissing the rest.
- **HARKing** — inventing the hypothesis after seeing the data, then calling it confirmed.
- **Moving the goalposts** — redefining success once results arrive.
- **Stopping early** on a favorable trend; **p-hacking** by slicing until something "works".
- **Confusing absence of disconfirmation with proof** — untested ≠ true.

## Validation checklist
- [ ] The hypothesis names an observation that would falsify it.
- [ ] Confirming and disconfirming predictions were written before gathering evidence.
- [ ] The null was a genuine possibility, not a formality.
- [ ] The test could have disconfirmed the belief, not only supported it.
- [ ] Evidence was gathered to a pre-set plan; goalposts didn't move.
- [ ] The belief was updated in proportion to evidence, alternatives considered.
- [ ] Revised confidence and residual uncertainty are stated.

## Edge cases
- **Can't experiment (history, one-shot events):** use natural variation or find a prediction the past should already satisfy.
- **Slow feedback:** pick a leading indicator that discriminates sooner.
- **Small samples:** report wide uncertainty; resist over-reading noise.
- **Multiple hypotheses:** rank by prior plausibility, then test the one a cheap observation could eliminate first.
- **The belief is really a value judgment:** stop — evidence can't settle it.

## Related skills
- [deciding-under-uncertainty](../deciding-under-uncertainty/SKILL.md), [estimating-under-uncertainty](../estimating-under-uncertainty/SKILL.md), [planning-scenarios](../planning-scenarios/SKILL.md).
- [analyzing-root-causes](../analyzing-root-causes/SKILL.md), [detecting-fallacies-and-inconsistencies](../detecting-fallacies-and-inconsistencies/SKILL.md).
- [verifying-facts](../../research/verifying-facts/SKILL.md), [assessing-source-credibility](../../research/assessing-source-credibility/SKILL.md).

## Examples
**Input:** "I think the checkout redesign is why conversions dropped."
**Output:** Hypothesis: the redesign (not seasonality) caused the drop. Prediction if
true: conversion falls only for users on the new flow, starting at rollout;
unchanged for the held-back cohort. If false: both cohorts fall together.
Test: compare rollout vs. held-back conversion around the launch date (cheap, already
logged). Evidence: both cohorts dropped equally, beginning a week before rollout →
disconfirms. Updated belief: redesign is likely not the cause (confidence 80%);
investigate the earlier external change. Residual: redesign's own effect still untested.

## Automation opportunities
- Log experiment predictions and stop-rules before data collection to prevent goalpost drift.
- Use A/B frameworks that fix sample size and significance up front.
- Dashboard leading indicators so hypotheses get early, pre-defined checks.
