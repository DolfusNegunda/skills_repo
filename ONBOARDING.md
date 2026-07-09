# skills_repo — Project Onboarding

A 5-minute orientation for anyone new to this project (leads included). For the
full technical catalog see [README.md](README.md) and [skills-index.md](skills-index.md).

## What this is

`skills_repo` is a shared library of **Agent Skills** — reusable, procedural
"playbooks" that an AI agent loads on demand to do a task the right way. Each skill
is a folder with a `SKILL.md` (instructions, checklists, decision rules) plus
optional `references/`, `templates/`, and `scripts/`.

It follows the open [Agent Skills standard](https://agentskills.io): a skill is
discovered by its `description`, then its body is loaded only when a task needs it.

## Why it exists (the business case)

**Goal: run everyday office and document work on cheaper, smaller AI models while
keeping quality acceptable — by giving those models a baked-in expert procedure to
follow.**

A frontier model "just knows" how to structure a report, extract a table from a
messy PDF, or review a contract. A smaller, cheaper model often doesn't — unless you
hand it the steps. These skills *are* those steps: checklists, rubrics, templates,
and decision trees that let a low-cost model produce professional output. The payoff
is lower per-task cost at controlled quality, plus consistency (everyone's output
follows the same house standard) and institutional memory (the "right way" is
written down, not trapped in people's heads).

## What's been built (current status)

**87 skills** across five areas, each validated (frontmatter, naming, links):

| Area | Count | Covers |
|---|---|---|
| [office/](office/README.md) | 42 | Documents, spreadsheets, slides, email, PDF/OCR, **document ingestion**, and writing genres (reports, proposals, policies, minutes, exec summaries) + editing/proofreading/formatting/templates/automation/dashboards |
| [review/](review/README.md) | 15 | Evidence-based review of code, SQL, Python, docs, architecture, requirements, business cases, contracts, policies, research, designs, dashboards, presentations |
| [business/](business/README.md) | 18 | Analysis, requirements, process mapping, stakeholders, risk, project planning, roadmaps, KPIs/OKRs, SWOT, cost-benefit, decision matrices, business cases, change, governance, facilitation, negotiation |
| [research/](research/README.md) | 11 | Evidence collection, source credibility, fact-checking, scientific reading, citation, literature/comparative/market research, tech evaluation, synthesis |
| [skill-builder/](skill-builder/SKILL.md) | 1 | The meta-skill: how to author new skills in house style |

Plus your own document-branding and lessons-learned skills, generalized to work for
any organization.

## How it's used (two audiences)

**1. By the agent (primary).** An AI agent is configured with the system prompt in
[docs/agent-system-prompt.md](docs/agent-system-prompt.md). For every request it:
reads `skills-index.md` (the map) → matches the request to a skill → follows that
skill's procedure → runs its validation checklist. Document tasks always start by
*ingesting* the file with the right `processing-*` skill. This is what lets a cheap
model behave like an expert.

**2. By people.** Anyone can open a `SKILL.md` and use it directly as a
best-practice guide/checklist for doing the task themselves — no AI required. The
review skills double as team quality rubrics.

## How to get the most from it

- **Start every document task with ingestion.** Point the agent at the file; it
  detects the type and extracts faithfully before doing anything else. Garbage-in is
  the #1 quality failure — this prevents it.
- **Trust the index for routing.** If a request matches a skill's "when to use," the
  agent should use it. If nothing matches, that's a gap to build (that's what
  `skill-builder` is for).
- **Use review skills as gates.** Draft with an authoring skill, then run the
  matching review skill before anything ships.
- **Compose skills.** Real work chains them: ingest → summarize → draft → review →
  render. The category READMEs show the common chains.

## How quality stays high

- **A validator** (`skill-builder/scripts/validate_skills.py`) checks every skill's
  frontmatter, naming, links, and uniqueness. A **GitHub Action** runs it on every
  change, so nothing broken merges.
- **A generated index** (`skills-index.md`, via `generate_index.py`) can't drift from
  reality.
- **House style + a worked example** keep every skill consistent and discoverable.

## How to contribute a skill

1. Read [skill-builder/SKILL.md](skill-builder/SKILL.md) (the process + house style).
2. Create `<category>/<skill-name>/SKILL.md`; keep it lean, push depth to `references/`.
3. Run `python skill-builder/scripts/validate_skills.py` (must pass) and
   `python skill-builder/scripts/generate_index.py`.
4. Open a PR — CI re-validates automatically.

## For the project lead — the one-paragraph version

We've built a validated library of 87 reusable "how-to" skills so that cheaper AI
models (and people) can do office, document-processing, review, business-analysis,
and research work to a consistent professional standard. An agent reads a lightweight
index, picks the right skill for each request, and follows its baked-in procedure —
cutting cost while holding quality. It's on GitHub, auto-validated on every change,
and easy to extend. Best next steps: point the agent at real tasks to pressure-test
quality, and pick a license so it can be shared.
