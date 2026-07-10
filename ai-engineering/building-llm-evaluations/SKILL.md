---
name: building-llm-evaluations
description: Build an evaluation system for an LLM feature — assemble a representative dataset, pick exact/semantic/LLM-judge/task-specific metrics, run offline and online (A/B) evals, gate releases with regression tests, and track drift. Use when the user says "how do I eval this", "set up evals", "measure LLM quality", "is the new prompt/model better", or "add a regression gate for our AI feature".
---

# Building LLM Evaluations

## Scope
Standing up a repeatable evaluation system for an LLM feature: a versioned
dataset, chosen metrics, offline scoring, online A/B measurement, a CI regression
gate, and drift tracking. Assumes a working feature that now needs to be measured,
compared, and defended over time.

## Purpose
Replace vibes with numbers — know whether a prompt, model, or pipeline change is
better, worse, or noise before it ships, and catch quality regressions and drift
after it ships.

## When to use this skill
- "Set up evals / measure quality / add a regression gate" for an LLM feature.
- Comparing prompts, models, or RAG configs and needing a defensible verdict.
- Deciding whether a change is safe to release, or diagnosing a live quality drop.

## When NOT to use this skill
- Ad-hoc judging of a single output → [evaluating-prompts-and-outputs](../evaluating-prompts-and-outputs/SKILL.md).
- Monitoring pipeline/infra health (latency, throughput, freshness) → [observing-data-pipelines](../../data-engineering/observing-data-pipelines/SKILL.md).
- Iterating the prompt itself → [engineering-prompts](../engineering-prompts/SKILL.md).

## Inputs
- The feature's task, target users, and what "good output" means to them.
- Real usage samples or logs; known failure cases and edge inputs.
- Constraints: labeling budget, latency/cost ceilings, release cadence.

## Outputs
- A versioned eval dataset (golden set + edge/adversarial cases) with references.
- A metric suite and scoring harness producing per-case and aggregate scores.
- A CI regression gate with thresholds, plus an online A/B plan and drift dashboard.

## Workflow
```
Progress:
- [ ] 1. Define the task and what "good" means; pick 3-5 quality dimensions
- [ ] 2. Assemble a representative, stratified dataset with references
- [ ] 3. Choose metrics per dimension; calibrate any LLM judge
- [ ] 4. Build the offline harness; establish a baseline
- [ ] 5. Wire a CI regression gate with thresholds and holdout
- [ ] 6. Run online A/B; track drift and refresh the set over time
```

**Step 1 — Define good.** Write down the task and 3-5 dimensions that matter
(correctness, relevance, format, safety, tone). Vague goals produce vague evals;
tie each dimension to a metric in Step 3.

**Step 2 — Dataset.** Sample from *real* usage, not invented prompts. Stratify by
input type, difficulty, and known failure modes; over-sample edges and adversarial
cases. Version it, hold out a slice CI never sees, and record references/expected
answers. An unrepresentative set is the deepest failure — every later number
inherits its blind spots.

**Step 3 — Metrics.** Match metric to dimension: exact/regex for structured
fields, semantic similarity for meaning, task-specific (BLEU/ROUGE, F1, pass@k,
tool-call accuracy) where apt, LLM-as-judge for open-ended quality. Prefer the
cheapest metric that correlates with human judgment.

**Step 4 — Harness + baseline.** Score the whole set deterministically (fixed
seeds, pinned judge model/prompt). Record the current system as the baseline; every
change is measured against it, not against zero.

**Step 5 — Regression gate.** Put the eval in CI. Fail the build when a key metric
drops beyond a threshold on the holdout. Without this gate, "we'll check later"
means regressions ship silently.

**Step 6 — Online + drift.** Validate offline wins with an A/B test on live
traffic and guardrail metrics. Track scores over time; alert on drift and refresh
the dataset as usage shifts. See [applying-guardrails](../applying-guardrails/SKILL.md)
for the online safety metrics.

