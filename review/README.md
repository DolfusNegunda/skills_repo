# Review Skills

Structured, evidence-based review of any artifact — documents, code, architecture,
presentations, business cases, requirements, SQL, Python, contracts, policies,
research, manuscripts, designs, and dashboards. Every skill here follows the house
style in [../skill-builder/SKILL.md](../skill-builder/SKILL.md).

## Design philosophy

A review is not an opinion — it is a **repeatable evaluation against explicit
criteria** that produces findings a non-expert can act on. Every review skill in
this category delivers the same five things the master standard requires:

1. **Evaluation rubric** — the dimensions assessed.
2. **Scoring framework** — how each dimension is rated.
3. **Checklist** — the concrete items to inspect.
4. **Severity classification** — how findings are ranked (Blocker → Nit).
5. **Recommended improvements** — specific, actionable fixes, not just problems.

## Start here

**[conducting-structured-reviews](conducting-structured-reviews/SKILL.md)** is the
foundational skill. It defines the shared severity taxonomy, scoring scales, review
workflow, and reviewer conduct that every domain review inherits. Read it first;
the domain skills reference it rather than repeating it.

## The domain reviews

| Skill | Reviews | Anchored on |
|---|---|---|
| [reviewing-documents](reviewing-documents/SKILL.md) | Any written document | clarity, structure, accuracy, audience fit |
| [reviewing-code](reviewing-code/SKILL.md) | Source code (any language) | correctness, design, readability, security, tests |
| [reviewing-sql](reviewing-sql/SKILL.md) | SQL queries & schemas | correctness, performance, safety |
| [reviewing-python](reviewing-python/SKILL.md) | Python code | idiom, structure, typing, tests, packaging |
| [reviewing-architecture](reviewing-architecture/SKILL.md) | System/software architecture | fit, scalability, resilience, cost, risk |
| [reviewing-requirements](reviewing-requirements/SKILL.md) | Requirements & user stories | clarity, completeness, testability |
| [reviewing-business-cases](reviewing-business-cases/SKILL.md) | Business cases & investment asks | assumptions, financials, risk, alternatives |
| [reviewing-presentations](reviewing-presentations/SKILL.md) | Decks & talks | narrative, message, slide design |
| [reviewing-contracts](reviewing-contracts/SKILL.md) | Contracts & agreements | obligations, risk, ambiguity (not legal advice) |
| [reviewing-policies](reviewing-policies/SKILL.md) | Policies & procedures | enforceability, clarity, coverage |
| [reviewing-research](reviewing-research/SKILL.md) | Research & analysis | method, evidence, validity, bias |
| [reviewing-books](reviewing-books/SKILL.md) | Books & long manuscripts | structure, argument, craft, audience |
| [reviewing-designs](reviewing-designs/SKILL.md) | UI/UX & visual designs | usability, accessibility, hierarchy |
| [reviewing-dashboards](reviewing-dashboards/SKILL.md) | Dashboards & reports | decision-fit, chart honesty, clarity |

## How they compose

- Every domain review inherits severity + scoring from
  [conducting-structured-reviews](conducting-structured-reviews/SKILL.md).
- Reviews pair with their authoring counterparts: `reviewing-documents` ↔
  [../office/writing-reports](../office/writing-reports/SKILL.md);
  `reviewing-dashboards` ↔ [../office/designing-dashboards](../office/designing-dashboards/SKILL.md);
  `reviewing-business-cases` ↔ [../business/writing-business-cases](../business/writing-business-cases/SKILL.md).
- This category is the **critique counterpart to
  [../software-engineering](../software-engineering/README.md)**: `reviewing-code` ↔
  [../software-engineering/implementing-features](../software-engineering/implementing-features/SKILL.md),
  `reviewing-python` ↔ [../software-engineering/writing-automated-tests](../software-engineering/writing-automated-tests/SKILL.md),
  `reviewing-sql` ↔ [../software-engineering/authoring-sql-queries](../software-engineering/authoring-sql-queries/SKILL.md),
  `reviewing-architecture` ↔ [../software-engineering/designing-apis](../software-engineering/designing-apis/SKILL.md).
- `reviewing-sql` also gates work from
  [../data-engineering](../data-engineering/README.md) (e.g.
  [../data-engineering/ensuring-data-quality](../data-engineering/ensuring-data-quality/SKILL.md)).
- `reviewing-code` uses the same discipline as Claude Code's built-in `/code-review`
  but is portable and language-agnostic.
