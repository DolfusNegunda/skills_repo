---
name: drafting-business-email
description: Draft, reply to, or rewrite professional business emails in a consistent company tone, and produce tone/length variants such as formal, concise, or warm-but-firm. Use when writing an email, replying to a thread, following up or chasing a response, declining a request, apologising for a delay, escalating an issue, making a cold introduction, or polishing a rough email draft.
---

# Drafting Business Email

## Overview
Turns a rough intent ("chase the vendor about the late invoice") or a pasted
thread into a polished, send-ready business email. Every draft ships with tone
and length variants so the user can pick the register that fits the
relationship, instead of iterating line by line.

## When to use this skill
- "Write / draft an email to..." or "reply to this" with a pasted thread
- Following up on something unanswered ("chase them", "nudge", "any update?")
- Declining a request, meeting, or proposal without burning the relationship
- Apologising for a delay, mistake, or missed deadline
- Escalating a blocked issue to a manager or account owner
- Cold introduction / first outreach to someone new
- Proposing or rescheduling a meeting
- "Make this email sound more professional / shorter / firmer / friendlier"

## Core principles
1. **One email, one ask.** Every email exists to get a single decision or
   action. Name it in the first two sentences; cut anything that doesn't serve it.
2. **Reader-first ordering.** Lead with what matters to the recipient (the ask,
   the answer, the apology) — background and justification come after, never before.
3. **Default to short.** 50–150 words covers most business email. Length must be
   earned by genuine complexity, not by throat-clearing.
4. **Match register to relationship and stakes.** A first contact, a peer, and
   an escalation each get a different tone — pick deliberately using
   [references/tone-and-scenarios.md](references/tone-and-scenarios.md), don't
   average them into beige corporate voice.
5. **Always offer variants.** Deliver a recommended draft plus two labelled
   alternatives (e.g. more formal, more concise, firmer) so the user chooses a
   tone rather than describing one.

## Workflow

```
Progress:
- [ ] 1. Extract: recipient, relationship, goal/ask, deadline, prior context
- [ ] 2. Classify the scenario; load its pattern from references/tone-and-scenarios.md
- [ ] 3. Choose the default tone (and note which two variants to offer)
- [ ] 4. Draft: subject line, opener, body, explicit ask, sign-off
- [ ] 5. Self-check: one ask? under length budget? no filler or hedging stacks?
- [ ] 6. Produce two labelled variants; flag anything the user must fill in
```

**Step 1 — Extract the brief.** From the request or pasted thread, identify:
who receives it, the sender's relationship to them, the single desired outcome,
any deadline, and prior commitments already made in the thread. If the ask
itself is ambiguous (e.g. cancel vs. reschedule), ask one clarifying question
before drafting — never guess the ask.

**Step 2 — Classify the scenario.** Match to the closest pattern in
[references/tone-and-scenarios.md](references/tone-and-scenarios.md) (decline,
follow-up, apology, escalation, cold intro, scheduling). The pattern supplies
structure and tone defaults; the brief supplies the content.

**Step 3 — Choose tone.** Pick a default register from the tone table and
decide which two variants are most useful for this situation (a second
follow-up wants a "firmer" variant; a cold intro wants a "shorter" one).

**Step 4 — Draft.** Write subject line first (see the subject-line rules in
the reference), then body. Replies keep the existing subject unless the topic
has genuinely changed. Use `[square brackets]` for any fact you don't have —
never invent names, dates, or figures.

**Step 5 — Self-check.** Verify: single clear ask, within length budget, no
apology-stacking or hedge-stacking, no placeholder left unflagged, and the
first sentence would survive being the only sentence read.

**Step 6 — Deliver with variants.** Present the recommended draft, then two
alternatives, each labelled with tone and approximate length. Close with a
one-line note listing anything in `[brackets]` the user must fill in.

## Examples

**Input:** "Reply to Priya — we can't take on the extra reporting module this
quarter, but keep the door open for Q4."

**Output (recommended — warm-but-firm, ~80 words):**
```
Subject: Reporting module — timing

Hi Priya,

Thanks for sending through the reporting module proposal — it's a strong fit
for what we're building.

We can't take it on this quarter: the team is fully committed through
September. Rather than start it under-resourced, I'd like to revisit it for
the Q4 plan.

Could we pencil in a call in early October to scope it properly? Happy to
share our current roadmap in the meantime.

Best,
[Name]
```
Followed by two labelled variants (e.g. *Formal* for a client relationship,
*Concise* at ~40 words for an internal peer). A full worked example with both
variants written out is in
[examples/example-followup.md](examples/example-followup.md).

## Anti-patterns
- **Burying the ask under paragraphs of context** — the recipient skims and
  misses it. Instead: state the ask in the first two sentences, context after.
- **Apologising more than once for the same thing** — repeated apologies read
  as weakness and invite pushback. Instead: one clear apology, then move to the fix.
- **Hedge-stacking ("just", "sorry to bother", "if it's not too much
  trouble")** — it drains authority from a legitimate request. Instead: polite
  and direct ("Could you confirm by Friday?").
- **Vague subject lines ("Quick question", "Update", "Hello")** — they get
  deprioritised and are unfindable later. Instead: topic + action, e.g.
  "Invoice 4417 — approval needed by 12 Jul".
- **Inventing facts to fill gaps** — a wrong date or name is worse than a
  blank. Instead: use `[bracketed placeholders]` and list them for the user.
- **Delivering a single take-it-or-leave-it draft** — the user then has to
  describe tone changes in words. Instead: always include two labelled variants.
- **Escalating with blame** — naming culprits makes the reader defensive.
  Instead: state impact, what was tried, and the specific decision needed.

## Related skills
- [producing-branded-documents](../producing-branded-documents/SKILL.md) — when
  the message should be a formal branded document (status report, client
  deliverable) rather than an email body.
- [skill-builder](../../skill-builder/SKILL.md) — for extending this skill with
  team-specific tone rules or new scenarios.

## Reference files
- [references/tone-and-scenarios.md](references/tone-and-scenarios.md) — tone
  register table, subject-line rules, and structural patterns for the six
  common scenarios (decline, follow-up, apology, escalation, cold intro,
  scheduling).
