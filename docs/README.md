# Documentation Index

Every document in this repo, grouped by who it's for. Start with the row that matches
you.

## For a project lead / manager

| Doc | What it gives you |
|---|---|
| [LEAD-BRIEF.md](LEAD-BRIEF.md) | One-page leadership briefing: business case, evidence, honest status, and the decisions to make. **Start here.** |
| [../ONBOARDING.md](../ONBOARDING.md) | 5-minute orientation — what the repo is, why it exists, what's built, how it's used. Ends with a one-paragraph version for the lead. |
| [benchmark-vs-anthropic.md](benchmark-vs-anthropic.md) | The quality assessment vs. Anthropic's own skills — scorecard, gaps, and how they were closed. |
| [REBENCHMARK-REQUEST.md](REBENCHMARK-REQUEST.md) | The brief for an independent AI re-assessment (what changed, how to verify, what to re-score). |

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
| Category indexes | [../office/README.md](../office/README.md) · [../review/README.md](../review/README.md) · [../business/README.md](../business/README.md) · [../research/README.md](../research/README.md) |
| [skills-catalog.md](skills-catalog.md) | The full backlog and roadmap. |

## Background / rationale

| Doc | What it gives you |
|---|---|
| [skill-selection-rationale.md](skill-selection-rationale.md) | The cited "why these skills" case. |
| [branded-templates-design.md](branded-templates-design.md) | Architecture of the branded-document templating system. |

## How quality is enforced (the machinery)

- `skill-builder/scripts/validate_skills.py` — consistency gate (frontmatter, naming,
  links, duplicates, script-gap warning). Currently **0 errors, 0 warnings**.
- `skill-builder/scripts/smoke_test_scripts.py` — runs every bundled document script
  against generated fixtures (**12/12**).
- `skill-builder/scripts/generate_index.py` — regenerates `skills-index.md`.
- `.github/workflows/validate-skills.yml` — runs the validator **and** the smoke test
  on every push/PR.
