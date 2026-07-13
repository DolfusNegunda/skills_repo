---
name: generating-structured-outputs
description: Get reliable structured output (JSON, enum, or typed object) from an LLM by defining a strict schema, using native structured-output/tool modes over free-text-then-parse, constraining enums and required fields, and validating every output against the schema with repair-and-retry on failure. Use when the goal is to "get JSON out of the model", "enforce a schema", "return a typed object", or fix cases where "the model returns invalid JSON" or drifts off the expected structured output.
---

# Generating Structured Outputs

## Scope
Getting machine-parseable output — JSON, an enum value, or a typed record — out of an
LLM reliably. Covers schema definition, native structured-output/tool modes, enum and
required-field constraints, and the produce→validate→repair loop. Not general prompt
wording, not tool-call design.

## Purpose
Turn a model response into data your code can consume without hand-written parsing:
a strict schema up front, a generation mode that constrains the model to it, and
validation that rejects malformed output before it reaches downstream code.

## When to use this skill
- "Get JSON out of the model", "return a typed object / structured output".
- "Enforce a schema", "constrain the output to these fields / these enum values".
- "The model returns invalid JSON", trailing prose, or drifts off the expected shape.
- Extraction/classification whose result feeds code, a DB, or another API.

## When NOT to use this skill
- General prompt wording and instruction quality → [engineering-prompts](../engineering-prompts/SKILL.md).
- Designing tools/functions the model calls to act → [integrating-tool-use](../integrating-tool-use/SKILL.md).
- Measuring output quality across a dataset → [building-llm-evaluations](../building-llm-evaluations/SKILL.md).

## Inputs
- The target shape: fields, types, which are required, and allowed enum values.
- The model/API and whether it supports a native JSON-schema or tool-call mode.
- Consumer expectations: how strict, what to do on failure, acceptable latency/retries.

## Outputs
- A strict schema (JSON Schema or typed model) and the generation mode bound to it.
- Validated output plus the produce→validate→repair loop that guarantees conformance.

## Workflow
```
Progress:
- [ ] 1. Define the strict schema: fields, types, required, enums, no extras
- [ ] 2. Pick the generation mode: native structured/tool > constrained > prompt-only
- [ ] 3. Prompt for the shape and give one exact example of valid output
- [ ] 4. Produce → validate against the schema → on failure feed the error back and retry
- [ ] 5. Accept only when valid; cap retries and handle exhaustion explicitly
- [ ] 6. Log failures and schema drift for evaluation
```

**Step 1 — Schema first.** Write the schema before prompting. Mark every field
`required` unless truly optional; set `additionalProperties: false` so extra keys are
rejected; make each enum an explicit value list, not "a string like X". Decide
nullable vs absent for each optional field — don't leave it ambiguous.

**Step 2 — Mode.** Prefer a native strict-schema or constrained-decoding mode that
*guarantees* shape. A general tool/function-calling mode strongly biases toward the
schema but does not hard-guarantee it (only strict/constrained variants do) — so
validate regardless. Free-text-then-regex is the last resort and the source of most breakage.

**Step 3 — Prompt.** State the shape and include one concrete valid example. Instruct:
output only the object, no markdown fences, no explanation before or after.

**Step 4 — Validate & repair.** Parse, then validate against the schema with
[scripts/validate_json_output.py](scripts/validate_json_output.py). On failure, feed
the exact validator error back to the model and ask it to return corrected output
matching the schema — do not hand-patch it yourself. Re-validate the retry.

**Step 5 — Accept or exhaust.** Accept only a response that validates clean. Cap
retries (2–3); on exhaustion raise/return an explicit error — never pass through
unvalidated output.

**Step 6 — Observe.** Record which field failed and how often, to catch enum drift and
schema mismatch over time.

## Principles
- Schema is the contract: define it first, validate against it always.
- Constrain generation, don't clean up after it — native mode over parse-and-pray.
- Every field has a decided type, requiredness, and (for enums) a closed value set.
- Invalid output is a failure to retry, not data to salvage by hand.
- Reject unknown keys and extra prose rather than tolerating them.

