---
name: conducting-structured-reviews
description: Run any review as a repeatable, evidence-based evaluation against explicit criteria — producing scored findings, a severity ranking, and specific recommended fixes rather than opinions. Use when the user asks to "review", "assess", "evaluate", "critique", or "give feedback on" any artifact, or as the foundation for a domain-specific review (code, documents, architecture, etc.). Defines the shared severity taxonomy, scoring scales, and reviewer conduct. Produces a structured, actionable review report.
---

# Conducting Structured Reviews

## Scope
The foundational method every review shares: how to evaluate any artifact against
explicit criteria and produce scored, severity-ranked, actionable findings. Domain
reviews (code, documents, contracts, dashboards, …) inherit this and add their own
rubric. If a domain skill exists, use it *and* this; if not, use this alone.

## Purpose
Turn "what do you think?" into a repeatable evaluation: consistent criteria, a
defensible score, findings ranked by severity, and a concrete fix for each — so any
reviewer produces comparable, trustworthy output.

## When to use this skill
- "Review / assess / evaluate / critique / give feedback on X."
- Any artifact lacking a dedicated domain review skill.
- Establishing a consistent review standard across a team.

## When NOT to use this skill
- A dedicated domain review exists → use it (it inherits this): e.g. [reviewing-code](../reviewing-code/SKILL.md), [reviewing-documents](../reviewing-documents/SKILL.md).
- Creating the artifact → the relevant authoring skill.
- A quick proofread → [proofreading-text](../../office/proofreading-text/SKILL.md).

## Inputs
- The artifact and its purpose/intended audience.
- The standard to judge against (requirements, house style, best practice).
- What the requester wants: gate decision, prioritized fixes, or a score.

## Outputs
- A review report: overall verdict + score, findings ranked by severity (each with
  location, why it matters, and a specific fix), and what's done well.

## Workflow
```
Progress:
- [ ] 1. Establish purpose, audience, and the standard to judge against
- [ ] 2. Choose/confirm the rubric dimensions
- [ ] 3. Inspect systematically against the checklist — collect evidence
- [ ] 4. Classify each finding by severity
- [ ] 5. Score each dimension; derive an overall verdict
- [ ] 6. Write specific, actionable recommendations per finding
- [ ] 7. Note strengths; deliver the report most-severe-first
```

**Step 1 — Standard first.** You cannot review without a bar. Fix the artifact's
purpose, its audience, and the criteria (requirements, spec, house style, or
recognized best practice). A review against no standard is just opinion.

**Step 2 — Rubric.** Confirm the dimensions you'll assess (the domain skill supplies
these; otherwise use: fitness-for-purpose, correctness/accuracy, completeness,
clarity, and risk). Each dimension gets its own findings and score.

**Step 3 — Systematic inspection.** Work the checklist, don't browse. For every
finding, capture **evidence** (a location/quote/example) — findings without evidence
are not credible.

**Step 4 — Severity.** Classify each finding using the shared taxonomy (Blocker /
Major / Minor / Nit / Praise). Severity, not volume, drives attention.

**Step 5 — Score.** Rate each dimension on the shared 1–5 scale; derive an overall
verdict (Approve / Approve-with-changes / Reject). Be consistent, not generous.

**Step 6 — Recommendations.** Every problem gets a specific, actionable fix — "do X"
not "this is weak". A review that only lists faults is half a review.

**Step 7 — Balance & order.** Note genuine strengths, then present findings
most-severe-first so the reader fixes what matters.

## Principles
1. **Criteria before critique.** No standard, no review.
2. **Evidence for every finding.** Cite the location; show, don't assert.
3. **Severity over volume.** One Blocker outweighs ten Nits.
4. **Every finding gets a fix.** Actionable beats accurate-but-useless.
5. **Judge the work, not the author.** Neutral, specific, respectful.
6. **Consistent and repeatable.** Another reviewer using the rubric should agree.

## Decision framework (verdict)
- **Any Blocker?** → Reject / do-not-proceed until resolved.
- **Majors but no Blockers?** → Approve-with-changes (fixes required).
- **Only Minors/Nits?** → Approve (fixes optional/advisory).
- **Unsure of the standard?** → Ask before scoring; don't invent a bar.

## Common mistakes
- **Reviewing without criteria** — produces unfalsifiable opinion.
- **No severity ranking** — reader can't tell critical from cosmetic.
- **Findings without fixes** — problems named, no path forward.
- **No evidence** — "this seems off" the author can't act on.
- **Nitpicking while missing Blockers** — volume mistaken for rigor.
- **Attacking the author** rather than the artifact.
- **Inconsistent scoring** — generous on one, harsh on the next.

## Validation checklist (of your own review)
- [ ] The standard/criteria are stated.
- [ ] Every finding has a location/evidence and a severity.
- [ ] Every problem finding has a specific recommended fix.
- [ ] Dimensions are scored on the 1–5 scale; overall verdict given.
- [ ] Strengths acknowledged.
- [ ] Findings ordered most-severe-first.
- [ ] Tone is neutral and about the work.

## Edge cases
- **Incomplete artifact:** review what exists; flag gaps as findings, don't guess intent.
- **Subjective domains (design, prose):** anchor to principles/heuristics, separate taste from defect.
- **You lack domain expertise:** say so; review what you can verify; flag the rest for a specialist.
- **Conflicting standards:** state which you applied and why.

## Related skills
- Domain reviews inherit this: [reviewing-documents](../reviewing-documents/SKILL.md), [reviewing-code](../reviewing-code/SKILL.md), [reviewing-architecture](../reviewing-architecture/SKILL.md), and the rest in [../README.md](../README.md).
- Reasoning support: [comparing-documents](../../office/comparing-documents/SKILL.md).

## Reference files
- [references/severity-and-scoring.md](references/severity-and-scoring.md) — the shared severity taxonomy, 1–5 scoring scale, and report template all reviews use.

## Examples
**Input:** "Review this onboarding checklist — no dedicated skill for it."
**Output:** Standard set (is it complete, unambiguous, and usable by a new hire on
day one?); dimensions scored; findings — **Major:** step 4 assumes access not yet
granted (fix: add a prerequisite step); **Minor:** two steps out of order; **Nit:**
inconsistent verb tense; **Praise:** clear ownership column. Verdict:
Approve-with-changes. Delivered most-severe-first with a fix on each.

## Automation opportunities
- Standardize the report template so every review is comparable.
- Use the severity taxonomy to gate approvals (no Blocker/Major open → proceed).
- Pair with domain checklists as reusable review rubrics.
