# Change-Note Formats Reference

## Contents
- Format A: Software release notes (Keep a Changelog)
  - Document skeleton
  - The six categories, defined
  - Categorization edge cases
  - Entry style rules
- Semantic Versioning: choosing the bump
- Format B: Business change note
  - Template
  - Field-by-field instructions
  - Tone and length
- Choosing between the two formats

## Format A: Software release notes (Keep a Changelog)

Follows the Keep a Changelog convention (keepachangelog.com): one section per
release, newest first, changes grouped under fixed category headings.

### Document skeleton

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Added
- ...

### Changed
- ...

### Deprecated
- ...

### Removed
- ...

### Fixed
- ...

### Security
- ...
```

Rules:
- Omit any category with no entries — never leave an empty heading.
- Use ISO dates (`2026-07-08`).
- An unreleased section is titled `## [Unreleased]`.
- If a release contains breaking changes, add a bolded callout line
  immediately under the version heading, before the categories:
  `**Breaking:** <one-line summary and link to migration steps>`.

### The six categories, defined

| Category   | Contains |
| ---------- | -------- |
| **Added**      | New features, endpoints, options, or capabilities that did not exist before. |
| **Changed**    | Altered behavior of existing functionality — different defaults, new output shape, renamed flags. |
| **Deprecated** | Features that still work but are scheduled for removal; state the replacement and, if known, the removal timeline. |
| **Removed**    | Features deleted in this release. Almost always implies a major bump. |
| **Fixed**      | Bug fixes — behavior now matches what was already documented or intended. |
| **Security**   | Vulnerability fixes. Reference the advisory or CVE if one exists; describe impact without giving an exploit recipe. |

### Categorization edge cases

- **Fix vs. Changed**: if the old behavior was a defect, it is Fixed; if the
  old behavior was intentional and is now different, it is Changed.
- **A rewrite with identical behavior**: omit it — no user-visible effect.
- **Performance improvements**: Changed ("Report generation is ~3x faster"),
  unless slowness was a reported bug, then Fixed.
- **Dependency bumps**: omit, unless the bump fixes a vulnerability (Security)
  or changes observable behavior (Changed).
- **One commit, two effects** (e.g. adds a feature and removes a flag): split
  into two entries in the appropriate categories.
- **Reverts**: if a change and its revert both fall inside the release window,
  neither appears.

### Entry style rules

- One bullet per user-visible change; lead with the effect, not the mechanism.
- Present tense or simple past, consistent within a document.
- Keep issue/PR references at the end of the line: `(#212)`.
- Name the surface where the change appears ("on the Reports page",
  "in the `/v2/orders` endpoint") so readers can locate it.

## Semantic Versioning: choosing the bump

Given the previous version `MAJOR.MINOR.PATCH`, pick the bump from the
categorized changes (semver.org):

| Bump | When | Typical categories present |
| ---- | ---- | -------------------------- |
| **Major** (X+1.0.0) | Any backward-incompatible change: removed features, changed defaults that break existing usage, incompatible API shapes. | Removed; breaking items in Changed |
| **Minor** (X.Y+1.0) | New backward-compatible functionality, or deprecations. | Added; Deprecated |
| **Patch** (X.Y.Z+1) | Only backward-compatible fixes. | Fixed; Security (non-breaking) |

Decision procedure: scan for anything breaking → major. Otherwise anything in
Added or Deprecated → minor. Otherwise → patch. The highest applicable bump
wins; a release with one breaking change and ten fixes is still major.

Additional guidance:
- Pre-1.0 versions (`0.y.z`) carry no compatibility promise; breaking changes
  may bump minor, but say so explicitly in the notes.
- A Security fix that requires users to change configuration is breaking —
  major, with the migration steps in the breaking callout.
- Always state the reasoning in one sentence next to the recommendation, e.g.
  "Minor: adds CSV export; nothing existing changes behavior."

## Format B: Business change note

For process, policy, tooling, or organizational changes aimed at the people
affected rather than at software users.

### Template

```markdown
# Change Note: <short title of the change>

**What is changing:** <one or two sentences describing the new state vs. the old state>

**Why:** <the driver — cost, compliance, audit finding, tool consolidation, feedback>

**Who is affected:** <teams, roles, or customer segments; name them specifically>

**Effective date:** <YYYY-MM-DD, plus any transition or grace period>

**Action required:** <who must do what, by when; "None" if truly none>

**Questions:** <owner or channel to contact>
```

### Field-by-field instructions

- **What is changing** — state both the old way and the new way in plain
  language; the contrast is what makes the change legible. Avoid project
  code names unless the audience knows them.
- **Why** — one honest sentence. Readers comply faster when the driver is
  stated; "to align with strategy" is not a driver.
- **Who is affected** — name groups precisely ("all people managers in EMEA",
  "vendors invoicing over $10k"). If a group is explicitly *not* affected and
  might worry, say so.
- **Effective date** — one unambiguous ISO date. If there is a transition
  window, give both dates ("old path accepted until 2026-08-15").
- **Action required** — the most important field. Each action names an actor,
  a verb, and a deadline. If no action is needed, write "None — the change is
  automatic" so readers stop scanning for a hidden task.
- **Questions** — a real owner or channel, not a generic alias nobody watches.

### Tone and length

- Whole note fits on one screen; under ~200 words is the target.
- Neutral and factual; no marketing language, no apology unless something
  actually went wrong.
- If the change is contentious, acknowledge the cost in one clause and move
  on — burying it erodes trust.

## Choosing between the two formats

| Signal | Format |
| ------ | ------ |
| Input is commits, PRs, or a feature list; readers are users or developers of the software | Release notes |
| Input describes a policy, workflow, tool rollout, deadline, or ownership change; readers must adjust how they work | Business change note |
| A software release forces a process change (e.g. new login flow for all staff) | Both: release notes for the record, a business change note for the announcement |

When in doubt, ask who will read it: if the reader's question is "what does
the product do now?", use release notes; if it is "what do I have to do
differently?", use the business change note.
