---
name: engineering-excel-workbooks
description: Build robust, auditable Microsoft Excel workbooks (.xlsx) — models, trackers, calculators, and reports — with clean structure, correct formulas, named ranges, data validation, tables, and pivot-ready data. Use when the user asks to "build an Excel spreadsheet", "create a model/tracker/calculator", "write a formula", fix a broken workbook, or turn data into an .xlsx. Produces a maintainable workbook, not a fragile one-off grid.
---

# Engineering Excel Workbooks

## Scope
Constructing `.xlsx` workbooks that are correct, auditable, and maintainable:
sheet architecture, formula design, named ranges, tables, data validation,
conditional formatting, and pivot-ready layouts. Platform-agnostic modeling
theory lives in [engineering-spreadsheets](../engineering-spreadsheets/SKILL.md);
dashboards in [designing-dashboards](../designing-dashboards/SKILL.md).

## Purpose
Deliver a workbook where every number is traceable to an input, formulas are
consistent across ranges, and someone else can safely change assumptions without
breaking the model.

## When to use this skill
- "Build/create an Excel spreadsheet, model, tracker, or calculator."
- "Write/fix an Excel formula" (XLOOKUP, SUMIFS, INDEX/MATCH, dynamic arrays).
- Turning raw CSV/data into a structured, analysis-ready workbook.
- Adding validation, dropdowns, or conditional formatting to control data quality.

## When NOT to use this skill
- Design of the underlying model (assumptions, structure) → [engineering-spreadsheets](../engineering-spreadsheets/SKILL.md).
- A visual dashboard is the goal → [designing-dashboards](../designing-dashboards/SKILL.md).
- Narrative/prose report → [writing-reports](../writing-reports/SKILL.md) or [generating-data-reports](../generating-data-reports/SKILL.md).
- Heavy transformation/ETL at scale → a data-engineering pipeline, not Excel.

## Inputs
- Purpose (what decision or output the workbook serves).
- Source data or its schema; expected volume and refresh cadence.
- Assumptions/parameters and who owns them.
- Required outputs (summary, charts, export).

## Outputs
- `.xlsx` with a clear sheet layout (Inputs / Calcs / Outputs / Data), Excel
  Tables for tabular data, named ranges for key inputs, validated entry cells,
  and consistent, filled-down formulas.
- A one-line map of where inputs live and where results surface.

## Workflow
```
Progress:
- [ ] 1. Define outputs and the decisions the workbook drives
- [ ] 2. Design the sheet layout (separate inputs, calcs, outputs, raw data)
- [ ] 3. Load/normalize data into Excel Tables
- [ ] 4. Build formulas: consistent, referenced to named inputs, no hardcoding
- [ ] 5. Add validation, dropdowns, and conditional formatting
- [ ] 6. Add summaries / pivots / charts on top of clean data
- [ ] 7. Audit: trace precedents, check totals, stress inputs
- [ ] 8. Recalculate (LibreOffice) so formula results are real, then validate & repair: fix every error, re-run until clean
```

**Step 1 — Outputs first.** Know the answer the sheet must produce before building.

**Step 2 — Separate concerns.** One sheet each for Inputs (assumptions), Calcs
(engine), Outputs (what users see), and Data (raw). Colour-code input cells so
users know exactly what is safe to change.

**Step 3 — Tables, not ranges.** Load tabular data into Excel Tables so formulas,
charts, and pivots auto-expand and use readable structured references
(`Sales[Amount]`).

**Step 4 — Formula discipline.** Reference named inputs, never hardcode a rate in
a formula. Keep each column's formula identical top to bottom. Prefer XLOOKUP and
SUMIFS over volatile/legacy patterns; prefer dynamic arrays over fragile copy-down.

**Step 5 — Control inputs.** Data validation and dropdowns stop bad entries;
conditional formatting flags outliers and errors.

**Step 6 — Summarize.** Build pivots/charts on the clean Data/Calcs layer.

**Step 7 — Audit.** Trace precedents on key outputs, reconcile totals, and stress-
test extreme inputs (zero, negative, blank) before delivery.

**Step 8 — Recalculate, then validate & repair (mandatory before delivery).** Do not
hand over a workbook you have only eyeballed. The validator reads *cached* formula
results (openpyxl cannot compute formulas), so **recalculate first** to make those
results real, then run the produce → recalculate → validate → fix → re-validate loop
until `status` is `OK`:

```bash
python scripts/recalculate_workbook.py path/to/workbook.xlsx   # writes *.recalc.xlsx
python scripts/validate_workbook.py path/to/workbook.recalc.xlsx
```

`recalculate_workbook.py` drives a headless LibreOffice pass that recomputes every
formula and writes fresh cached values. If LibreOffice is not installed it reports
`SKIPPED_NO_ENGINE` and exits 0 — in that case validate the original file and treat a
"no cached results" warning as an unresolved limitation, **not** a pass (never trust a
cached value you did not just recalculate). The validator then fails (exit 1) on stray
Excel error values (`#REF!`, `#DIV/0!`, …) and leftover placeholder text (`TBD`,
`{{tag}}`, …), and warns on merged cells, empty sheets, and external links.

## Principles
1. **Separate inputs, logic, and outputs.** Never bury an assumption inside a formula.
2. **One formula per column.** Consistency is auditability.
3. **Name what matters.** Named ranges/inputs make formulas self-documenting.
4. **No hardcoded magic numbers** in formulas — put them in labelled input cells.
5. **Data flows one direction:** raw → calc → output. No circular references.

