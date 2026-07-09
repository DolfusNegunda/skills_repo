---
name: authoring-google-docs
description: Produce well-structured Google Docs for real-time collaboration — using heading styles, the document outline, tables of contents, comments/suggestions, and clean shareable formatting. Use when the user asks to "create a Google Doc", "write this in Docs", set up a collaborative document, or convert content into Docs. Produces a navigable, collaboration-ready doc. For Word/.docx, use authoring-word-documents instead.
---

# Authoring Google Docs

## Scope
Structured authoring in Google Docs where collaboration and navigability matter:
heading styles, the outline pane, auto TOC, comments vs. suggestions, sharing, and
clean formatting. The Google-native counterpart to
[authoring-word-documents](../authoring-word-documents/SKILL.md).

## Purpose
Deliver a Google Doc that is easy to navigate, safe to co-edit, and structured so
its outline, TOC, and headings hold up as multiple people work in it.

## When to use this skill
- "Create/write a Google Doc" or "put this in Docs".
- Collaborative documents with multiple editors and reviewers.
- Docs needing an outline, TOC, or structured headings.
- Converting Markdown/text into a properly styled Google Doc.

## When NOT to use this skill
- `.docx` deliverable → [authoring-word-documents](../authoring-word-documents/SKILL.md).
- Spreadsheets → [engineering-google-sheets](../engineering-google-sheets/SKILL.md).
- Slides → [building-google-slides](../building-google-slides/SKILL.md).
- Pure prose craft → the relevant writing skill.

## Inputs
- Content or brief; document type and audience.
- Collaboration model: who edits, who comments, who approves.
- Sharing/permission requirements and any org template.

## Outputs
- A Google Doc with real heading styles, a working outline and auto TOC,
  appropriate sharing settings, and a comment/suggestion workflow for review.

## Workflow
```
Progress:
- [ ] 1. Confirm type, audience, and collaboration/permission model
- [ ] 2. Build the heading outline first
- [ ] 3. Apply heading styles (Title, Heading 1–3) — not manual bold
- [ ] 4. Insert an auto TOC; verify the outline pane
- [ ] 5. Set sharing + suggesting mode for review
- [ ] 6. Resolve comments/suggestions; finalize
```

**Step 1 — Frame & permissions.** Decide who can edit vs. comment vs. view before
sharing; wrong permissions cause the most collaboration pain.

**Step 2 — Outline first.** Draft the heading tree; it powers the outline pane and TOC.

**Step 3 — Style, don't fake.** Use paragraph styles (Title, Heading 1–3, Normal)
so the outline pane and TOC work and screen readers can navigate. Update the doc's
default styles once to change fonts globally.

**Step 4 — TOC & outline.** Insert an auto TOC (with links); confirm the left
outline pane reflects the true hierarchy.

**Step 5 — Review mode.** Share in *Suggesting* mode for edits and use *Comments*
(with @mentions and assignment) for questions and action items.

**Step 6 — Finalize.** Resolve all suggestions/comments, switch off suggesting,
set final permissions, and (if needed) export to `.docx`/PDF.

## Principles
1. **Headings are navigation.** The outline pane and TOC depend on real styles.
2. **Permissions before sharing.** Decide edit/comment/view deliberately.
3. **Suggest, don't overwrite,** when others own the content.
4. **Comments are tasks** — assign and resolve them, don't let them pile up.
5. **Link, don't paste,** related Docs/Sheets to keep one source of truth.

## Decision framework
- **Many editors?** Suggesting mode + assigned comments.
- **Reusable format?** Make it a template / use the org template gallery.
- **Needs offline `.docx`?** Author here, export at the end.
- **Living doc many will reference?** Add a TOC and stable heading anchors.

## Common mistakes
- **Manual bold as headings** — breaks the outline and TOC.
- **Sharing with edit access to everyone** — accidental overwrites.
- **Unresolved comment sprawl** — review state becomes unreadable.
- **Copy-pasting from Word** dragging in broken styles — paste-without-formatting, then restyle.
- **Multiple copies** instead of one shared source — versions diverge.

## Validation checklist
- [ ] All headings use styles; outline pane shows correct hierarchy.
- [ ] TOC inserted and links resolve.
- [ ] Sharing permissions match the intended audience.
- [ ] Suggestions resolved; suggesting mode off for the final.
- [ ] Comments assigned/closed; no orphan action items.
- [ ] Images have alt text; links have meaningful text.
- [ ] Exports cleanly to `.docx`/PDF if required.

## Edge cases
- **Cross-org sharing:** check domain sharing policy; use link-with-expiry if available.
- **Large docs:** consider splitting; heavy real-time editing can lag.
- **Word round-trips:** styles can shift on import/export — re-verify headings.
- **Version history:** name key versions so you can restore a known-good state.

## Related skills
- [authoring-word-documents](../authoring-word-documents/SKILL.md) — .docx equivalent.
- [comparing-documents](../comparing-documents/SKILL.md) — diff versions.
- [formatting-documents](../formatting-documents/SKILL.md), [editing-prose](../editing-prose/SKILL.md), [proofreading-text](../proofreading-text/SKILL.md).

## Examples
**Input:** "Set up a collaborative PRD in Google Docs for five reviewers."
**Output:** Doc with Title + Heading 1–3 structure, auto TOC, an owners/status
table at top, share set to Comment for reviewers and Edit for two authors,
suggesting mode on, and a "Decisions" section where resolved comments land.

## Automation opportunities
- Templatize recurring doc types in the org template gallery.
- Generate an initial Doc from structured content, then collaborate live.
- Use assigned comments to auto-create action items in a tracker (via connector).
