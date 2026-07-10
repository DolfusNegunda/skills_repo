---
name: designing-vector-search
description: Design the vector search layer — choose an index (HNSW/IVF/flat), tune recall against latency, filter by metadata, combine vector with keyword search (hybrid), rerank the shortlist, and measure retrieval quality with recall@k and nDCG. Use when the user asks "which vector index", "why is search slow / missing results", "how do I add filters", or "should I add hybrid search or reranking".
---

# Designing Vector Search

## Scope
The retrieval engine over an existing set of embeddings: index choice, recall/latency
tuning, metadata filtering, hybrid (vector + keyword) fusion, reranking, MMR, and
retrieval evaluation. Not producing the vectors ([chunking-and-embedding-content](../chunking-and-embedding-content/SKILL.md)),
not the generation loop ([building-rag-systems](../building-rag-systems/SKILL.md)).

## Purpose
Return the right chunks for a query fast enough for the product, with filtering and
reranking that lift precision, and metrics that prove the retrieval layer is good
before anyone blames the model.

## When to use this skill
- "Which vector index / HNSW vs IVF vs flat?" / "how do I scale to N vectors?"
- "Search is slow" or "search misses obvious results" — a recall/latency/tuning issue.
- "Add metadata filters", "add keyword/hybrid search", "add reranking".
- Measuring retrieval quality (recall@k, MRR, nDCG) or debugging a regression.

## When NOT to use this skill
- Chunk size, overlap, embedding-model choice → [chunking-and-embedding-content](../chunking-and-embedding-content/SKILL.md).
- Grounded prompting, citation, answer-quality eval → [building-rag-systems](../building-rag-systems/SKILL.md).
- General service latency/throughput tuning → [optimizing-code-performance](../../software-engineering/optimizing-code-performance/SKILL.md).

## Inputs
- Vector count and growth, dimension, and the distance metric the embedding expects.
- Latency/QPS budget and recall target; memory/cost ceiling.
- Metadata fields to filter on; whether exact keyword matching also matters.
- A labeled query→relevant-chunk set (even a small one) for evaluation.

## Outputs
- An index choice + build/query parameters, with the recall/latency tradeoff stated.
- Filtering, hybrid-fusion, and reranking configuration.
- Retrieval metrics (recall@k, nDCG, MRR) on a held-out query set.

## Workflow
```
Progress:
- [ ] 1. Set recall target, latency budget, and scale; confirm the distance metric
- [ ] 2. Choose an index type (flat / HNSW / IVF) for that point
- [ ] 3. Tune build/query params to the recall–latency curve
- [ ] 4. Add metadata filtering; decide pre- vs post-filter
- [ ] 5. Add hybrid (keyword + vector) fusion where lexical matches matter
- [ ] 6. Rerank the shortlist; measure recall@k / nDCG on a held-out set
```

**Step 1 — Fix the operating point.** Write down the recall target, the p95 latency
budget, and the vector count. These, not fashion, pick the index. Confirm the metric
(cosine/dot/L2) matches how the vectors were normalized — a mismatch returns garbage.

**Step 2 — Index type.** Small (<~50k) or accuracy-critical → **flat** (exact,
brute force). Large with tight latency → **HNSW** (fast, high recall, higher memory).
Very large / memory-bound → **IVF** (or IVF-PQ) trading recall for footprint.

**Step 3 — Tune the curve.** HNSW: raise `ef_search` (and build `M`/`ef_construction`)
for recall at the cost of latency. IVF: raise `nprobe` for recall, lower for speed;
size `nlist` to the corpus. Sweep the parameter and plot recall vs latency — pick the
knee, don't guess.

**Step 4 — Metadata filtering.** Filter by tenant, date, language, access scope.
Prefer an engine with **native filtered ANN**; naive post-filtering can empty a
top-k, and pre-filtering a huge set can be slow. Enforce access-control filters here.

**Step 5 — Hybrid search.** When exact terms matter (names, codes, rare tokens),
run BM25/keyword alongside vector and fuse (e.g. Reciprocal Rank Fusion). Pure vector
misses exact-match queries; pure keyword misses paraphrases — hybrid covers both.

