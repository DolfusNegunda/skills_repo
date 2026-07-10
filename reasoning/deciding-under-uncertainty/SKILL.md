---
name: deciding-under-uncertainty
description: Make a sound decision with incomplete information — reason with expected value, sort reversible (two-way door) from irreversible (one-way door) choices, anchor on base rates, and guard against bias. Use when a decision must be made before the facts are in, when outcomes are probabilistic, or when someone asks "what should we do given we don't know X".
---

# Deciding Under Uncertainty

## Scope
Choosing well when the information is incomplete and outcomes are probabilistic:
estimating expected value, classifying the decision by reversibility, anchoring on
base rates over vivid anecdotes, and countering the biases that distort judgment
under uncertainty. Not full-data comparison; not forecasting for its own sake.

## Purpose
Act rationally before certainty arrives — spend analysis where a wrong call is
costly and irreversible, move fast where it is cheap to undo, and avoid the
predictable errors that make uncertain decisions worse than the odds warrant.

## When to use this skill
- A decision must be made before the facts are fully in.
- Outcomes are probabilistic, not deterministic.
- Someone asks "what should we do given we don't know X".

## When NOT to use this skill
- Comparing options with full data via a scored matrix → [building-decision-matrices](../../business/building-decision-matrices/SKILL.md).
- Weighing known options against criteria → [analyzing-tradeoffs](../analyzing-tradeoffs/SKILL.md).
- Producing a numeric estimate of a quantity → [estimating-under-uncertainty](../estimating-under-uncertainty/SKILL.md).
- Exploring divergent futures in depth → [planning-scenarios](../planning-scenarios/SKILL.md).

## Inputs
- The decision, its deadline, and what is unknown.
- Plausible outcomes with rough probabilities and payoffs.
- Base rates or reference-class data; the cost of being wrong.

## Outputs
- A reversibility call (one-way vs two-way door) setting the rigor level.
- An expected-value comparison of the options under uncertainty.
- A decision with assumptions, the bias checks made, and what would change it.

## Workflow
```
Progress:
- [ ] 1. State the decision, deadline, and what is unknown
- [ ] 2. Classify reversibility: one-way vs two-way door
- [ ] 3. Anchor on the base rate / reference class
- [ ] 4. Lay out outcomes, probabilities, and payoffs; compute expected value
- [ ] 5. Run a bias check on the estimates and the framing
- [ ] 6. Decide; record assumptions and the trigger to revisit
```

**Step 1 — Frame.** State the decision, the deadline, and precisely what is not
known. Naming the unknown separates it from what is merely unexamined.

**Step 2 — Reversibility.** Classify the decision. A **two-way door** (cheaply
undone) warrants speed — deciding fast beats deciding perfectly. A **one-way door**
(hard/impossible to reverse) warrants more rigor and more information first.
Matching effort to reversibility is the highest-leverage move here.

**Step 3 — Base rate.** Anchor on how often this kind of thing works out — the
reference class — before adjusting for specifics. The outside view corrects the
optimism of the inside story.

**Step 4 — Expected value.** List plausible outcomes, assign rough probabilities
and payoffs, and compare options by expected value. Rough numbers beat none; they
make hidden assumptions explicit and comparable. Weigh downside asymmetry — ruin is
not just a low EV, it ends the game.

**Step 5 — Bias check.** Interrogate the estimates: overconfidence (too-narrow
ranges), anchoring, availability (vivid case over base rate), confirmation,
sunk-cost. Seek the disconfirming evidence deliberately.

**Step 6 — Decide.** Commit, record the assumptions and probabilities, and set a
trigger — the signal or date that reopens the decision. A decision under
uncertainty is a bet; log the reasoning so the bet can be judged apart from luck.

## Principles
1. **Reversibility sets the rigor** — sprint through two-way doors, study one-way doors.
2. **Expected value, not best case** — weight outcomes by probability.
3. **Base rate first,** then adjust for the specifics.
4. **Avoid ruin** — refuse bets whose downside ends the game, even at positive EV.
5. **Decide with the info that is worth its cost** — perfect information rarely pays.
6. **Judge the decision, not the outcome** — a good bet can lose.

## Decision framework
- **Cheaply reversible?** Decide now; do not gold-plate the analysis.
- **Irreversible and high-stakes?** Buy information or optionality first.
- **Estimate clashes with the base rate?** Justify the deviation or defer to it.
- **Downside is catastrophic?** Reject regardless of expected value.
- **Full data actually available?** Switch to [building-decision-matrices](../../business/building-decision-matrices/SKILL.md).

## Common mistakes
- **Analysis paralysis on reversible decisions** — over-studying a two-way door.
- **Ignoring base rates** — trusting the vivid story over the reference class.
- **Treating best case as expected** — planning on the optimistic tail.
- **Outcome bias** — grading the decision by the result, not the reasoning.
- **Overconfidence** — probability ranges far too narrow.
- **Chasing certainty** that costs more than the decision is worth.

## Validation checklist
- [ ] The decision, deadline, and unknowns are stated.
- [ ] Reversibility is classified and set the depth of analysis.
- [ ] A base rate / reference class was consulted.
- [ ] Outcomes, probabilities, and payoffs are laid out; EV compared.
- [ ] Catastrophic-downside (ruin) risk was checked separately from EV.
- [ ] Named biases were checked; assumptions and a revisit trigger recorded.

## Edge cases
- **Deep uncertainty (no probabilities):** shift to robust options and scenarios → [planning-scenarios](../planning-scenarios/SKILL.md).
- **Irreversible and urgent:** buy a small reversible step to learn before committing.
- **Group decision:** elicit estimates independently first to avoid anchoring.
- **Tail risk of ruin:** treat as a hard constraint, not a probability to average → [identifying-constraints](../identifying-constraints/SKILL.md).

## Related skills
- [analyzing-tradeoffs](../analyzing-tradeoffs/SKILL.md), [estimating-under-uncertainty](../estimating-under-uncertainty/SKILL.md), [planning-scenarios](../planning-scenarios/SKILL.md), [testing-hypotheses](../testing-hypotheses/SKILL.md), [detecting-fallacies-and-inconsistencies](../detecting-fallacies-and-inconsistencies/SKILL.md).
- [building-decision-matrices](../../business/building-decision-matrices/SKILL.md), [maintaining-risk-registers](../../business/maintaining-risk-registers/SKILL.md).

## Examples
**Input:** "Should we launch the beta now or wait a month for more data?"
**Output:** Reversibility: two-way door — a beta can be pulled. Base rate: similar
betas here shipped fine and taught more than another month of internal guessing.
EV: launch now ≈ faster learning, minor polish risk; wait ≈ marginal quality gain,
real opportunity cost. No ruin risk (limited audience, rollback ready). Bias check:
waiting is driven by availability of one bad past launch, not the base rate.
Decision: launch now; trigger to revisit — crash rate >2% reopens the call.

## Automation opportunities
- Template an EV table (outcome, probability, payoff) for repeat decisions.
- Add a one-way/two-way door tag to decision records to route rigor.
- Keep a decision journal with predicted probabilities to calibrate over time.
