---
name: evaluating-prompts-and-outputs
description: Judge LLM output quality rigorously — define a rubric, grade with pairwise, reference-based, and LLM-as-judge methods (accounting for their biases), catch regressions between prompt versions, and turn failures into concrete fixes. Use when the user asks "how do I evaluate this output", "which prompt is better", "is this response good enough", or "did my change make it worse".
---

# Evaluating Prompts and Outputs

## Scope
Measuring whether an LLM's output is good enough and whether one prompt/version beats
another. Covers rubric design, grading methods (pairwise, reference-based,
LLM-as-judge), regression detection, and converting failures into fixes. A judgment
loop, not a CI harness.

## Purpose
Replace "looks good to me" with evidence: a repeatable score that ranks options,
catches regressions before they ship, and points at the specific defect to fix.

## When to use this skill
- "Evaluate this output / which prompt is better / is this good enough."
- Comparing two prompt or model versions before shipping one.
- Confirming a change improved quality without breaking other cases.

## When NOT to use this skill
- Building a full eval dataset/harness that runs in CI → [building-llm-evaluations](../building-llm-evaluations/SKILL.md).
- Writing or fixing the prompt itself → [engineering-prompts](../engineering-prompts/SKILL.md).
- Checking factual grounding specifically → [detecting-hallucinations](../detecting-hallucinations/SKILL.md).

## Inputs
- The outputs to judge (or the prompt(s)/model(s) that produce them) and the inputs behind them.
- What "good" means for this task: correctness, format, tone, safety, cost/latency.
- Reference answers or preferences, if any; the versions being compared.

## Outputs
- A rubric with weighted, testable criteria.
- Scores/rankings per output or version, with the method stated.
- A failure catalog grouped by cause, each mapped to a concrete fix.

## Workflow
```
Progress:
- [ ] 1. Define what "good" means as a weighted, testable rubric
- [ ] 2. Assemble a representative input set incl. known-hard cases
- [ ] 3. Pick a grading method fit for the question
- [ ] 4. Grade; if using an LLM judge, calibrate and control its biases
- [ ] 5. Compare versions; separate real gains from noise (regressions)
- [ ] 6. Group failures by cause; map each to a fix; re-grade after
```

**Step 1 — Rubric.** Turn "good" into criteria that two people would score the same:
correctness, completeness, format, tone, safety. Weight them by what the task cares
about; a fuzzy rubric produces unrepeatable scores.

**Step 2 — Input set.** Gather inputs that mirror production and deliberately include
the hard, rare, and adversarial cases — averages hide the failures that matter.

**Step 3 — Choose method.** Reference-based when a gold answer exists; pairwise ("A or
B?") when quality is relative and absolute scores are noisy; human review for
high-stakes or subtle cases; LLM-as-judge to scale the rest.

**Step 4 — Grade.** For an LLM judge, give it the rubric and few-shot graded examples,
and control known biases: position bias (randomize/​swap A/B order), length and
self-preference bias, and leniency. Spot-check judge scores against human labels
before trusting them at scale.

**Step 5 — Compare.** Score the same inputs across versions. Distinguish a real gain
from run-to-run noise, and check that a win on one slice didn't regress another —
report per-slice, not just the mean.

**Step 6 — Fixes.** Cluster failures by root cause (format, missing context, reasoning,
hallucination). Map each cluster to a fix, most often a prompt change via
[engineering-prompts](../engineering-prompts/SKILL.md); re-grade to confirm.

## Principles
1. **Define good before you measure it** — no rubric, no evaluation.
2. **Test on the hard cases,** not a convenient average.
3. **Pairwise beats fuzzy absolute scores** when quality is comparative.
4. **Trust the LLM judge only after calibrating it** against human labels.
5. **A mean can hide a regression** — always slice.
6. **Every failure becomes a fix,** or the evaluation was for nothing.

## Decision framework
- **Gold answer exists?** Reference-based grading; else pairwise or rubric-scored.
- **Scores noisy/incomparable?** Switch to pairwise A/B.
- **Too many outputs for humans?** LLM-as-judge, but calibrate on a labeled subset first.
- **Version B wins on average?** Check per-slice before declaring it better.
- **High-stakes or subtle judgment?** Keep a human in the loop; don't auto-judge.

## Common mistakes
- **No rubric** — scoring on vibes, so results aren't repeatable.
- **LLM-judge bias ignored** — position, length, and self-preference inflate scores.
- **Trusting a judge uncalibrated** against any human labels.
- **Reporting only the mean,** missing a regression on an important slice.
- **Evaluating on the same examples the prompt was tuned on.**
- **Grading without a fix loop** — measuring, then changing nothing.

## Validation checklist
- [ ] Rubric is weighted, testable, and agreed before grading.
- [ ] Input set includes hard/rare/adversarial cases, not just typical ones.
- [ ] Grading method fits the question (reference / pairwise / judge / human).
- [ ] LLM judge calibrated vs. human labels; position order randomized.
- [ ] Version comparison reports per-slice, separating signal from noise.
- [ ] Failures grouped by cause and each mapped to a concrete fix.
- [ ] Re-graded after fixes to confirm no new regressions.

## Edge cases
- **No reference answers:** use pairwise or rubric-scored judging, not accuracy.
- **Subjective quality (tone, style):** anchor with graded examples; expect lower agreement.
- **Rare catastrophic failures:** weight severity, not just frequency — one unsafe output can outweigh many good ones.
- **Judge and generator share a model:** watch self-preference; consider a different judge model.

## Related skills
- [engineering-prompts](../engineering-prompts/SKILL.md) — where most fixes land.
- [building-llm-evaluations](../building-llm-evaluations/SKILL.md), [detecting-hallucinations](../detecting-hallucinations/SKILL.md), [generating-structured-outputs](../generating-structured-outputs/SKILL.md).
- [designing-ai-systems](../designing-ai-systems/SKILL.md), [applying-guardrails](../applying-guardrails/SKILL.md).

## Examples
**Input:** "I tweaked the summarization prompt — is the new version better?"
**Output:** Built a 4-criterion rubric (accuracy 0.5, coverage 0.2, format 0.2, length
0.1); ran both versions on 40 inputs including multi-issue and empty tickets; graded
pairwise with an LLM judge, swapping A/B order to cancel position bias, calibrated on
10 human-labeled pairs. New version won overall but regressed on multi-issue tickets;
traced to a dropped instruction, restored it, re-graded — win with no regression.

## Automation opportunities
- Promote a stable rubric + input set into a repeatable suite ([building-llm-evaluations](../building-llm-evaluations/SKILL.md)).
- Gate prompt/model changes on a no-regression check before merge.
- Log production outputs for periodic sampling into the input set.