## Decision framework
- **Native structured/tool mode vs prompt-only:** if the API offers schema binding, use it — always.
- **JSON object vs single enum:** one classification label → constrain to an enum, not a wrapping object.
- **Optional field vs nullable:** absent means "not provided", `null` means "known empty" — pick one per field and encode it.
- **Repair vs regenerate:** validator error is small/local → repair with the error fed back; response is garbled → regenerate fresh.
- **Strict vs lenient parse:** consumer is code/DB → strict, `additionalProperties: false`; exploratory → lenient, but still validate.

## Common mistakes
- **Free-text-then-regex** parsing instead of a native/constrained mode — brittle to any wording change.
- **Markdown code-fence wrapping** (```json …```) breaking `JSON.parse`; strip fences or forbid them in the prompt.
- **Trailing prose** ("Here is the JSON:" / "Hope this helps") before or after the object.
- **Unescaped strings** — literal newlines/quotes inside string values producing invalid JSON.
- **Optional-vs-required confusion** — no `required` list, so missing fields pass silently.
- **Enum drift** — model returns a synonym/casing variant not in the allowed set; constrain the enum.
- **Silent truncation** — output cut at the token limit yields incomplete JSON; check finish reason and length.
- **Skipping validation** because "it looked right" in testing.

## Validation checklist
- [ ] Schema defines types, `required`, enums, and `additionalProperties: false`.
- [ ] Generation uses a native structured/tool or constrained mode where available.
- [ ] Prompt forbids markdown fences and surrounding prose; includes one valid example.
- [ ] Every output validated against the schema before use; invalid output never consumed.
- [ ] Repair loop feeds the validator error back and re-validates; retries are capped.
- [ ] Enum values, nullability, and finish reason (truncation) all checked.
- [ ] Failures are logged for drift detection.

## Edge cases
- **Truncation:** if finish reason is length, raise the token limit or split the task; don't retry blindly.
- **Nested/recursive schemas:** validate the whole tree; deeply nested shapes lower reliability — flatten if you can.
- **Streaming:** you cannot validate until the object is complete; buffer, then validate.
- **Numbers vs strings:** pin numeric fields as numbers in the schema; models often quote them.
- **Empty/degenerate input:** define the valid "nothing found" result (e.g. `[]`) so the model has a legal answer.
- **Model can't satisfy the schema:** allow an explicit `{"error": ...}` branch instead of forcing a bad fit.

## Related skills
- [engineering-prompts](../engineering-prompts/SKILL.md) — general prompt wording and instruction design.
- [integrating-tool-use](../integrating-tool-use/SKILL.md) — designing the tools/functions a model calls.
- [building-llm-evaluations](../building-llm-evaluations/SKILL.md) — measuring output quality and drift over a dataset.
- [writing-automated-tests](../../software-engineering/writing-automated-tests/SKILL.md) — testing the parse/validate path.
- [handling-errors-and-logging](../../software-engineering/handling-errors-and-logging/SKILL.md) — failing loud and logging on exhaustion.

## Scripts
- [scripts/validate_json_output.py](scripts/validate_json_output.py) — validate a JSON output file against a JSON-Schema-subset file; exits non-zero with machine-readable errors, driving the produce→validate→fix loop.

## Examples
**Input:** "Extract `{name, email, priority}` from a support message; priority is one of
low/medium/high, and the model keeps wrapping JSON in ```json fences with a sentence after it."
**Output:** Define a schema with `required: [name, email, priority]`, `priority` as an
enum `["low","medium","high"]`, `additionalProperties: false`. Switch to the API's
native JSON-schema mode; prompt "output only the object, no fences, no prose".
Validate each response with the validator script; on failure feed the error back and
retry up to twice; accept only a clean pass, else raise.

## Automation opportunities
- Generate the schema from your typed model (Pydantic/TypeScript) so code and contract stay in sync.
- Wrap produce→validate→repair as a reusable helper; ban raw model-output parsing via lint/review.
- Run the validator in CI against captured sample outputs to catch schema drift early.
