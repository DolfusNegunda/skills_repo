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

**151 skills** across ten areas, each validated (frontmatter, naming, links), plus a
**determinism layer**: the document skills now ship **tested, runnable scripts** (not
just guidance) that validate produced files and ingest incoming ones — so a cheap
model runs a proven tool instead of improvising. All scripts are exercised
automatically in CI.

| Area | Count | Covers |
|---|---|---|
| [office/](office/README.md) | 42 | Documents, spreadsheets, slides, email, PDF/OCR, **document ingestion**, and writing genres (reports, proposals, policies, minutes, exec summaries) + editing/proofreading/formatting/templates/automation/dashboards |
| [review/](review/README.md) | 15 | Evidence-based review of code, SQL, Python, docs, architecture, requirements, business cases, contracts, policies, research, designs, dashboards, presentations |
| [business/](business/README.md) | 18 | Analysis, requirements, process mapping, stakeholders, risk, project planning, roadmaps, KPIs/OKRs, SWOT, cost-benefit, decision matrices, business cases, change, governance, facilitation, negotiation |
| [research/](research/README.md) | 11 | Evidence collection, source credibility, fact-checking, scientific reading, citation, literature/comparative/market research, tech evaluation, synthesis |
| [software-engineering/](software-engineering/README.md) | 14 | Implementing features, debugging, testing, refactoring, API design, patterns, Git, dependencies, packaging/release, performance, error handling, secure coding, SQL authoring |
| [data-engineering/](data-engineering/README.md) | 14 | Pipeline design, lakehouse & dimensional modeling, batch/streaming, incremental/CDC, orchestration, data quality, governance & lineage, schema evolution, Spark/warehouse performance, cost, observability |
| [ai-engineering/](ai-engineering/README.md) | 14 | Prompting, evaluation, context management, RAG, embeddings & vector search, agents, tool use, memory, structured outputs, LLM evals, guardrails, hallucination detection, AI system design |
| [reasoning/](reasoning/README.md) | 12 | Problem decomposition, root-cause & gap analysis, constraints, tradeoffs, deciding under uncertainty, prioritization, estimation, scenario planning, hypothesis testing, systems thinking, fallacy detection |
| [productivity/](productivity/README.md) | 10 | Daily/weekly planning, task & time management, task breakdown, personal knowledge management, note-taking, decision journaling, goal setting & tracking, learning plans, effective study |
| [skill-builder/](skill-builder/SKILL.md) | 1 | The meta-skill: how to author new skills in house style |

Plus your own document-branding and lessons-learned skills, generalized to work for
any organization.

**Quality has been benchmarked** against Anthropic's own method — the repo matches or
exceeds them on breadth, discoverability, and consistency; the one axis they led on
(executable, deterministic document tooling) has since been closed. See the current
assessment in
[docs/benchmark-2026-07-full-library.md](docs/benchmark-2026-07-full-library.md).

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
- **A smoke test** (`skill-builder/scripts/smoke_test_scripts.py`) generates real
  files and runs every bundled document script, asserting each behaves as documented
  — also enforced in CI, so the scripts can't silently rot.
- **A generated index** (`skills-index.md`, via `generate_index.py`) can't drift from
  reality.
- **House style, a determinism standard, and a worked example** keep every skill
  consistent, discoverable, and — where it produces files — backed by a tested tool.

## How to contribute a skill

1. Read [skill-builder/SKILL.md](skill-builder/SKILL.md) (the process + house style).
2. Create `<category>/<skill-name>/SKILL.md`; keep it lean, push depth to `references/`.
3. Run `python skill-builder/scripts/validate_skills.py` (must pass) and
   `python skill-builder/scripts/generate_index.py`.
4. Open a PR — CI re-validates automatically.

## For the project lead — the one-paragraph version

We've built a validated library of 151 reusable "how-to" skills so that cheaper AI
models (and people) can do office, document-processing, review, business-analysis,
research, software-, data-, and AI-engineering work (plus reasoning and productivity
methods) to a consistent professional standard. An agent reads a lightweight index,
picks the right skill for each request, and follows its baked-in procedure — cutting
cost while holding quality. Document work is backed by tested, deterministic scripts
(validated in CI), and quality has now been independently re-benchmarked against
Anthropic's own method. It's on GitHub, auto-checked on every change, and easy to
extend. Best next steps: run a real-task pilot to *measure* the cost/quality win, pick
a license so it can be shared, and act on the completed re-benchmark's follow-ups.

For the fuller leadership briefing (business case, evidence, decisions to make), see
[docs/LEAD-BRIEF.md](docs/LEAD-BRIEF.md).
