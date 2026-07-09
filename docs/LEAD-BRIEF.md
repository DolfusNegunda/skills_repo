# skills_repo — Leadership Brief

A one-page briefing for a project lead or manager. Outcomes and decisions, not
implementation detail. For orientation see [../ONBOARDING.md](../ONBOARDING.md); for
the quality assessment see [benchmark-vs-anthropic.md](benchmark-vs-anthropic.md).

## The one-paragraph version

We've built and validated a shared library of **87 reusable "skill" playbooks** that
let **cheaper, smaller AI models do everyday office, document, review,
business-analysis, and research work at a consistent professional standard** — cutting
per-task AI cost while holding quality. Document work (Word/Excel/PowerPoint/PDF) now
runs through **tested, deterministic scripts**, so a cheap model runs a proven tool
instead of improvising. It's on GitHub, **auto-checked on every change** (all checks
green), benchmarked against Anthropic's own skills, and ready for an independent
quality re-assessment.

## Why it exists (the business case)

A frontier model "just knows" how to structure a report, extract a table from a messy
PDF, or review a contract. A smaller, cheaper model often doesn't — unless you hand it
the steps. These skills *are* those steps: checklists, rubrics, templates, decision
trees, and now runnable tools.

**The payoff:**
- **Lower cost per task** — run routine knowledge work on a cheaper model tier.
- **Controlled quality** — output follows a baked-in expert procedure, not guesswork.
- **Consistency** — everyone's output meets the same house standard.
- **Institutional memory** — the "right way" is written down, not stuck in people's heads.

## Where we are (evidence, not claims)

- **87 skills** across office, review, business, and research, each passing an automated
  quality gate (**0 errors, 0 warnings**).
- **Benchmarked against Anthropic's own published skills:** the repo **matches or
  exceeds** them on breadth, discoverability, and repository consistency.
- **The one axis Anthropic led on — executable, deterministic document tooling — is now
  closed.** 11 document skills ship tested scripts (validators that catch errors before
  a file ships; extractors that ingest files faithfully), all **verified automatically
  in CI (12/12 checks passing)** on every change.

## Honest status (so nothing is over-sold)

- The quality score on the tooling axis is currently **self-assessed**. A formal
  **re-benchmark request** ([REBENCHMARK-REQUEST.md](REBENCHMARK-REQUEST.md)) is ready
  so an independent AI pass can confirm it. A fair independent score may land slightly
  lower — that's expected and healthy.
- A few operations remain library-dependent and are documented as guidance, not yet
  scripted (e.g. PDF/PowerPoint table-structure fidelity, true redaction).
- The cost/quality win is **designed-in but not yet measured on your workload** — a
  pilot turns "should save money" into a number.

## Decisions to make

1. **Run a real-task pilot** on a representative workload to *measure* actual cost
   savings and quality. This is the highest-value next step.
2. **Pick a license** (e.g. MIT for open reuse, or keep internal) so it can be shared
   and rolled out.
3. **Commission the independent re-benchmark** before citing any quality numbers
   externally.

## How it's used (two audiences)

- **By an AI agent** — configured with [agent-system-prompt.md](agent-system-prompt.md),
  it reads a lightweight index, picks the right skill per request, and follows its
  procedure. This is what lets a cheap model behave like an expert.
- **By people** — anyone can open a skill as a best-practice checklist; the review
  skills double as team quality rubrics. No AI required.

## Where to read more

- [../ONBOARDING.md](../ONBOARDING.md) — 5-minute orientation for anyone new.
- [benchmark-vs-anthropic.md](benchmark-vs-anthropic.md) — the quality assessment.
- [REBENCHMARK-REQUEST.md](REBENCHMARK-REQUEST.md) — the independent re-assessment brief.
- [USER-GUIDE.md](USER-GUIDE.md) — plain-language guide for non-technical users.
