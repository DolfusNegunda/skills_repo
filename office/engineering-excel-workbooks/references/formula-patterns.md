# Excel Formula Patterns

Canonical, maintainable formulas. Prefer the modern function; the legacy fallback
is for older Excel only.

## Contents
- Lookups
- Conditional aggregation
- Text
- Dates
- Error handling
- Dynamic arrays
- Performance rules

## Lookups
| Need | Modern | Legacy fallback |
|---|---|---|
| Look up a value | `=XLOOKUP(key, keys, results, "not found")` | `=INDEX(results, MATCH(key, keys, 0))` |
| Two-way lookup | `=XLOOKUP(rowKey, rowKeys, XLOOKUP(colKey, colKeys, grid))` | `INDEX/MATCH/MATCH` |
| Approximate/banded | `=XLOOKUP(v, thresholds, bands, , -1)` | `VLOOKUP(...,TRUE)` on sorted table |

Never use `VLOOKUP` with a hardcoded column index — it breaks when columns move.

## Conditional aggregation
- Sum with criteria: `=SUMIFS(Sales[Amt], Sales[Region], "EMEA", Sales[Year], 2026)`
- Count: `=COUNTIFS(...)`; Average: `=AVERAGEIFS(...)`
- Multi-condition beyond IFS: `=SUMPRODUCT((cond1)*(cond2)*values)`

## Text
- Join: `=TEXTJOIN(", ", TRUE, range)`
- Split: `=TEXTSPLIT(cell, delimiter)` (modern) or Text-to-Columns / Power Query.
- Clean: `=TRIM(CLEAN(cell))` to strip stray spaces/non-printables.
- Format number as text: `=TEXT(value, "#,##0.00")`.

## Dates
- Always store real dates. Build with `=DATE(y,m,d)`.
- Difference in months: `=DATEDIF(start, end, "m")`.
- Month end: `=EOMONTH(date, 0)`. Add working days: `=WORKDAY(date, n, holidays)`.

## Error handling
- Meaningful default: `=IFERROR(XLOOKUP(...), "review")`. Prefer `IFNA` when you
  only want to trap missing lookups, so real errors still surface.
- Do not blanket-wrap everything in IFERROR — it hides genuine bugs.

## Dynamic arrays (modern Excel)
- Filter: `=FILTER(Data, Data[Status]="Open")`
- Unique list: `=UNIQUE(Data[Customer])`
- Sort: `=SORT(range, col, order)`
- Sequence: `=SEQUENCE(n)`. Spill references with `range#`.
- Reusable logic: `=LAMBDA(x, x*Rate)` named `ApplyRate`, then `=ApplyRate(A2)`.

## Performance rules
- Avoid volatile functions in bulk: `OFFSET`, `INDIRECT`, `TODAY`, `NOW`, `RAND`.
- Reference used ranges/Tables, not whole columns, in array-heavy formulas.
- Replace thousands of lookup formulas with Power Query merges or the data model.
- Turn off automatic calculation only temporarily during bulk edits.
