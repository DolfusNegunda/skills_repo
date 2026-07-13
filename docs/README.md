# Documentation Index

Every document in this repo, grouped by who it's for. Start with the row that matches
you.

## For a project lead / manager

| Doc | What it gives you |
|---|---|
| [LEAD-BRIEF.md](LEAD-BRIEF.md) | One-page leadership briefing: business case, evidence, honest status, and the decisions to make. **Start here.** |
| [../ONBOARDING.md](../ONBOARDING.md) | 5-minute orientation — what the repo is, why it exists, what's built, how it's used. Ends with a one-paragraph version for the lead. |
| [benchmark-2026-07-full-library.md](benchmark-2026-07-full-library.md) | **Current** full-library quality assessment (all 151 skills, 12 dimensions incl. content correctness & model uplift). **Start here for quality.** |
| [correctness-audit-process.md](correctness-audit-process.md) | How content correctness is kept honest: the mechanical check, per-skill gate, and periodic adversarial audit. |

## For anyone new (non-technical welcome)

| Doc | What it gives you |
|---|---|
| [../ONBOARDING.md](../ONBOARDING.md) | The fastest way to understand the whole repo. |
| [USER-GUIDE.md](USER-GUIDE.md) / [user-guide.html](user-guide.html) | Plain-language guide — each skill in everyday terms with example phrases to say. No commands or setup. |
| [../skills-index.md](../skills-index.md) | A flat, generated list of every skill (name, when to use, path). |

## For someone running the AI agent

| Doc | What it gives you |
|---|---|
| [agent-system-prompt.md](agent-system-prompt.md) | The skill-first system prompt: read the index → match the skill → follow it → validate. Copy-paste ready. |

## For a maintainer / contributor

| Doc | What it gives you |
|---|---|
| [../README.md](../README.md) | The technical entry point: categories, layout, conventions, how to add a skill. |
| [../skill-builder/SKILL.md](../skill-builder/SKILL.md) | The meta-skill — house style, frontmatter rules, template, checklist, the determinism standard. |
| [skills-library.html](skills-library.html) | The technical catalog for setup/maintenance. |
| Category indexes | [../office/](../office/README.md) · [../review/](../review/README.md) · [../business/](../business/README.md) · [../research/](../research/README.md) · [../software-engineering/](../software-engineering/README.md) · [../data-engineering/](../data-engineering/README.md) · [../ai-engineering/](../ai-engineering/README.md) · [../reasoning/](../reasoning/README.md) · [../productivity/](../productivity/README.md) |
| [skills-catalog.md](skills-catalog.md) | The full backlog and roadmap. |

## Background / rationale

| Doc | What it gives you |
|---|---|
| [skill-selection-rationale.md](skill-selection-rationale.md) | The cited "why these skills" case. |
| [branded-templates-design.md](branded-templates-design.md) | Architecture of the branded-document templating system. |

## How quality is enforced (the machinery)

- `skill-builder/scripts/validate_skills.py` — consistency gate (frontmatter, naming,
  links, duplicates, script-gap + named-method-overclaim warnings). Currently **0 errors,
  0 warnings** (151 catalog skills + 1 worked example).
- `skill-builder/scripts/smoke_test_scripts.py` — runs every bundled document script
  against generated fixtures (**15/15**).
- `skill-builder/scripts/check_docs_fresh.py` — fails if a leadership doc's headline skill
  count or smoke-test count drifts from the canonical (derived) numbers.
- `skill-builder/scripts/generate_index.py` — regenerates `skills-index.md`.
- `.github/workflows/validate-skills.yml` — runs the validator, the smoke test, **and**
  the doc-freshness guard on every push/PR.
