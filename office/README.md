# Office Skills

Operational competencies for everyday office work: producing and reviewing
documents, spreadsheets, and presentations; processing PDFs and scans; and
writing well across business genres. Every skill here follows the house style in
[../skill-builder/SKILL.md](../skill-builder/SKILL.md).

## Design philosophy

These skills are **thin house-style layers**, not reimplementations. Claude Code
and claude.ai already generate `.docx`, `.xlsx`, `.pptx`, and `.pdf` files. Our
job is to add the parts a generic model can't guess: **what good looks like** —
structure, conventions, review rubrics, tone, checklists, and decision rules.
Never re-solve OOXML or PDF internals; ride on top of the built-in capability and
spend your effort on quality.

**Where prose isn't enough, skills ship tested scripts.** For deterministic,
mechanical checks a cheap model shouldn't have to reason through, document skills
bundle a `scripts/` tool wired into their workflow: **validators** for producers
(`engineering-excel-workbooks`, `authoring-word-documents`, `building-powerpoint-decks`)
that drive a produce → validate → fix → re-validate loop, and **extractors** for
processors (`processing-documents`, `processing-word-documents`,
`processing-powerpoint-files`, `processing-excel-files`, `processing-pdf-documents`)
that ingest deterministically and self-report fidelity. All are exercised by
`skill-builder/scripts/smoke_test_scripts.py` in CI.

## Two families

**Application skills** — how to operate a specific tool well:
| Skill | Focus |
|---|---|
| [authoring-word-documents](authoring-word-documents/SKILL.md) | Long-form structured Word docs (styles, TOC, sections). |
| [engineering-excel-workbooks](engineering-excel-workbooks/SKILL.md) | Robust, auditable Excel models and formulas. |
| [building-powerpoint-decks](building-powerpoint-decks/SKILL.md) | Clean, on-brand PowerPoint decks. |
| [managing-outlook-mail](managing-outlook-mail/SKILL.md) | Triage, rules, and professional mail handling in Outlook. |
| [collaborating-in-teams](collaborating-in-teams/SKILL.md) | Channels, meetings, and async etiquette in Microsoft Teams. |
| [authoring-google-docs](authoring-google-docs/SKILL.md) | Collaborative Docs authoring and structure. |
| [engineering-google-sheets](engineering-google-sheets/SKILL.md) | Sheets formulas, QUERY/ARRAYFORMULA, and models. |
| [building-google-slides](building-google-slides/SKILL.md) | Google Slides decks and reusable layouts. |

**Craft & processing skills** — genre and transformation competencies:
| Skill | Focus |
|---|---|
| [processing-pdf-documents](processing-pdf-documents/SKILL.md) | Extract, split, merge, redact, fill, and validate PDFs. |
| [extracting-text-with-ocr](extracting-text-with-ocr/SKILL.md) | Turn scans/images into accurate structured text. |
| [designing-forms](designing-forms/SKILL.md) | Design forms and surveys that collect clean data. |
| [comparing-documents](comparing-documents/SKILL.md) | Diff two document versions and report material changes. |
| [recording-meeting-minutes](recording-meeting-minutes/SKILL.md) | Formal minutes with decisions and actions. |
| [writing-business-prose](writing-business-prose/SKILL.md) | Clear, professional business writing fundamentals. |
| [writing-executive-summaries](writing-executive-summaries/SKILL.md) | One-page summaries that lead with the answer. |
| [writing-technical-documentation](writing-technical-documentation/SKILL.md) | READMEs, guides, references, runbooks. |
| [writing-policies](writing-policies/SKILL.md) | Enforceable, unambiguous policy documents. |
| [writing-proposals](writing-proposals/SKILL.md) | Persuasive proposals and SOWs. |
| [writing-reports](writing-reports/SKILL.md) | Structured analytical and status reports. |
| [proofreading-text](proofreading-text/SKILL.md) | Surface-level correctness pass (grammar, spelling, consistency). |
| [editing-prose](editing-prose/SKILL.md) | Substantive editing for clarity, flow, and structure. |
| [formatting-documents](formatting-documents/SKILL.md) | Consistent visual and structural formatting. |
| [building-document-templates](building-document-templates/SKILL.md) | Reusable, governed templates with placeholders. |
| [running-mail-merge](running-mail-merge/SKILL.md) | Personalized bulk documents from a data source. |
| [automating-document-generation](automating-document-generation/SKILL.md) | Data + template → finished documents at scale. |
| [engineering-spreadsheets](engineering-spreadsheets/SKILL.md) | Platform-agnostic spreadsheet modeling discipline. |
| [designing-dashboards](designing-dashboards/SKILL.md) | Decision-oriented dashboards and KPI layouts. |
| [crafting-presentation-narratives](crafting-presentation-narratives/SKILL.md) | Story structure before slide design. |

