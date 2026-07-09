---
name: reviewing-requirements
description: Review requirements, user stories, and specifications for clarity, completeness, testability, consistency, and feasibility — producing severity-ranked findings with specific fixes. Use when the user asks to "review these requirements", "check this spec/user story", "are these testable", or assess requirements before build. Inherits the shared severity/scoring model. Produces an actionable review that prevents ambiguous requirements reaching development.
---

# Reviewing Requirements

## Scope
Evaluation of requirements artifacts — specs, user stories, acceptance criteria,
PRDs — for whether they are clear, complete, and buildable/testable. Inherits
method/severity/scoring from
[conducting-structured-reviews](../conducting-structured-reviews/SKILL.md).
Gathering them is [gathering-requirements](../../business/gathering-requirements/SKILL.md).

## Purpose
Catch ambiguity, gaps, and untestability *before* they reach development, where they
cost far more — turning "the system should be fast" into something a team can build
and verify.

## When to use this skill
- "Review these requirements / this spec / these user stories / this PRD."
- "Are these testable / clear / complete?"
- A gate before requirements enter a sprint or a contract.

## When NOT to use this skill
- Eliciting/writing requirements → [gathering-requirements](../../business/gathering-requirements/SKILL.md).
- Design/architecture → [reviewing-architecture](../reviewing-architecture/SKILL.md).
- General document quality → [reviewing-documents](../reviewing-documents/SKILL.md).

## Inputs
- The requirements and their context (product, users, goals).
- Any standard (INVEST for stories, house template) and known constraints.

## Outputs
- A review: verdict + scores, severity-ranked findings per requirement (what's
  wrong + a rewritten example), and strengths.

## Evaluation rubric (dimensions)
1. **Clarity/unambiguity** — one interpretation only; no vague terms ("fast", "user-friendly", "etc.").
2. **Completeness** — no missing requirement, actor, precondition, or error/edge case.
3. **Testability** — measurable acceptance criteria; you can prove it's met.
4. **Consistency** — no requirements that contradict each other.
5. **Feasibility** — technically and operationally achievable within constraints.
6. **Atomicity/traceability** — one need per requirement; tied to a goal; uniquely identifiable.
7. **Necessity** — solves a real need; no gold-plating or solution-in-disguise.

## Scoring & severity
Score 1–5; rank Blocker→Praise (see
[foundation reference](../conducting-structured-reviews/references/severity-and-scoring.md)).
Examples: **Blocker** = two requirements contradict, or a critical flow is
unspecified; **Major** = "must be fast" with no measurable criterion; **Minor** = a
story bundling two needs; **Nit** = inconsistent ID format.

## Workflow
```
Progress:
- [ ] 1. Confirm context, users, goals, and the standard
- [ ] 2. Test each requirement for clarity and testability
- [ ] 3. Scan the set for gaps, contradictions, and duplication
- [ ] 4. Check feasibility and necessity
- [ ] 5. Severity-rank, score, verdict; rewrite examples per finding
```

**Step 2 — the testability test:** for each requirement ask "how would I prove this
is met?" If you can't, it's not a requirement yet. **Step 3** — completeness and
consistency are set-level, not per-item: hunt for the missing error case and the
pair that conflict.

## Recommended-improvements guidance
Don't just flag "vague" — supply the measurable rewrite ("responds within 2s for
95% of requests under 1k concurrent users"), the missing edge case, or the split of
a compound story into atomic ones.

## Validation checklist
- [ ] Each requirement has one interpretation and a way to test it.
- [ ] Set checked for gaps (actors, preconditions, error/edge cases).
- [ ] No contradictions or duplicates across the set.
- [ ] Feasibility and necessity assessed.
- [ ] Findings carry severity + a concrete rewrite; verdict + scores given.

## Common mistakes
- **Accepting vague terms** ("intuitive", "robust") as requirements.
- **Reviewing item-by-item, missing set-level gaps/conflicts.**
- **No testability check** — unverifiable requirements pass through.
- **Confusing solutions with requirements** ("add a dropdown" vs. the underlying need).

## Edge cases
- **Non-functional requirements:** demand numbers (latency, uptime, throughput).
- **Agile stories:** apply INVEST; acceptance criteria are the testability anchor.
- **Regulatory requirements:** trace each to its obligation; completeness is critical.
- **Early discovery:** flag known unknowns as open questions, not silent gaps.

## Related skills
- [conducting-structured-reviews](../conducting-structured-reviews/SKILL.md), [gathering-requirements](../../business/gathering-requirements/SKILL.md).
- [reviewing-documents](../reviewing-documents/SKILL.md), [reviewing-architecture](../reviewing-architecture/SKILL.md).

## Examples
**Input:** "Review these user stories before sprint planning."
**Output:** Verdict: Approve-with-changes (Testability 2/5). **Blocker:** story 4
("system handles errors gracefully") is untestable; rewrite with specific error
cases + expected behavior. **Major:** no story for the empty-search state. **Minor:**
story 7 bundles export + email; split. **Praise:** clear acceptance criteria on stories 1–3.

## Automation opportunities
- Reuse the rubric as a definition-of-ready gate before sprint intake.
- Flag vague-term keywords ("fast", "easy", "etc.") automatically for human check.
