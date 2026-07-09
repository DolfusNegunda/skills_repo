---
name: reviewing-contracts
description: Review contracts and agreements to surface obligations, risks, ambiguities, missing terms, and unfavorable clauses — producing severity-ranked findings a business owner can act on or escalate to legal. Use when the user asks to "review this contract/agreement/SOW/NDA", "what am I agreeing to", "flag risky clauses", or check terms before signing. Business/risk review, NOT legal advice. Inherits the shared severity/scoring model. Produces an actionable, escalation-ready review.
---

# Reviewing Contracts

## Scope
Business-and-risk review of contracts and agreements — obligations, liabilities,
ambiguities, and missing protections — to inform a signer or route issues to legal.
Inherits method/severity/scoring from
[conducting-structured-reviews](../conducting-structured-reviews/SKILL.md).

> **Not legal advice.** This surfaces risks and questions for a qualified lawyer;
> it does not replace one. Always flag material legal risk for professional review.

## Purpose
Let a business owner understand what they're committing to and where the risks are —
so obvious issues get fixed and genuine legal risks get escalated before signature.

## When to use this skill
- "Review this contract / agreement / SOW / NDA / MSA / terms."
- "What am I agreeing to? / flag risky clauses / check before I sign."
- A first-pass business review before legal, or a sanity check on standard terms.

## When NOT to use this skill
- Definitive legal opinion / negotiation strategy → a qualified lawyer.
- Policy documents → [reviewing-policies](../reviewing-policies/SKILL.md).
- Negotiating the deal → [negotiating-agreements](../../business/negotiating-agreements/SKILL.md).

## Inputs
- The contract and your role (which party you are).
- The deal intent (what you expect to give/get) and any must-haves/red-lines.
- Governing standards or a prior/standard version to compare against.

## Outputs
- A review: risk verdict + scores, severity-ranked findings (clause reference +
  plain-English meaning + why it matters + suggested action), obligations summary,
  and items to escalate to legal.

## Evaluation rubric (dimensions)
1. **Obligations** — what each party must do, by when; are yours achievable?
2. **Liability & indemnity** — caps, exclusions, who bears what; uncapped exposure.
3. **Risk allocation** — warranties, indemnities, insurance, force majeure.
4. **Commercials** — price, payment terms, changes, penalties, escalation.
5. **Term & exit** — duration, renewal (auto?), termination rights, notice, consequences.
6. **IP & data** — ownership, licenses, confidentiality, data protection/compliance.
7. **Clarity & completeness** — ambiguous terms, undefined words, missing clauses.

## Scoring & severity
Score 1–5; rank Blocker→Praise (see
[foundation reference](../conducting-structured-reviews/references/severity-and-scoring.md)).
Examples: **Blocker** = uncapped liability or an indemnity that could exceed the
contract value; **Major** = auto-renewal with a long notice window, or payment terms
worse than standard; **Minor** = an undefined term; **Nit** = clause numbering.

## Workflow
```
Progress:
- [ ] 1. Confirm your party, the deal intent, and red-lines
- [ ] 2. Extract obligations and key commercial terms
- [ ] 3. Assess liability, risk allocation, term/exit, IP/data
- [ ] 4. Flag ambiguities, missing terms, and unfavorable clauses
- [ ] 5. Severity-rank, score, verdict; action per finding + legal-escalation list
```

**Step 3 — asymmetry is the signal.** Look for terms that fall disproportionately on
your party (one-way indemnities, uncapped liability, unilateral termination).
**Always separate "fix in negotiation" from "escalate to legal"** and never present
a legal conclusion as settled.

## Recommended-improvements guidance
For each finding give the plain meaning, the risk, and the action: propose a
red-line (add a liability cap, mutualize the indemnity, shorten notice), request a
definition, or escalate to legal with the specific question.

## Validation checklist
- [ ] Reviewing party and deal intent confirmed.
- [ ] Obligations and commercial terms extracted in plain English.
- [ ] Liability, indemnity, term/exit, and IP/data assessed.
- [ ] Ambiguities and missing terms flagged.
- [ ] Findings carry clause ref + severity + action; legal-escalation items listed.
- [ ] "Not legal advice" stated; material legal risk routed to a lawyer.

## Common mistakes
- **Giving legal advice** instead of surfacing risks and questions.
- **Reading clauses in isolation** — missing how liability + indemnity + insurance interact.
- **Skimming boilerplate** where auto-renewal and uncapped liability hide.
- **Ignoring which party you are** — a term favorable to "them" is your risk.
- **No plain-English translation** — findings the business owner can't act on.

## Edge cases
- **Standard/click-through terms:** you may not be able to negotiate; flag risks to accept knowingly.
- **Cross-border:** governing law/jurisdiction and data-transfer terms need legal input.
- **High value/strategic:** recommend full legal review regardless of findings.
- **Amendments:** compare against the base contract → [comparing-documents](../../office/comparing-documents/SKILL.md).

## Related skills
- [conducting-structured-reviews](../conducting-structured-reviews/SKILL.md), [reviewing-policies](../reviewing-policies/SKILL.md).
- [negotiating-agreements](../../business/negotiating-agreements/SKILL.md), [comparing-documents](../../office/comparing-documents/SKILL.md).

## Examples
**Input:** "Review this vendor MSA before I sign — we're the customer."
**Output:** Risk: High — escalate (Liability 1/5, Term 2/5). **Blocker:** vendor
liability capped at one month's fees while our indemnity is uncapped — asymmetric;
action: red-line a mutual cap; escalate to legal. **Major:** auto-renews for 3 years
with 90-day notice; action: shorten to 30 days, annual term. **Praise:** clear SLA
credits. (Not legal advice.)

## Automation opportunities
- Maintain a red-line playbook of standard positions to compare against.
- Auto-extract obligations and dates into a tracker.
- Diff amendments against the executed version before review.
