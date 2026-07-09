# Google Sheets Formula Patterns

Sheets-specific patterns. Where Excel and Sheets share a function (SUMIFS, XLOOKUP,
INDEX/MATCH), see the Excel formula reference; below are the ones unique to Sheets.

## Contents
- QUERY
- ARRAYFORMULA
- IMPORTRANGE
- Dynamic subsets
- Guards and performance

## QUERY (SQL over a range)
`=QUERY(range, "select ... where ... group by ... order by ...", headerRows)`

Examples:
- Filter + pick columns: `=QUERY(Data!A:E, "select A, C where B = 'Open'", 1)`
- Aggregate: `=QUERY(Data!A:E, "select D, count(A) group by D order by count(A) desc", 1)`
- Date filter: `=QUERY(Data!A:E, "select * where C >= date '2026-01-01'", 1)`
- Reference a cell in the query string via concatenation:
  `=QUERY(Data!A:E, "select A where B = '"&F1&"'", 1)`

Notes: column letters are relative to the range; wrap literal dates in `date '...'`;
`label`/`format` clauses rename and format output columns.

## ARRAYFORMULA (compute a whole column once)
Put one formula in the header-adjacent cell instead of dragging down:
```
=ARRAYFORMULA(IF(ISBLANK(A2:A), "", A2:A * Rate))
```
- Always guard against blank rows with `IF(ISBLANK(...),"",...)` so the column
  doesn't fill the entire sheet with results.
- Combine with `IFERROR`, `VLOOKUP`/`XLOOKUP`, and arithmetic across ranges.
- Auto-extends as new rows arrive — no copy-down maintenance.

## IMPORTRANGE (link another file)
```
=IMPORTRANGE("spreadsheet_url_or_key", "Sheet1!A1:E")
```
- Grant access once when prompted; the connection persists.
- Alias imports with a named range to keep formulas readable.
- Use sparingly: each import is a recalculation and data-governance dependency.
  A moved/renamed source silently breaks it.

## Dynamic subsets
- `=FILTER(range, condition1, condition2)` — rows meeting all conditions.
- `=SORT(range, colIndex, TRUE/FALSE)` — ordered output.
- `=UNIQUE(range)` — distinct values/rows.
- `=SEQUENCE(rows, cols, start, step)` — generated series.
These "spill" — leave empty space below/right for the result.

## Guards and performance
- Wrap lookups in `IFNA`/`IFERROR` with a meaningful default.
- Minimize volatile functions (`NOW`, `TODAY`, `RAND`, broad `INDIRECT`).
- Prefer one ARRAYFORMULA/QUERY to thousands of cell formulas.
- For big or refreshed data, use Connected Sheets (BigQuery) instead of formulas.
