# Output Formats for Meeting Summaries

## Contents
- Choosing a format
- Canonical structure (default)
- Field rules
- Variant: Quick recap
- Variant: Formal minutes
- Handling missing information

## Choosing a format

| Format | Use when | Length target |
| ------ | -------- | ------------- |
| Canonical | Default; team syncs, project meetings, most requests | Half a page to one page |
| Quick recap | Chat/Slack post, "just the highlights", short standups | Under ~10 lines |
| Formal minutes | Steering committees, board/client meetings, anything needing a record | As long as needed; still no play-by-play |

If the user names a format ("minutes", "recap", "TL;DR"), use that variant. Otherwise produce the canonical structure and mention that the other two are available.

## Canonical structure (default)

```markdown
# Meeting Summary — <Meeting Name>
**Date:** <YYYY-MM-DD> | **Attendees:** <names>

## Decisions
- <Outcome, one line. Add a short "because ..." only if the rationale matters later.>

## Action Items
| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | <Verb-first task> | <One person> | <YYYY-MM-DD> |

## Risks & Blockers
- <Risk or blocker> — <impact, and who/what unblocks it if known>

## Open Questions
- <Unresolved question, phrased as a question. Note who raised it if relevant.>
```

Section order is fixed. Omit a section only when it is genuinely empty, and say so if the omission is surprising (e.g. "No decisions were made").

## Field rules

- **Action:** starts with a verb, one task per row. Split "Kai to fix creds and update the runbook" into two rows if they can complete independently.
- **Owner:** exactly one named person. Groups ("Ops", "the team") are only acceptable when the source names no individual — prefer `UNASSIGNED` plus a note about which group was mentioned.
- **Due:** absolute `YYYY-MM-DD`, converted from relative dates using the meeting date. Unknown → `TBD`.
- **Decisions:** past-tense, settled outcomes. Include reversals explicitly ("moved cutover from 07-10 to 07-14").
- **Risks & Blockers:** blockers are active impediments right now; risks are credible future problems. Both belong here, labeled by their wording.
- **Open Questions:** anything the meeting raised but did not resolve. These are prime candidates for the next agenda.

## Variant: Quick recap

For chat posts and short standups. No headings, no tables — just three tight blocks.

```markdown
**<Meeting Name> recap (<YYYY-MM-DD>)**
Decided: <decision 1>; <decision 2>.
To do: <Owner> — <task> (due <MM-DD>); <Owner> — <task> (due <MM-DD>).
Watch: <top risk/blocker or open question>.
```

Rules:
- Cap at roughly 10 lines; if it will not fit, the meeting needs the canonical format instead.
- Keep every action's owner and due date even here — compression never drops accountability.
- "Watch:" holds at most the two most important risks/blockers/questions; drop the rest, do not merge them into mush.

## Variant: Formal minutes

For meetings that need an official record. Adds attribution and administrative framing on top of the canonical sections.

```markdown
# Minutes — <Meeting Name>
**Date:** <YYYY-MM-DD> | **Time:** <start–end, if known> | **Location/Call:** <if known>
**Present:** <names, roles if known> | **Absent/Apologies:** <names or "—">
**Chair:** <name or "—"> | **Minutes by:** <name or "Prepared from notes">

## 1. Agenda Items Discussed
For each agenda item or major topic:
### 1.<n> <Topic>
<2-4 sentences: what was presented/discussed, attributed to speakers where the source supports it.>

## 2. Decisions
- D1: <decision> (proposed by <name>, if known)
- D2: ...

## 3. Action Items
| # | Action | Owner | Due | Raised in |
|---|--------|-------|-----|-----------|
| A1 | <task> | <person> | <YYYY-MM-DD> | 1.2 |

## 4. Risks & Blockers
- <as canonical, with the topic reference if useful>

## 5. Open Questions / Deferred Items
- <question> — deferred to <next meeting/owner>, if stated

## 6. Next Meeting
<Date/time if stated, otherwise "Not scheduled.">
```

Rules:
- Numbered decision (D1, D2) and action (A1, A2) IDs so later meetings can reference them.
- Attribute statements only where the source clearly supports it; otherwise write impersonally ("It was noted that...").
- Formal tone, but still outcomes over discussion — one short paragraph per topic, not a transcript.

## Handling missing information

| Missing | Do this |
| ------- | ------- |
| Owner for an action | `UNASSIGNED`, and note who the task most affects |
| Due date | `TBD`; if a vague timeframe was given ("soon", "next sprint"), quote it in the Due cell |
| Meeting date (but relative deadlines exist) | Ask the user; if not possible, state the assumed date at the top |
| Attendees | Omit the field rather than guessing from names mentioned in passing |
| Everything ambiguous | Prefer a flagged gap over an invented fact — always |
