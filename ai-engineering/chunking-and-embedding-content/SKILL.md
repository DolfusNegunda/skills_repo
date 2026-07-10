---
name: chunking-and-embedding-content
description: Prepare source content for retrieval — split documents into self-contained chunks with the right size and overlap, respect structure, attach metadata, pick an embedding model, and deduplicate. Use when preparing a corpus for a vector index, and the user asks "how should I chunk my docs", "what chunk size", "which embedding model", or "why is retrieval missing obvious answers".
---

# Chunking and Embedding Content

## Scope
Turning raw sources into retrieval-ready chunks and vectors: chunk strategy
(size/overlap/structure-aware), metadata, embedding-model choice, and dedup. Not
the index or query engine ([designing-vector-search](../designing-vector-search/SKILL.md)),
not the end-to-end RAG loop ([building-rag-systems](../building-rag-systems/SKILL.md)).

## Purpose
Produce chunks that each stand alone, carry enough context to answer a query, embed
with a model matched to the domain and query style, and don't flood the index with
near-duplicates.

## When to use this skill
- "How should I chunk these docs / what chunk size and overlap?"
- "Which embedding model should I use?" / domain-specific or multilingual corpus.
- "Retrieval misses obvious answers" traced to bad splits or lost context.
- Re-ingesting after documents changed; standing up a new corpus.

## When NOT to use this skill
- Index type, recall/latency, hybrid search → [designing-vector-search](../designing-vector-search/SKILL.md).
- Orchestrating ingest→retrieve→generate → [building-rag-systems](../building-rag-systems/SKILL.md).
- Source-format parsing/ETL at scale → [building-batch-transformations](../../data-engineering/building-batch-transformations/SKILL.md).

## Inputs
- The corpus: formats (PDF/HTML/Markdown/code), average length, structure, update cadence.
- Expected query style (short keyword vs full question) and language(s).
- Target index's vector dimensions/limits and any embedding-model constraints (cost, on-prem).

## Outputs
- Chunks with stable IDs, source metadata, and self-contained text.
- A chosen embedding model + its dimension; the chunking config (size/overlap/rule).
- A dedup pass report and re-embedding plan for changed sources.

## Workflow
```
Progress:
- [ ] 1. Inspect content shape; pick a structure-aware split boundary
- [ ] 2. Set chunk size + overlap for the query style and model window
- [ ] 3. Make each chunk self-contained (titles, headings, context prefix)
- [ ] 4. Attach metadata (source, section, timestamps, permissions)
- [ ] 5. Choose an embedding model; embed queries and chunks the same way
- [ ] 6. Deduplicate; verify with sample queries; plan re-embedding
```

**Step 1 — Split on structure, not bytes.** Break on natural boundaries first:
Markdown/HTML headings, code by function/class, transcripts by speaker turn. Only
fall back to fixed-size windows within a section. Blind character splitting cuts
sentences and separates a claim from its qualifier.

**Step 2 — Size and overlap.** Target ~200–500 tokens for prose Q&A; smaller for
dense facts, larger for narrative. Add 10–20% overlap so a boundary doesn't orphan
the answer. Too big dilutes the embedding and buries the match; too small loses the
context that makes a chunk answerable.

**Step 3 — Self-contained.** Prefix each chunk with its document title and section
path so an isolated chunk still reads unambiguously. Resolve pronouns/"it"/"the
above" that point outside the chunk. A chunk retrieved alone must answer on its own.

**Step 4 — Metadata.** Attach source URI, section, author, created/updated
timestamps, language, and access scope — these drive filtering and citation
downstream. Missing metadata means no filtering and unciteable answers.

**Step 5 — Embedding model.** Match the model to domain (general vs code/legal/bio),
languages, and query length; check the asymmetric case (short query vs long
passage) and use the model's query/passage instructions if it has them. Embed
queries with the **same** model and normalization as chunks — a mismatch destroys
similarity silently.

**Step 6 — Dedup and refresh.** Drop near-duplicate chunks (boilerplate, repeated
headers) via cosine threshold or hashing. Track content hashes so only changed
sources are re-embedded, and re-embed everything when you switch models.

## Principles
- Chunk on meaning: one chunk = one coherent, self-answering idea.
- A chunk must stand alone — assume it arrives with no neighbors.
- Query and chunk embeddings must come from the identical model + preprocessing.
- Metadata is part of the chunk, not an afterthought.
- Overlap buys boundary safety cheaply; duplicates cost recall and money.

## Decision framework
- **Fixed-size vs structure-aware:** structured docs → split on headings/code units; unstructured stream → fixed window + overlap.
- **Small vs large chunks:** precise fact lookup → smaller; reasoning over context → larger; when unsure, test both against real queries.
- **General vs domain embedding model:** jargon-heavy/code/multilingual → domain or larger model; generic English → a strong general model is fine.
- **Overlap amount:** self-contained sections → little; dense continuous prose → more (15–20%).
- **Re-embed vs incremental:** model change → re-embed all; content edit → re-embed only changed hashes.

## Common mistakes
- **Byte/character splitting** that severs sentences and separates claim from context.
- **Chunks too big** — the true match is diluted by surrounding noise.
- **Chunks too small** — the answer is split across two chunks, neither sufficient.
- **No overlap** — the answer straddles a boundary and is never fully retrieved.
- **Query/chunk model mismatch** or different normalization — silent recall collapse.
- **Stripping structure** (headings, titles) so chunks lose their context anchor.
- **No metadata** — cannot filter, cannot cite, cannot enforce access.
- **Never re-embedding** after a model or content change → stale vectors.

## Validation checklist
- [ ] Splits follow document structure; no mid-sentence cuts.
- [ ] Chunk size/overlap tuned to query style and validated on sample queries.
- [ ] Each chunk reads self-contained (title/section prefix; no dangling references).
- [ ] Metadata (source, section, timestamps, access) attached to every chunk.
- [ ] Same embedding model + preprocessing for queries and chunks; dimension matches the index.
- [ ] Near-duplicates removed; content hashes tracked for incremental re-embedding.

## Edge cases
- **Tables/code:** keep a table or function whole; splitting mid-structure destroys meaning.
- **Very long documents:** two-level chunking (section summaries + detail chunks).
- **Multilingual corpus:** a multilingual model, or embed per language; don't mix silently.
- **Frequently updated sources:** hash-based change detection to avoid full re-embeds.
- **Access-controlled content:** carry permission metadata so filtering can enforce it at query time.

## Related skills
- [designing-vector-search](../designing-vector-search/SKILL.md) — indexing and querying the vectors you produce.
- [building-rag-systems](../building-rag-systems/SKILL.md) — the full ingest→retrieve→generate pipeline.
- [governing-data-and-lineage](../../data-engineering/governing-data-and-lineage/SKILL.md) — provenance and access for source content.

## Examples
**Input:** "We chunk our handbook every 1000 characters and retrieval is flaky."
**Output:** Switch to heading-based sections (~300 tokens, 15% overlap), prefix each
chunk with `Doc > Section` for context, attach section + updated-at metadata, and
embed queries and chunks with the same model. Dedup repeated page headers. Re-test
on 20 real questions before re-indexing the whole corpus.

## Automation opportunities
- Make ingestion idempotent: hash content, re-embed only changed chunks.
- Assert chunk-size distribution and dimension in CI; fail on out-of-range chunks.
- Log the embedding model + config with each batch so query-time can detect mismatch.
