# Branded Document Template System — Design

How to produce Word / PowerPoint / PDF deliverables that look **identical across
every team** (layout, headers, footers, logo placement, colors, fonts) while
letting each project swap in a **client-specific logo** and content.

## The core principle: separate the invariant from the variable

Every branded deliverable is two things layered together:

| Invariant (same for everyone, defined once) | Variable (per project/client) |
|---|---|
| Page layout, margins, section order | The actual content (status, numbers, text) |
| Header / footer, page numbers | Client name, project name, date |
| Logo **position and size** | **Which** logo (client-specific) |
| Colors, fonts, heading styles | — |
| Boilerplate (confidentiality, legal) | — |

The whole design follows from this: **store the invariant as a real template
file; supply the variable as data.** Teams never rebuild layout — they fill a
template. That is what guarantees consistency.

## Why this respects "thin layer, not reimplementation"

We are **not** re-solving Word/PowerPoint internals (that's Anthropic's
source-available `docx`/`pptx` territory). We are:

1. Storing **pre-made native template files** (`.docx`, `.pptx`) as **assets**.
2. Running a small, deterministic script to **inject content + swap the logo**.

This is exactly the document skills' own pattern — *bundle template assets and a
fill script for fragile, must-be-exact operations* — applied to our brand.
Logo placement and headers must be pixel-consistent, so this is a **low-freedom**
task: a script + a template beats asking Claude to lay it out from scratch every
time.

## Architecture

A dedicated skill (proposed name: `producing-branded-documents`) owns the
template library and the fill scripts:

```text
producing-branded-documents/
├── SKILL.md                     # Procedure: pick template → fill → export → validate
├── assets/
│   ├── templates/
│   │   ├── weekly-project-update.docx     # Standard layout + header/footer + placeholders
│   │   ├── project-status-deck.pptx       # Standard slide master
│   │   └── formal-report.docx
│   ├── logos/
│   │   ├── company.png                     # Default / fallback logo
│   │   └── clients/                        # Client-specific logos, keyed by name
│   │       ├── acme.png
│   │       └── globex.png
│   └── brand/
│       └── brand-spec.md                    # Colors (hex), fonts, logo sizing/clear-space, margins
├── scripts/
│   ├── fill_docx.py             # Inject fields + swap logo into a .docx template
│   ├── build_pptx.py            # Same for a .pptx template
│   ├── export_pdf.py            # Convert .docx/.pptx → PDF for distribution
│   └── validate_output.py       # No leftover placeholders, logo present, required fields filled
└── references/
    └── template-catalog.md      # Which template for which deliverable + its field list
```

## How it works (the workflow)

```
1. Choose the template (weekly-project-update.docx)
2. Gather the variable data (client=acme, project=X, week=27, status content)
3. Run fill_docx.py: injects fields + places logos/clients/acme.png
4. Run validate_output.py: confirms no {{placeholders}} remain, logo present
5. Run export_pdf.py (if a PDF is the deliverable)
```

The **content** for step 2 comes from the content skills — e.g.
`writing-status-reports` produces the status text, and this skill *renders* it
into the branded file. Content and format stay cleanly separated.

## The template mechanism

Use **placeholder-driven native templates** (most reliable for "same layout, swap
content"):

- **Word:** a `.docx` where header/footer/logo/styles are fixed, and body fields
  are `{{ jinja }}` placeholders filled by **`docxtpl`** (python-docx-template).
  The logo is an `InlineImage` swapped by client. Header/footer and page numbers
  live in the template and are never touched.
- **PowerPoint:** a `.pptx` with a locked slide master; **`python-pptx`** fills
  named placeholders and replaces the logo picture per client.
- **PDF:** **not authored directly.** PDF is an **export** of the filled
  docx/pptx via LibreOffice (`soffice --headless --convert-to pdf`). Author in
  Word/PPT, distribute as PDF.

Dependencies to list in the skill: `docxtpl`, `python-docx`, `python-pptx`, and
LibreOffice for PDF export. (Available where code execution + package install is
available; the drafting logic degrades gracefully if not.)

## Client-specific logos, one standard placement

- Logos live in `assets/logos/clients/<client-key>.png`, plus a `company.png`
  fallback.
- The fill script takes `client=acme`, loads `clients/acme.png`, and drops it
  into the **fixed** logo frame defined in the template. If the client logo is
  missing, it falls back to `company.png` and warns.
- **Placement, size, and clear-space are defined once** — in the template frame
  and documented in `brand/brand-spec.md`. So every team, every client, gets the
  logo in the same spot at the same size. That's the guarantee you're after.

Adding a client = drop one PNG in `logos/clients/`. No template edits.

## Governance: the single source of truth

The real win isn't one document — it's **consistency at scale**:

- Templates and brand spec live in **one version-controlled place** (this skill).
  Teams stop keeping private copies that drift.
- Rebranding = update the template once; every future deliverable inherits it.
- The `validate_output.py` gate prevents shipping a file with a missing logo or
  an unfilled `{{client_name}}`.

## Format strategy — when to use which

| Deliverable | Author in | Distribute as |
|---|---|---|
| Weekly project update, status report, change notes, formal report | **Word (.docx)** | PDF |
| Exec/client status presentation, project kickoff | **PowerPoint (.pptx)** | PDF |
| Anything final/read-only sent outside the company | (either) | **PDF** |

PDF is an output stage, not a separate template system.

## Recommended build path

1. **Phase 1 — one template, one format.** Build `producing-branded-documents`
   with just `weekly-project-update.docx` + `fill_docx.py` + `validate_output.py`.
   Prove the invariant/variable split and per-client logo swap end to end.
2. **Phase 2 — add PDF export** (`export_pdf.py`).
3. **Phase 3 — add the PPTX template** (`project-status-deck.pptx` + `build_pptx.py`).
4. **Phase 4 — wire content skills in:** `writing-status-reports` feeds this skill.
5. **Phase 5 — expand the template catalog** (reports, proposals, HR docs) reusing
   the same brand spec and logo library.

## Key decisions to confirm before building

- Do company **Word/PPTX templates and a brand style guide already exist**, or
  does this skill establish them?
- Which **deliverable + format** to prototype first (recommended:
  weekly-project-update in Word)?
- Where do **client logos** come from, and what's the naming key (client short
  name? account ID)?
- Is **LibreOffice** available in your run environment for PDF export?
