# Status Data Contract

## Contents
- Purpose and compatibility
- Field reference
- Writing rules per field
- Complete valid example
- Validation checklist

## Purpose and compatibility

The JSON emitted by `writing-status-reports` is the direct input to the
sibling skill `producing-branded-documents` (its `scripts/fill_docx.py`),
which renders the branded Word/PDF. The fields below mirror that skill's
`examples/sample_update.json` exactly — same names, same shapes. Do not add,
rename, or omit fields; an unexpected shape breaks the template fill.

## Field reference

| Field             | Type              | Content |
| ----------------- | ----------------- | ------- |
| `company_name`    | string            | Your company (the report author's firm). |
| `client_name`     | string            | Client's full display name. |
| `client_key`      | string            | Lowercase slug; selects the client logo (`assets/logos/clients/<client_key>.png` in producing-branded-documents). |
| `project_name`    | string            | Project or engagement name as the client knows it. |
| `week`            | string            | ISO week number as a string, e.g. `"27"`. |
| `report_date`     | string            | `YYYY-MM-DD`. |
| `prepared_by`     | string            | Author, e.g. `"D. Negunda"`. |
| `overall_status`  | string            | Exactly `"Green"`, `"Amber"`, or `"Red"` (title case — the renderer color-codes on these values). |
| `summary`         | string            | 2-4 sentences justifying the status; trajectory + biggest risk. |
| `accomplishments` | array of strings  | Completed this period. |
| `in_progress`     | array of strings  | Started, not yet done; include % or x-of-y where known. |
| `blockers`        | array of strings  | Each names the unblocking party, the date it arose/was requested, and what it blocks. |
| `upcoming`        | array of strings  | Planned for next period. |
| `notes`           | string            | Single string (not an array). Asks, escalations, context. `""` if none. |

## Writing rules per field

- **Array items are complete sentences** ending in a period — the renderer
  places them verbatim as bullets. One work item per string; no nested
  structure, no markdown inside strings.
- **`overall_status`** must match the RAG definitions in
  `report-variants.md`. Never `"green"`, `"AMBER"`, or compound values.
- **`summary`** must stand alone: a reader who sees only the status and the
  summary should know how the project is going and why.
- **`blockers`** may be an empty array `[]` when there are none — never
  `["None."]` or a placeholder.
- **`client_key`**: lowercase letters/digits/hyphens only; confirm the
  matching logo exists before rendering (Step 1 of the
  producing-branded-documents workflow).
- **Client variant only**: this JSON produces a client-facing document.
  Scrub internal names, ticket IDs, and internal system names before emitting.

## Complete valid example

See `examples/status.json` in this skill for a full file, or the upstream
reference `producing-branded-documents/examples/sample_update.json`. Skeleton:

```json
{
  "company_name": "ACME Consulting",
  "client_name": "Globex Corporation",
  "client_key": "globex",
  "project_name": "Data Platform Migration",
  "week": "28",
  "report_date": "2026-07-10",
  "prepared_by": "D. Negunda",
  "overall_status": "Amber",
  "summary": "Two to four sentences: trajectory, then the biggest risk.",
  "accomplishments": ["Completed sentence.", "Another completed sentence."],
  "in_progress": ["Item with quantified progress (3 of 8 complete)."],
  "blockers": ["Blocker with unblocking party and date, and what it blocks."],
  "upcoming": ["Planned item for next period."],
  "notes": "Optional asks or escalations; empty string if none."
}
```

## Validation checklist

Before handing the file to `producing-branded-documents`:

- [ ] Valid JSON (parses cleanly), UTF-8, no trailing commas
- [ ] All 14 fields present; no extras
- [ ] `overall_status` is exactly `Green`, `Amber`, or `Red`
- [ ] `report_date` is `YYYY-MM-DD`; `week` is a string
- [ ] Every array item is a complete sentence; `notes` is a string, not an array
- [ ] Content matches the client variant rules (nothing internal-only)
- [ ] `client_key` slug corresponds to a real logo file, or the fallback is acceptable
