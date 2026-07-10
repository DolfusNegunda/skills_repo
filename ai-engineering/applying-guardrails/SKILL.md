---
name: applying-guardrails
description: Put safety guardrails around an LLM — validate and constrain inputs and outputs, defend against prompt injection and jailbreaks, filter unsafe/PII content, enforce allow-lists on tools and actions, and fail safe. Use when the user says "add guardrails", "protect against prompt injection", "sanitize LLM output", "restrict what the agent can do", or "make this AI feature safe to ship".
---

# Applying Guardrails

## Scope
Wrapping an LLM feature in a control layer: input validation, output filtering,
prompt-injection and jailbreak defense, PII/unsafe-content handling, tool/action
allow-lists, and safe-failure behavior. Assumes the model call already works and
now needs to be safe to expose.

## Purpose
Keep the system safe under adversarial and accidental misuse — block unsafe inputs
and outputs, contain what the model is allowed to do, and degrade gracefully instead
of dangerously when something slips through.

## When to use this skill
- "Add guardrails / protect against prompt injection / sanitize output."
- Exposing an LLM to untrusted users, retrieved content, or real-world actions.
- Restricting an agent's tools/actions or enforcing content and PII policy.

## When NOT to use this skill
- General secure coding (authn, secrets, injection in app code) → [writing-secure-code](../../software-engineering/writing-secure-code/SKILL.md).
- Factual grounding and citation of answers → [detecting-hallucinations](../detecting-hallucinations/SKILL.md).
- Tool wiring itself (schemas, execution) → [integrating-tool-use](../integrating-tool-use/SKILL.md).

## Inputs
- The feature's trust boundaries: who/what feeds the model, what it can act on.
- Policy: disallowed content, PII rules, regulatory constraints.
- The tool/action surface and the blast radius of each action.

## Outputs
- Input and output guard layers with defined block/allow/escalate behavior.
- A tool/action allow-list with per-action authorization and limits.
- A tested fail-safe path, plus logging/metrics for blocked and flagged events.

## Workflow
```
Progress:
- [ ] 1. Map trust boundaries, untrusted inputs, and action blast radius
- [ ] 2. Guard inputs: validate, constrain, detect injection/jailbreak
- [ ] 3. Guard outputs: filter unsafe content, redact PII, enforce format
- [ ] 4. Constrain tools/actions with an allow-list and authorization
- [ ] 5. Define fail-safe behavior for every guard
- [ ] 6. Red-team, tune thresholds, and log every decision
```

**Step 1 — Map trust.** List every untrusted source — user input, retrieved
documents, tool outputs, prior turns — and what the model can *do* (send, delete,
pay, expose). Guards go on boundaries; the highest-risk actions get the tightest ones.

**Step 2 — Guard inputs.** Validate structure and length; strip or neutralize
control instructions. Treat retrieved and tool-returned text as data, never as
instructions — injection via retrieved content is the classic breach. Detect
jailbreak patterns, but assume detection is porous and rely on Step 4 for real limits.

**Step 3 — Guard outputs.** Screen for unsafe/disallowed content, redact PII,
enforce the required schema before anything downstream consumes it. Never render or
execute raw model output in a sensitive sink without checking.

**Step 4 — Constrain actions.** Put tools behind an explicit allow-list. Authorize
each call against the *user's* permissions, not the model's persona; apply
rate/amount limits and require confirmation for irreversible actions. This is the
containment that holds when prompt-level defenses fail.

**Step 5 — Fail safe.** Decide per guard: block, redact, escalate to human, or
degrade. On uncertainty or guard error, deny — never fail open. Return a safe,
non-leaky message.

**Step 6 — Red-team + observe.** Attack it: injection strings in documents,
role-play jailbreaks, encoding tricks, tool-abuse chains. Tune thresholds against
over-blocking, and log every block/flag/allow. Feed adversarial cases into
[building-llm-evaluations](../building-llm-evaluations/SKILL.md).

