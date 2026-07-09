---
name: reviewing-policies
description: Review organizational policies and procedures for enforceability, clarity, completeness, consistency, and compliance — producing severity-ranked findings with specific fixes. Use when the user asks to "review this policy/procedure/SOP", "is this policy enforceable", "check this against regulation", or assess a policy before publication. Inherits the shared severity/scoring model. Produces an actionable review that catches ambiguity and gaps before a policy goes live.
---

# Reviewing Policies

## Scope
Evaluation of policies, procedures, and standards for whether they can actually be
followed and enforced. Inherits method/severity/scoring from
[conducting-structured-reviews](../conducting-structured-reviews/SKILL.md). Writing
them is [writing-policies](../../office/writing-policies/SKILL.md).

## Purpose
Ensure a policy is unambiguous, complete, consistent with other rules, and
compliant — before publication, when ambiguity becomes loopholes and gaps become risk.

## When to use this skill
- "Review this policy / procedure / SOP / standard."
- "Is this policy enforceable / clear / complete?"
- Checking a policy against regulation or other policies before it goes live.

## When NOT to use this skill
- Writing the policy → [writing-policies](../../office/writing-policies/SKILL.md).
- Legal/contractual documents → [reviewing-contracts](../reviewing-contracts/SKILL.md).
- General document quality → [reviewing-documents](../reviewing-documents/SKILL.md).

## Inputs
- The policy and its purpose/scope; who it governs.
- Applicable regulations and related/superseded policies.
- The owner and approval context.

## Outputs
- A review: verdict + scores, severity-ranked findings (clause + issue + fix), a
  gap/conflict list, and strengths.

## Evaluation rubric (dimensions)
1. **Enforceability** — requirements are specific, testable, and auditable ("must encrypt at rest", not "keep data safe").
2. **Clarity/unambiguity** — defined terms; consistent must/should/may; no vague language.
3. **Completeness** — scope, roles, procedures, exceptions, and consequences all present.
4. **Consistency** — no conflict with other policies; precedence stated where needed.
5. **Compliance** — satisfies the regulations it must; requirements traceable to them.
6. **Usability** — a target reader can find and follow what applies to them.
7. **Governance** — owner, approval, effective date, and review cycle present.

## Scoring & severity
Score 1–5; rank Blocker→Praise (see
[foundation reference](../conducting-structured-reviews/references/severity-and-scoring.md)).
Examples: **Blocker** = a requirement that contradicts a regulation, or a mandatory
control that's unenforceable as written; **Major** = "must" and "should" used
interchangeably so obligations blur; **Minor** = an undefined term; **Nit** = missing review date.

## Workflow
```
Progress:
- [ ] 1. Confirm purpose, scope, audience, and applicable regulations
- [ ] 2. Test each requirement for enforceability (can you audit it?)
- [ ] 3. Check clarity: defined terms and consistent modality
- [ ] 4. Check completeness, consistency with other policies, and compliance
- [ ] 5. Assess usability and governance metadata
- [ ] 6. Severity-rank, score, verdict; fixes per finding
```

**Step 2 — the audit test:** for each requirement ask "could an auditor objectively
determine compliance?" If not, it's unenforceable. **Step 4** — check the policy
against its regulatory obligations and against sibling policies for conflicts.

## Recommended-improvements guidance
Give the enforceable rewrite (vague → specific, testable requirement), the term to
define, the modality to fix (must vs. should), the missing section (exceptions,
consequences), or the regulation to cite and map.

## Validation checklist
- [ ] Every requirement is specific, testable, and auditable.
- [ ] Terms defined; must/should/may used consistently.
- [ ] Scope, roles, procedures, exceptions, and consequences all present.
- [ ] No conflicts with other policies; precedence stated where needed.
- [ ] Regulatory obligations covered and traceable.
- [ ] Owner, approval, effective date, and review cycle present.
- [ ] Findings carry severity + a fix; verdict + scores given.

## Common mistakes
- **Accepting vague requirements** that can't be enforced.
- **Missing must/should inconsistency** that blurs what's mandatory.
- **Reviewing in isolation** — missing conflicts with existing policy.
- **No compliance traceability** — assuming rather than checking regulatory coverage.
- **Ignoring usability** — technically complete but unfindable/unfollowable.

## Edge cases
- **Multi-jurisdiction:** check where requirements must differ by region/law.
- **Superseding a prior policy:** confirm transition, precedence, and no orphaned references.
- **High-risk domains (security, safety, privacy):** completeness and enforceability are Blocker-level.
- **Cross-references:** verify linked procedures/SOPs exist and match.

## Related skills
- [conducting-structured-reviews](../conducting-structured-reviews/SKILL.md), [writing-policies](../../office/writing-policies/SKILL.md).
- [reviewing-contracts](../reviewing-contracts/SKILL.md), [establishing-governance](../../business/establishing-governance/SKILL.md).

## Examples
**Input:** "Review our new data-retention policy before publishing."
**Output:** Verdict: Approve-with-changes (Enforceability 2/5, Compliance 3/5).
**Blocker:** "retain records as long as necessary" is unauditable; fix: specify
retention periods per record type. **Major:** conflicts with the backup policy's
90-day purge; state precedence. **Minor:** "sensitive data" undefined. **Praise:**
clear roles and exception process.

## Automation opportunities
- Reuse the rubric as a pre-publication policy gate.
- Maintain a term glossary and a policy register to catch conflicts automatically.
- Flag vague-language keywords for human review.
