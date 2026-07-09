---
name: engineering-google-sheets
description: Build robust, collaborative Google Sheets — trackers, models, and reports — using structured layouts, array formulas, QUERY, IMPORTRANGE, data validation, and named ranges. Use when the user asks to "build a Google Sheet", "write a Sheets formula", create a collaborative tracker/model, or turn data into Sheets. Produces a maintainable, shareable spreadsheet. For Excel .xlsx, use engineering-excel-workbooks; for modeling theory, see engineering-spreadsheets.
---

# Engineering Google Sheets

## Scope
Building Google Sheets that are correct, collaborative, and maintainable: sheet
layout, formulas (including Sheets-specific `QUERY`, `ARRAYFORMULA`, `IMPORTRANGE`),
validation, named ranges, and sharing. Google-native counterpart to
[engineering-excel-workbooks](../engineering-excel-workbooks/SKILL.md); modeling
theory in [engineering-spreadsheets](../engineering-spreadsheets/SKILL.md).

## Purpose
Deliver a Sheet where numbers trace to inputs, formulas stay consistent as data
grows and multiple people edit, and structure survives collaboration.

## When to use this skill
- "Build a Google Sheet / tracker / model / calculator."
- "Write a Sheets formula" (QUERY, ARRAYFORMULA, VLOOKUP/XLOOKUP, IMPORTRANGE).
- Collaborative data collection or reporting in Sheets.
- Pulling data across sheets/files and summarizing it.

## When NOT to use this skill
- `.xlsx` deliverable → [engineering-excel-workbooks](../engineering-excel-workbooks/SKILL.md).
- Model design/assumptions → [engineering-spreadsheets](../engineering-spreadsheets/SKILL.md).
- Visual dashboard → [designing-dashboards](../designing-dashboards/SKILL.md).
- Large-scale ETL → a data pipeline, not Sheets.

## Inputs
- Purpose and the decision/output it serves.
- Source data or schema; whether it's collected in-sheet or imported.
- Collaboration model and sharing needs; refresh cadence.

## Outputs
- A Sheet with clear tabs (Inputs / Data / Calcs / Outputs), array-driven formulas
  that auto-expand, validated entry, named ranges, and correct sharing.

## Workflow
```
Progress:
- [ ] 1. Define outputs and the decision they drive
- [ ] 2. Lay out tabs: Inputs, Data, Calcs, Outputs
- [ ] 3. Structure data as a clean table with a header row
- [ ] 4. Build formulas: ARRAYFORMULA/QUERY over copy-down; reference named inputs
- [ ] 5. Add data validation and protected ranges
- [ ] 6. Set sharing; add a summary/QUERY dashboard
- [ ] 7. Audit totals and edge inputs
```

**Step 1 — Outputs first.** Know the answer before building.

**Step 2 — Tabs.** Separate Inputs (assumptions), Data (raw), Calcs (engine), and
Outputs (what users read). Colour input cells.

**Step 3 — Clean tables.** One header row, one record per row, no merged cells, no
blank spacer columns — this keeps QUERY, filters, and pivots reliable.

**Step 4 — Array-first formulas.** Prefer a single `ARRAYFORMULA` or `QUERY` at the
top of a column over dragging a formula down thousands of rows — it auto-expands
with new data and can't drift. Use `QUERY` for SQL-like slicing, `FILTER`/`SORT`/
`UNIQUE` for dynamic subsets, `IMPORTRANGE` to link source files (with a named-range
alias). Reference named inputs, never hardcode constants.

**Step 5 — Control input.** Data validation for dropdowns/ranges; protect the
Calcs/Data ranges so collaborators can only edit Inputs.

**Step 6 — Share & summarize.** Set edit/comment/view correctly; build a summary
tab with QUERY/pivot for the headline numbers.

**Step 7 — Audit.** Reconcile totals; test blank/zero/negative/huge inputs.

## Principles
1. **Array formulas over copy-down** — they self-extend and can't rot row by row.
2. **Separate inputs, data, logic, outputs.**
3. **Clean tabular data** is the precondition for QUERY/pivots working.
4. **Name inputs and ranges;** no hardcoded magic numbers.
5. **Protect what users shouldn't touch;** colour what they should.

## Decision framework
- **Slice/aggregate like SQL?** → `QUERY`.
- **Compute a whole column at once?** → `ARRAYFORMULA` (+ IF/ISBLANK guards).
- **Pull from another file?** → `IMPORTRANGE` (grant access once, alias it).
- **Dynamic subset?** → `FILTER`/`SORT`/`UNIQUE`.
- **Heavy/slow sheet?** → reduce volatile funcs and cross-file imports; consider a database.

## Common mistakes
- **Dragging formulas down** instead of one array formula — breaks as rows are added.
- **Merged cells / blank columns** — break QUERY, sort, and filter.
- **Overusing IMPORTRANGE** — slow, fragile, and a data-governance risk.
- **Volatile functions everywhere** (`NOW`, `TODAY`, `RAND`, big `INDIRECT`) — recalcs lag.
- **Everyone has edit access** — accidental structural damage.

## Validation checklist
- [ ] Tabs separate Inputs/Data/Calcs/Outputs; inputs colour-coded.
- [ ] Data is clean tabular (one header row, no merges/blanks).
- [ ] Column logic uses array formulas or QUERY, not fragile copy-down.
- [ ] No hardcoded constants; named ranges resolve.
- [ ] Validation on entry cells; protected ranges on logic/data.
- [ ] Totals reconcile; edge inputs behave.
- [ ] Sharing matches intended audience; IMPORTRANGE access granted.

## Edge cases
- **Large datasets:** Sheets slows past ~100k rows of formulas; use BigQuery
  Connected Sheets or reduce formula load.
- **Cross-file dependencies:** document them; a moved/renamed source breaks IMPORTRANGE.
- **Locale/date formats:** set the spreadsheet locale; store real dates.
- **Concurrent edits:** protect logic ranges; use suggestions/comments for changes.

## Related skills
- [engineering-excel-workbooks](../engineering-excel-workbooks/SKILL.md) — Excel equivalent.
- [engineering-spreadsheets](../engineering-spreadsheets/SKILL.md) — modeling discipline.
- [designing-dashboards](../designing-dashboards/SKILL.md), [generating-data-reports](../generating-data-reports/SKILL.md).

## Reference files
- [references/sheets-formulas.md](references/sheets-formulas.md) — QUERY, ARRAYFORMULA, IMPORTRANGE patterns.

## Examples
**Input:** "Team tracker: rows of tasks, auto status counts, one place to edit."
**Output:** Data tab with a validated Status column; an Outputs tab with
`=QUERY(Data!A:E, "select D, count(A) group by D")` for counts and an
`=ARRAYFORMULA` days-open column; protected Data structure; edit access to the team,
comment access to stakeholders.

## Automation opportunities
- Connected Sheets over BigQuery for large, refreshed data.
- Apps Script for scheduled imports, notifications, or form-to-sheet flows.
- Combine with [running-mail-merge](../running-mail-merge/SKILL.md) as the data source.
