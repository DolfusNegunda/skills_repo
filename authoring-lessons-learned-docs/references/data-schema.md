# Lessons Learned — Data Schema

## Contents
- Full field reference
- Example JSON
- Notes on optional fields

## Full field reference
The `data` dict passed to `generate()` in
[../scripts/generate_lessons_learned.py](../scripts/generate_lessons_learned.py)
must have these keys:

| Key | Type | Required | Notes |
|---|---|---|---|
| `project_code` | string | Yes | BSC job number, e.g. `"RI.2001"`. For multi-project documents, join codes as shown to the user, e.g. `"RI.1819 & RI.1839"`. |
| `project_name` | string | Yes | Full project name. For multi-project documents, separate with newlines. |
| `project_manager` | string | Yes | Name of the project manager / engagement lead. |
| `cover_date` | string | Yes | Date shown on the cover page, format `YYYY/MM/DD` (matches existing BSC convention). |
| `metadata_date` | string | Yes | Date shown in the identity table; often the more recent "as of"/sign-off date. Can differ from `cover_date`. |
| `team` | list of dict | Yes | Each item: `{"name": str, "position": str, "allocation": str (optional, e.g. "40%")}`. |
| `deliverables_format` | `"A"` or `"B"` | Yes | See [../SKILL.md](../SKILL.md) Step 3 for which to choose. |
| `deliverables` | list of dict | Yes | Shape depends on `deliverables_format` — see below. |
| `positives` | list of dict | Yes | Each item: `{"title": str, "comment": str}`. |
| `challenges` | list of dict | Yes | Each item: `{"title": str, "comment": str}`. |
| `learnings` | list of dict | Yes | Each item: `{"title": str, "actions": str}` — `actions` holds the combined lesson/recommendation/next-step text. |

### `deliverables` shape for Format A (`deliverables_format = "A"`)
```python
{"item": "1.1", "description": "SOW Document: outlines model scope...", "status_note": "Delivered on time, met quality bar."}
```
- `item`: proposal item number (string, e.g. `"1.1"`)
- `description`: the deliverable description; may include literal `\n` for
  bullet sub-points to match the source style
- `status_note`: optional one-line note on time/quality achievement,
  appended as a bullet under the description (omit if not applicable)

### `deliverables` shape for Format B (`deliverables_format = "B"`)
```python
{"document": "Scope of Work", "status": "Delivered", "notes": "Signed 1 Jan 2026"}
```
- `document`: name of the issued document/output
- `status`: short status label (e.g. `"Delivered"`, `"In progress"`) —
  existing documents prefix delivered items with a checkmark, e.g.
  `"✔ Delivered"`; match that convention when status is "done"
- `notes`: free-text notes

## Example JSON
```json
{
  "project_code": "RI.2001",
  "project_name": "Test Mining Co - Fleet Optimisation Study",
  "project_manager": "Jane Doe",
  "cover_date": "2026/07/08",
  "metadata_date": "2026/07/08",
  "team": [
    {"name": "Jane Doe (BSC)", "position": "Engagement Lead", "allocation": "40%"},
    {"name": "John Smith (BSC)", "position": "Simulation Consultant", "allocation": "80%"},
    {"name": "Client Contact (Test Mining Co)", "position": "Project Sponsor"}
  ],
  "deliverables_format": "B",
  "deliverables": [
    {"document": "Scope of Work", "status": "Delivered", "notes": "Signed 1 Jan 2026"},
    {"document": "Simulation Model", "status": "Delivered", "notes": "Validated against benchmark data"},
    {"document": "Final Report", "status": "In progress", "notes": "Due end of sprint 3"}
  ],
  "positives": [
    {"title": "Strong Client Collaboration", "comment": "Client was responsive and provided data quickly."}
  ],
  "challenges": [
    {"title": "Late Data Availability", "comment": "Key throughput data arrived 2 weeks late, compressing the validation timeline."}
  ],
  "learnings": [
    {"title": "Request Data Earlier", "actions": "Issue the data request register at kickoff, not after scoping sign-off."}
  ]
}
```

## Notes on optional fields
- `allocation` in each `team` member dict is the only truly optional leaf
  field. If **no** team member has an allocation value, the generation
  script omits the allocation column entirely (matches the RI1949-style
  team table). If at least one member has it, include `""` for members
  where it's unknown rather than omitting the key.
- All list fields (`team`, `deliverables`, `positives`, `challenges`,
  `learnings`) must have at least one entry — an empty section reads as a
  mistake, not a deliberate omission. If a project genuinely has nothing
  for one of these, ask the user how they'd like it represented (e.g. a
  single row noting "None identified") rather than leaving the table
  empty.
