---
name: processing-excel-files
description: Ingest and extract data from Excel and CSV files (.xlsx/.xls/.csv) — reading each sheet's tables with headers, correct data types, dates, and formula results, into clean, structured, model-readable form. Use when the user gives you a spreadsheet to read, extract, or analyze, or asks to "read/parse this Excel/CSV", "pull the data from this workbook", or "get the tables out of this file". For building workbooks use engineering-excel-workbooks. Produces faithful tabular data with types preserved, not a mangled text scrape.
---

# Processing Excel Files

## Scope
Reading `.xlsx`/`.xls`/`.csv` into faithful tabular data: per-sheet tables, correct
headers, data types, dates, and formula *results* — handling the multi-sheet,
merged-cell, and type pitfalls. Ingestion, not authoring
([engineering-excel-workbooks](../engineering-excel-workbooks/SKILL.md)). Usually
reached via [processing-documents](../processing-documents/SKILL.md).

## Purpose
Get accurate data out of a spreadsheet — right types, right dates, the values a
formula produces — so analysis runs on correct numbers, not text-mangled or
misaligned data.

## When to use this skill
- "Read / parse / extract from this Excel or CSV file."
- "Pull the data / tables from this workbook."
- Ingesting spreadsheet data before analysis, reporting, or transformation.

## When NOT to use this skill
- Building/modeling a workbook → [engineering-excel-workbooks](../engineering-excel-workbooks/SKILL.md).
- Other formats → the matching processing skill via [processing-documents](../processing-documents/SKILL.md).
- Turning data into a report → [generating-data-reports](../generating-data-reports/SKILL.md).

## Inputs
- The file and what you need (which sheets, which ranges, values vs. formulas, headers).

## Outputs
- Structured tabular data (DataFrame/CSV/JSON) per sheet, with headers, correct
  types/dates, and a note on merged cells, multiple tables, or ambiguous ranges.

## Workflow
```
Progress:
- [ ] 1. Open with a proven library (pandas/openpyxl; csv for CSV)
- [ ] 2. Enumerate sheets; identify the real table region(s) per sheet
- [ ] 3. Detect header row(s); set correct data types and parse dates
- [ ] 4. Read formula RESULTS (values), not the formula strings, unless asked
- [ ] 5. Handle merged cells, blanks, and multiple tables per sheet
- [ ] 6. Verify totals/row counts against the source; check the fidelity warnings
```

The bundled `scripts/extract_workbook.py` does steps 1–5 deterministically for
`.xlsx`/`.csv` and emits a fidelity block — prefer it over an ad-hoc read:

```bash
python scripts/extract_workbook.py path/to/file.xlsx   # JSON per sheet + fidelity
```

**Step 2 — a sheet is not always one clean table.** There may be titles, blank
spacers, multiple stacked tables, or notes around the data — locate the actual table
region, don't assume A1 is the header. **Step 3 — types and dates are the classic
failures:** numbers read as text, and Excel serial dates read as integers (e.g.
`45000`) — set dtypes and parse dates explicitly. **Step 4 — values vs. formulas:**
read the computed values (`data_only=True` in openpyxl) unless the user wants the
formulas; note that a freshly-written file may have uncached formula values.
**Step 5 — merged cells** report their value only in the top-left cell — forward-fill
or flag, or rows misalign.

## Principles
1. **Preserve types and dates** — the #1 spreadsheet ingestion failure.
2. **Read formula results,** not formula text (unless asked).
3. **Find the real table region;** don't assume one clean table at A1.
4. **Handle merged cells and multiple tables** or rows misalign.
5. **Process every sheet** you need — data hides on other tabs.
6. **Verify totals/counts** against the source.

## Decision framework
- **Simple flat table?** pandas `read_excel`/`read_csv` with explicit dtypes.
- **Messy layout / need cell control?** openpyxl cell walk to find the region.
- **Formulas matter?** Read both values and formulas; state which you used.
- **Huge file?** Stream (`read_only`) / chunk; don't load all sheets at once.
- **CSV of unknown dialect?** Sniff delimiter/encoding first.

## Common mistakes
- **Dates as integers / numbers as text** — no explicit types.
- **Reading formula strings** instead of results.
- **Assuming A1 is the header** when titles/blanks precede the table.
- **Merged cells** silently misaligning rows.
- **Missing data on other sheets.**
- **CSV encoding/delimiter** misread (UTF-8 BOM, `;` vs `,`).

## Validation checklist
- [ ] Opened with a proven library; correct sheets targeted.
- [ ] Real table region(s) located; header row(s) correct.
- [ ] Data types set; dates parsed to real dates.
- [ ] Formula results read (or formulas, per the task) — stated which.
- [ ] Merged cells and multiple tables handled.
- [ ] Row counts/totals reconciled against the source.

## Edge cases
- **Multi-sheet workbooks:** enumerate and process each relevant sheet; label output by sheet.
- **Pivot tables/charts:** read the underlying data, not the rendered pivot.
- **Cross-sheet formulas:** results depend on other sheets — read values.
- **Locale dates/numbers:** DD/MM vs MM/DD, comma decimals — detect locale.
- **Very large/streamed:** use read-only mode; watch memory.

## Related skills
- [processing-documents](../processing-documents/SKILL.md) — the router that reaches this.
- [engineering-excel-workbooks](../engineering-excel-workbooks/SKILL.md) — the authoring counterpart.
- [generating-data-reports](../generating-data-reports/SKILL.md), [designing-dashboards](../designing-dashboards/SKILL.md).

## Examples
**Input:** "Pull the data from this financials workbook and total Q1 revenue."
**Output:** Enumerated 4 sheets; located the revenue table on "P&L" (skipping two
title rows); set numeric dtypes and parsed the month column as dates; read formula
*results* for the computed totals; forward-filled a merged "Region" column; verified
the extracted Q1 sum against the sheet's own total before reporting it.

## Scripts
- [scripts/extract_workbook.py](scripts/extract_workbook.py) — **run this** to ingest
  an `.xlsx`/`.csv` deterministically. Emits per-sheet JSON (header + typed rows, dates
  as ISO-8601, formula *results*, merged ranges, error cells) plus a `fidelity` block
  that flags what could not be read faithfully (uncached formulas, merged cells).
  Sniffs CSV delimiter/encoding (incl. UTF-8 BOM). Requires `openpyxl`.

## Automation opportunities
- The bundled extractor already does `xlsx/csv → clean per-sheet JSON`; chain its
  output into [generating-data-reports](../generating-data-reports/SKILL.md) or analysis.
