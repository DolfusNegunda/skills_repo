# AI Engineering Skills

Operational competencies for building with LLMs: prompting, retrieval, agents,
structured output, evaluation, safety, and production system design. Every skill here
follows the house style in [../skill-builder/SKILL.md](../skill-builder/SKILL.md).

## Design philosophy

Mostly **procedure and judgment skills** (like [../software-engineering](../software-engineering/README.md))
— the disciplined workflow, decision rules, and specific gotchas an expert AI engineer
applies (lost-in-the-middle, prompt overfitting, dense-only retrieval missing IDs,
free-text-then-regex parsing, infinite agent loops, LLM-judge bias, prompt injection,
fabricated citations). One skill —
[generating-structured-outputs](generating-structured-outputs/SKILL.md) — ships a
**tested, dependency-free script** because JSON-output validation is a genuine
deterministic check: it runs in the CI smoke test alongside the office document scripts.

## The skills

**Prompting & context**
| Skill | Focus |
|---|---|
| [engineering-prompts](engineering-prompts/SKILL.md) | Precise task/format, role/context, few-shot, decomposition, iterate on failures. |
| [evaluating-prompts-and-outputs](evaluating-prompts-and-outputs/SKILL.md) | Rubrics, pairwise/reference grading, LLM-as-judge (with caveats), regressions. |
| [managing-context-windows](managing-context-windows/SKILL.md) | Token budget, selection/ordering, compaction, lost-in-the-middle. |

**Retrieval (RAG)**
| Skill | Focus |
|---|---|
| [building-rag-systems](building-rag-systems/SKILL.md) | End-to-end grounded, cited Q&A over a corpus. |
| [chunking-and-embedding-content](chunking-and-embedding-content/SKILL.md) | Chunking strategy, embedding choice, metadata, self-contained chunks. |
| [designing-vector-search](designing-vector-search/SKILL.md) | Index choice, recall vs latency, hybrid search, reranking. |

**Agents**
| Skill | Focus |
|---|---|
| [designing-agent-systems](designing-agent-systems/SKILL.md) | Control loop, single vs multi-agent, budgets, stop conditions, observability. |
| [integrating-tool-use](integrating-tool-use/SKILL.md) | Tool schemas, argument validation, error/retry, small orthogonal tool sets. |
| [managing-agent-memory](managing-agent-memory/SKILL.md) | Short vs long-term memory, summarization, what to persist/retrieve. |

**Output, evaluation & safety**
| Skill | Focus |
|---|---|
| [generating-structured-outputs](generating-structured-outputs/SKILL.md) | Schema-constrained JSON/typed output + validate-and-repair loop (**ships a script**). |
| [building-llm-evaluations](building-llm-evaluations/SKILL.md) | Datasets, metrics, offline/online evals, regression gates, drift. |
| [applying-guardrails](applying-guardrails/SKILL.md) | Input/output constraints, injection/jailbreak defense, PII filtering, fail-safe. |
| [detecting-hallucinations](detecting-hallucinations/SKILL.md) | Grounding, citations, verification, self-consistency, abstention. |

**System design**
| Skill | Focus |
|---|---|
| [designing-ai-systems](designing-ai-systems/SKILL.md) | Prompt vs RAG vs agent vs fine-tune; quality/latency/cost; fallbacks; monitoring. |

## How they compose

- **Start a feature:** [designing-ai-systems](designing-ai-systems/SKILL.md) decides the
  pattern → drills into [building-rag-systems](building-rag-systems/SKILL.md) /
  [designing-agent-systems](designing-agent-systems/SKILL.md) /
  [engineering-prompts](engineering-prompts/SKILL.md).
- **Build RAG:** [chunking-and-embedding-content](chunking-and-embedding-content/SKILL.md) +
  [designing-vector-search](designing-vector-search/SKILL.md) →
  [building-rag-systems](building-rag-systems/SKILL.md) →
  [detecting-hallucinations](detecting-hallucinations/SKILL.md).
- **Build an agent:** [designing-agent-systems](designing-agent-systems/SKILL.md) +
  [integrating-tool-use](integrating-tool-use/SKILL.md) +
  [managing-agent-memory](managing-agent-memory/SKILL.md) +
  [applying-guardrails](applying-guardrails/SKILL.md).
- **Ship reliably:** [generating-structured-outputs](generating-structured-outputs/SKILL.md) +
  [building-llm-evaluations](building-llm-evaluations/SKILL.md) gate every release.

## Cross-category links

- **Build & run:** [../software-engineering/designing-apis](../software-engineering/designing-apis/SKILL.md),
  [../software-engineering/writing-secure-code](../software-engineering/writing-secure-code/SKILL.md),
  [../software-engineering/handling-errors-and-logging](../software-engineering/handling-errors-and-logging/SKILL.md).
- **Data for retrieval:** [../data-engineering/governing-data-and-lineage](../data-engineering/governing-data-and-lineage/SKILL.md),
  [../data-engineering/observing-data-pipelines](../data-engineering/observing-data-pipelines/SKILL.md).
- **Grounding & truth:** [../research/verifying-facts](../research/verifying-facts/SKILL.md),
  [../research/assessing-source-credibility](../research/assessing-source-credibility/SKILL.md).
