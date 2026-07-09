---
name: recording-meeting-minutes
description: Produce formal, accurate meeting minutes — attendees, agenda coverage, decisions, action items with owners and due dates, and a clear record suitable for governance, boards, and committees. Use when the user asks to "write meeting minutes", "formal minutes", "board/committee minutes", or a governance-grade record of a meeting. For quick action-item extraction from casual notes, use summarizing-meeting-notes instead. Produces an approvable minutes document.
---

# Recording Meeting Minutes

## Scope
Formal minutes — the official, approvable record of a meeting for governance,
boards, committees, and compliance. Distinct from
[summarizing-meeting-notes](../summarizing-meeting-notes/SKILL.md), which is the
fast, informal decisions-and-actions summary for working meetings.

## Purpose
Create a factual, neutral, complete record that can be tabled, approved, and relied
on later: who attended, what was decided, who owns what by when, and how each item
was resolved.

## When to use this skill
- "Write formal / board / committee meeting minutes."
- A governance-grade record (AGM, board, steering committee, statutory meeting).
- Minutes that will be formally approved and archived.
- Meetings with compliance, audit, or legal significance.

## When NOT to use this skill
- Quick working-meeting recap → [summarizing-meeting-notes](../summarizing-meeting-notes/SKILL.md).
- Just pulling out action items → [summarizing-meeting-notes](../summarizing-meeting-notes/SKILL.md).
- A narrative status update → [writing-reports](../writing-reports/SKILL.md).

## Inputs
- Raw notes, transcript, or recording of the meeting.
- Meeting metadata: title, date/time, location, chair, attendees, apologies, quorum.
- The agenda and any pre-read documents referenced.
- The house minutes format/standard (e.g. Robert's Rules) if applicable.

## Outputs
- A formal minutes document: header/metadata, attendance, agenda-by-agenda record
  of discussion summary + decisions + actions (owner, due date), and approval block.

## Workflow
```
Progress:
- [ ] 1. Capture metadata: date, attendees, apologies, quorum, chair
- [ ] 2. Follow the agenda; one section per item
- [ ] 3. For each item: brief discussion summary, decision, actions
- [ ] 4. Record decisions verbatim in intent; note votes if formal
- [ ] 5. Consolidate all actions into an owner/due table
- [ ] 6. Neutral tone, factual, past tense; no editorializing
- [ ] 7. Circulate as draft for approval; mark status
```

**Step 1 — Metadata.** Record title, date, time, location/platform, chair,
minute-taker, attendees, apologies/absences, and quorum status. These make minutes
official.

**Step 2 — Agenda structure.** One numbered section per agenda item, in order,
including "matters arising" from prior minutes and AOB.

**Step 3 — Per item.** Summarize the discussion briefly (key points and differing
views, not a transcript), then state the **decision** and any **actions**.

**Step 4 — Decisions & votes.** Record resolutions precisely; for formal bodies,
note proposer/seconder and the vote (for/against/abstain) and whether carried.

**Step 5 — Action register.** Pull every action into one table: action, owner, due
date, status. This is what people actually use afterward.

**Step 6 — Tone.** Neutral, factual, third person, past tense. Minutes record what
happened and was decided — not opinions, blame, or verbatim argument.

**Step 7 — Approval.** Issue as "Draft" for review; they become official only when
approved at the next meeting. Mark the status clearly.

## Principles
1. **Record decisions and actions, not the transcript.** Summarize discussion.
2. **Neutral and factual.** No editorializing, attribution of blame, or tone.
3. **Every action has an owner and a due date.** No orphan actions.
4. **Decisions are precise.** Ambiguous resolutions cause disputes later.
5. **Draft until approved.** Status matters for governance.

## Decision framework
- **Formal body (board/committee)?** Full protocol: quorum, votes, resolutions.
- **Working meeting?** Use [summarizing-meeting-notes](../summarizing-meeting-notes/SKILL.md) instead.
- **Disagreement recorded?** Note that views differed, neutrally, without naming winners/losers unless required.
- **Confidential items?** Minute separately/restricted per governance rules.

## Common mistakes
- **Transcribing everything** — minutes are a record, not a recording.
- **Vague decisions** ("discussed pricing") with no resolution.
- **Actions with no owner or date** — nothing happens.
- **Editorializing** ("after a heated argument") — non-neutral, disputable.
- **Publishing as final** before approval.
- **Missing quorum/attendance** — undermines validity for formal bodies.

## Validation checklist
- [ ] Complete metadata (date, chair, attendees, apologies, quorum).
- [ ] Every agenda item covered in order, including matters arising and AOB.
- [ ] Each item has a clear decision/outcome.
- [ ] Votes recorded where the body is formal.
- [ ] Every action has owner + due date, consolidated into one table.
- [ ] Neutral, factual, past-tense throughout.
- [ ] Marked "Draft" pending approval; approval block present.

## Edge cases
- **No quorum:** record it; note which decisions are consequently invalid/deferred.
- **In-camera/confidential sessions:** minute separately with restricted access.
- **Proxy/remote votes:** record how each was cast and counted.
- **Amendments to prior minutes:** capture under matters arising and re-approve.

## Related skills
- [summarizing-meeting-notes](../summarizing-meeting-notes/SKILL.md) — informal working-meeting recap.
- [authoring-word-documents](../authoring-word-documents/SKILL.md) — format the official document.
- [collaborating-in-teams](../collaborating-in-teams/SKILL.md) — post recaps to the channel.

## Examples
**Input:** "Turn this board call transcript into formal minutes."
**Output:** Minutes with header (date, attendees, apologies, quorum confirmed),
numbered agenda items each with a 2–4 line discussion summary and a stated
resolution (proposer/seconder/vote where applicable), a consolidated action table,
neutral past-tense throughout, marked "Draft — for approval at next meeting".

## Templates
- [templates/minutes-template.md](templates/minutes-template.md) — a governance-grade minutes structure.

## Automation opportunities
- Feed a meeting transcript straight into this structure for a first draft.
- Auto-extract the action table into a tracker (via connector).
- Reuse the template as the org standard for all formal minutes.
