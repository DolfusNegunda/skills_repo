---
name: reviewing-architecture
description: Review a software or system architecture for fitness to requirements, scalability, resilience, security, cost, operability, and risk — producing severity-ranked findings, trade-off analysis, and a recommendation. Use when the user asks to "review this architecture/design", "assess this system design", "critique this technical proposal", or evaluate an architecture before build. Inherits the shared severity/scoring model. Produces an actionable architecture review, not a redesign.
---

# Reviewing Architecture

## Scope
Evaluation of system/software architecture and design proposals against
requirements and quality attributes, surfacing risks and trade-offs. Inherits
method/severity/scoring from
[conducting-structured-reviews](../conducting-structured-reviews/SKILL.md).
Code-level review is [reviewing-code](../reviewing-code/SKILL.md).

## Purpose
Judge whether a design will meet its functional and non-functional requirements at
acceptable cost and risk — before expensive commitment — and name the trade-offs the
authors may have glossed over.

## When to use this skill
- "Review this architecture / system design / technical proposal / RFC."
- An architecture gate before build or major investment.
- Assessing scalability, resilience, or cost risk of a design.

## When NOT to use this skill
- Code review → [reviewing-code](../reviewing-code/SKILL.md).
- Business justification → [reviewing-business-cases](../reviewing-business-cases/SKILL.md).
- Designing the architecture → an architecture authoring skill.

## Inputs
- The design (diagram, RFC, ADRs) and the requirements — especially non-functional
  ones (scale, latency, availability, security, budget).
- Constraints: team skills, existing stack, timeline, compliance.

## Outputs
- A review: recommendation (proceed / proceed-with-changes / reconsider) + scores,
  severity-ranked findings with trade-offs, key risks, and strengths.

## Evaluation rubric (dimensions)
1. **Fitness for requirements** — meets functional + non-functional needs.
2. **Scalability** — handles expected growth in load/data/users.
3. **Resilience** — failure modes, redundancy, graceful degradation, recovery.
4. **Security** — trust boundaries, data protection, authn/z, attack surface.
5. **Operability** — observability, deployability, maintainability, on-call load.
6. **Cost** — build + run economics; cost scales sensibly with usage.
7. **Simplicity & risk** — least complexity that works; reversible decisions; no unproven bet on the critical path.
8. **Data** — modeling, consistency, integrity, lifecycle, migration.

## Scoring & severity
Score 1–5; rank Blocker→Praise (see
[foundation reference](../conducting-structured-reviews/references/severity-and-scoring.md)).
Examples: **Blocker** = a single point of failure on a system requiring HA, or no
plan for the stated 100× scale; **Major** = no observability strategy; **Minor** =
a component that could be simpler; **Nit** = diagram labeling.

## Workflow
```
Progress:
- [ ] 1. Confirm requirements — especially non-functional — and constraints
- [ ] 2. Map the design: components, data flow, trust boundaries, dependencies
- [ ] 3. Assess each quality attribute against the requirements
- [ ] 4. Probe failure modes and scale limits explicitly
- [ ] 5. Weigh trade-offs and simpler alternatives
- [ ] 6. Severity-rank, score, recommendation; fixes/mitigations per finding
```

**Step 1 — non-functional requirements are the review.** Most architecture failures
are meeting features while missing scale, availability, or cost targets. **Step 4** —
ask "what happens when X fails?" and "what breaks at 10×/100×?" for each component.
**Step 5** — every architecture is trade-offs; name what each choice buys and costs,
and whether a simpler option was dismissed too quickly.

## Recommended-improvements guidance
Give the mitigation, not just the risk: the redundancy to add, the bottleneck to
remove, the boundary to harden, the observability to include, or the simpler
alternative — with the trade-off it implies.

## Validation checklist
- [ ] Non-functional requirements identified and each assessed.
- [ ] Failure modes and scale limits probed per component.
- [ ] Security trust boundaries and data flows examined.
- [ ] Cost (build + run) and operability considered.
- [ ] Trade-offs and simpler alternatives named.
- [ ] Findings carry severity + a mitigation; recommendation + scores given.

## Common mistakes
- **Reviewing features, ignoring scale/resilience/cost.**
- **No failure-mode analysis** — happy-path only.
- **Complexity bias** — praising sophistication over fitness.
- **Ignoring team/operational reality** — elegant but unrunnable by this team.
- **No trade-off framing** — findings without the cost of the alternative.

## Edge cases
- **Greenfield vs. evolution:** for existing systems weigh migration risk and reversibility.
- **Early proposal:** review direction and biggest risks, not detail.
- **Vendor/managed choices:** assess lock-in, SLA, and exit cost.
- **Unstated requirements:** flag the gap; don't assume the numbers.

## Related skills
- [conducting-structured-reviews](../conducting-structured-reviews/SKILL.md), [reviewing-code](../reviewing-code/SKILL.md).
- [reviewing-business-cases](../reviewing-business-cases/SKILL.md) — for the investment side.

## Examples
**Input:** "Review this design for our new event-processing platform (must handle 50k events/sec, 99.9% uptime)."
**Output:** Recommendation: Proceed-with-changes (Resilience 2/5, Scalability 4/5).
**Blocker:** the single Postgres writer can't sustain 50k/sec and is a SPOF vs the
99.9% target; fix: partitioned/streamed ingestion + replica failover. **Major:** no
dead-letter handling for poison events. **Praise:** clean, well-bounded services.

## Automation opportunities
- Reuse the quality-attribute rubric as a standing architecture-review gate.
- Require an ADR + non-functional requirements before review.
- Pair with load/chaos testing to validate resilience findings.
