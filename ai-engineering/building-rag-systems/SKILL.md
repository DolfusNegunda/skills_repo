---
name: building-rag-systems
description: Build retrieval-augmented generation end-to-end — ingest and chunk sources, embed and index, retrieve and rerank, assemble grounded context, cite sources, and evaluate retrieval and answer quality. Use when the task is to "build a RAG system", "chat over my documents", "ground answers in our knowledge base", "reduce hallucinations with retrieval", or "answer from these sources".
---

# Building RAG Systems

## Scope
End-to-end retrieval-augmented generation: the pipeline from source documents to a
grounded, cited answer. Orchestrates the sub-skills — chunking/embedding, vector
search, prompting, and grounding — into one working system. Not the chunking details
alone ([chunking-and-embedding-content](../chunking-and-embedding-content/SKILL.md))
or the index internals ([designing-vector-search](../designing-vector-search/SKILL.md)).

## Purpose
Answer questions from a specific corpus so responses are grounded in retrieved
evidence and cite their sources — trading the model's fuzzy parametric memory for
verifiable, updatable, permission-aware knowledge.

## When to use this skill
- "Build a RAG pipeline / chat over our docs / Q&A on a knowledge base."
- "Ground the model's answers in our data", "answer only from these sources".
- Knowledge that changes often, is private, or must be cited rather than memorized.

## When NOT to use this skill
- Just the chunking/embedding step → [chunking-and-embedding-content](../chunking-and-embedding-content/SKILL.md).
- Just the index/search layer → [designing-vector-search](../designing-vector-search/SKILL.md).
- No external knowledge needed (pure reasoning/format task) → [engineering-prompts](../engineering-prompts/SKILL.md).
- Teaching the model a new *skill/style* rather than facts → fine-tuning, not RAG.

## Inputs
- The source corpus (formats, size, update cadence, access/permission rules).
- The question types and who asks them; latency, cost, and accuracy targets.
- Ground-truth Q&A pairs (or the means to create them) for evaluation.

## Outputs
- A pipeline: ingest → chunk → embed → index → retrieve → rerank → generate → cite.
- Grounded answers with source citations, plus retrieval and answer-quality metrics.

## Workflow
```
Progress:
- [ ] 1. Define the questions, sources, and an eval set of Q&A pairs
- [ ] 2. Ingest + chunk sources (structure-aware, with metadata)
- [ ] 3. Embed + index; carry permissions/metadata for filtering
- [ ] 4. Retrieve top-k; add hybrid search + a reranker
- [ ] 5. Assemble grounded context; prompt to answer ONLY from it and cite
- [ ] 6. Evaluate retrieval (recall/precision) and answers (grounding/quality); iterate
```

**Step 1 — Define + measure first.** Write real questions and expected answers before
building; you cannot tune retrieval you cannot score. See
[building-llm-evaluations](../building-llm-evaluations/SKILL.md).

**Step 2 — Ingest + chunk.** Parse each source faithfully and chunk structure-aware,
keeping chunks self-contained with source metadata (title, section, URL, permissions).
See [chunking-and-embedding-content](../chunking-and-embedding-content/SKILL.md).

**Step 3 — Embed + index.** Embed with a model matched to the query language/domain;
store metadata for filtering. See [designing-vector-search](../designing-vector-search/SKILL.md).

**Step 4 — Retrieve + rerank.** Retrieve top-k, combine dense + keyword (hybrid) so
exact terms/IDs aren't missed, then rerank with a cross-encoder and keep the top few.
Retrieval quality caps everything downstream — a great prompt cannot fix bad context.

**Step 5 — Generate grounded + cited.** Put retrieved chunks in context; instruct the
model to answer **only** from them, cite each claim, and say "not in the sources" when
absent. See [engineering-prompts](../engineering-prompts/SKILL.md) and
[detecting-hallucinations](../detecting-hallucinations/SKILL.md).

**Step 6 — Evaluate + iterate.** Measure retrieval (is the answer chunk in top-k?) and
answers (grounded? correct? cited?) separately, so you fix the right stage.

