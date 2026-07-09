# Workbook Architecture

Conventions that make a workbook auditable and safe to change.

## Contents
- Sheet layout
- Cell colour convention
- Naming
- Auditing
- Protection

## Sheet layout
Separate concerns onto distinct sheets, in flow order:

| Sheet | Contents |
|---|---|
| **Cover / README** | Purpose, owner, last updated, how to use, assumptions log. |
| **Inputs** | Every assumption/parameter, one per labelled cell, named. |
| **Data** | Raw source data in Excel Tables. No formulas here. |
| **Calcs** | The engine. Formulas only, referencing Inputs and Data. |
| **Outputs** | What the user reads: summaries, charts, export block. |

Data flows one direction: Inputs + Data → Calcs → Outputs. Never write back up.

## Cell colour convention
- **Blue font / light fill** = input the user may change.
- **Black** = formula / calculated, do not edit.
- **Green** = reference to another sheet.
- **Grey** = notes / labels.
Document this legend on the Cover sheet.

## Naming
- Name key inputs and outputs (`TaxRate`, `NetPresentValue`). Named cells make
  formulas readable and refactor-safe.
- Name Excel Tables meaningfully (`tblSales`, not `Table1`).
- Use scope deliberately: workbook-scope for shared constants, sheet-scope for locals.

## Auditing
- Trace precedents/dependents on every headline output.
- Cross-foot: row totals and column totals must reconcile to the grand total.
- Add a hidden check row: `=IF(ABS(check)<0.01,"OK","ERROR")`.
- Use Evaluate Formula to step through any formula you didn't write.

## Protection
- Lock all cells except inputs; protect the sheet so users can only edit inputs.
- Keep the raw Data sheet read-only or refreshed via Power Query.
- Never rely on hidden sheets for security — hide for tidiness only.
