---
name: authoring-lessons-learned-docs
description: Generate a standardized, BSC-branded Lessons Learned project document (.docx) by asking the required clarifying questions and filling a validated template. Use when the user asks to write, create, draft, or generate a lessons learned document, project retrospective, or post-project review for a BSC engagement.
---

# Authoring Lessons Learned Docs

Produces a branded BSC Lessons Learned `.docx` for a completed (or
completing) project, following the standard structure derived from prior
BSC lessons learned documents. Builds on the shared
[bsc-document-standards](../bsc-document-standards/SKILL.md) skill for
branding/logo/font conventions — read that skill first if this is your
first time authoring any BSC document.

## When to use this skill
- "Write a lessons learned document for [project]"
- "Create a post-project retrospective for [client]"
- Any request for a BSC project close-out / lessons learned deliverable

## Core principles
1. **Ask before drafting.** Never invent project details, team members, or
   lessons. Always run the full clarifying-question pass (below) first —
   a Lessons Learned document is only useful if its content is real.
2. **One standard skeleton, two deliverables-table formats.** All BSC
   lessons learned documents share the same 9-section skeleton (see
   Process). The Deliverables section has two valid formats — ask which
   fits before generating (see Step 3).
3. **Generate the real branded file, don't describe it.** This skill
   outputs an actual `.docx` using the base template and generation script
   in this skill's `assets/`/`scripts/` — never hand back plain markdown
   as the deliverable.
4. **Preserve the standard vocabulary.** Section headings are exactly:
   *Project Team*, *Deliverables*, *Commentary on Project Execution*
   (with sub-headings *Positives* and *Challenges*), and *Learnings and
   Suggestions*. Do not invent alternate headings (e.g. do not use
   "Negatives" — the standardized label is **Challenges**).

## Standard document skeleton
Every generated document follows this exact section order:
1. Cover page — `{Project Code} Lessons Learned`, cover date
2. Project identity table — Project Name, Project Code, Project Manager, Date
3. **Project Team** — table of name / position / (optional) allocation %
4. **Deliverables** — table, format A or B (see Step 3 below)
5. **Commentary on Project Execution**
   - **Positives** — table of Title / Comment
   - **Challenges** — table of Title / Comment
6. **Learnings and Suggestions** — table of Title / Learnings-Suggestions-Actions

## Process
```
Lessons learned doc progress:
- [ ] 1. Ask for project identity + team (name, code, manager, dates, team roster)
- [ ] 2. Ask for the client/project logo image
- [ ] 3. Ask which deliverables format fits (A: proposal items, or B: document status list)
- [ ] 4. Ask for deliverables content matching the chosen format
- [ ] 5. Ask for Positives, Challenges, and Learnings/Suggestions content
- [ ] 6. Assemble the data dict and run scripts/generate_lessons_learned.py
- [ ] 7. Validate the output (reopen and check every table + cover page)
- [ ] 8. Deliver the .docx to the user with a summary of what was generated
```

**Step 1 — Project identity + team.** Ask for, at minimum:
- Project name(s) and project code(s) (BSC `RI.####` format) — support
  multiple codes/names if this document covers more than one related
  project (combine them, comma- or newline-separated, matching how the
  prior multi-project example did it)
- Project manager / engagement lead name
- Cover date (date shown on the cover page) and metadata date (date shown
  in the identity table — these can differ; metadata date is usually the
  more recent "as of" date)
- Full team roster: each member's name, whether they're BSC or client-side
  (e.g. "Jane Doe (BSC)" vs "Client Contact (ClientName)"), their position/
  role, and optionally their average allocation % on the project. If
  allocation % isn't known for anyone, omit that column entirely rather
  than leaving it blank.

