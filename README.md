# Skills Repository

A shared library of [Agent Skills](https://agentskills.io) for our data
engineering team. A skill is a folder with a `SKILL.md` that gives Claude a
reusable procedure, checklist, or body of domain knowledge — loaded only when
relevant, so it costs almost nothing until used.

## Start here

**[skill-builder/](skill-builder/SKILL.md)** is the meta-skill for building every
other skill in this repo. Read it before authoring a new one. It defines our
house style, the frontmatter rules, a copy-paste template, and a pre-publish
checklist.

**New here / non-technical?** Read the plain-language
**[docs/USER-GUIDE.md](docs/USER-GUIDE.md)** — or open
**[docs/user-guide.html](docs/user-guide.html)** in any browser. It explains each
helper in everyday terms with example phrases to say. No commands or setup needed.

**Setting these up / maintaining the repo?** The technical catalog is
**[docs/skills-library.html](docs/skills-library.html)**.

**Want the whole map at a glance?** **[skills-index.md](skills-index.md)** is a
flat, generated index of every skill (name, when to use, path) — regenerate it
with `python skill-builder/scripts/generate_index.py`.

## Featured skills

The meta-skill plus the original core communication/delivery skills (now part of
the **[office/](office/README.md)** category). For the full catalog, see the
category tables below.

| Skill | What it does |
|---|---|
| [skill-builder](skill-builder/SKILL.md) | Author new skills in house style (the meta-skill). |
| [producing-branded-documents](office/producing-branded-documents/SKILL.md) | Render branded Word/PDF from templates with per-client logos + a validation gate. |
| [summarizing-meeting-notes](office/summarizing-meeting-notes/SKILL.md) | Raw notes/transcripts → decisions, action items (owner + due), risks, open questions. |
| [drafting-business-email](office/drafting-business-email/SKILL.md) | Draft/reply/rewrite emails in house tone, with tone/length variants. |
| [writing-status-reports](office/writing-status-reports/SKILL.md) | Scattered updates → RAG status report (4 variants) + JSON for the renderer. |
| [writing-change-notes](office/writing-change-notes/SKILL.md) | Changes → release notes (Keep a Changelog + SemVer) or a business change note. |
| [summarizing-documents](office/summarizing-documents/SKILL.md) | Long docs/PDFs → exec summary, key points, risks/obligations, grounded Q&A. |
| [generating-data-reports](office/generating-data-reports/SKILL.md) | CSV + brief → a single self-contained HTML report with tables and charts. |
| [authoring-brand-guidelines](office/authoring-brand-guidelines/SKILL.md) | Create/maintain a human-facing brand style guide, kept in sync with the renderer's spec. |

**How they compose:** `summarizing-meeting-notes` → `writing-status-reports`
(emits `status.json`) → `producing-branded-documents` (renders the branded
Word/PDF). `authoring-brand-guidelines` keeps that renderer's brand spec current.

## Skill categories

Beyond the top-level skills above, the repo is organized into category folders.
Each has its own README index and cross-links to the others.

| Category | Skills | What it covers |
|---|---|---|
| **[office/](office/README.md)** | 42 | Word/Excel/PowerPoint, Outlook/Teams, Google Docs/Sheets/Slides, PDF/OCR/forms, the writing genres (reports, proposals, policies, technical docs, minutes, exec summaries), editing, proofreading, templates, mail merge, document automation, dashboards, presentation narrative, plus the core communication/delivery skills (business email, meeting-note & document summarization, status reports, change notes, data reports, branded-document rendering, brand guidelines). |
| **[review/](review/README.md)** | 15 | Structured, evidence-based review of documents, code, SQL, Python, architecture, requirements, business cases, presentations, contracts, policies, research, books, designs, and dashboards — all inheriting a shared severity/scoring model from `conducting-structured-reviews`. |
| **[business/](business/README.md)** | 18 | Business analysis, requirements, process mapping, stakeholder analysis, risk registers, project planning, roadmaps, KPIs, OKRs, SWOT, cost-benefit, decision matrices, business cases, change management, governance, meeting facilitation, negotiation, and stakeholder communication. |
| **[research/](research/README.md)** | 11 | Evidence collection, source credibility, fact verification, scientific reading, citation, literature reviews, comparative research, competitor analysis, market research, technology evaluation, and research synthesis. |
| **[software-engineering/](software-engineering/README.md)** | 14 | Implementing features, debugging, reading unfamiliar codebases, automated testing, refactoring, API design, design patterns, Git workflows, dependency management, packaging/release, performance optimization, error handling & logging, secure coding, and SQL authoring — the *authoring* counterpart to the review category. |
| **[data-engineering/](data-engineering/README.md)** | 14 | Pipeline design, lakehouse architecture, dimensional modeling, batch/streaming transformation, incremental loading & CDC, orchestration, data quality, governance & lineage, schema evolution, Spark & warehouse performance, cost optimization, and pipeline observability. |

Each skill is a thin house-style layer that adds *what good looks like* — structure,
rubrics, checklists, decision rules — and cross-links to related skills. All skills
are validated by `skill-builder/scripts/validate_skills.py` (frontmatter, naming,
links, duplicates). See each category README for the full index and composition map.

## Docs

- [docs/USER-GUIDE.md](docs/USER-GUIDE.md) / [docs/user-guide.html](docs/user-guide.html) — **simple guide for everyone** (non-technical).
- [docs/skills-library.html](docs/skills-library.html) — technical catalog for setup/maintainers.
- [docs/skills-catalog.md](docs/skills-catalog.md) — the full backlog and roadmap.
- [docs/skill-selection-rationale.md](docs/skill-selection-rationale.md) — the cited "why these skills" case.
- [docs/branded-templates-design.md](docs/branded-templates-design.md) — architecture of the templating system.

## Repository layout

```text
.
├── README.md
├── docs/                                   # Catalog, rationale, design, HTML docs
├── skills-index.md                         # Flat index of every skill (generated)
├── skill-builder/                          # Meta-skill + references/ + scripts/ + examples/
├── office/                                 # 42 office-productivity skills (see office/README.md)
├── review/                                 # 15 structured-review skills (see review/README.md)
├── business/                               # 18 business-analysis/planning skills (see business/README.md)
├── research/                               # 11 research skills (see research/README.md)
├── software-engineering/                   # 14 software-engineering skills (see software-engineering/README.md)
└── data-engineering/                       # 14 data-engineering skills (see data-engineering/README.md)
```

Every skill lives in a category folder (`office/`, `review/`, `business/`,
`research/`) as a `<skill-name>/SKILL.md` (required), optionally with
`references/`, `scripts/`, `assets/`, and `templates/` subfolders. Only
`skill-builder` (the meta-skill) sits at the repo root.

## Conventions

- **One skill, one job.** Split anything you can't describe in one sentence.
- **Naming.** Folder name = skill name = `/command`. Lowercase, hyphens, ≤64
  chars, gerund preferred (`authoring-dbt-models`). Never contains `claude` or
  `anthropic`.
- **Description is required and matters most.** Third person, states what it does
  **and** when to use it, with the terms a user would actually say.
- **Keep `SKILL.md` lean** (< ~500 lines). Push long material into `references/`,
  linked one level deep.
- **Forward slashes** in all paths, even from Windows.
- **Know your runtime.** `name` + `description` are portable everywhere. Fields
  like `allowed-tools` are Claude Code extensions; the claude.ai upload validator
  reads only `name` + `description`. See
  [skill-builder/references/frontmatter.md](skill-builder/references/frontmatter.md).

## Adding a new skill

1. Read [skill-builder/SKILL.md](skill-builder/SKILL.md) and copy the template
   from [skill-builder/references/skill-template.md](skill-builder/references/skill-template.md).
2. Create `<category>/your-skill-name/SKILL.md` in the fitting category folder
   (`office/`, `review/`, `business/`, or `research/`) and add it to that
   category's README index.
3. Run the mechanical gate: `python skill-builder/scripts/validate_skills.py`,
   then the human [authoring-checklist](skill-builder/references/authoring-checklist.md).
4. Regenerate the flat index: `python skill-builder/scripts/generate_index.py`.
5. Test it triggers on a realistic request, then open a PR.

## Using these skills in Claude Code

Point Claude Code at these skills by placing (or symlinking) a skill folder under
`.claude/skills/` in a project, or under `~/.claude/skills/` for personal use.
Invoke directly with `/skill-name`, or let Claude load one automatically when a
request matches its description.