## Principles
1. **Defense in depth** — input, output, and action layers; no single choke point.
2. **Untrusted content is data, never instructions** — including retrieved and tool text.
3. **Contain, don't just detect** — allow-lists and authz hold when classifiers miss.
4. **Fail safe, fail closed** — deny on doubt; safe error messages.
5. **Least privilege for actions** — smallest tool surface, per-user authorization.
6. **Tune for both errors** — measure false blocks and false allows; over-blocking is a failure too.

## Decision framework
- **Input from an untrusted source?** Validate + treat as data; isolate from system instructions.
- **Output hits a sensitive sink (DB, shell, browser, user)?** Filter/validate before it lands.
- **Action irreversible or high-value?** Allow-list + per-user authz + confirmation/limit.
- **Guard classifier uncertain?** Escalate or deny — don't pass through.
- **Legit users hitting blocks?** Loosen thresholds or add context; don't ship an unusable guard.

## Common mistakes
- **Prompt-injection via retrieved content** — trusting document/tool text as instructions.
- **Over-blocking** — aggressive filters that reject safe inputs and frustrate users.
- **Detection without containment** — a jailbreak classifier but no action allow-list behind it.
- **Failing open** — errors or timeouts in a guard let unchecked output through.
- **Authorizing on the model's persona** instead of the actual user's permissions.
- **Guarding input only** — no output filter, so unsafe generations still reach users.
- **Leaky error messages** — refusals that echo the blocked content or system prompt.

## Validation checklist
- [ ] Every untrusted input source identified and guarded; retrieved text treated as data.
- [ ] Output filtered for unsafe content, PII redacted, schema enforced before use.
- [ ] Tools behind an allow-list; each action authorized against the user, with limits.
- [ ] Every guard has a defined fail-safe; guard errors deny, not allow.
- [ ] Red-teamed against injection, jailbreaks, and tool abuse; cases captured.
- [ ] False-block and false-allow rates measured and acceptable.
- [ ] Blocks/flags/allows logged; no sensitive data leaked in errors or logs.

## Edge cases
- **Multilingual / obfuscated attacks:** encoding, translation, and homoglyph evasions bypass keyword filters — test them.
- **Multi-turn escalation:** attacks that build across turns; guard on conversation state ([managing-context-windows](../managing-context-windows/SKILL.md)).
- **Agentic chains:** a benign-looking step enabling a harmful one; authorize each action, not just the first ([designing-agent-systems](../designing-agent-systems/SKILL.md)).
- **PII in outputs from context:** redact even when the model merely echoes retrieved PII.

## Related skills
- [writing-secure-code](../../software-engineering/writing-secure-code/SKILL.md), [detecting-hallucinations](../detecting-hallucinations/SKILL.md), [integrating-tool-use](../integrating-tool-use/SKILL.md).
- [building-llm-evaluations](../building-llm-evaluations/SKILL.md), [generating-structured-outputs](../generating-structured-outputs/SKILL.md), [designing-agent-systems](../designing-agent-systems/SKILL.md).
- [managing-context-windows](../managing-context-windows/SKILL.md), [building-rag-systems](../building-rag-systems/SKILL.md).

## Examples
**Input:** "Our agent can email customers and issue refunds — make it safe."
**Output:** Mapped trust: user chat + retrieved KB (both untrusted) and two
actions, one irreversible (refund). Inputs validated and marked as data; KB text
never merged into system instructions. Output filter redacts PII before send. Tools
allow-listed: email capped per hour; refunds require per-user authz, an amount
limit, and human confirmation above threshold. Guards fail closed with a generic
message. Red-teamed injection-in-KB and refund-escalation chains; both contained.
Block/allow events logged and fed into the eval set.

## Automation opportunities
- Run the red-team suite in CI on any change to prompts, tools, or retrieval.
- Auto-block deploys when false-allow rate on the adversarial set rises.
- Alert on spikes in blocked events (possible attack) and false blocks (broken guard).
