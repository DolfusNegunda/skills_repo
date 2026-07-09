---
name: formatting-documents
description: Apply consistent, professional visual and structural formatting to documents — headings, spacing, lists, tables, fonts, numbering, and layout — so they look coherent and are easy to scan. Use when the user asks to "format this", "make it look professional/consistent", "clean up the formatting", or fix inconsistent styling. Emphasizes style-based (not manual) formatting and accessibility. Produces a clean, consistent, accessible document. For corporate brand, use producing-branded-documents.
---

# Formatting Documents

## Scope
The visual and structural presentation of a document — consistency of headings,
spacing, lists, tables, fonts, and numbering — independent of the words. Applies
across Word, Docs, and PDF output. Corporate brand application is
[producing-branded-documents](../producing-branded-documents/SKILL.md); the app
mechanics are in the Word/Docs skills.

## Purpose
Make a document look coherent and professional and be easy to scan, using styles so
consistency holds and the document can be restyled without retyping.

## When to use this skill
- "Format this / make it look professional / consistent / clean it up."
- Fixing a document with inconsistent fonts, spacing, or heading styles.
- Preparing a document's presentation before publishing/sending.

## When NOT to use this skill
- Applying corporate brand → [producing-branded-documents](../producing-branded-documents/SKILL.md).
- Content clarity/structure of the writing → [editing-prose](../editing-prose/SKILL.md).
- Building the document from scratch → [authoring-word-documents](../authoring-word-documents/SKILL.md) / [authoring-google-docs](../authoring-google-docs/SKILL.md).

## Inputs
- The document and its output medium (screen, print, PDF).
- Any style guide/brand spec; accessibility requirements.

## Outputs
- A consistently formatted document driven by styles, with a coherent visual
  hierarchy, aligned elements, and accessibility basics met.

## Workflow
```
Progress:
- [ ] 1. Audit current formatting for inconsistencies
- [ ] 2. Establish a style system (heading levels, body, lists, tables)
- [ ] 3. Replace manual formatting with named styles
- [ ] 4. Standardize spacing, alignment, and lists
- [ ] 5. Format tables and figures consistently
- [ ] 6. Check accessibility and print/export fidelity
```

**Step 1 — Audit.** Find the inconsistencies: mixed fonts/sizes, manual vs. styled
headings, uneven spacing, bullets vs. dashes, ragged tables.

**Step 2 — Style system.** Decide the hierarchy: one heading style per level, one
body style, defined list and table styles, one or two fonts. Consistency comes from
a small, deliberate set.

**Step 3 — Styles, not manual formatting.** Apply named styles so every like element
matches and the whole document can be restyled at once. Manual formatting is the
root cause of inconsistency — replace it.

**Step 4 — Spacing & alignment.** Use paragraph spacing (not blank lines), consistent
indents, and alignment to a grid. One list marker style; consistent list indentation.

**Step 5 — Tables & figures.** Uniform table styles (header row, borders, padding),
captions, and consistent image sizing/placement.

**Step 6 — Accessibility & output.** Real heading styles, alt text, sufficient
contrast, meaningful link text; then verify it prints/exports to PDF without breaks.

## Principles
1. **Styles create consistency;** manual formatting destroys it.
2. **Less is more** — few fonts, few styles, consistent spacing.
3. **Hierarchy guides the eye** — sizes/weights signal structure.
4. **Whitespace is a tool,** not wasted space.
5. **Accessible formatting is correct formatting.**

## Decision framework
- **Recurring format?** Save it as a template → [building-document-templates](../building-document-templates/SKILL.md).
- **Corporate identity needed?** → [producing-branded-documents](../producing-branded-documents/SKILL.md).
- **Print vs. screen?** Adjust margins, contrast, and image resolution accordingly.
- **Inconsistent inherited doc?** Clear manual formatting, then reapply styles.

## Common mistakes
- **Manual formatting** (bold text as "headings", tabs for layout, blank lines for spacing).
- **Font/size soup** — many typefaces and sizes with no system.
- **Inconsistent lists** mixing markers and indents.
- **Ragged tables** with varying borders, padding, and alignment.
- **Ignoring accessibility** — color-only meaning, missing alt text, unstyled headings.
- **Formatting that breaks on export/print** — untested output.

## Validation checklist
- [ ] One style per element type; no manual formatting standing in for a style.
- [ ] ≤2 fonts; consistent sizes and weights signaling hierarchy.
- [ ] Uniform paragraph spacing (no blank-line spacing) and alignment.
- [ ] Consistent list markers and indentation.
- [ ] Tables share a style; figures sized and captioned consistently.
- [ ] Accessibility: styled headings, alt text, contrast, link text.
- [ ] Prints/exports to PDF cleanly.

## Edge cases
- **Merging docs from many authors:** normalize to one style set; strip incoming manual formatting.
- **Long documents:** ensure heading styles feed a working TOC and navigation.
- **Dense data tables:** prioritize readability (alignment, number formatting) over decoration.
- **Cross-platform (Word↔Docs↔PDF):** re-verify; styles can shift on conversion.

## Related skills
- [authoring-word-documents](../authoring-word-documents/SKILL.md), [authoring-google-docs](../authoring-google-docs/SKILL.md) — style mechanics.
- [building-document-templates](../building-document-templates/SKILL.md) — lock formatting into reuse.
- [producing-branded-documents](../producing-branded-documents/SKILL.md) — brand layer.

## Examples
**Input:** "This doc has 4 fonts, headings that are just bold text, and blank lines
everywhere — make it consistent."
**Output:** One font pair; Heading 1–3 styles applied to the former bold "headings";
paragraph spacing replacing blank lines; a single bullet style; a uniform table
style with a marked header row; alt text added; verified TOC and clean PDF export.

## Automation opportunities
- Define a style set once and reuse it as a template across documents.
- A "clean formatting" pass: clear manual formatting, reapply the style system.
- Batch-apply a house style to a folder of documents.