**Step 6 — Rerank and measure.** Over-retrieve (top 50–100), then reorder with a
**cross-encoder reranker** for precision; use **MMR** when results are redundant and
diversity helps. Report recall@k, nDCG, and MRR on a labeled set; re-run on every
index or param change.

## Principles
- The recall/latency/cost triangle is the whole game — state the target first.
- Retrieve wide, then rerank narrow: cheap ANN for recall, cross-encoder for precision.
- Filtering is a first-class query concern (correctness and access), not a bolt-on.
- Measure retrieval separately from generation, or you can't localize failures.
- The distance metric must match the embedding's training/normalization.

## Decision framework
- **Flat vs HNSW vs IVF:** tiny/exact → flat; low-latency at scale → HNSW; memory-bound at huge scale → IVF/IVF-PQ.
- **Recall vs latency:** raise `ef_search`/`nprobe` for recall, lower for speed — tune to the p95 budget.
- **Pre- vs post-filter:** highly selective filter → pre-filter; low selectivity → filtered ANN or post-filter with over-fetch.
- **Vector vs hybrid:** exact tokens/IDs/rare terms matter → hybrid; pure semantic paraphrase → vector may suffice.
- **Rerank or not:** precision@k matters and shortlist is affordable → cross-encoder rerank; latency-critical bulk → skip.
- **MMR:** results redundant / need coverage → MMR; single best fact → plain top-k.

## Common mistakes
- **No recall target** — "make it fast" with no accuracy floor, or vice versa.
- **Metric mismatch** (cosine index on un-normalized dot-product vectors) → wrong neighbors.
- **HNSW `ef_search` left at default** — silently low recall on hard queries.
- **Post-filtering after top-k** returns fewer (or zero) results than expected.
- **No hybrid** — exact-match queries (SKUs, error codes, names) miss entirely.
- **No reranking** — top ANN hits are approximately relevant but poorly ordered.
- **Stale index** — new/updated content not indexed, so it's never retrievable.
- **Evaluating only end-to-end** — can't tell a retrieval miss from a generation miss.

## Validation checklist
- [ ] Recall target, latency budget, and scale written down; index chosen to match.
- [ ] Distance metric matches embedding normalization.
- [ ] Build/query params tuned on a recall–latency sweep, not defaults.
- [ ] Metadata + access filters correct; pre/post-filter behavior verified (no empty top-k).
- [ ] Hybrid fusion added where exact matches matter; reranking on the shortlist.
- [ ] recall@k / nDCG / MRR measured on a held-out query set; index freshness monitored.

## Edge cases
- **Multi-tenant:** partition or hard-filter by tenant; never leak across tenants.
- **High update rate:** choose an index/engine that supports incremental upserts and deletes.
- **Very high dimensions:** consider dimensionality reduction or PQ to control memory.
- **Cold-start with no labels:** bootstrap eval with a handful of hand-labeled queries; grow from logs.
- **Duplicated corpus:** near-duplicate hits crowd the top-k — apply MMR or dedup upstream.

## Related skills
- [chunking-and-embedding-content](../chunking-and-embedding-content/SKILL.md) — producing the vectors and metadata this layer serves.
- [building-rag-systems](../building-rag-systems/SKILL.md) — consuming retrieval in a grounded-generation loop.
- [optimizing-code-performance](../../software-engineering/optimizing-code-performance/SKILL.md) — broader latency/throughput work.

## Examples
**Input:** "10M chunks, p95 under 100ms, but users say search misses exact error codes."
**Output:** HNSW for the latency budget; add BM25 + vector via RRF so error codes
match lexically; over-fetch top 100 and cross-encoder rerank to top 5; pre-filter by
tenant and product version. Sweep `ef_search` to hit the recall knee under 100ms, and
report recall@10 / nDCG on a labeled query set before and after.

## Automation opportunities
- Add a recall@k / nDCG regression gate in CI on every index or param change.
- Alert on index freshness lag (unindexed new content) and on p95 latency drift.
- Log per-query retrieval scores to build a labeled eval set from real traffic.
