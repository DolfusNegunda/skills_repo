---
name: detecting-hallucinations
description: Reduce and detect LLM hallucinations — ground answers in retrieved context, require and verify citations, check claims against sources, use self-consistency and abstention, and flag low-confidence output. Use when the user says "it's making things up", "stop the hallucinations", "verify the answer is grounded", "add citations", or "make the model say I don't know".
---

# Detecting Hallucinations

## Scope
Reducing and catching fabricated or ungrounded LLM output: grounding answers in
retrieved context, requiring verifiable citations, checking claims against sources,
applying self-consistency and abstention, and surfacing confidence. Assumes a
feature that must be factually faithful to given sources or reality.

## Purpose
Make the system say what the sources support — and say "I don't know" when they
don't — instead of confidently fabricating facts, quotes, or citations.

## When to use this skill
- "It's making things up / add citations / verify the answer is grounded."
- Building Q&A, summarization, or RAG where faithfulness to sources is required.
- Getting the model to abstain or hedge instead of guessing.

## When NOT to use this skill
- Fact-checking human-written content → [verifying-facts](../../research/verifying-facts/SKILL.md).
- Designing the retrieval layer itself → [building-rag-systems](../building-rag-systems/SKILL.md).
- Judging general output quality → [evaluating-prompts-and-outputs](../evaluating-prompts-and-outputs/SKILL.md).

## Inputs
- The task and its source of truth: retrieved context, a knowledge base, or none.
- Faithfulness bar: how costly a wrong claim is; whether abstention is acceptable.
- Latency/cost budget for verification passes.

## Outputs
- A grounding + citation setup so claims trace to source spans.
- A verification/abstention layer that flags or blocks unsupported claims.
- A faithfulness metric wired into the eval suite.

## Workflow
```
Progress:
- [ ] 1. Classify the task: grounded (has sources) vs open-domain
- [ ] 2. Ground the answer in retrieved context; instruct source-only answering
- [ ] 3. Require citations tied to specific source spans
- [ ] 4. Verify claims against sources; check every citation resolves
- [ ] 5. Add self-consistency and an abstention path for low support
- [ ] 6. Score faithfulness in evals; monitor unsupported-claim rate in prod
```

**Step 1 — Classify.** Grounded tasks answer *from provided sources*; open-domain
lean on parametric memory and hallucinate far more. Prefer converting open-domain
into grounded by retrieving sources first ([building-rag-systems](../building-rag-systems/SKILL.md)).

**Step 2 — Ground.** Feed relevant context and instruct the model to answer only
from it, saying it lacks the information otherwise. Quality of grounding is bounded
by retrieval — thin or off-topic context produces confident guessing.

**Step 3 — Cite.** Require each claim to cite the specific supporting span, not a
vague document reference. Citations that can't be checked are theater; make them
resolvable to exact source text.

**Step 4 — Verify.** Check that cited spans exist and actually support the claim
(string/entailment check, or an LLM verifier prompted with the source). Flag claims
with no supporting span. Fabricated citations — plausible references to text that
doesn't exist or doesn't say that — are the signature failure; catch them here.

**Step 5 — Self-consistency + abstain.** For high-stakes or shaky answers, sample
multiple times and keep only claims that agree; divergence signals invention. Give
the model a real abstention path — "not stated in the sources" must be an acceptable,
rewarded answer, not a failure.

**Step 6 — Measure.** Add a faithfulness/groundedness metric (supported-claim rate,
citation-resolves rate) to evals and monitor unsupported-claim rate in production.
See [building-llm-evaluations](../building-llm-evaluations/SKILL.md).

## Principles
1. **Grounded beats parametric** — answer from retrieved sources, not memory.
2. **Every claim traces to a span** — unverifiable citations don't count.
3. **Abstention is a correct answer** — reward "I don't know" over a confident guess.
4. **Verify, don't trust** — check citations resolve and entail the claim.
5. **Disagreement signals fabrication** — self-consistency exposes invented facts.
6. **Faithfulness ≠ fluency** — confident, well-written text is not evidence of truth.

## Decision framework
- **Sources available?** Ground and cite; forbid outside-knowledge answers.
- **No sources and none retrievable?** Add retrieval first, or hedge and lower confidence.
- **Claim has no supporting span?** Drop it, flag it, or abstain — don't emit it.
- **High-stakes answer?** Self-consistency + verifier pass despite the extra cost.
- **Model won't abstain?** The prompt/rubric penalizes "don't know" — fix the incentive.

## Common mistakes
- **Ungrounded answers** — relying on parametric memory when sources were available.
- **Fabricated citations** — references to nonexistent text, or spans that don't support the claim.
- **Citation theater** — document-level pointers no one can verify against actual text.
- **No abstention path** — the model must answer, so it invents rather than declines.
- **Trusting fluency** — treating a confident, coherent answer as a correct one.
- **Grounding on bad retrieval** — thin/irrelevant context, so the model fills gaps by guessing.
- **Verifying only the happy path** — never testing whether the checker catches a planted false claim.

## Validation checklist
- [ ] Task classified; grounded tasks answer only from provided sources.
- [ ] Each claim cites a specific, resolvable source span.
- [ ] Citations verified to exist and to support the claim; unsupported claims flagged.
- [ ] Abstention path exists and is rewarded, not penalized.
- [ ] Self-consistency applied to high-stakes or low-confidence answers.
- [ ] Faithfulness metric in the eval suite; unsupported-claim rate monitored in prod.
- [ ] Verifier itself tested against planted false claims and bad citations.

## Edge cases
- **Partially supported claims:** the source backs some but not all — split and flag the unsupported part.
- **Conflicting sources:** surface the conflict rather than silently picking one ([assessing-source-credibility](../../research/assessing-source-credibility/SKILL.md)).
- **Summarization drift:** paraphrase that adds unstated implications; check the summary entails only source content.
- **Numeric/quote fidelity:** figures and quotations demand exact-match verification, not semantic similarity.

## Related skills
- [building-rag-systems](../building-rag-systems/SKILL.md), [building-llm-evaluations](../building-llm-evaluations/SKILL.md), [evaluating-prompts-and-outputs](../evaluating-prompts-and-outputs/SKILL.md).
- [applying-guardrails](../applying-guardrails/SKILL.md), [engineering-prompts](../engineering-prompts/SKILL.md), [designing-vector-search](../designing-vector-search/SKILL.md).
- [verifying-facts](../../research/verifying-facts/SKILL.md), [assessing-source-credibility](../../research/assessing-source-credibility/SKILL.md).

## Examples
**Input:** "Our doc-Q&A bot keeps inventing policy details and citing sections that
don't exist."
**Output:** Switched to strict grounding: answers only from retrieved passages,
each sentence citing a passage id. Added a verifier that confirms the cited span
exists and entails the sentence; unsupported sentences are dropped and the bot
abstains when no passage supports the question. Self-consistency (3 samples) on
policy-critical answers. Faithfulness metric (supported-claim + citation-resolves
rate) added to evals; fabricated-citation rate fell to near zero, with abstention
replacing the invented answers.

## Automation opportunities
- Run the citation-resolves and entailment checks inline on every response.
- Gate releases on the faithfulness metric alongside quality scores.
- Alert when production unsupported-claim or abstention rate shifts.
