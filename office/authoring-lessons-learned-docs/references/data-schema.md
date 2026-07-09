# Lessons Learned — Data Schema

Required `data` keys for `generate()`:
- `org_name`
- `project_code`
- `project_name`
- `project_manager`
- `cover_date`
- `metadata_date`
- `team` (list of `{name, position, allocation?}`)
- `deliverables_format` (`"A"` or `"B"`)
- `deliverables`
- `positives`
- `challenges`
- `learnings`

## Format A deliverables
`{"item": "1.1", "description": "...", "status_note": "Delivered on time..."}`

## Format B deliverables
`{"document": "Scope of Work", "status": "Delivered", "notes": "Signed 1 Jan 2026"}`

## Base template requirements
The base template must contain these headings verbatim:
- Project Team
- Deliverables
- Commentary on Project Execution
- Positives
- Challenges
- Learnings and Suggestions

It must also contain these tokens somewhere appropriate:
- `{{ORG_NAME}}`
- `{{PROJECT_CODE}}`
- `{{PROJECT_NAME}}`
- `{{PROJECT_MANAGER}}`
- `{{COVER_DATE}}`
- `{{METADATA_DATE}}`
