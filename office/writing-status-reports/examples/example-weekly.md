# Worked Example: Raw Updates to Client Status Report

A real-shaped pass through the workflow: messy inputs in, client-variant
report and data file out. The matching JSON is `status.json` in this folder.

## Input — raw updates as received

Slack thread, standup notes, and a ticket comment, verbatim:

```
[slack, Priya, Tue] dashboards: sales + ops + finance rebuilt and matching
old numbers. 5 more to go. margin dashboard is gnarly, might need Raj

[standup, Marco, Wed] cutover runbook first draft done, rollback section
still empty. also recon job flagged 2 null-rate breaches on the CRM feed,
turned out to be upstream, globex fixed same day

[ticket DPM-412, comment] Still no prod read access to Globex CRM.
Original request 2026-07-02. Chased their IT twice this week. This gates
the whole reporting cutover.

[slack, Dana, Fri] finance signed off revenue recon logic today. also FYI
I'm out mon-tue next week

[Marco, Fri] staging env for cutover dry-run is booked for thu next week
```

## Step-by-step

**Variant:** client (Globex receives this; it will be rendered by
producing-branded-documents), so: no internal ticket IDs, no "Dana is out
Mon-Tue", the null-rate incident framed as an outcome not a scare.

**Sorting:** finance sign-off and 3 dashboards → accomplishments; runbook and
remaining 5 dashboards → in progress; CRM access → blockers; dry-run and
dashboard completion → upcoming. The null-rate incident becomes an
accomplishment (detection worked, client fixed same day). Dana's absence and
"might need Raj" are internal — dropped.

**RAG:** the CRM access blocker is on the critical path and has been open
since 2026-07-02 — more than one reporting period. Per the RAG edge cases,
that is Amber even though everything else advanced. Summary must say what
returns it to Green: Globex IT granting access.

## Output — client-variant report

```markdown
# Weekly Project Update — Data Platform Migration
**Client:** Globex Corporation | **Week:** 28 | **Date:** 2026-07-10
**Prepared by:** D. Negunda | **Overall status:** Amber

## Summary
Delivery advanced on all fronts this week: revenue reconciliation logic is
signed off and three of eight executive dashboards are rebuilt and validated
against current figures. The project remains Amber solely due to the pending
production CRM read access (requested 2026-07-02), which gates the reporting
cutover; access this week would return the project to Green.

## Accomplishments
- Finance signed off the revenue reconciliation logic.
- Rebuilt and validated 3 of 8 executive dashboards (Sales, Operations,
  Finance) against current production figures.
- Nightly reconciliation checks detected two data-quality breaches on the CRM
  feed; the upstream issue was corrected by the Globex team the same day.

## In progress
- Rebuilding the remaining 5 executive dashboards.
- Drafting the cutover runbook; the rollback plan section is next.

## Blockers
- Awaiting production read access to the Globex CRM (requested 2026-07-02,
  requires Globex IT approval) — this blocks the reporting cutover and is the
  sole driver of the Amber status.

## Upcoming
- Dry-run the cutover in the staging environment (booked for Thursday).
- Complete the remaining dashboards and begin UAT.

## Notes
We recommend the CRM access request be raised at the Thursday steering
committee if not resolved beforehand.
```

## Output — data file

The same content as JSON per `references/status-data-contract.md`:
see [status.json](status.json). Render it with the sibling skill:

```bash
# from producing-branded-documents/
python scripts/fill_docx.py --data ../writing-status-reports/examples/status.json \
    --out output/globex-week-28.docx
python scripts/validate_output.py output/globex-week-28.docx
```

## What changed from raw to report (and why)

| Raw fragment | Became | Why |
| --- | --- | --- |
| "margin dashboard is gnarly, might need Raj" | (omitted) | Internal resourcing; no client-facing impact yet. |
| "recon job flagged 2 null-rate breaches" | Accomplishment about detection + same-day fix | The system worked; framed as value, credits the client's fast fix. |
| "Still no prod read access... DPM-412" | Blocker with date and unblocking party; no ticket ID | Client action needed; internal IDs stripped. |
| "Dana out mon-tue" | (omitted) | Internal-only. |
| Everything went well except one blocker | Amber, not Green | Critical-path blocker open >1 period (RAG edge case). |
