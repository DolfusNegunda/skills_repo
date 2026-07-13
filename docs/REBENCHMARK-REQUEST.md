# Re-benchmark — COMPLETED (2026-07-10)

> This file previously asked an independent agent to re-benchmark the repo after the
> document-script gap was closed. **That re-benchmark has been done.** This is now a
> pointer/changelog entry, not an open request.

## Outcome

The full-library re-benchmark ran on **2026-07-10** and lives at
**[benchmark-2026-07-full-library.md](benchmark-2026-07-full-library.md)** — read that for
the scorecard, evidence, and prioritized recommendations. Headline results:

- **Script gap confirmed closed.** Validator **0 errors / 0 warnings**; smoke test
  **14/14**; the produce → validate → fix → re-validate loop was exercised end-to-end.
- **Scope widened.** The benchmark now covers all **151 catalog skills across ten areas**
  (not just the original office/review/business/research batch), and added two dimensions
  the earlier scorecard lacked: **content correctness** and **model uplift**.
- **Real issues found and fixed.** ~10 grounded content-correctness errors (e.g. a RICE
  formula stated as a sum, a Spark join-salting pattern that silently dropped rows) were
  corrected, and three frontmatter over-claims (RACI/Kotter/SIFT) reconciled with their bodies.
- **A correctness feedback loop was added** so the class of error can't recur silently:
  a named-method-overclaim check in `validate_skills.py`, a doc-count guard
  (`check_docs_fresh.py`), and [correctness-audit-process.md](correctness-audit-process.md).

## Still open (tracked in the current benchmark)

- Leanness trim of the heaviest data-/AI-engineering bodies.
- Resolve a few genuine duplicate skills.
- **Excel formula recalculation:** a `recalculate_workbook.py` (headless LibreOffice) has
  been added and its fallback path tested, but the real recalculation path is **not yet
  verified in a LibreOffice-enabled environment** — do not claim that specific gap closed
  until it is.
- A correctness sample of the `review/` category (its reader hit a session limit; only
  structural inheritance was independently confirmed).

## Licensing constraint (unchanged, must hold)

`anthropics/skills` document skills (`docx`/`pdf`/`pptx`/`xlsx`) are source-available,
all-rights-reserved. **Describe and re-implement their *patterns*; never copy their files,
prose, script names, or layouts.** Everything here was authored fresh from our own
reference implementation. Keep it that way in any future work.
