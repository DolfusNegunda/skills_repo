---
name: engineering-spreadsheets
description: Design sound spreadsheet models — the platform-agnostic discipline of structuring inputs, calculations, and outputs so a model is correct, auditable, and maintainable regardless of Excel or Sheets. Use when the user asks to "design/structure a model", "build a financial/forecast model", "my spreadsheet is a mess", or needs modeling best practices before implementation. Produces a model design and standards; implement it with engineering-excel-workbooks or engineering-google-sheets.
---

# Engineering Spreadsheets

## Scope
The modeling *discipline* — how to structure a spreadsheet so it's correct,
auditable, and maintainable — independent of the tool. The design layer above the
tool-specific [engineering-excel-workbooks](../engineering-excel-workbooks/SKILL.md)
and [engineering-google-sheets](../engineering-google-sheets/SKILL.md).

## Purpose
Prevent the failure mode of spreadsheets: models nobody can trust or safely change.
Establish structure and standards so every number is traceable and every assumption
is explicit — before a single formula is written.

## When to use this skill
- "Design / structure a model" or "build a financial / forecast / pricing model."
- "My spreadsheet is a mess / I don't trust these numbers."
- Setting modeling standards before implementation.
- Reviewing/refactoring an inherited model.

## When NOT to use this skill
- Tool-specific implementation → [engineering-excel-workbooks](../engineering-excel-workbooks/SKILL.md) / [engineering-google-sheets](../engineering-google-sheets/SKILL.md).
- A visual reporting layer → [designing-dashboards](../designing-dashboards/SKILL.md).
- Simple data entry/tracking → a basic sheet, no modeling discipline needed.

## Inputs
- The decision/output the model must produce and its required accuracy.
- Known drivers/assumptions and who owns them; data sources.
- Time horizon, scenarios, and how often it will change.

## Outputs
- A model design: structure (inputs/calcs/outputs), driver list, calculation flow,
  scenario approach, and a standards/conventions note — ready to implement.

## Workflow
```
Progress:
- [ ] 1. Define the output/decision and required precision
- [ ] 2. Identify drivers (assumptions) vs. calculations vs. outputs
- [ ] 3. Design the structure: one direction of flow
- [ ] 4. Plan calculation logic and granularity
- [ ] 5. Decide the scenario/sensitivity approach
- [ ] 6. Set conventions (naming, units, colour, checks)
- [ ] 7. Plan validation and audit checks
```

**Step 1 — Output first.** Model backward from the decision. Over-precision and
irrelevant detail are as harmful as inaccuracy.

**Step 2 — Classify everything.** Every cell is an **input** (assumption you set), a
**calculation** (derived), or an **output** (result). Confusing these is the root of
untrustworthy models. Inputs are the only things a user should change.

**Step 3 — One-directional flow.** Inputs → calculations → outputs, never looping
back. No circular references. This makes the model traceable and stops error
cascades.

**Step 4 — Logic & granularity.** Choose the right level of detail (monthly vs.
daily; per-product vs. total). More granular isn't more accurate — it's more to get
wrong. Build calculations in clear, single-purpose steps.

**Step 5 — Scenarios.** Design how assumptions flex: a scenario switch, a sensitivity
table, or a base/best/worst set — so "what if" doesn't mean editing the guts.

**Step 6 — Conventions.** Naming, consistent units (state them!), a colour code for
input vs. formula, and a documentation/assumptions log. Conventions are what let
someone else trust and edit the model.

**Step 7 — Checks.** Build in reconciliations (totals cross-foot), sanity checks
(ratios in expected ranges), and error flags. A model without self-checks silently
ships wrong numbers.

## Principles
1. **Separate inputs, calculations, and outputs** — the foundational rule.
2. **One-directional flow;** no circular references.
3. **Assumptions are explicit and owned,** never buried in formulas.
4. **Right granularity** — model to the decision, not to the maximum detail.
5. **Build in checks** — reconciliations and sanity flags catch errors early.
6. **Design for change** — scenarios via switches, not surgery.

## Decision framework
- **One-off estimate?** Simple structure; still separate inputs.
- **Reused/maintained model?** Full discipline: structure, conventions, checks, scenarios.
- **High-stakes (financial, board)?** Add independent review and an audit trail.
- **Frequent scenario analysis?** Design a scenario engine up front.

## Common mistakes
- **Assumptions hardcoded in formulas** — invisible, unchangeable, wrong when they change.
- **Mixing inputs and calculations** in the same area — no one knows what's safe to edit.
- **Circular references / two-way flow** — untraceable, unstable.
- **Over-granularity** mistaken for accuracy — more surface area for error.
- **No units stated** — the classic million/thousand and %/decimal disasters.
- **No checks** — errors ship silently; the model looks fine but isn't.

## Validation checklist
- [ ] Output and required precision defined; model built backward from it.
- [ ] Every cell classified input / calculation / output.
- [ ] Flow is one-directional; no circular references.
- [ ] Assumptions explicit, owned, and separated from logic.
- [ ] Granularity matches the decision, not maxed out.
- [ ] Units stated and consistent; naming conventions set.
- [ ] Reconciliation and sanity checks built in.
- [ ] Scenario/sensitivity approach designed.

## Edge cases
- **Inherited messy model:** map inputs/calcs/outputs first, add checks, then refactor incrementally.
- **Multi-contributor models:** conventions and protection are essential; agree ownership.
- **Long-horizon forecasts:** flag that uncertainty compounds; show ranges, not false precision.
- **Regulatory/financial models:** independent review and version control are mandatory.

## Related skills
- [engineering-excel-workbooks](../engineering-excel-workbooks/SKILL.md), [engineering-google-sheets](../engineering-google-sheets/SKILL.md) — implementation.
- [designing-dashboards](../designing-dashboards/SKILL.md) — the output/reporting layer.
- [writing-reports](../writing-reports/SKILL.md) — communicate the model's conclusions.

## Examples
**Input:** "Design a 3-year revenue forecast model we can run scenarios on."
**Output:** A design with an Inputs sheet of named drivers (growth %, churn, price,
headcount) owned by finance; a monthly Calcs engine flowing inputs→revenue→costs→
cash; a scenario switch (base/best/worst) driving the drivers; stated units ($000s);
colour conventions; and check rows (revenue reconciles, margins within plausible
bounds) — handed to implementation in Excel or Sheets.

## Automation opportunities
- Codify the standard structure and checks as a starter template.
- Automated audit: a checker that flags hardcoded constants and circular refs.
- Drive scenarios from a parameter table for repeatable analysis.
