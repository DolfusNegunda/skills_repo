---
name: reviewing-python
description: Review Python code for Pythonic idiom, structure, type hints, error handling, testing, performance, and packaging — beyond language-agnostic code review. Use when the user asks to "review this Python", "is this Pythonic", "check my Python code", or assess a Python module/package before merge. Inherits the general code-review dimensions and the shared severity/scoring model, adding Python-specific checks. Produces severity-ranked findings with idiomatic fixes and a verdict.
---

# Reviewing Python

## Scope
Python-specific code review layered on top of the language-agnostic
[reviewing-code](../reviewing-code/SKILL.md): idiom, typing, packaging, and the
Python gotchas a generic pass misses. Inherits severity/scoring from
[conducting-structured-reviews](../conducting-structured-reviews/SKILL.md).

## Purpose
Ensure Python code is correct *and* Pythonic, well-typed, testable, and packaged
right — catching the language's specific traps (mutable defaults, late binding,
broad excepts) that cause real bugs.

## When to use this skill
- "Review this Python / is this Pythonic / check my Python."
- Assessing a Python module, script, or package before merge.
- Improving Python code quality or modernizing an old codebase.

## When NOT to use this skill
- Non-Python code → [reviewing-code](../reviewing-code/SKILL.md) or [reviewing-sql](../reviewing-sql/SKILL.md).
- System design → [reviewing-architecture](../reviewing-architecture/SKILL.md).
- Writing/refactoring the code → an authoring skill.

## Inputs
- The Python code/package, target Python version, and its purpose.
- Whether it's a script, library, or service; existing tests and type coverage.
- Standards in play (PEP 8, project style, typing strictness).

## Outputs
- A review: verdict + scores, severity-ranked findings (file:line + why + idiomatic
  fix), and strengths.

## Evaluation rubric (dimensions)
Inherits the eight general code dimensions, specialized for Python:
1. **Correctness & Python gotchas** — mutable default args, late-binding closures,
   `is` vs `==`, integer/float, iterator exhaustion, mutating during iteration.
2. **Pythonic idiom** — comprehensions over manual loops, context managers,
   `enumerate`/`zip`, EAFP where apt, standard-library use over reinvention.
3. **Structure** — cohesive modules, small functions, no god-objects, clear `__init__`.
4. **Typing** — type hints on public APIs, correct generics/Optional, passes a type checker.
5. **Error handling** — specific exceptions, no bare `except:`, no swallowed errors, cleanup via `with`.
6. **Testing** — pytest coverage of behavior + edges; fixtures over duplication.
7. **Performance** — right data structures, generators for large data, no needless copies; avoid premature optimization.
8. **Packaging & deps** — `pyproject.toml`, pinned/managed deps, no unused imports, clean public surface.

## Scoring & severity
Score 1–5; rank Blocker→Praise (see
[foundation reference](../conducting-structured-reviews/references/severity-and-scoring.md)).
Examples: **Blocker** = mutable default `def f(x=[])` causing shared state, or bare
`except:` hiding failures; **Major** = untyped public API + no tests; **Minor** =
manual loop that should be a comprehension; **Nit** = import ordering.

## Workflow
```
Progress:
- [ ] 1. Understand purpose, version, and whether it's script/lib/service
- [ ] 2. Correctness + Python gotchas pass
- [ ] 3. Idiom + structure pass
- [ ] 4. Typing + error handling pass
- [ ] 5. Tests + performance + packaging pass
- [ ] 6. Severity-rank, score, verdict; idiomatic fixes per finding
```

## Recommended-improvements guidance
Show the idiomatic form: the comprehension, the context manager, the specific
exception, the type annotation, the missing test case, or the `pyproject`/dependency
fix. Reference file:line and keep the fix minimal.

## Validation checklist
- [ ] Python gotchas explicitly checked (mutable defaults, bare excepts, closures).
- [ ] Public APIs typed; passes a type checker if one is configured.
- [ ] Idiomatic constructs used where they improve clarity.
- [ ] Tests cover behavior and edges; run green.
- [ ] Packaging/deps sane; no unused imports.
- [ ] Findings carry file:line, severity, and an idiomatic fix; verdict + scores given.

## Common mistakes
- **Style-only feedback** (PEP 8 nits) missing a mutable-default bug.
- **Demanding types/idiom on throwaway scripts** — match the bar to the context.
- **Ignoring tests** while polishing style.
- **Over-engineering advice** — recommending abstractions a script doesn't need.

## Edge cases
- **Notebooks/scripts:** relax packaging/typing; keep correctness and gotchas.
- **Libraries:** raise the bar on typing, public API, and docs.
- **Async code:** check for blocking calls in async paths, un-awaited coroutines.
- **Legacy Python 2-isms:** flag and modernize.

## Related skills
- [reviewing-code](../reviewing-code/SKILL.md) — the general dimensions it extends.
- [conducting-structured-reviews](../conducting-structured-reviews/SKILL.md), [reviewing-sql](../reviewing-sql/SKILL.md).

## Examples
**Input:** "Review this Python util module before I publish it as a package."
**Output:** Verdict: Request changes (Typing 2/5, Correctness 3/5). **Blocker:**
`def add_tag(item, tags=[])` shares the list across calls; fix: default `None`, set
inside. **Major:** public functions untyped and untested. **Minor:** manual index
loop → `enumerate`. **Praise:** clean use of `pathlib` and context managers.

## Automation opportunities
- Run ruff/flake8, mypy/pyright, and pytest first; reserve review for judgment.
- Enforce "no bare except / no mutable default" via lint rules.
- Mirror the rubric in the project's contribution guide.
