---
name: bsc-document-standards
description: Apply BSC (Business Science Corporation) branding, layout, and metadata conventions shared across all BSC project administration documents (lessons learned, change notes, project signoffs, presentations). Use as a shared foundation whenever authoring or reviewing a BSC project document, or when a document-type-specific skill (e.g. authoring-lessons-learned-docs) references "the shared BSC standards".
---

# BSC Document Standards

Shared branding and structural conventions for BSC project administration
documents. This is not used directly to produce a full document — it is the
foundation that document-type skills (lessons learned, change notes,
signoffs, presentations) build on, so every BSC document looks consistent
regardless of type or author.

## When to use this skill
- Building a new document-type skill for a BSC project admin document
- Reviewing an existing BSC document for branding/formatting consistency
- Answering questions about BSC's document color scheme, fonts, footer text,
  or logo placement rules

## Core principles
1. **One BSC identity, many client logos.** Every document carries the fixed
   BSC brand (logo lockup, color bar, footer, watermark) plus exactly one
   swappable client/project logo on the cover. Never redesign the BSC
   elements per project — only the client logo changes.
2. **Reuse a real prior document as the base file.** Do not build documents
   from a blank page. Copy the closest existing branded `.docx` and edit
   its content programmatically. This is the only reliable way to preserve
   Word content controls, header/footer XML, and embedded theme fonts —
   manual recreation in a fresh document loses fidelity.
3. **Metadata first, narrative second.** Every document opens with a
   compact project identity block (name, code, manager, date) before any
   narrative content.

## BSC brand identity (fixed across all document types)
- **Company:** Business Science Corporation ("BSC"), tagline **"SOLVE ·
  AUTOMATE · PROSPER"**.
- **Color palette** (from the BSC Office theme, `clrScheme name="BSC"`):
  - Text/dark: `#141515`
  - Heading blue (dk2/text2): `#006395`
  - Secondary navy (lt2): `#163E64`
  - Accent teal/cyan (accent1): `#148AB7`, (accent2): `#39C2D8`
  - Accent red (accent5): `#C20000`
  - Accent orange (accent6): `#EC5D34`
  - The three-color rule bar under the BSC logo lockup is red → navy → teal
    (left to right).
- **Fonts:** Arial throughout (both major/minor theme fonts). Body text
  additionally uses the `MinionPro-Regular` fallback font in some legacy
  paragraph styles (`[Basic Paragraph]`) — prefer Arial-based styles
  (`Normal`, `Body`, `Numbered Heading 1/2`) for anything new.
- **Heading style:** Numbered headings via custom styles `Numbered Heading
  1` (24pt-ish, color `#006395`, auto-numbered) and `Numbered Heading 2`
  (smaller, same color, auto-numbered sub-level). Do not use Word's default
  `Heading 1/2/3` styles — use the `Numbered Heading *` styles so section
  numbering stays consistent with existing BSC documents.
- **Table styles:** `GridTable4-Accent1` for structured data tables (team,
  metadata), `ListTable3-Accent1` for narrative/lesson tables.
- **Footer (every page):** centered, small Arial text:
  `© BUSINESS SCIENCE CORPORATION {year} | CONFIDENTIAL | PAGE {n}`, plus a
  company details block (address, phone, VAT/reg numbers, directors) on
  later pages. Preserve this verbatim — do not edit or remove it.
- **Cover page footer/contact block:** `1st Floor, North Wing, 90 Rivonia
  Road, Sandton, 2196, South Africa | Tel: +27 11 595 2500 | Fax: +27 86 627
  8068 | www.bscglobal.com`.

## Logo placement rules
Every BSC document ships with 5 fixed image assets plus 1 swappable one:
| Image | Role | Swap per project? |
|---|---|---|
| Client/project logo (header, top of cover) | The client's own logo | **Yes — always replace** |
| BSC logo lockup with tagline (below the color rule) | BSC brand identity | No — fixed |
| Three-color rule bar (red/navy/teal) | Visual divider | No — fixed |
| Abstract blue "data wave" graphic | Cover page background art | No — fixed |
| BSC logo lockup (large, cover footer area) | Repeated BSC brand mark | No — fixed |
| Small BSC logo mark (page footer) | Footer branding | No — fixed |

**Only the client/project logo changes between documents.** It lives in the
Word package at `word/media/image1.*` (jpeg or png depending on the source
file). See [references/logo-swap-procedure.md](references/logo-swap-procedure.md)
for the exact swap mechanics.

## Document identity metadata (common to every document type)
Every BSC project document opens with a compact identity table capturing at
minimum:
- **Project Name** (or **Project Names** if the document covers more than
  one related project)
- **Project Code** (or **Project Codes**) — BSC's internal `RI.####` job
  number format
- **Project Manager** / **Engagement Lead**
- **Date** — the document's own date, which may differ from any date shown
  on the cover page (cover page date can reflect when the doc was first
  drafted; the metadata table date reflects last update/sign-off)

## Base-file generation approach (use for every document type)
1. Identify the closest existing branded `.docx` for that document type.
2. Copy it as the base template; never start from a blank Word file.
3. Edit content programmatically (python-docx / raw OOXML), not by hand in
   Word, so results are repeatable and scriptable.
4. Cover-page title/date usually live inside Word content controls
   (`w:sdt` elements), which are **not** reachable via
   `python-docx`'s `doc.paragraphs` — they must be walked directly via the
   document XML. See
   [references/docx-editing-patterns.md](references/docx-editing-patterns.md).
5. Swap only the client/project logo; leave all other embedded images
   untouched.
6. Validate the output by re-opening it with python-docx and checking every
   table's cell text and the cover page text before considering the job
   done — don't assume a script "worked" just because it ran without error.

## Reference files
- [references/docx-editing-patterns.md](references/docx-editing-patterns.md)
  — Battle-tested python-docx/OOXML patterns for editing branded Word
  documents: content-control (sdt) text replacement, multi-paragraph cell
  clearing, row cloning, and swapping whole table structures.
- [references/logo-swap-procedure.md](references/logo-swap-procedure.md) —
  Exact steps and code for replacing the client/project logo image inside
  a `.docx` package without corrupting the file.
