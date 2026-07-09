---
name: writing-policies
description: Write clear, enforceable organizational policies, procedures, and standards — with unambiguous scope, defined terms, specific requirements (must/should/may), roles, and compliance/enforcement sections. Use when the user asks to "write a policy", "draft a procedure/SOP/standard", document rules or governance, or improve an existing policy. Produces an unambiguous, auditable policy document, not a vague guideline.
---

# Writing Policies

## Scope
Formal governing documents: policies (what and why), procedures/SOPs (how, step by
step), and standards (specific measurable requirements). Emphasis on being
unambiguous and enforceable. Not general prose or technical how-tos
([writing-technical-documentation](../writing-technical-documentation/SKILL.md)).

## Purpose
Produce a document that removes ambiguity: readers know exactly what is required of
them, who is responsible, what happens on non-compliance, and it can be audited
against.

## When to use this skill
- "Write a policy / procedure / SOP / standard / guideline."
- Documenting rules, governance, compliance, or acceptable-use requirements.
- Formalizing an informal practice into an enforceable standard.
- Improving a vague or unenforceable existing policy.

## When NOT to use this skill
- Technical/system docs → [writing-technical-documentation](../writing-technical-documentation/SKILL.md).
- Persuasive documents → [writing-proposals](../writing-proposals/SKILL.md).
- General communication → [writing-business-prose](../writing-business-prose/SKILL.md).

## Inputs
- The behavior/outcome the policy must govern and why (the risk it addresses).
- Scope: who and what it applies to, and exceptions.
- Legal/regulatory requirements it must satisfy; the owner and approval authority.

## Outputs
- A structured policy: purpose, scope, definitions, policy statements
  (must/should/may), roles/responsibilities, procedures, compliance/enforcement,
  and version/review metadata.

## Workflow
```
Progress:
- [ ] 1. Define purpose (the risk/objective) and scope (who/what/exceptions)
- [ ] 2. Define terms precisely
- [ ] 3. State requirements with must/should/may — no ambiguity
- [ ] 4. Assign roles and responsibilities
- [ ] 5. Add procedures (the how) where needed
- [ ] 6. Add compliance, enforcement, and exceptions
- [ ] 7. Add ownership, approval, effective date, review cycle
```

**Step 1 — Purpose & scope.** State the objective/risk and precisely who and what it
covers ("all employees and contractors handling customer data") and what it doesn't.

**Step 2 — Definitions.** Define every term that could be read two ways
("confidential data", "device", "promptly"). Ambiguous terms make a policy
unenforceable.

**Step 3 — Requirements.** Use RFC-2119-style modality consistently: **must/shall**
= mandatory, **should** = recommended, **may** = optional. Each statement is
specific and testable ("must encrypt at rest using AES-256"), not aspirational
("should keep data safe").

**Step 4 — Roles.** State who is responsible, accountable, and who enforces. A
requirement with no owner isn't enforceable.

**Step 5 — Procedures.** Where the policy implies actions, give the step-by-step
procedure (or link an SOP).

**Step 6 — Compliance & exceptions.** State how compliance is verified, consequences
of violation, and the exception process (who can grant, how).

**Step 7 — Governance.** Owner, approver, effective date, version, and review cycle.
Policies without a review date rot into non-compliance.

## Principles
1. **Unambiguous or unenforceable.** Every requirement must be testable.
2. **Consistent modality.** Must/should/may used precisely, never interchangeably.
3. **Define your terms.** Undefined words are loopholes.
4. **Assign responsibility.** No orphan requirements.
5. **Governed and dated.** Owner, approval, and review cycle are mandatory.

## Decision framework
- **What & why?** Policy. **How, step by step?** Procedure/SOP. **Exact measurable bar?** Standard.
- **Regulatory driver?** Cite the regulation and map requirements to it.
- **High-risk behavior?** Mandatory (must) + enforcement + audit.
- **Judgment allowed?** Should/may + guidance, not a hard rule.

## Common mistakes
- **Vague requirements** ("handle data appropriately") that can't be audited.
- **Mixing must/should** so mandatory and optional blur.
- **Undefined terms** creating loopholes.
- **No enforcement or exception process** — the policy is ignored.
- **No owner/review date** — it silently becomes outdated and non-compliant.
- **Writing procedure as policy** (or vice versa) — the reader can't tell rule from step.

## Validation checklist
- [ ] Purpose (risk/objective) and scope (who/what/exceptions) are explicit.
- [ ] All ambiguous terms defined.
- [ ] Every requirement uses must/should/may consistently and is testable.
- [ ] Roles and responsibilities assigned.
- [ ] Compliance verification, enforcement, and exception process stated.
- [ ] Regulatory requirements cited and covered (if applicable).
- [ ] Owner, approver, effective date, version, and review cycle present.

## Edge cases
- **Multi-jurisdiction:** note where requirements differ by region/law.
- **Conflicting policies:** state precedence and cross-reference.
- **Transition periods:** give an effective date and grace period for existing cases.
- **Emergency exceptions:** define a break-glass process with retrospective approval.

## Related skills
- [writing-technical-documentation](../writing-technical-documentation/SKILL.md) — for the SOPs it references.
- [writing-business-prose](../writing-business-prose/SKILL.md), [authoring-word-documents](../authoring-word-documents/SKILL.md).
- [comparing-documents](../comparing-documents/SKILL.md) — review policy revisions.

## Examples
**Input:** "Write a remote-work equipment policy."
**Output:** Policy with purpose (security + cost control), scope (all remote staff),
definitions (company device, personal device, sensitive data), requirements
(employees **must** use company-issued devices for sensitive data; **should**
report loss within 24h; **may** use personal devices for email only), roles (IT
enforces, managers approve exceptions), an exception process, and owner/approval/
review-annually metadata.

## Automation opportunities
- Maintain a policy register with owners and review dates; flag overdue reviews.
- Version and diff revisions with [comparing-documents](../comparing-documents/SKILL.md).
- Generate an attestation/quiz form from the requirements with [designing-forms](../designing-forms/SKILL.md).
