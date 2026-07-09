---
name: writing-change-notes
description: Generates change and release notes from raw inputs such as git commits, feature lists, or described process and policy changes. Produces either software release notes (Keep a Changelog categories with Semantic Versioning guidance) or a business change note (what changed, why, who is affected, effective date, action required). Use when asked to write release notes, a changelog entry, a change announcement, or a change communication for a process or policy update.
---

# Writing Change Notes

## Overview
Turns an unpolished list of changes into a clear, audience-ready change note. Supports two output formats: **software release notes** built on the Keep a Changelog and Semantic Versioning standards, and **business change notes** for process, policy, or organizational changes. The skill handles grouping, rewording for the reader, and flagging anything that demands action.

## When to use this skill
- "Write release notes for these commits" or "turn this git log into a changelog entry"
- "Draft a changelog for v2.3.0" or "what version bump does this deserve?"
- "Announce this process change to the team" or "write a change note for the new expense policy"
- Preparing an entry for `CHANGELOG.md`, a release page, or an internal change bulletin
- Summarizing a sprint's merged work for stakeholders who did not follow the commits

## Core principles
1. **Write for the reader, not the author**: describe the effect of the change ("Exports now include a timezone column"), never the implementation ("refactored ExportService").
2. **Pick the format from the audience**: developers and users of software get release notes; employees, customers, or partners affected by a process get a business change note.
3. **Group before you write**: sort every change into a category first (Added/Changed/Deprecated/Removed/Fixed/Security, or the business template fields), then draft prose.
4. **Surface breaking changes and required actions loudly**: they go first, never buried mid-list.
5. **Drop the noise**: merge commits, "fix typo", "wip", and internal-only refactors with no observable effect are omitted or collapsed.

## Workflow

Copy this checklist and track progress through it:

```
Change-note progress:
- [ ] Step 1: Gather the raw changes (commits, feature list, or change description)
- [ ] Step 2: Choose the format — software release notes or business change note
- [ ] Step 3: Filter noise; deduplicate; merge related items
- [ ] Step 4: Categorize each item (changelog categories or business fields)
- [ ] Step 5: Draft entries in reader-facing language
- [ ] Step 6: Software only — recommend a version bump (major/minor/patch)
- [ ] Step 7: Put breaking changes / required actions at the top
- [ ] Step 8: Review against the anti-patterns list, then deliver
```

**Step 1 — Gather.** Collect the input: a pasted commit list, `git log --oneline <last-tag>..HEAD` output, a feature summary, or a described process change. Ask for the date range or version boundary if it is ambiguous.

**Step 2 — Choose format.** Software behavior changed → release notes. A process, policy, tool rollout, or responsibility changed → business change note. If the user names a format, use it. See [references/formats.md](references/formats.md) for both templates.

**Step 3 — Filter.** Remove merge commits, reverted pairs, and purely internal changes. Combine multiple commits that deliver one user-visible change into a single entry.

**Step 4 — Categorize.** Release notes: assign each entry to exactly one of Added, Changed, Deprecated, Removed, Fixed, Security. Business note: fill what / why / impact / effective date / action required. Definitions and edge cases are in the reference file.

**Step 5 — Draft.** One line per change, present tense or simple past, leading with the user-visible effect. Include issue/PR numbers when the input provides them.

**Step 6 — Version (software only).** Recommend major for breaking changes or removals, minor for backward-compatible additions, patch for fixes only. State the reasoning in one sentence.

**Step 7 — Order.** Breaking changes, security fixes, and "action required" items lead the document. Categories follow the Keep a Changelog order; empty categories are omitted.

**Step 8 — Review.** Check each entry against the anti-patterns below; verify every action item names who must act and by when.

## Examples

**Software input:** `a1f9c2e feat: add CSV export to reports page`, `77b0d1a fix: crash when filter list is empty`, `c3e8f44 chore: bump lodash`
**Output (excerpt):**
```markdown
## [1.4.0] - 2026-07-08

### Added
- CSV export on the Reports page (#212)

### Fixed
- Crash when applying a filter with an empty selection list (#218)
```
Version reasoning: new backward-compatible feature → minor bump. The dependency bump is omitted (no user-visible effect).

**Business input:** "Starting August 1 all vendor invoices go through Coupa instead of email to AP."
**Output (excerpt):**
```markdown
**What is changing:** Vendor invoices must be submitted through Coupa; the ap-invoices@ mailbox is retired.
**Effective date:** 2026-08-01
**Action required:** Requesters notify active vendors of the new submission path before July 25.
```

Full worked examples: [examples/example-release-notes.md](examples/example-release-notes.md) and [examples/example-business-change.md](examples/example-business-change.md).

## Anti-patterns
- **Copying commit messages verbatim** — commit messages describe code, not outcomes. Instead: rewrite each entry around what the reader will notice.
- **A single flat "Changes" list** — readers cannot scan for what matters to them. Instead: use the six changelog categories or the business template fields.
- **Burying a breaking change in "Changed"** — users miss it and things break. Instead: call it out at the top with migration steps.
- **Vague action items ("please be aware")** — nobody acts on awareness. Instead: state who does what by when.
- **Including every commit** — noise drowns signal. Instead: filter merges, typo fixes, and internal refactors.
- **Guessing the version bump without reasons** — the number carries a compatibility promise. Instead: justify major/minor/patch from the categorized changes.

## Related skills
- **writing-status-reports** — change notes often ship alongside a status update; use that skill for the progress narrative and this one for the change record.

## Reference files
- [references/formats.md](references/formats.md) — Keep a Changelog category definitions, Semantic Versioning bump guidance, and the business change-note template with field-by-field instructions.
