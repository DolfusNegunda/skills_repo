# Software Engineering Skills

Operational competencies for building software: turning requirements into working,
tested, secure, shippable code — and the delivery practices around it. Every skill
here follows the house style in [../skill-builder/SKILL.md](../skill-builder/SKILL.md).

## Design philosophy

These are **procedure and judgment skills** (like [../review](../review/README.md)),
not file generators — so they don't bundle scripts. Each adds what a generic model
can't guess: the *disciplined workflow*, the *decision rules*, and the *specific
mechanical gotchas* an expert engineer applies (grain/fan-out in SQL, non-sargable
predicates, big-bang commits, force-push on shared branches, swallowed exceptions,
optimizing before profiling). They are the **authoring counterpart** to the review
category: `review/` critiques an artifact; `software-engineering/` builds it.

## The skills

**Working in code**
| Skill | Focus |
|---|---|
| [implementing-features](implementing-features/SKILL.md) | Requirement → working, tested code in small green slices. |
| [debugging-systematically](debugging-systematically/SKILL.md) | Reproduce → isolate → fix the root cause → add a regression test. |
| [reading-unfamiliar-codebases](reading-unfamiliar-codebases/SKILL.md) | Orient fast: entry points, build/run, trace a flow, find where to change. |

**Code quality**
| Skill | Focus |
|---|---|
| [writing-automated-tests](writing-automated-tests/SKILL.md) | Test pyramid, what to test, deterministic AAA tests, coverage as a guide. |
| [refactoring-code](refactoring-code/SKILL.md) | Behavior-preserving change behind a test safety net, in small steps. |

**Design**
| Skill | Focus |
|---|---|
| [designing-apis](designing-apis/SKILL.md) | Contract-first REST/HTTP: resources, versioning, errors, idempotency, auth. |
| [applying-design-patterns](applying-design-patterns/SKILL.md) | Pick the pattern that fits — without over-engineering. |

**Delivery**
| Skill | Focus |
|---|---|
| [using-git-workflows](using-git-workflows/SKILL.md) | Branching, atomic commits, reviewable PRs, rebase vs merge, safe undo. |
| [managing-dependencies](managing-dependencies/SKILL.md) | Minimal deps, lockfiles, semver, safe updates, vulnerability response. |
| [packaging-and-releasing-software](packaging-and-releasing-software/SKILL.md) | SemVer, changelog, reproducible artifacts, release checklist, rollback. |

**Runtime quality**
| Skill | Focus |
|---|---|
| [optimizing-code-performance](optimizing-code-performance/SKILL.md) | Profile first, fix the real hotspot, verify with a benchmark. |
| [handling-errors-and-logging](handling-errors-and-logging/SKILL.md) | Fail-fast vs recover, structured logs, no secrets/PII in logs. |
| [writing-secure-code](writing-secure-code/SKILL.md) | Input validation, injection prevention, authn/z, secrets, OWASP mindset. |

**Data-adjacent**
| Skill | Focus |
|---|---|
| [authoring-sql-queries](authoring-sql-queries/SKILL.md) | Correct, sargable, injection-safe SQL; set-based thinking. |

## How they compose

- **Build a change:** [implementing-features](implementing-features/SKILL.md) (using
  [reading-unfamiliar-codebases](reading-unfamiliar-codebases/SKILL.md) to orient) →
  [writing-automated-tests](writing-automated-tests/SKILL.md) →
  [using-git-workflows](using-git-workflows/SKILL.md) → self-review, then gate with
  [../review/reviewing-code](../review/reviewing-code/SKILL.md).
- **Fix a defect:** [debugging-systematically](debugging-systematically/SKILL.md) →
  regression test → [refactoring-code](refactoring-code/SKILL.md) if structure was the cause.
- **New service/API:** [designing-apis](designing-apis/SKILL.md) +
  [applying-design-patterns](applying-design-patterns/SKILL.md) →
  [writing-secure-code](writing-secure-code/SKILL.md) +
  [handling-errors-and-logging](handling-errors-and-logging/SKILL.md) → implement → release.
- **Ship it:** [managing-dependencies](managing-dependencies/SKILL.md) →
  [packaging-and-releasing-software](packaging-and-releasing-software/SKILL.md)
  (notes via [../office/writing-change-notes](../office/writing-change-notes/SKILL.md)).

## Cross-category links

- **Review counterparts:** [../review/reviewing-code](../review/reviewing-code/SKILL.md),
  [../review/reviewing-python](../review/reviewing-python/SKILL.md),
  [../review/reviewing-sql](../review/reviewing-sql/SKILL.md),
  [../review/reviewing-architecture](../review/reviewing-architecture/SKILL.md) — draft here,
  gate there.
- **Requirements:** [../business/gathering-requirements](../business/gathering-requirements/SKILL.md)
  feeds [implementing-features](implementing-features/SKILL.md).
- **Docs:** [../office/writing-technical-documentation](../office/writing-technical-documentation/SKILL.md)
  for the READMEs/runbooks these skills produce.
