---
name: engineering-prompts
description: Write effective prompts for LLMs — state the task and output format precisely, supply role and context, add few-shot examples and chain-of-thought where they earn their place, set constraints, and iterate against real failures. Use when the user asks "how do I prompt for X", "write a prompt for...", "why is the model ignoring my instructions", or "improve this prompt".
---

# Engineering Prompts

## Scope
Authoring and refining a single prompt (system + user, with optional examples) so an
LLM reliably produces the wanted output. Covers task framing, output specs, role and
context, few-shot, decomposition/chain-of-thought, constraints, and failure-driven
iteration. Not scoring or context budgeting.

## Purpose
Get correct, well-formatted output on the first shot as often as possible, and make
the remaining failures cheap to diagnose and fix — instead of guessing at wording.

## When to use this skill
- "Write / improve / debug a prompt for this task."
- The model ignores instructions, rambles, or returns the wrong shape.
- Turning a fuzzy ask into a precise, repeatable instruction.

## When NOT to use this skill
- Systematically scoring outputs against a rubric → [evaluating-prompts-and-outputs](../evaluating-prompts-and-outputs/SKILL.md).
- Fitting large inputs/history into the window → [managing-context-windows](../managing-context-windows/SKILL.md).
- Enforcing a strict machine-readable shape → [generating-structured-outputs](../generating-structured-outputs/SKILL.md).
- Building a scored dataset/harness in CI → [building-llm-evaluations](../building-llm-evaluations/SKILL.md).

## Inputs
- The task, its audience, and what a good output looks like (a real example beats a description).
- Known failure modes or wrong outputs from prior attempts.
- Constraints: length, format, tone, forbidden content, latency/cost budget.

## Outputs
- A prompt (system + user template, few-shot if used) with variables marked.
- A short rationale: why each part is there and which failure it prevents.
- Notes on residual failure modes and what to try next.

## Workflow
```
Progress:
- [ ] 1. State the task and success criteria in one sentence
- [ ] 2. Specify the output format concretely (shape + a filled example)
- [ ] 3. Add role, context, and constraints the model can't infer
- [ ] 4. Add few-shot / decomposition only where a plain prompt fails
- [ ] 5. Run on varied inputs incl. edge cases; collect failures
- [ ] 6. Fix the prompt against those failures; re-run; lock the version
```

**Step 1 — Frame the task.** Say exactly what to produce and how success is judged.
Put the core instruction first; ambiguity here surfaces as inconsistent output later.

**Step 2 — Specify output.** Describe the shape *and* show one filled example — a
vague output spec is the top cause of malformed results. Name the format (JSON,
markdown table, bullet list) and what to do when a field is unknown.

**Step 3 — Role and context.** Give the persona, domain facts, and constraints the
model cannot infer (audience, length ceiling, tone, what to refuse). State negatives
as positives where possible ("answer only from the passage" beats "don't hallucinate").

**Step 4 — Examples and reasoning.** Add few-shot only when instructions alone fail;
2–5 diverse, correct examples that cover edge cases beat many near-duplicates — an
over-long few-shot block wastes budget and biases toward its surface patterns. For
multi-step reasoning, ask for step-by-step work or decompose into chained prompts;
skip chain-of-thought for simple lookups where it only adds latency.

**Step 5 — Stress-test.** Run on varied and adversarial inputs (empty, huge,
malformed, out-of-scope). Record each failure verbatim.

**Step 6 — Iterate.** Change one thing per failure and re-run the whole set, so a fix
doesn't regress another case. Version the prompt once it holds.

## Principles
1. **Precision over politeness** — concrete instructions beat hedged, wordy ones.
2. **Show, don't just tell** — one worked example clarifies more than a paragraph.
3. **Front-load what matters** — key instructions first, not buried mid-prompt.
4. **Positive, testable constraints** — "use only X" over "never do Y".
5. **One change per iteration** — otherwise you can't attribute the fix.
6. **Least machinery that works** — reach for few-shot/CoT only when needed.

## Decision framework
- **Output shape wrong?** Add a filled example and name the format explicitly.
- **Reasoning wrong on multi-step tasks?** Add CoT or decompose into steps.
- **Instructions ignored?** Move them to the top; cut competing/contradictory text.
- **Inconsistent across inputs?** Add few-shot covering the varied cases.
- **Works on your examples only?** Suspect overfitting — test held-out inputs.

## Common mistakes
- **Vague output spec** — describing the format without showing one filled instance.
- **Over-long few-shot** — many similar examples that bloat cost and bias the style.
- **Prompt overfitting** — tuning until your handful of examples pass, then it breaks on new inputs.
- **Contradictory instructions** competing across a long prompt.
- **Chain-of-thought everywhere,** paying latency on tasks that don't need it.
- **Editing many things at once,** so no failure can be tied to a change.

## Validation checklist
- [ ] Task and success criteria stated in one sentence, up front.
- [ ] Output format specified with a concrete filled example.
- [ ] Role, context, and constraints the model can't infer are present.
- [ ] Few-shot/CoT used only where a plain prompt measurably failed.
- [ ] Tested on edge and adversarial inputs, not just the happy path.
- [ ] Held-out inputs pass (not just the examples you tuned on).
- [ ] Prompt versioned; residual failure modes noted.

## Edge cases
- **Format must be strictly parseable:** delegate the contract to [generating-structured-outputs](../generating-structured-outputs/SKILL.md).
- **Answer must stay grounded in sources:** pair with [building-rag-systems](../building-rag-systems/SKILL.md) and instruct "answer only from context".
- **Prompt is part of an agent loop:** keep tool instructions in [integrating-tool-use](../integrating-tool-use/SKILL.md), not the task prompt.
- **Refusals/safety needed:** encode allowed/forbidden behavior via [applying-guardrails](../applying-guardrails/SKILL.md).

## Related skills
- [evaluating-prompts-and-outputs](../evaluating-prompts-and-outputs/SKILL.md), [managing-context-windows](../managing-context-windows/SKILL.md), [generating-structured-outputs](../generating-structured-outputs/SKILL.md).
- [building-rag-systems](../building-rag-systems/SKILL.md), [integrating-tool-use](../integrating-tool-use/SKILL.md), [applying-guardrails](../applying-guardrails/SKILL.md), [detecting-hallucinations](../detecting-hallucinations/SKILL.md).

## Examples
**Input:** "The model summarizes support tickets but the summaries are inconsistent and too long."
**Output:** Set the task ("one-line summary + priority") first; specified output as a
2-field format with a filled example; capped length; added 3 few-shot cases covering
a bug, a billing issue, and an unclear ticket; instructed "if priority is unclear,
say 'unclear'". Stress-tested on empty and multi-issue tickets, fixed the multi-issue
case with an explicit rule, versioned the prompt.

## Automation opportunities
- Keep prompts in version control with the examples they were tuned against.
- Wire the stress-test inputs into a repeatable run ([building-llm-evaluations](../building-llm-evaluations/SKILL.md)).
- Template variables so the same prompt serves many inputs without hand-editing.
