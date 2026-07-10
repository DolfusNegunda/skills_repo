---
name: managing-context-windows
description: Fit the right information into a limited context window — budget tokens, select and order what matters, compact or summarize history, chunk long inputs, and avoid lost-in-the-middle and context rot. Use when input is "too long for the context", "hitting token limits", "the model ignores the middle", "truncating my prompt", or costs/latency climb with prompt size.
---

# Managing Context Windows

## Scope
Deciding what goes into a single model call and in what order: token budgeting,
selection, ordering, compaction, and chunking of oversized inputs. The per-request
context discipline — not corpus retrieval
([building-rag-systems](../building-rag-systems/SKILL.md)) or cross-session memory
([managing-agent-memory](../managing-agent-memory/SKILL.md)).

## Purpose
Get the highest-value information into the window at the lowest token cost, positioned
where the model actually uses it — so answers stay accurate as inputs grow and cost
and latency stay controlled.

## When to use this skill
- "Input is too long / exceeds the context / hitting the token limit."
- "The model ignores details in the middle of a long prompt."
- Long chat histories, big documents, or many retrieved chunks to fit in one call.
- Prompt-size-driven cost or latency needs cutting.

## When NOT to use this skill
- Selecting *which documents* to fetch from a corpus → [building-rag-systems](../building-rag-systems/SKILL.md).
- Persisting state across sessions → [managing-agent-memory](../managing-agent-memory/SKILL.md).
- Wording of the instruction itself → [engineering-prompts](../engineering-prompts/SKILL.md).

## Inputs
- The candidate content (instructions, history, documents, retrieved chunks, tools).
- The model's context limit and your token/cost/latency budget.
- What the task actually needs vs. what is merely available.

## Outputs
- A context assembled within budget: essential content selected, ordered for use, with
  history compacted and oversized inputs chunked — plus what was dropped and why.

## Workflow
```
Progress:
- [ ] 1. Set a token budget (leave headroom for the response)
- [ ] 2. Rank candidate content by relevance to THIS request
- [ ] 3. Select the essential; drop or defer the rest
- [ ] 4. Compact what stays (summarize history, trim boilerplate)
- [ ] 5. Order for salience (critical items at start and end)
- [ ] 6. If still over budget, chunk and process iteratively; verify nothing vital was cut
```

**Step 1 — Budget.** Know the limit; reserve tokens for the output. Treat context as a
scarce resource with a ceiling, not a bucket to fill.

**Step 2–3 — Rank + select.** Include only what changes the answer. More context is not
better — irrelevant filler dilutes attention and raises cost ("context rot").

**Step 4 — Compact.** Summarize old turns, strip repeated boilerplate, keep decisions
and open threads. Replace raw dumps with distilled facts.

**Step 5 — Order for salience.** Models attend most to the **start and end** and can
miss the middle ("lost in the middle"). Put the instruction and the most critical
evidence at the edges; bury nothing important mid-prompt.

**Step 6 — Chunk if needed.** When content genuinely can't fit, split and process in
passes (map-reduce/refine), then combine — and confirm the split didn't drop essentials.

## Principles
1. **Context is a budget, not a bucket** — every token competes and costs.
2. **Relevance over volume** — less, sharper context beats more, noisier context.
3. **Position matters** — exploit the start and end; distrust the middle.
4. **Compact, don't truncate blindly** — summarize to keep meaning, not just cut length.
5. **Preserve the essential** — instructions, constraints, and the actual question survive any trim.

## Decision framework
- **Over budget?** Cut lowest-relevance first; compact next; chunk only as a last resort.
- **Long chat history?** Summarize older turns; keep recent turns verbatim + key decisions.
- **Many retrieved chunks?** Rerank and keep the top few; more chunks ≠ better answers.
- **One huge document?** Chunk + map-reduce, or retrieve the relevant sections instead.
- **Critical instruction being ignored?** Move it to the very start or end; restate briefly at the end.

## Common mistakes
- **Stuffing the window "just in case"** — dilutes attention, raises cost, invites context rot.
- **Burying the key instruction/evidence in the middle** of a long prompt.
- **Truncating from the top/bottom blindly** — silently dropping the instruction or the question.
- **Never summarizing history** — the conversation grows until it breaks or drifts.
- **Ignoring output headroom** — no room left for the model to answer.
- **Equating a big window with "no need to manage"** — quality and cost still degrade with bloat.

## Validation checklist
- [ ] Total tokens are within budget, with headroom reserved for the response.
- [ ] Only content relevant to this request is included; filler removed.
- [ ] The instruction and most critical evidence sit at the start and/or end.
- [ ] Long history is summarized; decisions and open items preserved.
- [ ] Oversized inputs are chunked; nothing essential was dropped in the split.
- [ ] Cost/latency are acceptable for the value delivered.

## Edge cases
- **Very large context models:** still curate — accuracy and cost degrade with bloat.
- **Structured/tabular input:** compress to the needed rows/columns, not the whole table.
- **Multi-turn tool output:** keep results, drop verbose intermediate logs.
- **Hard limit mid-task:** checkpoint a summary, continue in a fresh window.
- **Latency-critical path:** smaller focused context beats a maximal one.

## Related skills
- [engineering-prompts](../engineering-prompts/SKILL.md) — wording within the budget you set here.
- [building-rag-systems](../building-rag-systems/SKILL.md) — choosing what to retrieve into context.
- [managing-agent-memory](../managing-agent-memory/SKILL.md) — state across turns/sessions.
- [designing-ai-systems](../designing-ai-systems/SKILL.md) — cost/latency budgets at system level.

## Examples
**Input:** "This 80-page report won't fit and the model misses key numbers."
**Output:** Retrieve/keep only the sections the question needs; summarize the rest to
a few bullet facts; place the question and the target figures at the start and end of
the prompt; process the remaining long tail in a map-reduce pass. Result fits budget,
key numbers land in high-attention positions, and cost drops versus stuffing all 80 pages.

## Automation opportunities
- Add a token-budget check that trims/summarizes context before each call.
- Auto-summarize chat history past a threshold, retaining decisions and open items.
- Log dropped content so retrieval/compaction choices can be audited and tuned.
