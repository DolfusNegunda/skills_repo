# Skills Repository

A shared library of [Agent Skills](https://agentskills.io). A skill is a folder
with a `SKILL.md` that gives an agent a reusable procedure, checklist, or body
of domain knowledge — loaded only when relevant, so it costs almost nothing
until used.

This repo is maintained by the Skills Builder agent.

## Start here

- **[skills-index.md](skills-index.md)** — the map of every skill. Read this
  first; open a skill's `SKILL.md` only when a task needs it.
- **[skill-builder/](skill-builder/SKILL.md)** — the meta-skill for building
  every other skill here. It defines the house style, frontmatter rules, a
  copy-paste template, and a pre-publish checklist.

## Layout

```text
.
├── README.md
├── skills-index.md             # The map, read first
└── skill-builder/
    ├── SKILL.md                # The meta-skill: how to build skills
    ├── references/             # Deep guidance, loaded on demand
    │   ├── frontmatter.md
    │   ├── skill-template.md
    │   ├── authoring-checklist.md
    │   └── anti-patterns.md
    └── examples/
        └── authoring-dbt-models/SKILL.md   # Worked example
```

Each new skill is a top-level folder with a `SKILL.md` (required) and,
optionally, `references/`, `scripts/`, and `assets/` subfolders.

## Adding a new skill

1. Follow the process in [skill-builder/SKILL.md](skill-builder/SKILL.md) and
   copy the template from
   [skill-builder/references/skill-template.md](skill-builder/references/skill-template.md).
2. Create `your-skill-name/SKILL.md` at the repo root.
3. Validate against
   [skill-builder/references/authoring-checklist.md](skill-builder/references/authoring-checklist.md).
4. Add a one-line row for it to [skills-index.md](skills-index.md).

## Conventions

- **One skill, one job.** Split anything you can't describe in one sentence.
- **Naming.** Folder name = skill name = `/command`. Lowercase, hyphens, ≤64
  chars, gerund preferred. Never contains `claude` or `anthropic`.
- **Description matters most.** Third person, states what it does **and** when
  to use it, with the terms a user would actually say.
- **Keep `SKILL.md` lean** (< ~500 lines). Push long material into `references/`,
  linked one level deep.
- **Forward slashes** in all paths, even from Windows.
