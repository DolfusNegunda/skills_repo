---
name: integrating-tool-use
description: Give an LLM reliable tool/function calling — design clear tool schemas and descriptions, validate arguments, handle tool errors and retries, prevent unsafe calls, and keep the tool set small and orthogonal. Use when the user asks to "add tools to my agent", "define a function schema", fix a model that calls the wrong tool or passes bad arguments, or make tool calls safe and robust.
---

# Integrating Tool Use

## Scope
The interface between an LLM and its tools: schema and description design, argument
validation, error and retry handling, safety gating, and keeping the tool set small and
orthogonal. Not the agent's control loop, not memory, not free-form structured output
that isn't a tool call.

## Purpose
Make the model pick the right tool and pass valid arguments the first time, fail safely
when it doesn't, and never fire a dangerous call — so the tool layer is a reliable
contract, not a source of silent corruption.

## When to use this skill
- "Add tools / function calling to my agent" or "define a tool schema."
- The model calls the wrong tool, passes malformed or hallucinated arguments, or ignores a tool.
- Making tool calls safe: validation, retries, and blocking destructive actions.

## When NOT to use this skill
- Overall agent architecture and the loop → [designing-agent-systems](../designing-agent-systems/SKILL.md).
- Structured output that isn't a tool call → [generating-structured-outputs](../generating-structured-outputs/SKILL.md).
- Content-level safety and policy filtering → [applying-guardrails](../applying-guardrails/SKILL.md).

## Inputs
- The actions the agent must perform and the underlying APIs/functions behind them.
- Which actions are read-only, costly, or irreversible; auth/permission context.
- Existing tool definitions to stay consistent with.

## Outputs
- A set of tool schemas (name, description, typed parameters, required/optional) with examples.
- Argument-validation and error-return conventions.
- A safety policy for costly/irreversible tools.

## Workflow
```
Progress:
- [ ] 1. List needed actions; merge/drop until the set is small and orthogonal
- [ ] 2. Write each tool schema: name, description, typed params, required flags
- [ ] 3. Sharpen descriptions so tool choice and args are unambiguous
- [ ] 4. Validate arguments before executing; reject with an actionable message
- [ ] 5. Define error returns, bounded retries, and safety gates
- [ ] 6. Test with adversarial and ambiguous prompts; check the model's calls
```

**Step 1 — Curate the tool set.** Start from the actions the agent truly needs. Keep the
set small and orthogonal — each tool does one thing, no two overlap. Overlapping or
near-duplicate tools make the model pick wrong; a huge menu degrades selection. Prefer a
few composable tools over many specific ones.

**Step 2 — Design schemas.** Give each tool a verb-based name, a one-line description of
when to use it, and a typed parameter schema (JSON Schema) with `required` marked, enums
for closed sets, and formats/ranges. Constrain at the schema level so invalid arguments
are unrepresentable rather than caught later.

