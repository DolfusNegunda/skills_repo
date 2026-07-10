---
name: detecting-fallacies-and-inconsistencies
description: Examine an argument, proposal, or document for logical fallacies, internal contradictions, unstated assumptions, and reasoning errors, then report each flaw with where it occurs and why it breaks. Use when someone says "poke holes in this", "does this argument hold up", "find the flaws", "is this logic sound", or hands over a case/memo to stress-test. Produces a list of named flaws, each located and explained.
---

# Detecting Fallacies and Inconsistencies

## Scope
Stress-testing the *reasoning* in a piece of writing or a spoken case: whether
conclusions follow from premises, whether claims contradict each other, what the
argument quietly assumes, and which named fallacies are in play. Focuses on logical
validity and internal consistency, not spelling, prose, or factual accuracy.

## Purpose
Find where an argument fails *before* someone acts on it — separating what is
actually established from what only sounds convincing.

## When to use this skill
- "Poke holes in / stress-test / find the flaws in this argument."
- Evaluating a proposal, business case, or memo before endorsing it.
- Checking whether a document contradicts itself across sections.
- Auditing one's own reasoning before presenting it.

## When NOT to use this skill
- Spelling, grammar, and surface polish → [proofreading-text](../../office/proofreading-text/SKILL.md).
- A full multi-dimension review with scores → [conducting-structured-reviews](../../review/conducting-structured-reviews/SKILL.md).
- Checking whether facts are *true* against sources → [verifying-facts](../../research/verifying-facts/SKILL.md).
- Testing a factual belief with new evidence → [testing-hypotheses](../testing-hypotheses/SKILL.md).

## Inputs
- The argument/document, and its main claim or conclusion.
- The audience and stakes — how rigorous the bar should be.
- Any context needed to know what the author is assuming as shared ground.

## Outputs
- A list of flaws: each named (fallacy/contradiction/assumption), located, and explained.
- For each, why it weakens the argument and what would be needed to repair it.
- An overall verdict: does the conclusion actually follow?

## Workflow
```
Progress:
- [ ] 1. Extract the conclusion and the premises meant to support it
- [ ] 2. Test validity: do the premises actually entail the conclusion?
- [ ] 3. Scan for named fallacies in the reasoning
- [ ] 4. Cross-check for internal contradictions across the whole document
- [ ] 5. Surface unstated assumptions the argument depends on
- [ ] 6. Report each flaw located; give the overall verdict
```

**Step 1 — Map the argument.** Write the conclusion in one line, then list the
premises offered for it. Much sloppy reasoning hides until the skeleton is exposed.

**Step 2 — Test validity.** Ask: if every premise were true, would the conclusion
*have* to follow? A gap here is the deepest flaw — the argument is invalid regardless
of the facts.

**Step 3 — Scan for fallacies.** Check against a concrete list, not a vague sense:
**strawman** (attacking a distorted version), **false dichotomy** (only two options
when more exist), **ad hominem**, **appeal to authority/popularity**, **base-rate
neglect** (ignoring prior frequency), **survivorship bias** (only winners in the
sample), **circular reasoning**, **slippery slope**, **hasty generalization**,
**correlation-as-causation**, **sunk cost**, **equivocation** (a word shifting meaning).

**Step 4 — Cross-check consistency.** Read the whole document for claims that
contradict each other — a number in the summary that differs from the table, a
principle asserted in one section and violated in another.

**Step 5 — Surface assumptions.** Name what must be true but is never stated: the
hidden premise the whole case rests on. Ask "what has to hold for this to work?"

**Step 6 — Report.** For each flaw give the location, the name, why it breaks the
reasoning, and the fix. Then judge whether the conclusion stands.

## Principles
1. **Attack the reasoning, not the author** — and never a strawman of their case.
2. **Invalid beats false** — a gap from premises to conclusion outranks a wrong detail.
3. **Name the flaw concretely** — "false dichotomy" beats "this feels off".
4. **Steelman first** — repair the argument's best form before judging it fails.
5. **A weak argument for a true conclusion is still a weak argument.**
6. **Absence of a fallacy isn't soundness** — the premises still have to hold.

## Decision framework
- **Conclusion doesn't follow even if premises hold?** Flag as invalid — the top-priority flaw.
- **Two statements can't both be true?** Contradiction; quote both and their locations.
- **Argument leans on an unstated claim?** Surface it; ask whether it holds.
- **Only two options presented?** Check for a false dichotomy before accepting the frame.
- **A single case used to prove a rule?** Hasty generalization / survivorship — demand the base rate.
- **Can't tell if it's a flaw or a style choice?** Note it as a question, not a verdict.

## Common mistakes
- **Fallacy-hunting by label** — slapping names on valid arguments to sound rigorous.
- **The fallacy fallacy** — concluding a claim is false merely because its argument is flawed.
- **Strawmanning while critiquing** — refuting a weaker version than what was written.
- **Missing contradictions** by reviewing sections in isolation, never end-to-end.
- **Stopping at surface fallacies** and never surfacing the load-bearing hidden assumption.
- **Nitpicking wording** and calling it a reasoning flaw.

## Validation checklist
- [ ] Conclusion and premises were explicitly extracted.
- [ ] Validity tested: premises-to-conclusion link checked, not just the facts.
- [ ] Reasoning scanned against a concrete fallacy list, not a vibe.
- [ ] Whole document cross-checked for internal contradictions.
- [ ] Load-bearing unstated assumptions named.
- [ ] Each flaw located, named, explained, and given a repair.
- [ ] Verdict states whether the conclusion actually follows.

## Edge cases
- **Rhetorical/persuasive text:** distinguish legitimate emphasis from a genuine fallacy.
- **Missing data, not bad logic:** flag as unsupported, not fallacious.
- **Author's own words ambiguous:** ask which reading is meant before calling it equivocation.
- **Domain jargon:** a term shifting meaning across sections is equivocation; confirm it isn't standard usage.
- **True conclusion, broken argument:** say so — the flaw is the support, not the claim.

## Related skills
- [conducting-structured-reviews](../../review/conducting-structured-reviews/SKILL.md), [proofreading-text](../../office/proofreading-text/SKILL.md).
- [testing-hypotheses](../testing-hypotheses/SKILL.md), [analyzing-tradeoffs](../analyzing-tradeoffs/SKILL.md), [identifying-constraints](../identifying-constraints/SKILL.md).
- [verifying-facts](../../research/verifying-facts/SKILL.md), [assessing-source-credibility](../../research/assessing-source-credibility/SKILL.md).

## Examples
**Input:** "We must launch now or lose the market — every successful competitor
launched early, and the team that delayed last year failed."
**Output:** Conclusion: launch now. Flaws: (1) **False dichotomy** — "now or lose the
market" ignores a phased or slightly-later launch. (2) **Survivorship bias** — "every
successful competitor" samples only survivors; the failed early-launchers aren't
counted. (3) **Hasty generalization** — one delayed team failing doesn't establish
that delay caused failure (correlation-as-causation). (4) **Unstated assumption** —
that the product is ready enough that launching helps rather than hurts. Verdict:
conclusion does not follow; the urgency is asserted, not established.

## Automation opportunities
- Keep a reusable fallacy checklist to run against every proposal.
- Diff figures across summary vs. tables to catch numeric contradictions automatically.
- Add a "hidden assumptions" prompt to the review template so it's never skipped.
