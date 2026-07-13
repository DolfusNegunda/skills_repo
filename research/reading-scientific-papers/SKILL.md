---
name: reading-scientific-papers
description: Read academic and technical papers efficiently and critically — extracting the question, method, findings, and limitations without getting lost, and judging what the paper actually shows. Use when the user asks to "read/summarize this paper", "explain this study", "what does this research say", or extract findings from academic literature. Uses a strategic non-linear reading order. Produces an accurate extraction and critical read, not a naive abstract restatement.
---

# Reading Scientific Papers

## Scope
Efficiently and critically reading research/technical papers: extracting the core
question, method, results, and limitations, and judging what the paper genuinely
supports. Feeds literature reviews and synthesis. Formal appraisal is
[reviewing-research](../../review/reviewing-research/SKILL.md).

## Purpose
Get the real signal from a paper fast — not by reading front-to-back, but by
extracting what matters and reading critically enough to know what the results
actually mean versus what the abstract claims.

## When to use this skill
- "Read / summarize / explain this paper or study."
- "What does this research actually say / show?"
- Extracting findings from academic or technical literature.

## When NOT to use this skill
- Formal quality appraisal/critique → [reviewing-research](../../review/reviewing-research/SKILL.md).
- Combining many papers → [conducting-literature-reviews](../conducting-literature-reviews/SKILL.md) / [synthesizing-research](../synthesizing-research/SKILL.md).
- Verifying one claim → [verifying-facts](../verifying-facts/SKILL.md).

## Inputs
- The paper and your goal (understand the finding? assess the method? extract a number?).
- Your background in the domain (affects how much to unpack).

## Outputs
- A structured extraction: research question, method, key findings, limitations, and
  what it does/doesn't support — plus relevance to your goal.

## Workflow
```
Progress:
- [ ] 1. Define your goal for reading this paper
- [ ] 2. First pass: title, abstract, figures, conclusion — get the gist
- [ ] 3. Decide relevance — read deeper or stop
- [ ] 4. Second pass: method and results (how, and what was found)
- [ ] 5. Read critically: limitations, do conclusions follow?
- [ ] 6. Extract findings + caveats tied to your goal
```

**Step 2 — read non-linearly.** Abstract → figures/tables → conclusion first gives
the gist in minutes; the introduction and related work can wait. Many papers can be
triaged out at this stage. **Step 4 — method before believing results:** the method
determines what the numbers mean; the results are in the figures more than the prose.
**Step 5 — read the discussion skeptically:** authors present their work favorably;
check the limitations section and ask whether the conclusions actually follow from the
results (the abstract often overstates). **Step 6 — extract with caveats:** capture
the finding *and* its conditions (sample, context), not a context-free claim.

## Principles
1. **Read for your goal,** not cover to cover.
2. **Non-linear order** — abstract, figures, conclusion first.
3. **Method determines meaning** — understand it before trusting results.
4. **Figures carry the results** — read them closely.
5. **Trust the data over the abstract's spin** — verify each claim against the actual results (which are themselves bounded by the method).
6. **Extract findings with their conditions,** never context-free.

## Decision framework
- **Triaging many papers?** First-pass only; deep-read the few that matter.
- **Need a specific number?** Go straight to results/tables, then check method for validity.
- **Assessing rigor?** → [reviewing-research](../../review/reviewing-research/SKILL.md).
- **Unfamiliar domain?** Read a review/primer first for context, then the paper.

## Common mistakes
- **Reading linearly** and drowning in the intro.
- **Trusting the abstract** as the finding — it's the authors' spin.
- **Skipping the method** — can't judge what results mean.
- **Ignoring limitations** the authors themselves state.
- **Extracting context-free claims** (dropping sample/conditions).
- **Not stopping** on irrelevant papers.

## Validation checklist
- [ ] Reading goal defined.
- [ ] First pass done (abstract, figures, conclusion); relevance decided.
- [ ] Method understood well enough to interpret results.
- [ ] Figures/tables read, not just the prose.
- [ ] Limitations noted; conclusions checked against results.
- [ ] Findings extracted with their conditions/caveats.

## Edge cases
- **Highly technical/math-heavy:** extract the claim and conditions; flag where you can't verify the proof.
- **Preprints:** lower certainty; not yet peer-reviewed.
- **Conflicting papers:** note the disagreement for synthesis; don't pick one arbitrarily.
- **Retracted/old papers:** check retraction status and whether findings still hold.

## Related skills
- [reviewing-research](../../review/reviewing-research/SKILL.md), [conducting-literature-reviews](../conducting-literature-reviews/SKILL.md), [synthesizing-research](../synthesizing-research/SKILL.md).
- [verifying-facts](../verifying-facts/SKILL.md), [citing-sources](../citing-sources/SKILL.md).

## Examples
**Input:** "Explain what this RCT on a new teaching method actually shows."
**Output:** Question (does method X raise test scores vs. standard?); method (RCT,
n=240, one district, one semester); finding (X group +8% on the post-test, p<0.05);
limitations (single district, short duration, no long-term follow-up); what it
supports: a short-term gain in one context — not that X works universally or lasts.

## Automation opportunities
- Extract structured fields (question/method/n/finding/limitations) per paper into a table.
- Feed extractions into a literature-review synthesis matrix.
