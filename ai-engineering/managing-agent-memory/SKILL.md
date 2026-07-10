---
name: managing-agent-memory
description: Manage agent state and memory — distinguish short-term (context) from long-term (store) memory, summarize and compact history, decide what to persist and retrieve, and avoid stale or contradictory memory. Use when the user asks to "add memory to my agent", "remember across sessions", compact a growing conversation, or fix an agent that forgets, repeats itself, or acts on outdated facts.
---

# Managing Agent Memory

## Scope
How an agent holds and reuses state: short-term (what's in the context window this turn)
vs long-term (an external store across turns/sessions); summarization/compaction, what to
write and read back, and keeping memory fresh and consistent. Not fitting a single
request in the window, and not retrieval over a document corpus.

## Purpose
Give an agent the right facts at the right time without unbounded growth, staleness, or
contradiction — so it remembers what matters, forgets what doesn't, and never acts on a
fact that's since changed.

## When to use this skill
- "Add memory / remember across sessions / persist state" for an agent.
- A conversation grows past the window and needs summarizing or compaction.
- An agent forgets earlier decisions, repeats work, or acts on stale/contradictory facts.

## When NOT to use this skill
- Fitting one request/prompt in the window → [managing-context-windows](../managing-context-windows/SKILL.md).
- Retrieval over a document corpus → [building-rag-systems](../building-rag-systems/SKILL.md).
- The agent loop, budgets, and termination → [designing-agent-systems](../designing-agent-systems/SKILL.md).

## Inputs
- The agent's task and how long state must live (single run, session, forever).
- What facts recur, change, or must survive restarts; privacy/retention constraints.
- Context-window size and the store available (KV, vector, relational).

## Outputs
- A memory design: what lives short-term vs long-term, and the schema of each.
- Compaction/summarization rules and a write/read (persist/retrieve) policy.
- Freshness/invalidation rules and a retention/privacy plan.

## Workflow
```
Progress:
- [ ] 1. Classify state: ephemeral, session, or durable
- [ ] 2. Split short-term (context) vs long-term (store); pick the store
- [ ] 3. Define what to persist and the retrieval trigger for each
- [ ] 4. Set compaction/summarization rules for growing history
- [ ] 5. Add freshness/invalidation to prevent stale, contradictory memory
- [ ] 6. Test recall, compaction fidelity, and update-then-retrieve
```

**Step 1 — Classify state.** For each piece of state decide its lifetime: ephemeral
(this turn only), session (this run), or durable (across sessions). Most working state is
ephemeral and should never be persisted. Persisting everything is the primary failure
mode — it bloats the store and breeds stale facts.

**Step 2 — Short-term vs long-term.** Short-term memory = the context window: recent
turns, current plan, scratchpad. Long-term = an external store keyed for retrieval. Keep
the window lean; offload durable facts to the store and pull them back on demand. Pick the
store by access pattern: KV for known keys, vector for semantic recall, relational for
structured/queryable facts.

**Step 3 — Persist and retrieve policy.** Write to long-term memory only salient, reusable
facts (user preferences, decisions, entities, outcomes) — not raw transcript. Define the
retrieval trigger for each memory type: by key, by semantic similarity to the current
task, or by recency. Retrieve the minimum relevant; irrelevant memory is noise that
degrades output.

**Step 4 — Compact growing history.** When history nears the window budget, summarize
older turns into a running summary and drop the raw text, preserving decisions, open
threads, and commitments. Compact hierarchically (rolling summary + recent verbatim
turns). Never silently truncate the middle — that drops facts the agent still needs.

**Step 5 — Freshness and consistency.** Timestamp and version memories. On write, resolve
conflicts (new fact supersedes old) rather than appending contradictions. Invalidate or
update facts that change (status, preferences). Prefer the latest authoritative value; when
memory and live data disagree, live data wins. Stale memory acted on as truth is worse
than no memory.

**Step 6 — Test.** Verify recall of a persisted fact in a later session, summary fidelity
after compaction (are decisions preserved?), and the update-then-retrieve path (change a
fact, confirm the new value is returned, not the old).

## Principles
- **Most state is ephemeral.** Persist only salient, reusable facts — not the transcript.
- **Two tiers, kept separate.** Lean context for now; external store for later.
- **Summarize, don't truncate.** Compact old history into decisions and open threads.
- **Retrieve the minimum relevant.** Irrelevant memory is noise, not help.
- **Fresh beats complete.** Version and invalidate; live data outranks stale memory.
- **Resolve conflicts on write.** New facts supersede old — never store contradictions side by side.

## Decision framework
- **Persist this or not?** Reusable across turns/sessions → store; only-this-turn → keep in context, drop after.
- **Which store?** Known key → KV; semantic recall → vector; structured/queryable → relational.
- **Compact or extend context?** History exceeds budget or has stale bulk → compact; still small → extend.
- **Retrieve by key, similarity, or recency?** Exact entity → key; fuzzy relevance → similarity; "recent" → recency.
- **Conflict on write?** Same key, newer/authoritative → overwrite/version; genuinely additive → append.

## Common mistakes
- **Persisting everything** — the store balloons with transcript nobody retrieves.
- **Unbounded context growth** — never compacting until the window overflows and calls fail.
- **Stale memory as truth** — acting on a fact that changed; no invalidation.
- **Contradictory memories** — appending new facts without superseding old ones.
- **Over-retrieval** — dumping all memory into context, drowning the signal.
- **Lossy truncation** — cutting the middle of history and losing decisions/commitments.
- **No retrieval key** — writing memories that can never be found again.

## Validation checklist
- [ ] Each state item classified ephemeral / session / durable.
- [ ] Short-term vs long-term split defined; store chosen per access pattern.
- [ ] Persist policy stores only salient facts; each has a retrieval trigger.
- [ ] Compaction summarizes old history, preserving decisions and open threads.
- [ ] Memories are timestamped/versioned; conflicts resolved on write; stale facts invalidated.
- [ ] Retrieval returns the minimum relevant set.
- [ ] Recall, compaction fidelity, and update-then-retrieve tested.

## Edge cases
- **Multi-agent shared memory:** define ownership and write conflicts; decide what's shared vs private per agent.
- **Privacy/PII:** apply retention limits and redaction; support deletion on request.
- **Concurrent writes:** use versioning/locking so parallel updates don't clobber each other.
- **Cold start:** define behavior with an empty store — don't hallucinate remembered facts.
- **Summary drift:** re-derive summaries from source periodically so compounding errors don't accumulate.

## Related skills
- [managing-context-windows](../managing-context-windows/SKILL.md) — fitting a single request in the window.
- [building-rag-systems](../building-rag-systems/SKILL.md), [designing-vector-search](../designing-vector-search/SKILL.md), [chunking-and-embedding-content](../chunking-and-embedding-content/SKILL.md).
- [designing-agent-systems](../designing-agent-systems/SKILL.md), [integrating-tool-use](../integrating-tool-use/SKILL.md).
- [writing-secure-code](../../software-engineering/writing-secure-code/SKILL.md).

## Examples
**Input:** "My support agent forgets a customer's plan tier between sessions and sometimes quotes their old tier after they upgrade."
**Output:** Durable store keyed by `customer_id` holding `plan_tier` with a timestamp
(relational — structured, queryable). Short-term keeps only the current conversation.
Retrieval by key at session start. On upgrade, overwrite the tier (new supersedes old),
don't append. Retrieval returns just tier + open tickets, not full history. When the CRM
disagrees with memory, CRM wins. Tested: upgrade → next session quotes the new tier.

## Automation opportunities
- Run compaction automatically when context crosses a token threshold.
- Add TTL/versioning in the store layer so staleness is handled centrally, not per-agent.
- Periodically reconcile long-term memory against systems of record to purge drift.