## Decision framework
- **Lookup:** XLOOKUP (or INDEX/MATCH for legacy) over VLOOKUP.
- **Conditional aggregation:** SUMIFS/COUNTIFS/AVERAGEIFS over array hacks.
- **Growing data:** Excel Tables + structured references.
- **Repeated summary shapes:** PivotTables over hand-built formulas.
- **Reused calculation:** a named LAMBDA (modern Excel) over copy-paste.
- **Cross-workbook links:** avoid; consolidate or use Power Query instead.

## Common mistakes
- **Hardcoding constants** in formulas (tax rate, FX) — breaks silently when they change.
- **Inconsistent column formulas** — one edited cell corrupts an aggregate.
- **Merged cells** — they break sorting, filtering, and references. Use "center across selection".
- **Whole-column volatile formulas** (e.g. entire-column array math) — kills performance.
- **No error handling** — wrap risky lookups with IFERROR/IFNA meaningfully, not to hide bugs.
- **Data and presentation mixed** — makes refresh and reuse impossible.

## Known gotchas (mechanical, tool-specific)
- **openpyxl does not calculate formulas.** A workbook written by openpyxl has
  formula *strings* but no cached results, so `data_only=True` returns `None` for
  them and the validator cannot check for `#DIV/0!`/`#REF!`. Open and save once in
  Excel (or run a recalc step) to populate cached values, then validate.
- **`data_only=True` reads the last cached value, not the live one.** If a formula
  changed since the file was last opened in Excel, the cached result is stale. Never
  trust a cached value you did not just recalculate.
- **Dates are numbers.** Excel stores dates as serials; a "date" typed as text
  (`"2026-07-08"`) will not sort or calculate. Store real dates, format for display.
- **`read_only=True` speeds up large scans** but disables access to merged ranges
  and some structure — use the normal mode when you need `merged_cells`.
- **Merged cells hold their value only in the top-left cell**; the others read as
  `None`. This silently breaks lookups and aggregates over the range.
- **Leading apostrophe forces text** (`'0123`), so ZIP/ID codes keep leading zeros
  but no longer compute — intended for codes, a bug for numbers.

## Validation checklist
- [ ] Input cells are visually distinct and the only cells users edit.
- [ ] No hardcoded numbers inside formulas.
- [ ] Each column's formula is identical throughout its Table.
- [ ] No unintended circular references; iterative calc off unless intended.
- [ ] Totals reconcile (cross-foot rows and columns).
- [ ] Errors handled deliberately; no stray #REF!/#DIV/0!/#N/A.
- [ ] Edge inputs (0, blank, negative, max) behave correctly.
- [ ] Named ranges resolve; no broken external links.

## Edge cases
- **Large data (100k+ rows):** use Power Query / the data model, not cell formulas.
- **Multi-currency / multi-unit:** store the unit alongside the value; convert in calcs.
- **Dates across locales:** store as real dates, format for display; beware text dates.
- **Shared/concurrent editing:** avoid volatile functions and cross-file links.

## Related skills
- [engineering-spreadsheets](../engineering-spreadsheets/SKILL.md) — the modeling discipline.
- [engineering-google-sheets](../engineering-google-sheets/SKILL.md) — the Sheets equivalent.
- [designing-dashboards](../designing-dashboards/SKILL.md) — turning a workbook into a decision view.
- [generating-data-reports](../generating-data-reports/SKILL.md) — CSV → HTML report alternative.

## Reference files
- [references/formula-patterns.md](references/formula-patterns.md) — canonical formulas and when to use each.
- [references/workbook-architecture.md](references/workbook-architecture.md) — sheet layout, naming, and audit conventions.

## Scripts
- [scripts/recalculate_workbook.py](scripts/recalculate_workbook.py) — **run this first**
  in Step 8. Drives a headless LibreOffice pass to recompute every formula and write fresh
  cached values (openpyxl can't compute formulas), so the validator checks *real* results.
  Writes `*.recalc.xlsx`; degrades gracefully (`SKIPPED_NO_ENGINE`, exit 0) if LibreOffice
  is absent. Requires a LibreOffice install for the real path.
- [scripts/validate_workbook.py](scripts/validate_workbook.py) — **run this** on the
  recalculated file before delivery. Deterministic gate over a produced `.xlsx`: flags
  Excel error values and leftover placeholders (fail), and merged cells / empty sheets /
  external links (warn). Prints a JSON report and exits non-zero on error, so it drives the
  Step 8 fix-and-re-validate loop. Requires `openpyxl` (`pip install openpyxl`).

## Examples
**Input:** "Build a loan calculator: principal, rate, term → monthly payment and schedule."
**Output:** Inputs sheet with three validated cells (named `Principal`, `Rate`,
`Term`), an Outputs cell `=PMT(Rate/12, Term*12, -Principal)`, and a Calcs table
amortization schedule using structured references, with a chart of balance over time.

## Templates
- [templates/model-layout.md](templates/model-layout.md) — the Inputs/Calcs/Outputs/Data sheet convention.

## Automation opportunities
- Use Power Query to refresh source data without rebuilding formulas.
- Generate the workbook from a data source via [automating-document-generation](../automating-document-generation/SKILL.md).
- Named LAMBDA + Excel Tables make the model self-extending as data grows.
