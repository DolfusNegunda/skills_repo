# Re-benchmark Request — skills_repo vs. anthropics/skills

**To the benchmarking agent:** the repo has changed materially since the last
assessment. This brief tells you *what changed*, *how to verify it yourself*, and
*what to re-score*. Please run a fresh, file-grounded benchmark and quality
assessment — do not rely on the previous report's numbers; several are now stale.

## Why you're being asked again

The previous benchmark's single biggest finding was correct and has now been acted
on: **executable, deterministic scripts for document work** (the one axis where
Anthropic's flagship `docx`/`xlsx`/`pptx` skills clearly led). That gap has been
closed for every local document skill. Re-benchmark to confirm — independently.

## What changed since the last version

**1. Script coverage: 4 → 11 skills.** Every local file-producing/processing office
skill now ships a tested `scripts/` tool wired into its `## Workflow`:

| Skill | Script | Pattern |
|---|---|---|
| engineering-excel-workbooks | `validate_workbook.py` | producer: validate → fix → re-validate loop |
| authoring-word-documents | `validate_docx.py` | producer: same loop |
| building-powerpoint-decks | `validate_pptx.py` | producer: same loop |
| processing-documents | `detect_type.py` | router: signature detection + routing (stdlib) |
| processing-word-documents | `extract_docx.py` | processor: extract + fidelity self-check |
| processing-excel-files | `extract_workbook.py` | processor: extract + fidelity |
| processing-powerpoint-files | `extract_pptx.py` | processor: extract + fidelity |
| processing-pdf-documents | `extract_pdf.py` | processor: extract + text-vs-scanned classify |

(Pre-existing: `producing-branded-documents`, `generating-data-reports`,
`authoring-lessons-learned-docs`.)

**2. Reproducible test harness in CI.** `skill-builder/scripts/smoke_test_scripts.py`
generates real `.xlsx`/`.docx`/`.pptx`/`.pdf`/`.csv` fixtures and asserts each script's
exit code and verdict (12/12 checks). It runs in
`.github/workflows/validate-skills.yml` alongside the consistency validator.

**3. Determinism is now an enforced authoring standard.** New "Determinism" section in
`skill-builder/references/authoring-checklist.md`; a script-bundling note in
`skill-builder/references/skill-template.md`; and a scoped warning in
`skill-builder/scripts/validate_skills.py` that flags any local file-producing/
processing skill with no `scripts/` (currently **0 hits**). Google Workspace (API)
skills are deliberately exempt — they produce cloud documents, not local files.

**4. Correctness note:** two fidelity-detection bugs in `extract_docx.py` (always-true
header/footer flags; substring false-positives on footnotes/comments) were fixed to use
body-reference detection. See git history.

**Count correction:** the repo is **87 skills** (office 42 / review 15 / business 18 /
research 11 / meta 1), not 83 — the earlier snapshot predated the ingestion skills.

## Verify it yourself (don't take this brief's word)

```bash
python skill-builder/scripts/validate_skills.py        # expect 0 errors, 0 warnings
pip install openpyxl python-docx python-pptx pypdf reportlab
python skill-builder/scripts/smoke_test_scripts.py     # expect 12/12 checks passed
find office -type d -name scripts | sort               # expect 11 skills
```

Read the actual scripts and their wired `## Workflow` / `## Scripts` sections. Confirm
the loop is real (JSON errors → fix → re-run), not a one-time lint.

## What to re-score

- **Dimension 4 (executable scripts / determinism)** — previously the repo trailed
  Anthropic badly here. Re-assess against the 11 scripts + CI smoke test.
- Whether the **produce → validate → fix → re-validate loop** is genuinely wired (read
  the workflows), and whether **extractor fidelity self-checks** are sound.
- Anything still **over-claimed**: call out any script that is inert, untested, or whose
  SKILL.md promises more than the script delivers.
- Remaining honest gaps: PDF/PPTX **table-structure** fidelity and **true redaction** are
  still library-dependent operations documented in references, not scripted. Excel
  formula-error detection needs an external recalc (openpyxl doesn't compute formulas).

## Licensing constraint (unchanged, must hold)

`anthropics/skills` document skills (`docx`/`pdf`/`pptx`/`xlsx`) are source-available,
all-rights-reserved. **Describe and re-implement their *patterns*; never copy their
files, prose, script names, or layouts.** Do not clone, vendor, or retain their content
— even temporarily. Everything in this repo was authored fresh from our own reference
implementation (`producing-branded-documents/scripts/validate_output.py`). Keep it that
way in any recommendation you make.

## Deliverable

A fresh scorecard (same 10 dimensions as `benchmark-vs-anthropic.md`), a verdict on
whether the script gap is genuinely closed, and a prioritized list of what remains —
grounded in files you actually read and commands you actually ran.
