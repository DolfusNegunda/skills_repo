---
name: designing-forms
description: Design forms and surveys that collect clean, complete, analyzable data — choosing the right question types, ordering and grouping fields, writing clear labels, adding validation, and minimizing friction and bias. Use when the user asks to "create a form/survey/questionnaire", "design an intake form", or improve a form's response quality. Covers Microsoft Forms, Google Forms, Typeform, and printable/PDF forms. Produces a form spec plus field-by-field design.
---

# Designing Forms

## Scope
The design of data-collection instruments — forms, surveys, questionnaires, intake
sheets — so the data that comes back is clean, complete, and analyzable. Tool-
agnostic (Microsoft/Google Forms, Typeform, PDF/print). Building fillable PDF
mechanics is [processing-pdf-documents](../processing-pdf-documents/SKILL.md).

## Purpose
Get high-quality data with minimum respondent effort: every field earns its place,
answers are constrained to valid values, and the results need no cleanup.

## When to use this skill
- "Create a form / survey / questionnaire / poll / intake form."
- "Improve my form" (low completion, messy data, biased results).
- Designing feedback, registration, application, or request forms.

## When NOT to use this skill
- Fillable-PDF mechanics/redaction → [processing-pdf-documents](../processing-pdf-documents/SKILL.md).
- Analyzing responses after collection → a data-analysis skill.
- Formal documents → the relevant writing skill.

## Inputs
- The decision the data will inform (this drives every field).
- Audience, channel (mobile/desktop/paper), and expected volume.
- Any required fields, compliance/consent needs, and downstream system schema.

## Outputs
- A form spec: ordered list of fields with type, label, help text, required/optional,
  validation rules, and answer options — ready to build in any form tool.

## Workflow
```
Progress:
- [ ] 1. Define the decision; list only the data that serves it
- [ ] 2. Choose a question type per field
- [ ] 3. Order and group logically; put easy/relevant first
- [ ] 4. Write clear, unbiased labels and help text
- [ ] 5. Add validation and required flags
- [ ] 6. Add logic (branching) and a confirmation
- [ ] 7. Test for friction, bias, and clean output
```

**Step 1 — Decision-first.** Start from what you'll do with the data. Delete any
field you can't tie to a decision — every extra field lowers completion.

**Step 2 — Question types.** Match type to data: single-select for mutually
exclusive options, multi-select for "all that apply", scales for intensity, short
text only when options can't enumerate it, dates via a date picker, numbers with
ranges. Prefer closed (constrained) over open text — closed data is analyzable.

**Step 3 — Order & group.** Group related fields into sections; put easy,
non-threatening questions first; ask sensitive/demographic questions last.

**Step 4 — Labels.** Write neutral, specific labels. Avoid leading, double-barreled
("rate speed and quality"), and jargon. Add help text/examples for anything ambiguous.

**Step 5 — Validation.** Constrain inputs: email format, number ranges, required
fields, character limits, dropdowns instead of free text. This is where clean data
is won or lost.

**Step 6 — Logic & confirmation.** Branch so respondents see only relevant
questions; confirm submission and set expectations for what happens next.

**Step 7 — Test.** Complete it yourself on mobile; check for friction, bias, and
whether the exported data is analysis-ready.

## Principles
1. **Every field must earn its place.** Length is the enemy of completion.
2. **Constrain answers.** Closed > open; dropdowns/validation > free text.
3. **Neutral wording.** The question must not lead the answer.
4. **Respect the respondent.** Short, clear, mobile-friendly, sensitive-questions-last.
5. **Design for the export,** not just the screen — plan the resulting columns.

## Decision framework
- **Mutually exclusive options?** Single-select. **Multiple apply?** Checkboxes.
- **Degree/intensity?** Balanced Likert (odd point count if a neutral is valid).
- **Can you enumerate answers?** Do — avoid free text.
- **Conditional questions?** Branching logic, not "skip if…" instructions.
- **High volume + downstream system?** Match field names/values to its schema.

## Common mistakes
- **Too many fields** — completion drops with every one.
- **Open text where options fit** — unanalyzable, inconsistent data.
- **Leading/double-barreled questions** — biased or unusable answers.
- **Unbalanced scales** (more positive than negative options) — skewed results.
- **No validation** — typos, wrong formats, and blanks pollute the dataset.
- **Sensitive questions up front** — abandonment.

## Validation checklist
- [ ] Every field maps to a decision; nothing extra.
- [ ] Question type fits the data for each field.
- [ ] Labels are neutral, specific, single-barreled.
- [ ] Scales are balanced; option lists are complete and mutually exclusive.
- [ ] Validation and required flags set; free text minimized.
- [ ] Branching hides irrelevant questions.
- [ ] Mobile-tested; consent/compliance included if needed.
- [ ] Exported columns are analysis-ready.

## Edge cases
- **Anonymous vs. identified:** state which; don't collect identity if it's meant to be anonymous.
- **Compliance (GDPR/consent/medical):** include explicit consent and lawful basis.
- **Accessibility:** labels tied to inputs, keyboard navigable, sufficient contrast.
- **Multilingual audiences:** translate carefully; keep option sets equivalent.
- **Paper/PDF forms:** leave enough space; use checkboxes over write-in where possible.

## Related skills
- [processing-pdf-documents](../processing-pdf-documents/SKILL.md) — build/flatten fillable PDFs.
- [extracting-text-with-ocr](../extracting-text-with-ocr/SKILL.md) — digitize returned paper forms.
- [engineering-excel-workbooks](../engineering-excel-workbooks/SKILL.md) / [engineering-google-sheets](../engineering-google-sheets/SKILL.md) — analyze responses.

## Examples
**Input:** "Event feedback survey, keep it short, we want NPS and top issues."
**Output:** 6-field spec — NPS 0–10 (single-select), one balanced satisfaction
Likert, a multi-select "what could be better" with an "Other" text, one open
"anything else", attendance-type (branching), and optional email — sensitive/
optional fields last, all validated, ~90 seconds to complete on mobile.

## Automation opportunities
- Pipe responses straight into a Sheet/Excel with a fixed schema for live analysis.
- Trigger follow-ups (thank-you, routing) on submission via a connector.
- Reuse a validated form spec as an org template for recurring collections.
