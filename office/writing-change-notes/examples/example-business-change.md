# Worked Example: Described Process Change → Business Change Note

## Input

The user describes the change informally:

> "Finance decided that from September 1st, all software purchases over $500
> need a ticket in the Procurement Hub before anyone buys anything — no more
> just expensing it on a card. Anything under $500 stays on the card like
> today. It came out of the Q2 audit, we had a bunch of duplicate SaaS
> subscriptions nobody could account for. Team leads need to log any existing
> subscriptions their team pays for by mid-August so Finance can dedupe.
> Questions go to the #procurement Slack channel."

## Reasoning applied

- Old state vs. new state extracted: card-expensed purchases → pre-approval
  ticket, with the $500 threshold as the boundary.
- The unaffected group (purchases under $500) is called out explicitly so
  those readers stop worrying.
- Two distinct actions with different actors and deadlines: team leads must
  log existing subscriptions (by 2026-08-15), and all buyers must use the
  ticket flow (from 2026-09-01). Both get an actor, a verb, and a date.
- The audit finding is the honest "why" — stated plainly, not dressed up.

## Output

```markdown
# Change Note: Pre-approval required for software purchases over $500

**What is changing:** Software purchases over $500 can no longer be expensed
directly on a company card. Starting on the effective date, submit a request
in the Procurement Hub and wait for approval before purchasing. Purchases of
$500 or less continue on the card exactly as today.

**Why:** The Q2 audit found duplicate SaaS subscriptions that could not be
traced to an owner. Central approval lets Finance catch overlapping tools
before money is spent.

**Who is affected:** Anyone who buys software on behalf of their team.
Team leads have an additional one-time action below. Purchases of $500 or
less are not affected.

**Effective date:** 2026-09-01. Card purchases over $500 made before this
date are still accepted.

**Action required:**
- Team leads: log every software subscription your team currently pays for
  in the Procurement Hub by 2026-08-15, so Finance can deduplicate before
  the cutover.
- All buyers: from 2026-09-01, open a Procurement Hub ticket and receive
  approval before any software purchase over $500.

**Questions:** #procurement on Slack.
```
