# Model Layout Template

A starting sheet structure for any Excel model. Create these sheets in order.

```
[Cover]
  Purpose:        <one line>
  Owner:          <name>
  Last updated:   <date>
  How to use:     Edit only blue cells on Inputs.
  Legend:         Blue = input | Black = formula | Green = link
  Assumptions:    <bulleted list of key assumptions>

[Inputs]
  | Parameter        | Value | Unit | Notes |
  |------------------|-------|------|-------|
  | (named cells, blue)                     |

[Data]
  Excel Table(s) of raw data. No formulas.

[Calcs]
  Formulas referencing Inputs + Data. One formula per column.
  Include a check row that reconciles totals.

[Outputs]
  Summary block + charts. Read-only for users.
  Export-ready range if the workbook feeds another system.
```

Protect every sheet, unlocking only the blue Input cells.
