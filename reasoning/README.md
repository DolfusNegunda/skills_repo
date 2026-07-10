# Reasoning & Decision-Making Skills

The thinking methods underneath every other category: how to decompose a problem,
find a root cause, weigh tradeoffs, decide under uncertainty, prioritize, estimate,
and stress-test reasoning. Every skill here follows the house style in
[../skill-builder/SKILL.md](../skill-builder/SKILL.md).

## Design philosophy

Pure **procedure and judgment skills** — no scripts. Each captures a reusable
cognitive method with its steps, decision rules, and the specific traps that derail
it (non-MECE splits, stopping 5-whys too early, correlation-as-cause, ignoring
opportunity cost, optimizing a non-binding constraint, analysis paralysis on
reversible decisions, unfalsifiable hypotheses, false precision in estimates). These
sharpen the business, research, review, and engineering skills that lean on them.

## The skills

**Framing the problem**
| Skill | Focus |
|---|---|
| [decomposing-problems](decomposing-problems/SKILL.md) | Break an ambiguous problem into MECE parts via issue/problem trees. |
| [analyzing-root-causes](analyzing-root-causes/SKILL.md) | 5-whys, fishbone, causal chains; cause vs. symptom. |
| [analyzing-gaps](analyzing-gaps/SKILL.md) | Current vs. desired state, quantified, with what closes the gap. |
| [identifying-constraints](identifying-constraints/SKILL.md) | Find the binding constraint (Theory of Constraints); hard vs. soft. |

**Deciding**
| Skill | Focus |
|---|---|
| [analyzing-tradeoffs](analyzing-tradeoffs/SKILL.md) | Weigh options against criteria; make opportunity cost explicit. |
| [deciding-under-uncertainty](deciding-under-uncertainty/SKILL.md) | Expected value, reversible vs. irreversible, base rates, bias. |
| [prioritizing-options](prioritizing-options/SKILL.md) | Order many items by value/effort (RICE, WSJF, MoSCoW, Eisenhower). |

**Reasoning under uncertainty**
| Skill | Focus |
|---|---|
| [estimating-under-uncertainty](estimating-under-uncertainty/SKILL.md) | Fermi decomposition, ranges, explicit assumptions, sanity checks. |
| [planning-scenarios](planning-scenarios/SKILL.md) | Multiple futures, pre-mortem, leading indicators, contingency triggers. |
| [testing-hypotheses](testing-hypotheses/SKILL.md) | Falsifiable hypotheses, evidence that confirms/disconfirms, honest updating. |

**Checking the thinking**
| Skill | Focus |
|---|---|
| [thinking-in-systems](thinking-in-systems/SKILL.md) | Feedback loops, delays, stocks/flows, second-order effects. |
| [detecting-fallacies-and-inconsistencies](detecting-fallacies-and-inconsistencies/SKILL.md) | Logical fallacies, contradictions, unstated assumptions. |

## How they compose

- **Attack a hard problem:** [decomposing-problems](decomposing-problems/SKILL.md) →
  [analyzing-root-causes](analyzing-root-causes/SKILL.md) /
  [identifying-constraints](identifying-constraints/SKILL.md) →
  [analyzing-tradeoffs](analyzing-tradeoffs/SKILL.md) →
  [deciding-under-uncertainty](deciding-under-uncertainty/SKILL.md).
- **Plan amid uncertainty:** [estimating-under-uncertainty](estimating-under-uncertainty/SKILL.md) +
  [planning-scenarios](planning-scenarios/SKILL.md) +
  [testing-hypotheses](testing-hypotheses/SKILL.md).
- **Pressure-test a conclusion:** [detecting-fallacies-and-inconsistencies](detecting-fallacies-and-inconsistencies/SKILL.md) +
  [thinking-in-systems](thinking-in-systems/SKILL.md) before committing.

## Cross-category links

- **Business decisions:** [../business/building-decision-matrices](../business/building-decision-matrices/SKILL.md),
  [../business/analyzing-cost-benefit](../business/analyzing-cost-benefit/SKILL.md),
  [../business/running-swot-analysis](../business/running-swot-analysis/SKILL.md),
  [../business/maintaining-risk-registers](../business/maintaining-risk-registers/SKILL.md).
- **Evidence & review:** [../research/verifying-facts](../research/verifying-facts/SKILL.md),
  [../review/conducting-structured-reviews](../review/conducting-structured-reviews/SKILL.md).
- **Applied root-causing:** [../software-engineering/debugging-systematically](../software-engineering/debugging-systematically/SKILL.md),
  [../data-engineering/observing-data-pipelines](../data-engineering/observing-data-pipelines/SKILL.md).