**Document ingestion skills** — read and parse any incoming file into clean, structured content (the front door for document tasks):
| Skill | Focus |
|---|---|
| [processing-documents](processing-documents/SKILL.md) | Document-type awareness + router: detect type, ingest, route to the right handler. |
| [processing-word-documents](processing-word-documents/SKILL.md) | Extract Word (.docx) content, headings, tables, notes, tracked changes. |
| [processing-powerpoint-files](processing-powerpoint-files/SKILL.md) | Extract PowerPoint (.pptx) per-slide text, tables, and speaker notes. |
| [processing-excel-files](processing-excel-files/SKILL.md) | Extract Excel/CSV data with correct types, dates, and formula results. |
| [processing-pdf-documents](processing-pdf-documents/SKILL.md) | PDF extraction, split/merge, redaction, forms (also listed above). |
| [extracting-text-with-ocr](extracting-text-with-ocr/SKILL.md) | Scans/images → accurate structured text (also listed above). |

**Communication, reporting & delivery skills** — the original core skills, now part of this category:
| Skill | Focus |
|---|---|
| [drafting-business-email](drafting-business-email/SKILL.md) | Draft/reply/rewrite emails in house tone, with tone/length variants. |
| [summarizing-meeting-notes](summarizing-meeting-notes/SKILL.md) | Raw notes/transcripts → decisions, action items, risks, open questions. |
| [summarizing-documents](summarizing-documents/SKILL.md) | Long docs/PDFs → exec summary, key points, risks, grounded Q&A. |
| [writing-status-reports](writing-status-reports/SKILL.md) | Scattered updates → RAG status report (4 variants) + JSON for the renderer. |
| [writing-change-notes](writing-change-notes/SKILL.md) | Changes → release notes (Keep a Changelog + SemVer) or a business change note. |
| [generating-data-reports](generating-data-reports/SKILL.md) | CSV + brief → a single self-contained HTML report with tables and charts. |
| [producing-branded-documents](producing-branded-documents/SKILL.md) | Render branded Word/PDF from templates with per-client logos + a validation gate. |
| [authoring-brand-guidelines](authoring-brand-guidelines/SKILL.md) | Create/maintain a human-facing brand style guide, kept in sync with the renderer's spec. |
| [document-branding-standards](document-branding-standards/SKILL.md) | Org-agnostic branding-profile foundation (logo/template/header-footer as swappable data) for any document-type skill. |
| [authoring-lessons-learned-docs](authoring-lessons-learned-docs/SKILL.md) | Generate a standardized Lessons Learned / retrospective `.docx` for any organization from a brand-agnostic template. |

## How they compose

- Draft with a craft skill (`writing-reports`, `writing-proposals`), then render
  with an application skill and [producing-branded-documents](producing-branded-documents/SKILL.md).
- `summarizing-meeting-notes` → `writing-status-reports` (emits `status.json`) →
  `producing-branded-documents` (renders the branded Word/PDF); `authoring-brand-guidelines`
  keeps that renderer's brand spec current.
- `crafting-presentation-narratives` (the story) → `building-powerpoint-decks`
  or `building-google-slides` (the artifact).
- `engineering-spreadsheets` (the model design) → `engineering-excel-workbooks`
  or `engineering-google-sheets` (the implementation) → `designing-dashboards`.
- **Any document task starts with ingestion:** `processing-documents` detects the
  type and routes to `processing-word-documents` / `processing-powerpoint-files` /
  `processing-excel-files` / `processing-pdf-documents` / `extracting-text-with-ocr`,
  then hands clean content to `summarizing-documents`, `comparing-documents`, or analysis.
- Every draft ends with `proofreading-text` and, when substantive, `editing-prose`.

## Cross-category links

Office skills pair with the other categories: draft with a craft skill, then
quality-gate with a [../review](../review/README.md) skill (e.g.
`writing-reports` ↔ [../review/reviewing-documents](../review/reviewing-documents/SKILL.md),
`designing-dashboards` ↔ [../review/reviewing-dashboards](../review/reviewing-dashboards/SKILL.md));
and they render deliverables produced by the [../business](../business/README.md)
and [../research](../research/README.md) skills.
