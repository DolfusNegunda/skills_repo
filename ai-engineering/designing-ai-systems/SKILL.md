---
name: designing-ai-systems
description: Design production LLM systems end-to-end — pick the pattern (single prompt vs RAG vs agent vs fine-tune), balance quality/latency/cost, add caching and fallbacks, handle failure modes and rate limits, and plan evaluation, monitoring, safety, and iteration. Use when the user asks to "design an LLM feature/system", weigh "RAG vs fine-tune vs agent", "make this AI feature production-ready", or "reduce LLM latency/cost".
---

# Designing AI Systems

## Scope
End-to-end design of a production system built on an LLM: choosing the pattern, sizing
the model, wiring caching/fallbacks/rate-limit handling, and planning evals, monitoring,
safety, and iteration. Not the internals of one sub-component (RAG, agents, evals,
guardrails), and not non-AI architecture.

## Purpose
Turn a fuzzy "add AI here" into a system that hits a quality bar within a latency and
cost budget, degrades gracefully when the model fails, and can be measured and improved
after launch — instead of a clever demo that breaks in production.

## When to use this skill
- "Design an LLM feature/system" or "make this AI feature production-ready."
- Deciding "RAG vs fine-tune vs agent vs a single prompt" for a use case.
- "Reduce LLM latency/cost," add fallbacks/caching, or handle outages and rate limits.

## When NOT to use this skill
- One sub-component: retrieval → [building-rag-systems](../building-rag-systems/SKILL.md); tool-using loops → [designing-agent-systems](../designing-agent-systems/SKILL.md); measurement → [building-llm-evaluations](../building-llm-evaluations/SKILL.md); safety filters → [applying-guardrails](../applying-guardrails/SKILL.md).
- Prompt-level authoring → [engineering-prompts](../engineering-prompts/SKILL.md); context budgeting → [managing-context-windows](../managing-context-windows/SKILL.md).
- Non-AI system architecture → [reviewing-architecture](../../review/reviewing-architecture/SKILL.md).

## Inputs
- The user job to be done, the quality bar, and how success is judged (who accepts output).
- Latency budget, cost ceiling (per request and per month), and expected volume/QPS.
- Data available (docs, labels, examples), privacy/compliance constraints, and integration surface.

## Outputs
- A design: chosen pattern + why, model choice, data/retrieval flow, and the request path.
- Caching, fallback, and rate-limit strategy; an eval plan and monitoring signals; a safety plan.
- A cost/latency estimate and a first iteration plan (ship-measure-improve).

## Workflow
```
Progress:
- [ ] 1. Nail the task, quality bar, and how it's judged
- [ ] 2. Set latency + cost budgets and volume before choosing tech
- [ ] 3. Choose the pattern: prompt → RAG → agent → fine-tune (simplest that clears the bar)
- [ ] 4. Choose model size; decide sync vs async and where caching helps
- [ ] 5. Design failure handling: fallbacks, retries, rate limits, timeouts
- [ ] 6. Plan evals + monitoring; plan safety/guardrails
- [ ] 7. Estimate cost/latency; write the iteration loop
```

**Step 1 — Define the task and bar.** State the one job, an example input/output, and
who accepts the result. Without a measurable bar you cannot compare patterns or know when
you're done. Prefer offline evals for the bar, not vibes.

**Step 2 — Set budgets first.** Fix a p95 latency target, a per-request and monthly cost
ceiling, and expected volume. These constraints, not novelty, pick the pattern and model —
decide them before you fall in love with an architecture.

**Step 3 — Choose the pattern.** Climb the ladder and stop at the first rung that clears
the bar: single prompt → prompt + retrieval (RAG) → tool-using agent → fine-tune. Most
"needs an agent" tasks are a prompt or RAG. See Decision framework.

**Step 4 — Model, sync/async, caching.** Start with the strongest model to prove the bar
is reachable, then step down to the cheapest model that still passes evals. Make it async
when latency budget < model latency; cache aggressively (exact-match, semantic, and
prompt-prefix caching) for repeated or expensive calls.

**Step 5 — Failure handling.** Providers have outages, rate limits, and slow tails. Design
timeouts, bounded retries with backoff+jitter, a fallback model/provider, and a graceful
degraded response. Never let a single upstream 429 or 500 become a user-facing failure.

**Step 6 — Evals, monitoring, safety.** Plan the eval set before building
([building-llm-evaluations](../building-llm-evaluations/SKILL.md)). Log inputs/outputs,
latency, cost, and quality signals; alert on drift and error rate. Add input/output
guardrails ([applying-guardrails](../applying-guardrails/SKILL.md)) for injection, PII, and
unsafe content.

**Step 7 — Estimate and iterate.** Compute tokens × price × volume against the ceiling and
p95 against the budget before building. Ship the simplest version behind the evals, measure
in production, and improve one variable at a time.

