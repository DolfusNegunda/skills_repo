---
name: verifying-facts
description: Verify specific factual claims by tracing them to primary sources and corroborating across independent sources — returning confirmed, refuted, or unverifiable with evidence. Use when the user asks to "fact-check this", "verify this claim/statistic", "is this true", or check accuracy before publishing. Traces claims to their origin, detects misattribution and outdated data, and states confidence. Produces a verdict per claim with evidence, never an unsupported "true/false".
---

# Verifying Facts

## Scope
Checking whether specific claims are true — tracing each to its primary source and
corroborating independently — and returning a verdict with confidence. Per-claim
verification, distinct from judging a whole source
([assessing-source-credibility](../assessing-source-credibility/SKILL.md)).

## Purpose
Stop false, misattributed, or outdated claims from propagating: confirm each claim
against primary evidence, or clearly mark it refuted or unverifiable — with the
evidence and a confidence level, never a bare assertion.

## When to use this skill
- "Fact-check this / verify this claim or statistic / is this true?"
- Checking accuracy before publishing, citing, or deciding.
- Vetting numbers, quotes, dates, and attributions.

## When NOT to use this skill
- Judging a source's overall reliability → [assessing-source-credibility](../assessing-source-credibility/SKILL.md).
- Appraising research methodology → [reviewing-research](../../review/reviewing-research/SKILL.md).
- Gathering a broad evidence base → [collecting-evidence](../collecting-evidence/SKILL.md).

## Inputs
- The specific claim(s) to check, with enough context to interpret them.
- The stakes and any deadline (affects depth).

## Outputs
- Per claim: a verdict (**confirmed / partially true / refuted / unverifiable**), the
  primary source(s), corroboration, confidence level, and any needed caveat/correction.

## Workflow
```
Progress:
- [ ] 1. Isolate the exact claim (what precisely is asserted?)
- [ ] 2. Trace it to the primary/original source
- [ ] 3. Corroborate across independent sources
- [ ] 4. Check for misattribution, missing context, and staleness
- [ ] 5. Assign a verdict + confidence; supply the correction if needed
```

**Step 1 — pin the exact claim.** "Crime is rising" vs. "violent crime rose 5% in
2025 in city X" are different checks. Vague claims must be made precise first.
**Step 2 — go to the primary source;** a claim repeated by ten outlets citing one
original is one source, not ten. Trace the chain to the origin. **Step 3 —
independent corroboration** raises confidence; circular citation doesn't. **Step 4 —
the common failure modes:** misattributed quotes, real numbers stripped of context,
and once-true-now-stale figures. **Step 5 — verdict with confidence,** and if
refuted/partial, state the accurate version. Some claims are genuinely
**unverifiable** — say so rather than guessing.

## Principles
1. **Trace to the primary source** — repetition isn't corroboration.
2. **Independent corroboration** raises confidence; circular citation doesn't.
3. **Precise claim first** — verify what's actually asserted.
4. **Context and currency matter** — a true-out-of-context number misleads.
5. **"Unverifiable" is a valid, honest verdict.**
6. **Always show evidence** — never a bare true/false.

## Decision framework
- **Statistic?** Find the originating dataset/study, check date and definition.
- **Quote?** Find the original utterance/text; beware paraphrase and misattribution.
- **Repeated everywhere?** Trace the chain to one origin before counting it corroborated.
- **Can't reach a primary source?** Mark unverifiable; state what's missing.
- **High stakes?** Require multiple independent primary confirmations.

## Common mistakes
- **Counting repetition as corroboration** (citogenesis).
- **Stopping at a secondary source** that cites the real one.
- **Verifying a vague version** of the claim.
- **Ignoring context/date** — a real number, misleading as used.
- **Forcing a true/false** on an unverifiable claim.
- **No evidence trail** behind the verdict.

## Validation checklist
- [ ] The exact claim is isolated and precise.
- [ ] Traced to a primary/original source.
- [ ] Corroborated by independent sources (not circular).
- [ ] Misattribution, context, and currency checked.
- [ ] Verdict (confirmed/partial/refuted/unverifiable) + confidence assigned.
- [ ] Evidence shown; correction supplied where needed.

## Edge cases
- **Predictions/opinions:** not facts — label as such; verify only the factual basis.
- **Contested facts:** present the state of evidence and where authorities disagree.
- **Rapidly changing data:** note the as-of date; "true last quarter" may be false now.
- **Manipulated media/quotes:** trace to the original; flag doctoring.

## Related skills
- [assessing-source-credibility](../assessing-source-credibility/SKILL.md), [collecting-evidence](../collecting-evidence/SKILL.md), [citing-sources](../citing-sources/SKILL.md).
- [reviewing-research](../../review/reviewing-research/SKILL.md).

## Examples
**Input:** "Fact-check: 'The Great Wall of China is visible from space with the naked eye.'"
**Output:** **Refuted** (high confidence). Traced to a long-repeated myth; astronauts
and NASA state it is not visible unaided from low Earth orbit. Corroborated by
multiple independent authoritative sources. Accurate version: it's generally not
distinguishable to the naked eye from space without aid.

## Automation opportunities
- Use the deep-research harness's adversarial verification for batches of claims.
- Maintain a claim → primary-source ledger to avoid re-verifying.