**Step 3 — Write descriptions for the model.** The description is a prompt: state what
the tool does, when to use it, when NOT to, and what each parameter means. Disambiguate
tools that could be confused ("use `search_docs` for internal docs; `web_search` for
public web"). Most wrong-tool and bad-argument bugs are description bugs.

**Step 4 — Validate arguments.** Never trust model-supplied arguments. Validate against
the schema, then apply business rules (existence, permissions, bounds). On failure,
return a structured error the model can act on ("`user_id` not found; call `list_users`
first"), not a stack trace. Treat arguments as untrusted input for injection/path/SQL.

**Step 5 — Errors, retries, safety.** Return errors as structured tool results so the
loop can recover; distinguish retryable (timeout, rate limit → bounded backoff) from
terminal (bad args, not found → don't retry). Gate irreversible or costly tools behind
confirmation, dry-run, or a permission check. Make idempotent tools safe to retry.

**Step 6 — Test the calls.** Exercise each tool with ambiguous, adversarial, and
missing-argument prompts; confirm the model selects correctly and validation catches bad
args. Log every call (tool, args, result) for debugging and evals.

## Principles
- **Small, orthogonal tool set.** One job per tool, no overlap; composition over a huge menu.
- **The description is the interface.** The model chooses from prose — make it unambiguous.
- **Constrain in the schema.** Types, enums, and required flags make bad calls unrepresentable.
- **Never trust model arguments.** Validate against schema and business rules before executing.
- **Errors are structured returns, not crashes.** Give the model something it can recover from.
- **Irreversible tools need a gate.** Confirm, dry-run, or permission-check first.

## Decision framework
- **One tool or several?** If a param cleanly selects behavior, one tool with an enum; if concerns differ (tools/errors/permissions), split.
- **Retry or not?** Transient (timeout/429) → bounded backoff; terminal (bad args/not found) → return error, no retry.
- **Enum vs free string?** Closed set of valid values → enum, always; open text only when genuinely unbounded.
- **Gate a tool?** Read-only → open; writes/costs money/irreversible → confirmation or dry-run.
- **Fix wrong-tool bugs where?** First in descriptions/schema, only then in the loop logic.

## Common mistakes
- **Too many tools / overlapping tools** — the model can't reliably choose.
- **Vague descriptions** — "does stuff with users" yields wrong calls and bad args.
- **Trusting arguments** — executing model-supplied values without validation (injection, wrong IDs, out-of-range).
- **Unstructured errors** — raising exceptions instead of returning a result the model can recover from.
- **Blind retries** — retrying terminal errors, or retrying non-idempotent writes and duplicating side effects.
- **No safety gate** — a `delete_all` tool exposed with no confirmation.
- **Free-text where an enum belongs** — the model invents invalid values.

## Validation checklist
- [ ] Tool set is minimal and orthogonal; no two tools overlap.
- [ ] Each tool has a verb name, a when-to-use description, and a typed schema with required flags.
- [ ] Closed-value params use enums; ranges/formats constrained.
- [ ] Arguments validated against schema and business rules before execution.
- [ ] Errors returned as structured, actionable results; retryable vs terminal distinguished.
- [ ] Irreversible/costly tools are gated; idempotent tools safe to retry.
- [ ] Calls logged; tested against ambiguous and adversarial prompts.

## Edge cases
- **Parallel tool calls:** ensure argument validation and side effects are safe when several fire at once.
- **Long-running tools:** return a handle/status to poll rather than blocking the call.
- **Streaming/partial args:** validate only once the full argument object is assembled.
- **Auth per tool:** enforce the caller's permissions server-side; the model's role is not authorization.
- **Large tool outputs:** truncate or summarize before returning so one result doesn't blow the context.

## Related skills
- [designing-agent-systems](../designing-agent-systems/SKILL.md) — the loop that invokes these tools.
- [generating-structured-outputs](../generating-structured-outputs/SKILL.md), [applying-guardrails](../applying-guardrails/SKILL.md).
- [engineering-prompts](../engineering-prompts/SKILL.md), [managing-context-windows](../managing-context-windows/SKILL.md).
- [designing-apis](../../software-engineering/designing-apis/SKILL.md), [writing-secure-code](../../software-engineering/writing-secure-code/SKILL.md), [handling-errors-and-logging](../../software-engineering/handling-errors-and-logging/SKILL.md).

## Examples
**Input:** "My agent keeps calling `get_user` with names instead of IDs and sometimes calls `delete_user` by mistake."
**Output:** Split ambiguity: `find_user(query: string)` returns candidates with IDs;
`get_user(user_id: string)` takes only an ID (schema `format`, validated to exist).
Descriptions state the order explicitly ("resolve a name with `find_user` first").
`delete_user` gated behind a confirmation flag and a permission check, and marked
irreversible. Bad-ID calls return `{error: "user_id not found, call find_user"}` — a
recoverable result, no retry. Calls logged for eval.

## Automation opportunities
- Generate tool schemas from existing API/function signatures so they can't drift.
- Enforce schema validation in a shared tool-runner wrapper, not per-tool.
- Build a regression suite of prompts → expected tool calls; run in CI on schema changes.
