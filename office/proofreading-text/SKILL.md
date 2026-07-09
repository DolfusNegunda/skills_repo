---
name: proofreading-text
description: Perform a final surface-level correctness pass on text — grammar, spelling, punctuation, typos, and consistency — without changing meaning or rewriting. Use when the user asks to "proofread", "check for typos/errors", "final pass", or "check grammar" on near-final text. This is the last step before publishing, distinct from substantive editing. Produces corrections (and optionally a marked-up list) while preserving the author's voice and intent.
---

# Proofreading Text

## Scope
The final correctness pass: catching grammar, spelling, punctuation, typos, and
consistency errors on near-final text **without** rewriting or restructuring. If
the text needs clarity/flow/structure work, that's
[editing-prose](../editing-prose/SKILL.md) and should happen first.

## Purpose
Make text error-free and internally consistent while preserving the author's exact
meaning and voice — the last quality gate before it ships.

## When to use this skill
- "Proofread this" / "check for typos / errors / grammar."
- A final pass on near-final text before publishing or sending.
- Verifying consistency (spelling variants, capitalization, formatting of numbers).

## When NOT to use this skill
- The text needs clarity/flow/structure work → [editing-prose](../editing-prose/SKILL.md) first.
- Drafting from scratch → the relevant writing skill.
- Comparing two versions → [comparing-documents](../comparing-documents/SKILL.md).

## Inputs
- Near-final text and its variant/style (e.g. US vs UK English, house style guide).
- Whether to apply corrections directly or return a marked list.

## Outputs
- Corrected text (or a list of corrections with locations), preserving meaning and
  voice, plus a note on any consistency decisions made.

## Workflow
```
Progress:
- [ ] 1. Confirm language variant and any style guide
- [ ] 2. Pass 1: spelling and typos
- [ ] 3. Pass 2: grammar, punctuation, agreement
- [ ] 4. Pass 3: consistency (terms, capitalization, numbers, formatting)
- [ ] 5. Pass 4: names, numbers, dates, links (factual surface errors)
- [ ] 6. Deliver corrections; preserve voice; flag, don't rewrite, unclear bits
```

**Step 1 — Set the standard.** Confirm US/UK spelling and any house style, so
"organize/organise" and comma conventions are corrected consistently, not
arbitrarily.

**Step 2–4 — Layered passes.** Proofread in focused passes; hunting all error types
at once misses things. Spelling/typos → grammar/punctuation → consistency
(one spelling per term, consistent capitalization, number and date formatting).

**Step 5 — High-cost surface facts.** Verify proper nouns, figures, dates, and that
links/emails are well-formed. A misspelled client name or wrong number is the most
damaging "typo".

**Step 6 — Preserve voice.** Fix errors only. If a sentence is awkward but correct,
leave it (or flag it) — rewriting is editing, not proofreading. Flag genuine
ambiguities rather than guessing the author's intent.

## Principles
1. **Correct, don't rewrite.** Preserve meaning and voice; fix only errors.
2. **Layered passes** beat one all-at-once scan.
3. **Consistency is an error class** — one spelling, one capitalization, one format.
4. **Verify names, numbers, dates** — the costliest surface mistakes.
5. **Flag, don't guess,** on true ambiguity.

## Decision framework
- **Awkward but correct?** Leave/flag — that's editing.
- **Ambiguous meaning?** Flag for the author; don't silently reinterpret.
- **Inconsistent term/spelling?** Standardize to the chosen variant/style.
- **Possible factual slip (name/number)?** Flag for verification.

## Common mistakes
- **Rewriting** under the guise of proofreading — changes voice/meaning.
- **One-pass scanning** — mixed error types slip through.
- **Ignoring consistency** (color/colour, e-mail/email) across the document.
- **Trusting spell-check alone** — it misses correct-but-wrong words (their/there, form/from).
- **Overlooking headings, captions, footers, and tables** — errors hide there.

## Validation checklist
- [ ] Language variant/style applied consistently.
- [ ] Spelling and typos corrected (including homophones spell-check misses).
- [ ] Grammar, punctuation, and subject-verb/tense agreement correct.
- [ ] Terminology, capitalization, and number/date formats consistent.
- [ ] Proper nouns, figures, dates, and links verified.
- [ ] Headings, captions, footers, tables checked, not just body text.
- [ ] Author's meaning and voice unchanged.

## Edge cases
- **Technical/legal text:** don't "correct" domain terms or defined terms you don't recognize — verify first.
- **Intentional style choices** (fragments in marketing copy): preserve; confirm if unsure.
- **Non-native or quoted text:** don't alter direct quotes; flag issues in quotations.
- **Mixed variants by design** (brand names): note exceptions.

## Related skills
- [editing-prose](../editing-prose/SKILL.md) — substantive improvement (do first).
- [writing-business-prose](../writing-business-prose/SKILL.md) — the writing base.
- [comparing-documents](../comparing-documents/SKILL.md) — verify what changed.

## Examples
**Input:** "Its been a pleasure working with the Johnson & Johnston team, we look
forward to the next fase of the the project on Jan 31st 2026."
**Output:** "It's been a pleasure working with the Johnson & Johnston team. We look
forward to the next phase of the project on 31 January 2026." — flag: confirm client
name is "Johnson & Johnston" (not "& Johnson"); fixed "Its"→"It's", "fase"→"phase",
duplicated "the the", comma splice, and date format per UK style.

## Automation opportunities
- Run a spell/grammar checker first, then a human/model consistency pass for what it misses.
- Maintain a house style sheet (preferred spellings, terms) the pass enforces.
- Chain after [editing-prose](../editing-prose/SKILL.md) as the automatic final gate.
