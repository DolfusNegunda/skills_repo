---
name: writing-status-reports
description: Turn scattered task updates, standup notes, and ticket comments into a structured status report with a Red/Amber/Green status, in individual, team roll-up, executive, or client variants. Use when writing a weekly status report, project update, RAG status, team roll-up, or the content for a client-facing progress report.
---

# Writing Status Reports

## Overview
Converts raw, unordered progress material — standup notes, ticket comments,
chat snippets, half-finished lists — into a clean status report with an honest
RAG (Red/Amber/Green) status. It produces the *content* in two forms: readable
markdown for the chosen audience, and a JSON data file that the sibling skill
`producing-branded-documents` renders into the branded Word/PDF deliverable.

## When to use this skill
- "Write my weekly status report" / "turn these notes into a status update"
- Rolling up several people's updates into one team report
- Preparing an executive summary or steering-committee update from project detail
- Drafting the content for a client-facing progress report (before branding)
- Deciding or defending a RAG status ("are we Amber or Red?")

## Core principles
1. **Status is a verdict, not a mood.** Pick Green/Amber/Red from the RAG
   definitions in [references/report-variants.md](references/report-variants.md),
   then make the summary justify it. Never let optimism upgrade the color.
2. **Sort by audience, not by source.** The same facts become four different
   reports (individual, team, executive, client). Choose the variant first;
   it decides what to keep, cut, and reword.
3. **Every item is an outcome with an owner.** "Worked on dashboards" becomes
   "Rebuilt 3 of 8 executive dashboards (Priya)". Verb, object, quantity where known.
4. **Blockers name the unblocking party and the date.** A blocker without who
   can clear it and since when is a complaint, not a status item.
5. **Emit data, not just prose.** Finish by writing the JSON per
   [references/status-data-contract.md](references/status-data-contract.md) so
   the branded document can be generated without re-extraction.

## Workflow

Copy this checklist and track progress:

```
Status report progress:
- [ ] 1. Gather raw updates and confirm the reporting period
- [ ] 2. Pick the variant (individual / team / executive / client)
- [ ] 3. Sort every fact into: accomplishments, in progress, blockers, upcoming
- [ ] 4. Assign the RAG status and write a summary that justifies it
- [ ] 5. Draft the report in the variant's tone and depth
- [ ] 6. Emit the JSON data file (status-data-contract.md)
- [ ] 7. Hand off to producing-branded-documents if a branded doc is needed
```

**Step 1 — Gather.** Collect everything: notes, tickets, messages. Confirm the
period (week number, report date) and who the report is from/about. Ask for
anything obviously missing (e.g. no mention of a previously reported blocker).

**Step 2 — Pick the variant.** Individual, team roll-up, executive, or client —
selection rules and per-variant depth are in
[references/report-variants.md](references/report-variants.md).

**Step 3 — Sort.** Place each fact into exactly one bucket: done this period
(accomplishments), started but not done (in progress), stuck and needs someone
(blockers), planned next period (upcoming). Deduplicate; merge fragments about
the same work item into one line.

**Step 4 — RAG + summary.** Apply the RAG definitions. Then write 2–4 sentences
that state overall trajectory and the single biggest risk — a reader who stops
after the summary should still know the status and why.

**Step 5 — Draft.** Write the report for the chosen variant. Client and
executive variants: strip internal names/jargon, lead with outcomes. Team
roll-up: attribute work per person or workstream. Individual: keep detail.

**Step 6 — Emit JSON.** Write a data file matching
[references/status-data-contract.md](references/status-data-contract.md)
exactly (same fields as `producing-branded-documents/examples/sample_update.json`).
Validate: every array item is a complete sentence; `overall_status` is exactly
`Green`, `Amber`, or `Red`.

**Step 7 — Hand off.** For a branded Word/PDF deliverable, pass the JSON to the
`producing-branded-documents` skill:
`python scripts/fill_docx.py --data status.json --out <file>.docx` (run from
that skill's folder). That skill owns rendering, logos, and validation — this
one owns the content.

## Examples

Full worked example (raw notes → report → JSON):
[examples/example-weekly.md](examples/example-weekly.md), with the matching
data file [examples/status.json](examples/status.json).

Condensed illustration —

**Input (raw):**
```
- crm access STILL not granted, asked on the 2nd
- finished ingestion for all 12 sources, recon checks automated
- priya doing dashboards, 3 of 8 done
```

**Output (client variant, excerpt):**
```
Overall status: Amber

Summary: Delivery is broadly on track — ingestion is complete and validated
across all 12 source systems. Reporting cutover is at risk pending production
CRM access (requested 2026-07-02); this is the main threat to the go-live date.

Blockers:
- Awaiting production read access to the CRM (requested 2026-07-02; needs
  Globex IT approval) — blocking the reporting cutover.
```

## Anti-patterns
- **Green-until-proven-Red** — declaring Green because nothing has exploded yet.
  Instead: apply the RAG definitions; an open blocker on the critical path is
  Amber at best.
- **Activity lists** — "attended meetings, worked on pipeline". Instead: state
  the outcome ("validated the ingestion pipeline for all 12 sources").
- **Burying the blocker** — mentioning a hard blocker in passing under "notes".
  Instead: blockers get their own section, with the unblocking party and date.
- **One report for all audiences** — sending the internal roll-up to the client.
  Instead: re-cut per variant; the client version never carries internal jargon
  or unvetted names.
- **Prose only, no data file** — skipping the JSON and forcing re-extraction at
  render time. Instead: always emit `status.json` per the data contract.
- **Inventing content** — padding thin weeks with plausible-sounding items.
  Instead: report what happened; a short honest report beats a long fabricated one.

## Related skills
- `producing-branded-documents` — consumes this skill's JSON output
  (via its `scripts/fill_docx.py`) to render the branded Word/PDF deliverable.
  Raw updates → this skill → status.json → that skill → shipped document.

## Reference files
- [references/report-variants.md](references/report-variants.md) — the four
  audience variants, when to use each, and the RAG status definitions.
- [references/status-data-contract.md](references/status-data-contract.md) —
  the JSON schema for the report content, field by field, compatible with
  `producing-branded-documents`.