**Step 2 — Client/project logo.** Ask the user to supply the client or
project logo image (the one element that changes per document — see
[bsc-document-standards](../bsc-document-standards/SKILL.md)). If the user
has no logo file handy, ask if they'd like to proceed without a logo swap
(document ships with a placeholder/previous project's logo) or pause until
they can supply one.

**Step 3 — Deliverables format.** Ask the user which format fits this
project, describing both plainly:
- **Format A** — tracks each deliverable against the original proposal:
  an item number, a description (can include bullet sub-points), and
  inline notes on whether it was delivered on time and met the quality
  bar. Best for projects with a formal signed Scope of Work / Proposal.
- **Format B** — a simpler running list of documents/outputs issued
  during the project with a status (e.g. "✔ Delivered", "In progress")
  and free-text notes. Best for projects tracked more informally or with
  many interim documents.

**Step 4 — Deliverables content.** Collect the actual list matching the
chosen format (see [references/data-schema.md](references/data-schema.md)
for exact field names).

**Step 5 — Positives / Challenges / Learnings.** Ask for:
- **Positives**: a short title + a comment (can be multi-sentence) for
  each thing that went well
- **Challenges**: same shape, for things that didn't go well or were hard
- **Learnings and Suggestions**: a short title + the combined
  lesson/recommendation/next-action text for each item (BSC's standard
  format merges these three into one field — do not split into separate
  owner/due-date/priority columns unless the user explicitly asks for a
  stricter tracked-action format as a one-off customization)

Don't over-prompt: if the user pastes a rough dump of bullet points
covering several of these sections at once, parse and sort it into the
right buckets rather than re-asking for content already given. Only ask
follow-up questions for genuinely missing pieces.

**Step 6 — Assemble and generate.** Build a `data` dict matching
[references/data-schema.md](references/data-schema.md) exactly, then run:
```python
import sys
sys.path.insert(0, "authoring-lessons-learned-docs/scripts")
from generate_lessons_learned import generate

generate(
    data=data,
    template_path="authoring-lessons-learned-docs/assets/lessons-learned-base-template.docx",
    output_path="RI.XXXX_Lessons_Learned.docx",
    logo_path="client_logo.png",       # None if no logo supplied
    assets_dir="authoring-lessons-learned-docs/assets",
)
```
Adjust the `sys.path`/asset paths to wherever this skill folder was synced
into the working environment.

**Step 7 — Validate.** Re-open the generated file and confirm: the cover
page shows the right project code and date; the identity table, team
table, deliverables table, and all three lesson tables contain exactly the
rows provided (no leftover template text, no missing rows); and the logo
swap (if requested) shows the correct image. See the validation checklist
in [bsc-document-standards/references/docx-editing-patterns.md](../bsc-document-standards/references/docx-editing-patterns.md).

**Step 8 — Deliver.** Hand back the `.docx` file with a short summary of
what was populated (project, section counts) — don't repeat the full
document content back in chat.

## Anti-patterns
- **Skipping the clarifying questions and inventing plausible-sounding
  lessons.** Instead: always collect real content first; a fabricated
  lessons learned document is worse than no document.
- **Using "Negatives" as the section heading.** The standardized label is
  **Challenges**. Instead: always use "Challenges".
- **Splitting Learnings/Suggestions into Owner/Due Date/Priority columns
  by default.** Instead: keep the simple merged Title + combined text
  format unless the user explicitly asks for stricter action tracking.
- **Building the deliverables table by hand for whichever format wasn't
  shipped in the base template.** Instead: always swap in the correct
  format's table skeleton first (`assets/deliverables-table-format-A.xml`
  or `-B.xml`) via `replace_table_with_skeleton` — see
  [bsc-document-standards/references/docx-editing-patterns.md](../bsc-document-standards/references/docx-editing-patterns.md).
- **Returning markdown/plain text as "the document."** Instead: always run
  the generation script and hand back an actual `.docx` file.

## Reference files
- [references/data-schema.md](references/data-schema.md) — Exact field
  names and shapes for the `data` dict passed to `generate()`.
- [scripts/generate_lessons_learned.py](scripts/generate_lessons_learned.py)
  — Run this to produce the document; see its module docstring for the
  full function signature.
- [assets/lessons-learned-base-template.docx](assets/lessons-learned-base-template.docx)
  — The validated BSC-branded base file (do not hand-edit; edit only via
  the generation script).
- [assets/deliverables-table-format-A.xml](assets/deliverables-table-format-A.xml),
  [assets/deliverables-table-format-B.xml](assets/deliverables-table-format-B.xml)
  — Stored table skeletons for the two deliverables formats.
