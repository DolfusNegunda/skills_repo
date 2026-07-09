---
name: reviewing-research
description: Review research, studies, and analyses for methodological soundness, evidence quality, validity, bias, and whether conclusions follow from the data — producing severity-ranked findings. Use when the user asks to "review this research/study/analysis", "critique this methodology", "does the data support this claim", or assess a report's rigor. Inherits the shared severity/scoring model. Produces a rigorous, actionable critique that separates supported conclusions from overreach.
---

# Reviewing Research

## Scope
Critical appraisal of research and data-driven analysis — method, evidence,
validity, bias, and whether the conclusions are warranted. Inherits method/severity/
scoring from [conducting-structured-reviews](../conducting-structured-reviews/SKILL.md).
Producing/synthesizing research lives in
[synthesizing-research](../../research/synthesizing-research/SKILL.md).

## Purpose
Separate what the evidence actually supports from what the authors claim — exposing
weak method, bias, and overreach so decisions aren't built on shaky findings.

## When to use this skill
- "Review this research / study / analysis / whitepaper."
- "Critique this methodology / does the data support this conclusion?"
- Appraising evidence quality before acting on findings.

## When NOT to use this skill
- Reading to extract findings → [reading-scientific-papers](../../research/reading-scientific-papers/SKILL.md).
- Combining multiple studies → [synthesizing-research](../../research/synthesizing-research/SKILL.md).
- General document quality → [reviewing-documents](../reviewing-documents/SKILL.md).

## Inputs
- The research (method, data, results, conclusions) and its purpose/claims.
- The domain's expected standard of evidence; any conflicts of interest disclosed.

## Outputs
- A review: verdict on how much to trust it + scores, severity-ranked findings, a
  "what the evidence actually supports" statement, and strengths.

## Evaluation rubric (dimensions)
1. **Question & design** — clear question; design appropriate to answer it.
2. **Method** — sound, replicable, adequately described; controls where needed.
3. **Data & sample** — sufficient, representative, correctly collected; limitations acknowledged.
4. **Analysis** — appropriate techniques; correct stats; no p-hacking/cherry-picking.
5. **Validity** — internal (causal claims justified) and external (generalizability).
6. **Bias** — selection, confirmation, funding/conflict, survivorship addressed.
7. **Conclusions** — follow from results; caveated; no correlation-as-causation or overreach.

## Scoring & severity
Score 1–5; rank Blocker→Praise (see
[foundation reference](../conducting-structured-reviews/references/severity-and-scoring.md)).
Examples: **Blocker** = a causal claim from purely correlational data, or a sample
that can't support the generalization; **Major** = no control group where one is
needed; **Minor** = an unstated limitation; **Nit** = a citation format slip.

## Workflow
```
Progress:
- [ ] 1. Identify the question, claims, and expected evidence standard
- [ ] 2. Assess design and method fit
- [ ] 3. Scrutinize data, sample, and analysis
- [ ] 4. Test internal/external validity and hunt for bias
- [ ] 5. Check conclusions against results (claim vs. evidence)
- [ ] 6. Severity-rank, score, verdict; what the evidence truly supports
```

**Step 5 — claim vs. evidence is the core test.** Line up each conclusion against
what the data can actually bear; the most common defect is conclusions stronger than
the method supports. **Correlation ≠ causation** and small/biased samples ≠
generalizable are the recurring Blockers.

## Recommended-improvements guidance
State what would make the claim credible: the control/comparison needed, the sample
required, the correct statistical test, the caveat to add, or the weaker (accurate)
version of the conclusion the data supports.

## Validation checklist
- [ ] Research question and claims identified.
- [ ] Method and design assessed for fitness and rigor.
- [ ] Sample size/representativeness and analysis checked.
- [ ] Internal and external validity evaluated; biases probed.
- [ ] Each conclusion tested against the evidence.
- [ ] Findings carry severity + a fix; trust verdict + scores given.

## Common mistakes
- **Accepting conclusions without checking the method behind them.**
- **Missing the correlation-to-causation leap.**
- **Ignoring sample bias / size.**
- **Not checking for conflicts of interest / funding effects.**
- **Confusing statistical significance with practical importance.**

## Edge cases
- **Non-peer-reviewed/industry reports:** weight funding bias and method transparency heavily.
- **Qualitative research:** judge by trustworthiness/credibility criteria, not sample size.
- **Meta-analyses:** check inclusion criteria and heterogeneity, not just the pooled result.
- **Outside your expertise:** appraise structure/logic you can verify; flag the rest for a specialist.

## Related skills
- [conducting-structured-reviews](../conducting-structured-reviews/SKILL.md), [reading-scientific-papers](../../research/reading-scientific-papers/SKILL.md).
- [assessing-source-credibility](../../research/assessing-source-credibility/SKILL.md), [verifying-facts](../../research/verifying-facts/SKILL.md).

## Examples
**Input:** "Review this study claiming our feature increased retention 30%."
**Output:** Trust: Low (Validity 2/5, Analysis 2/5). **Blocker:** retention compared
across two different time periods with no control — the 30% may be seasonal, not
causal; fix: A/B or matched-cohort comparison. **Major:** sample skews to power
users. **Praise:** transparent data collection. Evidence supports "retention rose
among power users in Q4," not "the feature caused +30%".

## Automation opportunities
- Reuse the rubric as an evidence-quality gate before acting on findings.
- Pair with [assessing-source-credibility](../../research/assessing-source-credibility/SKILL.md) for the source dimension.
