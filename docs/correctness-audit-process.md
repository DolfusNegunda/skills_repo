# Content-Correctness Audit Process

The validator and script smoke-test catch *structural* and *mechanical* faults. Neither
catches a knowledge skill that is well-structured, confident, and **factually wrong** —
the highest-severity failure mode for a library deployed to cheaper models in client
environments, which cannot sanity-check authoritative-but-wrong guidance. This process
closes that gap. It complements, does not replace, `validate_skills.py`.

## Three layers

**1. Mechanical (every run, automated).** `validate_skills.py` now flags any description
that advertises a distinctive named framework (RACI, Kotter, SIFT, RICE, SWOT, BATNA, …)
the body never uses — the "frontmatter over-claim" class. Extend `NAMED_METHODS` in the
script when a new named method enters the library. Advisory warning; align the frontmatter
with the method actually taught.

**2. Per-skill (at authoring time, human).** Before publishing a technical skill, the
author runs the Content-Correctness gate in
[../skill-builder/references/authoring-checklist.md](../skill-builder/references/authoring-checklist.md):
every load-bearing claim (formulas, algorithm steps, framework definitions, "always/never"
absolutes) is checked against a primary source, and worked-example arithmetic is
reproduced. A claim that is contested pop-wisdom is framed as such, not as settled fact.

**3. Periodic (cadence, adversarial).** Run a full-library claim-audit:
- **On every new technical skill** (ai/data/software-engineering, and any skill making
  quantitative or algorithmic claims) before it merges.
- **Quarterly** across the whole library, or after any batch of ≥10 new skills.

### How to run a periodic audit (the method used in July 2026)

1. One file-grounded reader per category (parallel). Each reads *every* SKILL.md and
   returns, per category: structure conformance, **≥2 verified-correct and ≤3
   wrong/oversimplified claims each cited `skill:line`**, staleness flags, model-uplift
   judgment, and redundancy flags.
2. **Re-verify every Major/consequential finding yourself** against the cited line before
   it drives an edit — readers are single-source and can misread. Mark each finding
   *confirmed* vs *reader-reported*.
3. Fix confirmed findings; re-run `validate_skills.py`, `smoke_test_scripts.py`, and
   `generate_index.py`.
4. Log the audit as a dated `docs/benchmark-<date>-*.md` so correctness has a paper trail.

## Highest-risk claim types (look hardest here)

Formulas stated in prose (RICE, NPV/IRR, ROI); algorithm steps that silently lose data
(join-salting, MERGE without dedup, CDC without delete-reconciliation); framework
definitions (CRAAP, ADKAR, SCD types); "always/never" absolutes; and any statistic
presented without a source. These are where the July 2026 audit found all its real errors.
