---
name: building-document-templates
description: Design reusable, governed document templates (Word .dotx, Docs, Excel, slides) with clear placeholders, locked structure, built-in styles, and guidance so anyone can produce consistent documents. Use when the user asks to "create a template", "make this reusable", "build a standard format", or turn a one-off document into a repeatable one. Produces a maintainable template with placeholder conventions and usage notes, not just an empty copy.
---

# Building Document Templates

## Scope
Turning a document into a reusable, consistent, governed template: placeholder
design, style/structure locking, embedded guidance, and versioning. Applies to
Word/Docs, spreadsheets, and slides. The one-off document itself is built with the
relevant authoring skill; brand comes from
[producing-branded-documents](../producing-branded-documents/SKILL.md).

## Purpose
Let non-experts produce consistent, correct documents fast — with clear
placeholders, protected structure, built-in styles, and instructions — and keep the
template maintainable as needs change.

## When to use this skill
- "Create a template" / "make this reusable" / "build a standard format."
- Turning a good one-off document into a repeatable standard.
- Standardizing a recurring document type across a team/org.

## When NOT to use this skill
- A single document → the relevant authoring skill.
- Data-driven bulk generation → [automating-document-generation](../automating-document-generation/SKILL.md) / [running-mail-merge](../running-mail-merge/SKILL.md).
- Brand rendering pipeline → [producing-branded-documents](../producing-branded-documents/SKILL.md).

## Inputs
- A strong example of the target document and which parts are fixed vs. variable.
- Who will use it and their skill level; governance owner.
- Any brand/style spec to inherit.

## Outputs
- A template file (e.g. `.dotx`) with named styles, clearly marked placeholders,
  protected fixed structure, embedded guidance, and version/owner metadata.

## Workflow
```
Progress:
- [ ] 1. Identify fixed vs. variable content from a good example
- [ ] 2. Build the structure with named styles
- [ ] 3. Mark placeholders with a clear, consistent convention
- [ ] 4. Add embedded guidance/instructions
- [ ] 5. Protect fixed structure; leave placeholders editable
- [ ] 6. Add version, owner, and change-log; test with a real user
```

**Step 1 — Fixed vs. variable.** From a good example, separate what never changes
(boilerplate, structure, legal text) from what the user fills each time.

**Step 2 — Style-driven structure.** Build on named styles so every instance is
consistent and re-brandable (see [formatting-documents](../formatting-documents/SKILL.md)).

**Step 3 — Placeholder convention.** Mark every variable clearly and consistently —
e.g. `[Client Name]`, `{{amount}}`, or content controls with prompt text. Users
must instantly see what to replace and nothing should ship with a placeholder left in.

**Step 4 — Embedded guidance.** Add short instructions (in comments, hidden guidance
text, or a first-page note) explaining how to complete each section. The template
should teach its own use.

**Step 5 — Protect structure.** Lock/protect fixed regions and styles so users can't
accidentally break the format; leave placeholder fields editable.

**Step 6 — Govern & test.** Add version, owner, and last-updated; keep a change log.
Have a real user complete it — if they misuse a placeholder or break structure, fix
the template, not the user.

## Principles
1. **Separate fixed from variable** — the core of any template.
2. **Obvious placeholders** — impossible to miss, consistent convention, never shipped filled-in wrong.
3. **Style-driven,** so instances are consistent and re-brandable.
4. **Self-documenting** — guidance travels with the template.
5. **Governed** — one owner, versioned, with a change log.

## Decision framework
- **Free-form fill?** Placeholder text + guidance.
- **Controlled fields (dates, dropdowns)?** Content controls / form fields.
- **Feeds automation later?** Use machine-readable placeholders (`{{field}}`) → [automating-document-generation](../automating-document-generation/SKILL.md).
- **Brand-critical?** Inherit from the brand spec / renderer.

## Common mistakes
- **Placeholders that look like real content** — users miss them and ship `[Client Name]`.
- **No guidance** — users don't know what goes where or how.
- **Unprotected structure** — users break the format; every instance drifts.
- **Baking in one instance's data** (a real client name/number left in).
- **No owner or version** — the template forks and rots.
- **Over-locking** — so rigid users abandon it for their own copy.

## Validation checklist
- [ ] Fixed and variable content clearly separated.
- [ ] Placeholders use one consistent, unmissable convention.
- [ ] Built on named styles; brand/style inherited.
- [ ] Guidance embedded for each section.
- [ ] Fixed structure protected; placeholders editable.
- [ ] No leftover real data from the source example.
- [ ] Owner, version, and change log present; tested by a real user.

## Edge cases
- **Legal/regulated templates:** lock mandatory clauses; control who can edit them.
- **Multi-variant (regions/languages):** manage variants under one owner, not divergent copies.
- **Long-lived templates:** schedule periodic review so they stay current.
- **Downstream automation:** align placeholder names to the data source schema.

## Related skills
- [formatting-documents](../formatting-documents/SKILL.md), [authoring-word-documents](../authoring-word-documents/SKILL.md).
- [running-mail-merge](../running-mail-merge/SKILL.md), [automating-document-generation](../automating-document-generation/SKILL.md).
- [producing-branded-documents](../producing-branded-documents/SKILL.md).

## Examples
**Input:** "Make our consulting SOW into a reusable template."
**Output:** A `.dotx` with fixed boilerplate and legal clauses (protected), styled
headings, clearly marked `[Client]`, `[Scope]`, `[Fee]`, `[Start Date]` content
controls with prompt text, a first-page how-to note, no leftover client data, and
owner/version/change-log metadata — tested by a consultant who filled it error-free.

## Automation opportunities
- Machine-readable placeholders let the same template drive mail merge or generation.
- Central template gallery so teams always start from the current version.
- A pre-send check that flags any unfilled placeholder.