## Principles
1. **Representative beats large** — a stratified golden set of real cases outranks
   thousands of synthetic ones.
2. **Multiple metrics, no single number** — a lone score gets gamed; triangulate.
3. **Offline predicts, online decides** — ship on A/B evidence, not offline deltas alone.
4. **Always measure against a baseline,** with a holdout CI never trains or tunes on.
5. **Calibrate the judge** against human labels before trusting it.
6. **Datasets rot** — treat refresh as routine, not a one-time build.

## Decision framework
- **Structured/closed output?** Exact or field-level match; skip the LLM judge.
- **Open-ended quality?** LLM-as-judge, but calibrate and audit it (Common mistakes).
- **Offline win, unsure it's real?** A/B before rollout; small deltas are often noise.
- **Metric plateaued while quality clearly changed?** The metric is wrong — add a dimension.
- **No labeled references?** Start with a small human-labeled golden set before scaling.

## Common mistakes
- **Unrepresentative eval set** — invented or narrow prompts that miss real inputs.
- **Gaming a single metric** — optimizing one number while overall quality drops.
- **LLM-judge bias** — position, verbosity, and self-preference bias; uncalibrated
  against humans; judge and generator from the same family.
- **No regression gate** — evals exist but nothing blocks a merge that regresses.
- **Train/test leakage** — tuning prompts on the same cases used to score.
- **Offline-only** — shipping on offline deltas without an online A/B check.
- **Frozen dataset** — never refreshed, so drift and new failure modes go unseen.

## Validation checklist
- [ ] Dataset sampled from real usage, stratified, versioned, with a CI holdout.
- [ ] Each quality dimension maps to a metric; rationale recorded.
- [ ] Any LLM judge is calibrated against human labels; bias controls in place.
- [ ] Baseline captured; changes reported as deltas with significance, not raw scores.
- [ ] CI gate fails on regression beyond agreed thresholds.
- [ ] Online A/B plan defines primary + guardrail metrics and stop conditions.
- [ ] Drift tracked; dataset-refresh cadence owned.

## Edge cases
- **No ground truth (summaries, chat):** use pairwise LLM-judge or human preference; report win rates, not absolute scores.
- **Rare high-cost failures:** weight or over-sample them; aggregate averages hide tail risk.
- **Non-deterministic outputs:** fix seeds/temperature for eval runs; report variance.
- **Multi-turn/agentic tasks:** score trajectories and task completion, not just the final message ([designing-agent-systems](../designing-agent-systems/SKILL.md)).

## Related skills
- [evaluating-prompts-and-outputs](../evaluating-prompts-and-outputs/SKILL.md), [engineering-prompts](../engineering-prompts/SKILL.md), [applying-guardrails](../applying-guardrails/SKILL.md).
- [detecting-hallucinations](../detecting-hallucinations/SKILL.md), [building-rag-systems](../building-rag-systems/SKILL.md), [designing-agent-systems](../designing-agent-systems/SKILL.md).
- [writing-automated-tests](../../software-engineering/writing-automated-tests/SKILL.md), [observing-data-pipelines](../../data-engineering/observing-data-pipelines/SKILL.md).

## Examples
**Input:** "We rewrote the support-reply prompt — is it actually better?"
**Output:** Built a 120-case set stratified by intent and sampled from real tickets,
with human-rated references and a 30-case holdout. Metrics: field-exact for the
structured tags, LLM-judge (calibrated to human labels, verbosity-controlled) for
reply quality, regex for the required disclaimer. Baseline = current prompt. New
prompt +9% judge score offline; confirmed with a 2-week A/B (CSAT up, escalation
flat). Added a CI gate failing on >3% judge drop; drift dashboard live.

## Automation opportunities
- Run the offline eval on every PR touching prompts, models, or retrieval.
- Schedule dataset refresh from sampled production logs on a fixed cadence.
- Auto-open a regression ticket when the drift alert or CI gate trips.
