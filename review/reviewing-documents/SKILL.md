---
name: reviewing-documents
description: Review any written document — report, memo, proposal, policy, spec, or article — against clarity, structure, accuracy, completeness, and audience-fit, producing scored, severity-ranked findings with specific fixes. Use when the user asks to "review this document", "give feedback on this doc/report/memo", "critique my writing", or check a document before it ships. Inherits the shared severity/scoring model. Produces an actionable review, not a rewrite.
---

# Reviewing Documents

## Scope
Evaluation of written documents for how well they serve their reader and purpose.
Inherits method, severity, and scoring from
[conducting-structured-reviews](../conducting-structured-reviews/SKILL.md). Not a
rewrite (that's [editing-prose](../../office/editing-prose/SKILL.md)) or a
typo-only pass ([proofreading-text](../../office/proofreading-text/SKILL.md)).

## Purpose
Tell the author, with evidence, whether the document works and exactly what to
change — ranked so they fix what matters first.

## When to use this skill
- "Review / give feedback on / critique this document, report, memo, proposal."
- A quality gate before a document ships to its audience.
- Assessing a draft against a brief or house standard.

## When NOT to use this skill
- Rewrite/restructure it yourself → [editing-prose](../../office/editing-prose/SKILL.md).
- Typos/grammar only → [proofreading-text](../../office/proofreading-text/SKILL.md).
- Domain-specific docs → [reviewing-requirements](../reviewing-requirements/SKILL.md), [reviewing-policies](../reviewing-policies/SKILL.md), [reviewing-business-cases](../reviewing-business-cases/SKILL.md).

## Inputs
- The document, its purpose, intended audience, and any brief/house style.
- The desired outcome: gate decision, prioritized edits, or a score.

## Outputs
- A review report: verdict + per-dimension scores, findings (location + why + fix)
  ranked by severity, and strengths — per the shared template.

## Evaluation rubric (dimensions)
1. **Fitness for purpose** — does it achieve its goal for this audience?
2. **Structure** — logical order; point-first; scannable; sections earn their place.
3. **Clarity** — plain language, unambiguous, no unexplained jargon.
4. **Accuracy** — claims supported; facts, figures, and names correct.
5. **Completeness** — nothing critical missing; no unanswered obvious question.
6. **Concision** — no padding; length matches value.
7. **Tone & correctness** — audience-appropriate register; grammar/consistency.

## Scoring & severity
Score each dimension 1–5 and rank findings Blocker→Praise per
[references in the foundation](../conducting-structured-reviews/references/severity-and-scoring.md).
Domain examples: **Blocker** = a factually wrong claim that misleads a decision;
**Major** = the main point is buried so readers miss it; **Minor** = an unclear
paragraph; **Nit** = inconsistent heading capitalization.

## Workflow
```
Progress:
- [ ] 1. Confirm purpose, audience, and standard
- [ ] 2. Read once for the whole: does it work?
- [ ] 3. Assess each rubric dimension with evidence
- [ ] 4. Classify severity; score dimensions
- [ ] 5. Write specific fixes; note strengths
- [ ] 6. Deliver most-severe-first with a verdict
```

**Step 2** — first read as the target reader: is the message clear, is the ask
obvious? Capture the gestalt before nitpicking. **Step 3** — then work the rubric,
citing locations. **Step 5** — every problem gets a concrete fix ("move the
recommendation to the top", not "improve flow").

## Recommended-improvements guidance
Tie each fix to a dimension and give the move: restructure (reorder/lead with the
point), cut (specific padding), clarify (rewrite the ambiguous sentence), support
(add evidence for the claim), or complete (add the missing section).

## Validation checklist
- [ ] Purpose/audience/standard stated.
- [ ] All seven dimensions assessed with evidence.
- [ ] Findings carry severity + location + a fix.
- [ ] Verdict and per-dimension scores given.
- [ ] Strengths noted; ordered most-severe-first.
- [ ] Feedback is about the document, not the author.

## Common mistakes
- **Line-editing instead of reviewing** — drowning the big structural issue in commas.
- **No verdict** — the author doesn't know if it's ready.
- **Vague feedback** ("tighten this") with no location or fix.
- **Ignoring audience-fit** — judging by your taste, not the reader's need.
- **Missing accuracy checks** — style feedback while a wrong number stands.

## Edge cases
- **Early draft:** review structure and argument; skip line-level polish.
- **Sensitive/political content:** flag risk factually; note tone implications.
- **Specialist content you can't verify:** review clarity/structure; flag facts for an expert.

## Related skills
- [conducting-structured-reviews](../conducting-structured-reviews/SKILL.md) — the method it inherits.
- [editing-prose](../../office/editing-prose/SKILL.md), [proofreading-text](../../office/proofreading-text/SKILL.md), [writing-reports](../../office/writing-reports/SKILL.md).

## Examples
**Input:** "Review this 6-page strategy memo before I send it to the exec team."
**Output:** Verdict: Approve-with-changes (Structure 2/5, Clarity 4/5, Accuracy
4/5). **Major:** recommendation appears on page 5 — execs will miss it; fix: add a
BLUF summary up front. **Minor:** section 3 repeats section 1. **Nit:** figure
labels inconsistent. **Praise:** strong, quantified evidence in section 4.

## Automation opportunities
- Reuse the rubric as a standing pre-send gate for a document type.
- Pair with [editing-prose](../../office/editing-prose/SKILL.md) to apply the accepted fixes.
