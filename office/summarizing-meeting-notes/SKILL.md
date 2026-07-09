---
name: summarizing-meeting-notes
description: Transforms raw meeting notes, transcripts, or chat logs into a structured summary with decisions, action items (owner + due date), risks/blockers, and open questions. Use when asked to summarize a meeting, clean up meeting notes, extract action items or decisions from a transcript, or produce meeting minutes or a recap.
---

# Summarizing Meeting Notes

## Overview
Turns messy meeting input — hand-typed notes, call transcripts, chat threads — into a clean, scannable summary organized around what actually matters afterward: what was decided, who owes what by when, what is at risk, and what is still unresolved. The output follows a canonical structure with two lighter/heavier variants for different audiences.

## When to use this skill
- "Summarize these meeting notes" / "clean up my notes from the sync"
- "Pull the action items out of this transcript"
- "What was decided in this meeting?"
- "Write up minutes for the steering committee" / "give me a quick recap for Slack"
- Any pasted transcript, call recording text, or raw bullet dump that needs structuring

## Core principles
1. **Action items are the product.** Every action item must name one accountable owner and a due date. If either is missing from the source, extract the item anyway and flag the gap explicitly — never invent an owner or date.
2. **Decisions, not discussion.** Record the outcome and (briefly) why; drop the back-and-forth that led there. A decision is something the team will act on as settled.
3. **Separate signal types.** Decisions, action items, risks/blockers, and open questions go in distinct sections. An unresolved debate is an open question, not a decision; a missed dependency is a risk, not an action item.
4. **Stay faithful to the source.** Summarize only what the notes say. Resolve names and dates from context ("Fri" + a dated meeting → the actual date), but mark anything inferred, and never fabricate attendees, commitments, or conclusions.
5. **Match the format to the audience.** Default to the canonical structure; use the quick-recap variant for chat posts and the formal-minutes variant for records of official meetings.

## Workflow

```
Progress:
- [ ] Step 1: Establish context (meeting name, date, attendees, requested format)
- [ ] Step 2: First pass — tag decisions, actions, risks, questions
- [ ] Step 3: Normalize action items (owner, due date, flag gaps)
- [ ] Step 4: Assemble in the chosen format from references/output-format.md
- [ ] Step 5: Verify against the source (nothing invented, nothing dropped)
```

**Step 1 — Establish context.** Identify the meeting name, date, and attendees from the notes or the user's message. If the meeting date is unknown and relative dates ("by Friday") appear, ask for it or state the assumption. Choose the format: canonical by default, or a variant if the user's phrasing suggests one ("quick recap", "minutes").

**Step 2 — Tag the content.** Read the whole input once, classifying each substantive line as decision, action item, risk/blocker, open question, or context. Discussion that produced no outcome is context and is usually dropped.

**Step 3 — Normalize action items.** For each item: one verb-first task, one owner (a person, not "the team"), one due date. Convert relative dates to absolute ones using the meeting date. Where owner or date is genuinely absent, write `owner: UNASSIGNED` or `due: TBD` so the gap is visible.

**Step 4 — Assemble.** Build the summary using the exact section order and table shapes in [references/output-format.md](references/output-format.md). Keep decisions to one line each; keep the whole summary shorter than the source.

**Step 5 — Verify.** Re-scan the source for any commitment, decision, or concern not yet captured, and confirm every statement in the summary traces back to the input. Present the result and offer the other format variants if useful.

## Examples

**Input (raw notes):**
```
standup 7/7 - kai, mira, deshawn
mira: auth migration done!! decided we cut over prod next tues not this week
kai blocked - staging db creds expired again, needs ops
deshawn to draft rollback plan by thurs
do we even need the legacy endpoints after cutover?? nobody sure
```

**Output (canonical):**
```markdown
# Meeting Summary — Standup
**Date:** 2026-07-07 | **Attendees:** Kai, Mira, Deshawn

## Decisions
- Production cutover for the auth migration moves to Tuesday 2026-07-14 (not this week).

## Action Items
| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | Draft rollback plan for the auth cutover | Deshawn | 2026-07-09 |
| 2 | Renew expired staging DB credentials (via Ops) | UNASSIGNED — Kai is blocked on this | TBD |

## Risks & Blockers
- Kai is blocked: staging DB credentials expired (recurring issue); needs Ops.

## Open Questions
- Are the legacy endpoints still needed after cutover? No one was sure.
```

Full worked example with all three format variants: [examples/example-standup.md](examples/example-standup.md).

## Anti-patterns
- **Inventing owners or dates to make the table look complete** — fabricated accountability is worse than a visible gap. Instead: write `UNASSIGNED` / `TBD` and call out the gap in the summary.
- **Recapping the discussion chronologically** — a play-by-play buries the outcomes. Instead: organize by signal type (decisions, actions, risks, questions).
- **Logging tentative ideas as decisions** — "maybe we should X" is not settled. Instead: file it under open questions or drop it.
- **Assigning actions to "the team" or "everyone"** — shared ownership means no ownership. Instead: name one person, or mark it `UNASSIGNED` for follow-up.
- **Keeping relative dates ("by Friday")** — meaningless a week later. Instead: convert to absolute dates from the meeting date, or ask.
- **Producing a summary longer than the notes** — that is expansion, not summarization. Instead: one line per decision, one row per action.

## Related skills
- **writing-status-reports** — the Action Items table (task, owner, due date, plus any blockers) maps directly into a status report's progress and blockers sections; feed extracted items there when the user needs a weekly or project status update.
- **skill-builder** — conventions used to author and maintain this skill.

## Reference files
- [references/output-format.md](references/output-format.md) — canonical output structure, field rules, and the two variants: "quick recap" and "formal minutes".
