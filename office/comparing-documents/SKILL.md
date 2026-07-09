---
name: comparing-documents
description: Compare two versions of a document and report the material changes — additions, deletions, edits, and moved sections — separating substantive changes from cosmetic ones. Use when the user asks to "compare these documents", "what changed between these versions", "diff these files/contracts", "redline this", or review edits between drafts. Works for Word, PDF, text, and contracts. Produces a clear, prioritized change summary, not a raw character diff.
---

# Comparing Documents

## Scope
Version comparison: identifying and explaining what changed between two documents
and why it matters. Covers Word, PDF, plain text, and contracts. Not creating a
tracked-changes workflow (that's [authoring-word-documents](../authoring-word-documents/SKILL.md))
and not proofreading a single version (that's [proofreading-text](../proofreading-text/SKILL.md)).

## Purpose
Give a reviewer a trustworthy, prioritized account of what changed — surfacing the
substantive edits and separating them from formatting noise — so nothing material
slips through.

## When to use this skill
- "Compare / diff these two documents or versions."
- "What changed between v1 and v2?" / "Redline this contract."
- Reviewing edits between drafts before approval or signature.
- Confirming a supposedly-minor edit didn't change meaning.

## When NOT to use this skill
- Proofread/edit one document → [proofreading-text](../proofreading-text/SKILL.md) / [editing-prose](../editing-prose/SKILL.md).
- Set up live tracked changes → [authoring-word-documents](../authoring-word-documents/SKILL.md).
- Merge conflicting edits from many people → a collaboration workflow.

## Inputs
- Both document versions (and which is "old" vs "new").
- What the reader cares about (legal terms, numbers, obligations, scope).
- Whether cosmetic/formatting changes matter for this comparison.

## Outputs
- A prioritized change report: material changes first (with old→new and impact),
  then minor edits, then cosmetic — plus an overall verdict (substantive or not).

## Workflow
```
Progress:
- [ ] 1. Confirm which version is old/new and what matters
- [ ] 2. Normalize both to comparable text (OCR/convert if needed)
- [ ] 3. Diff structurally: additions, deletions, edits, moves
- [ ] 4. Classify each change: material vs. minor vs. cosmetic
- [ ] 5. Assess impact of material changes
- [ ] 6. Report, most-significant first, with a verdict
```

**Step 1 — Orient.** Fix old vs. new and the reader's priorities (a contract review
weights obligations and numbers; a marketing draft weights message).

**Step 2 — Normalize.** Convert both to comparable text (extract PDF text, OCR
scans, strip incomparable formatting) so you diff content, not encoding.

**Step 3 — Diff structurally.** Detect additions, deletions, in-place edits, and
**moved** sections (a moved paragraph is not a delete+add — say so).

**Step 4 — Classify.** Tag each change **material** (changes meaning, numbers,
obligations, scope), **minor** (wording with same meaning), or **cosmetic**
(formatting, whitespace). Do not drown material changes in cosmetic ones.

**Step 5 — Assess impact.** For each material change, state old→new and *why it
matters* (e.g. "payment terms 30→60 days — worse cash position").

**Step 6 — Report.** Lead with material changes, then minor, then a note on
cosmetic. End with a one-line verdict: are the changes substantive?

## Principles
1. **Meaning over characters.** A raw diff is noise; classify by impact.
2. **Detect moves,** don't report relocated text as deleted-and-added.
3. **Material first.** The reader's time goes to what changes outcomes.
4. **Show old→new** for every material change so it's verifiable.
5. **State a verdict.** "12 changes, 2 material" beats an undifferentiated list.

## Decision framework
- **Same format, text-based?** Direct structural diff.
- **PDF or scanned?** Normalize/OCR first via the PDF/OCR skills.
- **Contract/legal?** Weight defined terms, numbers, dates, obligations, liability.
- **Many small wording edits?** Summarize the pattern, list only the material ones.

## Common mistakes
- **Dumping a raw diff** with no classification — the reader still has to do the work.
- **Reporting moves as delete+add** — inflates the change list and hides real edits.
- **Missing changes in headers/footers/footnotes/tables** — check all regions.
- **Treating formatting changes as substantive** (or vice versa).
- **No impact assessment** on material changes — "changed X" without "which means Y".

## Validation checklist
- [ ] Old/new direction confirmed and stated.
- [ ] Both versions normalized to comparable text.
- [ ] Additions, deletions, edits, and moves each identified.
- [ ] Every change classified material / minor / cosmetic.
- [ ] Material changes show old→new and impact.
- [ ] Headers, footers, footnotes, tables, and numbers checked.
- [ ] Clear overall verdict provided.

## Edge cases
- **Reformatted-but-unchanged docs:** report "no substantive changes" explicitly.
- **Numbers/dates:** every numeric change is potentially material — never skip.
- **Reordered clauses:** flag as moves and check whether order changes meaning.
- **Different formats (PDF vs Word):** compare normalized text, note formatting isn't comparable.
- **Tables:** compare cell-by-cell; row insert/delete shifts alignment.

## Related skills
- [proofreading-text](../proofreading-text/SKILL.md), [editing-prose](../editing-prose/SKILL.md) — improve one version.
- [processing-pdf-documents](../processing-pdf-documents/SKILL.md), [extracting-text-with-ocr](../extracting-text-with-ocr/SKILL.md) — normalize inputs.
- [authoring-word-documents](../authoring-word-documents/SKILL.md) — tracked changes for live review.

## Examples
**Input:** "Compare our contract v3 and the counterparty's v4."
**Output:** Report: **Material (3)** — liability cap $1M→$5M (worse for us),
payment 30→45 days, added auto-renewal clause; **Minor (5)** — reworded recitals;
**Cosmetic** — numbering restyled. Verdict: substantive — legal review required
before signing.

## Automation opportunities
- Batch-compare a folder of before/after files, flagging only those with material changes.
- Auto-normalize (OCR/convert) mixed-format inputs before diffing.
- Gate approvals: block sign-off when material changes are detected but unreviewed.