## Principles
1. **Retrieval quality is the ceiling** — fix retrieval before prompt-tuning.
2. **Ground and cite** — every claim traces to a retrieved chunk, or is withheld.
3. **Evaluate retrieval and generation separately** — they fail for different reasons.
4. **Chunks must stand alone** — retrieved out of context, each must still make sense.
5. **Carry permissions through** — filter by access at retrieval, not after generation.
6. **Keep the corpus fresh** — re-index on change; stale answers erode trust.

## Decision framework
- **Missing exact terms/IDs/codes?** Add keyword/hybrid search alongside dense.
- **Right docs retrieved but wrong order?** Add a reranker before trimming to top-k.
- **Answers ungrounded despite good retrieval?** Tighten the prompt; enforce citation; lower k to reduce distraction.
- **Recall low?** Revisit chunking (too big/small) and the embedding model, not the LLM.
- **Huge/!low-latency corpus?** Pre-filter by metadata; cache frequent queries.
- **RAG vs long-context stuffing?** Corpus bigger than the window, changing, or permissioned → RAG.

## Common mistakes
- **Tuning the prompt to fix a retrieval problem** — the evidence never arrived.
- **One giant vague chunk or hundreds of tiny ones** — both wreck retrieval.
- **Dense-only search** missing exact identifiers, names, or error codes.
- **No reranking** — top-k by raw similarity buries the best passage.
- **No citations / no abstention** — the model fills gaps by inventing.
- **Ignoring permissions** — retrieving documents a user may not see.
- **Evaluating end-to-end only** — can't tell if retrieval or generation failed.
- **Stale index** — answering from documents that changed or were deleted.

## Validation checklist
- [ ] An eval set of real Q&A exists; retrieval and answer quality scored separately.
- [ ] Chunks are self-contained and carry source + permission metadata.
- [ ] Hybrid (dense + keyword) retrieval with a reranker is in place.
- [ ] The prompt forces answers grounded in context, with citations and abstention.
- [ ] Access control is enforced at retrieval time.
- [ ] Re-indexing on source change is defined; no stale content served.

## Edge cases
- **Multi-hop questions:** retrieve iteratively or decompose; one pass rarely suffices.
- **Tables/figures:** extract structure; embed a text description alongside.
- **Conflicting sources:** surface both with citations; prefer the most recent/authoritative.
- **No relevant chunk:** answer "not found in sources," never fabricate.
- **Very long documents:** chunk hierarchically; retrieve section then passage.

## Related skills
- [chunking-and-embedding-content](../chunking-and-embedding-content/SKILL.md), [designing-vector-search](../designing-vector-search/SKILL.md) — the retrieval building blocks.
- [engineering-prompts](../engineering-prompts/SKILL.md), [managing-context-windows](../managing-context-windows/SKILL.md), [detecting-hallucinations](../detecting-hallucinations/SKILL.md) — grounded generation.
- [building-llm-evaluations](../building-llm-evaluations/SKILL.md) — scoring the system; [designing-ai-systems](../designing-ai-systems/SKILL.md) — where RAG fits.
- [governing-data-and-lineage](../../data-engineering/governing-data-and-lineage/SKILL.md), [assessing-source-credibility](../../research/assessing-source-credibility/SKILL.md).

## Examples
**Input:** "Build Q&A over our policy handbook; answers must cite the policy."
**Output:** Chunked by section (heading + clause) with doc/section metadata; hybrid
retrieval + cross-encoder rerank to top-4; prompt answers only from context, cites
`[doc §]`, and abstains when absent; eval set of 50 HR questions scores retrieval
recall@4 and answer groundedness. Fixed low recall by shrinking oversized chunks —
not by editing the prompt.

## Automation opportunities
- Re-index on source change via the ingestion pipeline ([building-batch-transformations](../../data-engineering/building-batch-transformations/SKILL.md)).
- Run the retrieval + answer eval in CI to catch regressions on corpus or prompt changes.
- Log retrieved chunks with each answer for auditing and offline evaluation.
