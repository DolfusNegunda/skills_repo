---
name: collaborating-in-teams
description: Set up and run effective collaboration in Microsoft Teams — structure teams and channels, choose chat vs channel vs meeting, apply async etiquette, organize files and tabs, run productive meetings with agendas and recaps, and reduce notification overload. Use when the user asks to "organize Teams", "set up channels", improve Teams meetings or communication, or decide where a conversation belongs. Produces a clear collaboration structure and working norms.
---

# Collaborating in Teams

## Scope
The structure and norms of Microsoft Teams: team/channel architecture, the
chat-vs-channel-vs-meeting decision, async etiquette, files/tabs organization,
meeting hygiene, and notification control. Not the writing of individual messages
or formal minutes.

## Purpose
Make collaboration findable and calm: the right conversation in the right place,
decisions captured where the team looks, and notifications that signal rather than nag.

## When to use this skill
- "Set up / organize Teams or channels."
- "Our Teams is chaotic / I can't find anything."
- Improving Teams meetings, async work, or notification overload.
- Deciding chat vs channel vs meeting vs email for a conversation.

## When NOT to use this skill
- Formal meeting records → [recording-meeting-minutes](../recording-meeting-minutes/SKILL.md).
- One-off message wording → [drafting-business-email](../drafting-business-email/SKILL.md).
- Email system design → [managing-outlook-mail](../managing-outlook-mail/SKILL.md).

## Inputs
- Team/project structure and membership; what work happens where today.
- Current pain (scattered files, missed messages, meeting overload).
- Governance constraints (guest access, private channels, retention).

## Outputs
- A team/channel scheme, posting conventions, a meeting protocol (agenda → run →
  recap), a files/tabs layout, and notification norms — described for adoption.

## Workflow
```
Progress:
- [ ] 1. Map the work: which groups, projects, and audiences exist
- [ ] 2. Design teams (broad) and channels (topics within a team)
- [ ] 3. Set the medium-choice rule (chat / channel / meeting / email)
- [ ] 4. Organize files, tabs, and pinned resources per channel
- [ ] 5. Define meeting protocol and async etiquette
- [ ] 6. Set notification and status norms
```

**Step 1 — Map work.** A *team* = a stable group of people; a *channel* = a topic
that group works on. Don't create a team per project if one team with channels fits.

**Step 2 — Channel design.** Keep channels topic-clear and few. Use a General/
Announcements channel for team-wide notices; standard channels for ongoing topics;
private channels only for genuinely restricted work.

**Step 3 — Medium choice.** **Channel post** = anything others may need to see or
search later (decisions, questions, updates). **Chat** = quick, ephemeral, small
group. **Meeting** = needs real-time discussion/decision. **Email** = external or
formal record. Default work conversations to channels so they're findable.

**Step 4 — Files & tabs.** Files posted in a channel live in that channel's
folder — keep the folder structure shallow and consistent. Pin key docs, plans,
and dashboards as tabs so nobody hunts for them.

**Step 5 — Meetings.** Every meeting has an agenda in the invite; record/transcribe
when useful; post a recap with decisions and actions to the channel afterward (feed
it through [recording-meeting-minutes](../recording-meeting-minutes/SKILL.md)).

**Step 6 — Notifications & status.** Configure channel notifications (follow only
what matters), use @mentions deliberately, respect status/focus, and set quiet hours.

## Principles
1. **Findable over fast.** Prefer channels to DMs so knowledge is searchable.
2. **@mention with intent.** @channel is a loud tool; use sparingly.
3. **Async by default,** meet only when real-time truly helps.
4. **One home per topic.** Don't spread a project across chat, channel, and email.
5. **Decisions get posted,** not left in a call nobody re-watches.

## Decision framework
- **Will someone need this later?** → channel post, not chat.
- **Restricted audience?** → private channel (sparingly).
- **Needs live back-and-forth / a decision now?** → meeting.
- **External party or formal record?** → email.
- **Reference doc?** → pin as a tab.

## Common mistakes
- **DM sprawl** — decisions trapped in chats nobody else can find.
- **Too many channels/teams** — the structure itself becomes the confusion.
- **@channel for everything** — notification fatigue, then ignored mentions.
- **No agenda/recap** — meetings that don't produce durable outcomes.
- **Files uploaded to chat** — lost outside the channel's document library.

## Validation checklist
- [ ] Teams map to stable groups; channels to clear topics.
- [ ] A written rule exists for chat vs channel vs meeting vs email.
- [ ] Key documents are pinned as tabs; file folders are shallow.
- [ ] Meetings have agendas and post recaps to the channel.
- [ ] Notification norms and @mention etiquette are agreed.
- [ ] Guest/private-channel access matches governance policy.

## Edge cases
- **External collaborators:** use guest access or shared channels per policy; mind data governance.
- **Very large orgs:** consider an org-wide team plus focused project teams.
- **Regulated industries:** ensure retention/compliance on channels and recordings.
- **Hybrid meetings:** assign a facilitator to include remote participants explicitly.

## Related skills
- [recording-meeting-minutes](../recording-meeting-minutes/SKILL.md) / [summarizing-meeting-notes](../summarizing-meeting-notes/SKILL.md).
- [managing-outlook-mail](../managing-outlook-mail/SKILL.md) — when email is the right medium.
- [drafting-business-email](../drafting-business-email/SKILL.md).

## Examples
**Input:** "Our project lives across 5 group chats and email — nobody can find decisions."
**Output:** One project team; channels for Delivery, Design, Ops, and Announcements;
rule that decisions/questions go to channels; pinned plan + dashboard tabs; a
meeting recap posted to Delivery after each standup; @channel reserved for
Announcements only.

## Automation opportunities
- Standardize channel templates and pinned tabs when spinning up new projects.
- Auto-post meeting recaps via a transcription → minutes flow.
- Use workflow bots for approvals and routine status prompts.
