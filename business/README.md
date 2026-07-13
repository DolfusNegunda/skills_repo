# Business Skills

Operational competencies for business analysis, planning, and management — turning
ambiguous situations into structured analysis, plans, and decisions. Every skill
here follows the house style in [../skill-builder/SKILL.md](../skill-builder/SKILL.md).

## Design philosophy

These skills produce **artifacts and decisions, not theory**. Each one takes real
inputs (a problem, a set of options, a group of stakeholders) and yields a
structured deliverable a team can act on — a requirements set, a risk register, a
business case, a decision. They cross-link to the office authoring skills for
rendering and to the review skills for quality gates.

## The skills

**Analysis & discovery**
| Skill | Produces |
|---|---|
| [performing-business-analysis](performing-business-analysis/SKILL.md) | Problem framed, root cause, and options |
| [gathering-requirements](gathering-requirements/SKILL.md) | Clear, testable requirements |
| [mapping-processes](mapping-processes/SKILL.md) | As-is/to-be process maps |
| [analyzing-stakeholders](analyzing-stakeholders/SKILL.md) | Stakeholder map + engagement plan |

**Planning & tracking**
| Skill | Produces |
|---|---|
| [planning-projects](planning-projects/SKILL.md) | Project charter/plan (scope, milestones, RACI) |
| [building-roadmaps](building-roadmaps/SKILL.md) | Outcome-oriented roadmap |
| [maintaining-risk-registers](maintaining-risk-registers/SKILL.md) | Scored, owned risk register |
| [defining-kpis](defining-kpis/SKILL.md) | Meaningful, gameable-resistant KPIs |
| [setting-okrs](setting-okrs/SKILL.md) | Aligned objectives + measurable key results |

**Decision & justification**
| Skill | Produces |
|---|---|
| [running-swot-analysis](running-swot-analysis/SKILL.md) | Actionable SWOT (not a list) |
| [analyzing-cost-benefit](analyzing-cost-benefit/SKILL.md) | CBA with NPV/ROI/payback |
| [building-decision-matrices](building-decision-matrices/SKILL.md) | Weighted decision matrix |
| [writing-business-cases](writing-business-cases/SKILL.md) | Fundable business case |

**Organization & people**
| Skill | Produces |
|---|---|
| [managing-change](managing-change/SKILL.md) | Change/adoption plan |
| [establishing-governance](establishing-governance/SKILL.md) | Decision rights + governance model |
| [facilitating-meetings](facilitating-meetings/SKILL.md) | Productive, outcome-driven meetings |
| [negotiating-agreements](negotiating-agreements/SKILL.md) | Prepared, principled negotiation |
| [communicating-with-stakeholders](communicating-with-stakeholders/SKILL.md) | Targeted stakeholder communications |

## How they compose

- `performing-business-analysis` → `gathering-requirements` → `writing-business-cases`
  → (review with [../review/reviewing-business-cases](../review/reviewing-business-cases/SKILL.md)).
- `analyzing-stakeholders` feeds `communicating-with-stakeholders`, `managing-change`, and `planning-projects`.
- `analyzing-cost-benefit` + `running-swot-analysis` + `building-decision-matrices`
  feed the recommendation in `writing-business-cases`.
- `planning-projects` uses `maintaining-risk-registers` and `analyzing-stakeholders`.
- Render deliverables with the office skills ([../office/writing-reports](../office/writing-reports/SKILL.md),
  [../office/engineering-excel-workbooks](../office/engineering-excel-workbooks/SKILL.md)).
- The decision and analysis skills lean on the
  [../reasoning](../reasoning/README.md) methods: `building-decision-matrices` ↔
  [../reasoning/analyzing-tradeoffs](../reasoning/analyzing-tradeoffs/SKILL.md),
  `performing-business-analysis` ↔ [../reasoning/analyzing-root-causes](../reasoning/analyzing-root-causes/SKILL.md),
  `analyzing-cost-benefit` ↔ [../reasoning/estimating-under-uncertainty](../reasoning/estimating-under-uncertainty/SKILL.md).
- For rolling out an AI system as an organizational change, pair `managing-change`
  with [../ai-engineering](../ai-engineering/README.md) (e.g.
  [../ai-engineering/designing-ai-systems](../ai-engineering/designing-ai-systems/SKILL.md)).
