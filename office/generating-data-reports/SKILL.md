---
name: generating-data-reports
description: Turns a CSV dataset plus a short brief into a single self-contained HTML report with summary statistics tables and charts embedded as base64 PNGs. Use when asked to generate a data report, summarize or visualize a CSV, analyze tabular data, or produce a shareable one-file HTML analysis from a spreadsheet export.
---

# Generating Data Reports

## Overview

This skill converts a CSV file and a one-or-two-sentence brief into a polished,
portable HTML report. The bundled script loads the data with pandas, computes
summary statistics for every numeric column, renders one or two matplotlib
charts (a trend line when a date-like column exists, a category bar chart when
a low-cardinality text column exists), and writes everything to a **single
.html file** — the charts are embedded as base64 PNG data URIs, so the report
can be emailed or dropped in a chat with no attachments or image folders.

## When to use this skill

- The user hands over a CSV (sales export, survey results, metrics dump) and
  asks for "a report", "a summary", "some charts", or "an analysis I can share".
- A recurring dataset needs a repeatable, scripted report rather than a
  hand-built one.
- The deliverable must be a single file that opens in any browser.

Do **not** use it for Word or PDF deliverables (see
`producing-branded-documents`), or for narrative status updates with no
dataset behind them (see `writing-status-reports`).

## Core principles

1. **One file out.** Everything — styles, tables, chart images — lives inside
   the generated HTML. Never write side-car PNGs or link external assets.
2. **Let the data pick the charts.** Date-like column present → trend line.
   Low-cardinality category column present → bar chart of totals. Neither →
   tables only, and say so; never force a meaningless chart.
3. **Fail loudly, fix quietly.** Missing files, empty datasets, and
   no-numeric-column CSVs produce specific, actionable error messages. Numeric
   values stored as text (e.g. `"$1,200"`) are coerced automatically.
4. **Brief drives the title, data drives the body.** Use the user's brief for
   the report title and framing; never invent numbers not present in the CSV.

## Workflow

Copy this checklist into your working notes and tick items off:

```
- [ ] Confirm the CSV path and skim its header row (column names, likely types)
- [ ] Extract a report title from the user's brief (fall back to the filename)
- [ ] Read references/report-structure.md if unsure which chart fits the data
- [ ] Run scripts/build_report.py with --data, --title, and --out
- [ ] If the script errors, fix the root cause it names (path, empty file,
      column types) — do not suppress the error
- [ ] Open/inspect the HTML: title correct, stats table populated, charts render
- [ ] Deliver the single .html file path to the user
```

## Examples

Generate the sample report shipped with this skill (run from the skill root,
`generating-data-reports/`):

```
python scripts/build_report.py --data examples/sample_sales.csv --title "Q2 Sales Snapshot" --out examples/output/report.html
```

A user-supplied dataset:

```
python scripts/build_report.py --data /path/to/support_tickets.csv --title "Support Ticket Volume, June 2026" --out /path/to/ticket-report.html
```

Expected output on success:

```
Report written: examples/output/report.html (rows: 14, numeric columns: 2, charts: 2)
```

## Anti-patterns

- **Writing chart PNGs next to the HTML.** Breaks portability; the script
  embeds base64 data URIs for a reason.
- **Hand-editing the generated HTML to "fix" numbers.** Fix the CSV or the
  script; the report must be reproducible from the command alone.
- **Piling every column into one chart.** Two focused charts beat one
  unreadable one; the script caps bar charts at its documented limit.
- **Swallowing script errors and shipping a blank report.** The error messages
  name the fix — apply it.
- **Reaching for Word/PDF conversion here.** Out of scope for this skill.

## Related skills

- `producing-branded-documents` — branded Word/PDF deliverables from templates.
- `writing-status-reports` — narrative status updates without a dataset.
- `summarizing-meeting-notes` — prose summaries, no tables or charts.

## Reference files

- `references/report-structure.md` — recommended report sections and a
  decision guide for choosing the right chart type for a given dataset.

## Dependencies

```
pip install pandas matplotlib
```

Python 3.9+ and the two packages above; nothing else. The script is fully
self-contained (no MCP servers, no network access, no external assets).
