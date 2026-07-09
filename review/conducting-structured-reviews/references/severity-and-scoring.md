# Severity Taxonomy & Scoring

The shared rating system every review in this category uses. Domain reviews add
their own rubric dimensions but rank and score with these scales.

## Contents
- Severity taxonomy
- Dimension scoring scale (1–5)
- Overall verdict
- Report template

## Severity taxonomy

| Severity | Meaning | Action |
|---|---|---|
| **Blocker** | Wrong, unsafe, or unfit for purpose; ships harm or fails the goal. | Must fix before proceeding. |
| **Major** | Significant defect degrading quality/correctness/usability. | Should fix before approval. |
| **Minor** | Real issue but limited impact; work is usable without it. | Fix when convenient. |
| **Nit** | Cosmetic/preference; no functional impact. | Optional; author's discretion. |
| **Praise** | Something done well, worth keeping/repeating. | Acknowledge; don't "fix". |

Rank by severity, not count. One Blocker outranks any number of Nits. Label each
finding explicitly so the reader triages in seconds.

## Dimension scoring scale (1–5)

Apply per rubric dimension (e.g. correctness, clarity, completeness):

| Score | Label | Meaning |
|---|---|---|
| 5 | Excellent | Meets and exceeds the standard; a model example. |
| 4 | Good | Meets the standard; minor improvements possible. |
| 3 | Adequate | Acceptable; some Minor/Major issues to address. |
| 2 | Weak | Below standard; Major issues; needs rework. |
| 1 | Poor | Fails the standard; Blockers present. |

Score against the *standard*, not relative to expectations of the author. Be
consistent across reviews so scores are comparable.

## Overall verdict

Derive from the findings, not an average:
- **Reject / Do not proceed** — any Blocker open.
- **Approve with changes** — Majors present, no Blockers; list required fixes.
- **Approve** — only Minors/Nits; note advisory improvements.

State the verdict up front, then the evidence.

## Report template

```
REVIEW: [artifact]
Standard applied: [requirements / house style / best practice]
Verdict: [Approve | Approve with changes | Reject]
Scores: [dimension: n/5, ...]

Findings (most severe first)
[SEVERITY] [dimension] — [what], at [location/evidence].
   Fix: [specific action].
...

Strengths
- [what to keep]
```

Keep findings one line of problem + one line of fix. Group by severity or list in
strict severity order.