## Principles
- **Simplest pattern that clears the bar.** Complexity is a cost; add a rung only when evals demand it.
- **Budgets drive design.** Latency and cost ceilings are requirements, not afterthoughts.
- **The model will fail — design for it.** Fallbacks, timeouts, and degraded modes are part of the design, not add-ons.
- **Evals before scale.** You cannot improve or safely change what you don't measure.
- **Cache the expensive and the repeated.** Retrieval, embeddings, and identical prompts should rarely hit the model twice.
- **Non-determinism is a system property.** Assume variance; constrain with structure, validation, and retries, not hope.

## Decision framework
- **Prompt vs RAG vs agent vs fine-tune?** Knowledge in the model + fits context → single prompt. Needs current/private facts → RAG. Needs multi-step tool use with branching → agent. Needs a fixed style/format or latency/cost cut on a narrow task with lots of labels → fine-tune. Fine-tune last, not first — it can't add fresh knowledge.
- **Model size vs cost?** Prove reachability with the top model, then downshift until evals fail; keep the cheapest passing model. Route easy cases to a small model, hard cases to a big one.
- **Sync vs async?** Interactive and under budget → sync/stream. Over budget, batchable, or long agent loops → async with a job/status resource.
- **Cache vs recompute?** Deterministic or repeated inputs → cache (exact/semantic/prefix). Highly unique inputs → skip and spend the budget on quality.
- **Fallback ladder?** Primary model → retry → cheaper/alt-provider model → cached/templated degraded answer → honest error. Never a single point of failure.

## Common mistakes
- **Jumping to fine-tuning** for a problem a prompt or RAG solves — expensive, slow to iterate, and can't add knowledge.
- **No evals** — shipping on demo vibes, then unable to tell if a change helped or regressed.
- **No fallback for model outages/rate limits** — one 429 or provider blip takes the feature down.
- **Ignoring latency/cost budgets** — a great answer that arrives in 40s or costs $2/call is a failed design.
- **No cost ceiling** — token spend scales with traffic and quietly explodes; set a per-request and monthly cap.
- **Over-engineering an agent** — a multi-tool loop where one prompt would do, adding latency, cost, and failure modes.
- **Trusting model output blindly** — no validation, no guardrails on untrusted input or unsafe output.

## Validation checklist
- [ ] One task, an example I/O, a measurable quality bar, and a named acceptor.
- [ ] p95 latency target and per-request + monthly cost ceiling written down.
- [ ] Pattern is the simplest rung that clears the bar; escalation justified by evals.
- [ ] Model chosen by downshifting from strongest until evals fail; sync/async decided.
- [ ] Caching strategy set; fallback ladder + retries/timeouts + rate-limit handling in place.
- [ ] Eval set exists; monitoring logs quality/latency/cost and alerts on drift.
- [ ] Guardrails for injection/PII/unsafe output; cost/latency estimated against budgets.

## Edge cases
- **Streaming UX:** stream tokens to hide latency, but still enforce output validation before acting on results.
- **Multi-tenant/PII:** isolate caches and prompts per tenant; never leak one user's context via a shared cache key.
- **Provider lock-in:** keep the prompt/interface abstract so a fallback or replacement model is a config change.
- **Bursty traffic:** queue and rate-limit inbound to stay under provider quotas; shed load gracefully.
- **Regulated domains:** log for audit, keep a human in the loop, and prefer extractive/grounded answers over free generation.

## Related skills
- [building-rag-systems](../building-rag-systems/SKILL.md), [designing-agent-systems](../designing-agent-systems/SKILL.md), [building-llm-evaluations](../building-llm-evaluations/SKILL.md) — the sub-components this design composes.
- [applying-guardrails](../applying-guardrails/SKILL.md), [managing-context-windows](../managing-context-windows/SKILL.md), [engineering-prompts](../engineering-prompts/SKILL.md).
- [designing-apis](../../software-engineering/designing-apis/SKILL.md), [optimizing-code-performance](../../software-engineering/optimizing-code-performance/SKILL.md), [reviewing-architecture](../../review/reviewing-architecture/SKILL.md), [analyzing-cost-benefit](../../business/analyzing-cost-benefit/SKILL.md).

## Examples
**Input:** "We want an AI assistant that answers customer questions from our help docs, fast and cheap."
**Output:** Bar: correct, grounded answers judged against 50 labeled Q&A. Budget: p95 < 3s, < $0.01/call. Pattern: RAG (private, changing docs) — not fine-tune. Model: prove with the top model, ship the cheapest that passes evals; stream responses. Caching: cache embeddings and semantic-match repeated questions. Failure: retry → alt model → "I couldn't find that, here's how to reach support." Evals: grounding + accuracy set in CI; monitor cost/latency/deflection. Guardrails: injection filter on retrieved text, PII scrub on logs. Iterate: ship behind evals, tune retrieval first.

## Automation opportunities
- Run the eval suite in CI on every prompt/model/retrieval change; block regressions.
- Dashboard cost, latency (p50/p95), error/fallback rate, and quality signals per release.
- Alert on budget breach, rate-limit spikes, and eval-score drift; auto-fail deploys past a cost ceiling.
