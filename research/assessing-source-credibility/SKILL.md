---
name: assessing-source-credibility
description: Evaluate the credibility of a source — its authority, accuracy, objectivity, currency, and evidence — to decide how much to trust and rely on it. Use when the user asks to "is this source reliable/credible", "evaluate this source", "can I trust this", or vet sources before citing them. Uses CRAAP-style criteria and lateral reading, and detects bias and misinformation signals. Produces a credibility judgment with reasoning, not a binary trust/distrust.
---

# Assessing Source Credibility

## Scope
Judging how far a given source can be trusted and relied on — authority, accuracy,
objectivity, currency, purpose, and supporting evidence — plus bias and
misinformation detection. Applies per-source; combining sources is
[synthesizing-research](../synthesizing-research/SKILL.md).

## Purpose
Prevent building conclusions on unreliable foundations: assess each source's
trustworthiness with explicit criteria and assign a calibrated level of reliance,
rather than treating all sources — or all of one source — as equally credible.

## When to use this skill
- "Is this source reliable / credible / can I trust this?"
- Vetting sources before citing or acting on them.
- Screening for bias, conflicts of interest, or misinformation.

## When NOT to use this skill
- Confirming a specific factual claim → [verifying-facts](../verifying-facts/SKILL.md).
- Appraising a study's method → [reviewing-research](../../review/reviewing-research/SKILL.md).
- Gathering the sources → [collecting-evidence](../collecting-evidence/SKILL.md).

## Inputs
- The source (author/publisher, date, content) and the claim/context you'd use it for.
- The stakes — how much rides on relying on it.

## Outputs
- A credibility judgment: reliability level (high/moderate/low), the reasoning across
  criteria, noted biases/conflicts, and how to use it (rely, corroborate, or discard).

## Workflow
```
Progress:
- [ ] 1. Identify the source, author/publisher, and its purpose
- [ ] 2. Authority: who made it, and what's their expertise/standing?
- [ ] 3. Accuracy: is it evidenced, sourced, and corroborated?
- [ ] 4. Objectivity: bias, funding, conflicts, agenda?
- [ ] 5. Currency: current enough for the claim?
- [ ] 6. Judge reliability and how to use it
```

**Step 2–5 — CRAAP-style criteria:** Authority (author's credentials, publisher
reputation), Accuracy (evidence, citations, corroboration by independent sources),
Objectivity/Purpose (bias, funding, is it selling or informing?), and Currency (date
vs. how fast the field changes). **Step 4 — follow the money and the motive:** funding
and agenda quietly shape conclusions. **Step 6 — calibrate, don't binary-judge:** even
credible sources are weaker outside their expertise; even weak sources may be usable
if corroborated. Lateral reading (what other sources say *about* this source) beats
reading it in isolation.

## Principles
1. **Credibility is a spectrum,** not trust/distrust — and it's claim-specific.
2. **Check authority, accuracy, objectivity, currency** explicitly.
3. **Corroborate** — independent confirmation raises reliance.
4. **Follow funding and motive** for hidden bias.
5. **Read laterally** — check the source's reputation elsewhere.
6. **Match scrutiny to stakes.**

## Decision framework
- **Primary vs. secondary?** Prefer primary for facts; secondary for context/synthesis.
- **Extraordinary claim?** Demand extraordinary, corroborated evidence.
- **Commercial/advocacy source?** Usable for their position, not as neutral fact.
- **Anonymous/no provenance?** Low reliance; corroborate before any use.
- **Outside author's expertise?** Discount even a credible author.

## Common mistakes
- **Binary trust/distrust** — ignoring the spectrum and the claim context.
- **Authority bias** — trusting a big name outside their field.
- **Ignoring funding/conflicts.**
- **Not corroborating** a lone source.
- **Confusing popularity/ranking with reliability.**
- **Reading only the source itself,** never what others say about it.

## Validation checklist
- [ ] Author/publisher and purpose identified.
- [ ] Authority, accuracy, objectivity, and currency assessed.
- [ ] Bias, funding, and conflicts examined.
- [ ] Corroboration sought; lateral reading done.
- [ ] Reliability level assigned with reasoning.
- [ ] Guidance on how to use it (rely / corroborate / discard) given.

## Edge cases
- **Preprints/non-peer-reviewed:** flag lower certainty; corroborate.
- **Social media/anonymous:** trace to a primary source before any reliance.
- **State/corporate sources:** authoritative for their own data, biased on contested topics.
- **AI-generated content:** treat as unverified; trace claims to primary sources.

## Related skills
- [verifying-facts](../verifying-facts/SKILL.md), [collecting-evidence](../collecting-evidence/SKILL.md), [reviewing-research](../../review/reviewing-research/SKILL.md).
- [citing-sources](../citing-sources/SKILL.md), [synthesizing-research](../synthesizing-research/SKILL.md).

## Examples
**Input:** "Can I trust this industry blog's stat that AI boosts productivity 40%?"
**Output:** Moderate-to-low reliance. Authority: vendor blog, not independent —
conflict of interest (they sell AI tools). Accuracy: the 40% traces to their own
unpublished survey, uncorroborated. Currency: recent. Objectivity: promotional.
Use: cite as a vendor claim, not a fact; corroborate with independent studies before
relying on the number.

## Automation opportunities
- Maintain a source-tier list (peer-reviewed > reputable press > vendor > anonymous).
- Flag conflict-of-interest signals (vendor, advocacy, funded-by) for review.
