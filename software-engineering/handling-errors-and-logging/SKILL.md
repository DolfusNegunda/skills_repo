---
name: handling-errors-and-logging
description: Design robust error handling and useful logs — decide fail-fast vs recover, use exceptions or result types deliberately, never swallow errors, and emit structured logs at the right level with context and correlation IDs but no secrets or PII. Use when the user asks to "add error handling", "improve logging", "why is this error silent", "make failures debuggable", or set up observability for a service. Produces a deliberate failure and logging strategy, not scattered try/catch.
---

# Handling Errors and Logging

## Scope
How code fails and how it reports — error-handling strategy (raise, recover, retry)
and logging/observability (levels, structure, context). Not a full security audit of
the system.

## Purpose
Make failures safe and diagnosable: fail fast on programmer errors, recover
deliberately from expected ones, never hide a failure, and leave logs that let
someone reconstruct what happened — with enough context and zero leaked secrets.

## When to use this skill
- "Add error handling / improve logging / make failures debuggable."
- "Why is this error silent / swallowed?" or errors vanish in production.
- Setting up logging, log levels, or correlation IDs for a service.

## When NOT to use this skill
- Whole-system threat review → [writing-secure-code](../writing-secure-code/SKILL.md) or [reviewing-code](../../review/reviewing-code/SKILL.md).
- Chasing a specific defect → [debugging-systematically](../debugging-systematically/SKILL.md).
- Public error contracts of an API → [designing-apis](../designing-apis/SKILL.md).

## Inputs
- The operation and its failure modes (expected vs. unexpected, transient vs. fatal).
- The runtime context: service/CLI/library, callers, existing logging stack.
- What's sensitive (secrets, PII) and any correlation/trace conventions in use.

## Outputs
- A failure strategy per path (fail-fast vs. recover/retry) and structured logs at
  correct levels with context and IDs — no swallowed errors, no leaked secrets.

## Workflow
```
Progress:
- [ ] 1. Enumerate failure modes per operation (expected vs. unexpected)
- [ ] 2. Decide fail-fast vs. recover/retry for each; pick exceptions vs. results
- [ ] 3. Handle at the layer that can act; preserve cause and context
- [ ] 4. Add structured logs at the right level with correlation IDs
- [ ] 5. Scrub secrets/PII from logs and error messages
- [ ] 6. Verify: failures surface, logs reconstruct the story, tests cover paths
```

**Step 2 — expected vs. exceptional.** Recover from things you anticipate (bad
input, transient network); let programmer errors and unrecoverable states fail fast
and loud. Use exceptions for exceptional flow, result/error types where failure is a
normal outcome the caller must handle. **Step 3 — never swallow:** an empty `catch`,
`except: pass`, or a caught error logged and dropped hides bugs. Handle where you can
act; otherwise propagate, wrapping to add context while preserving the original cause
(chained exception / wrapped error). **Step 4 — log for the reader:** structured
key/value fields, one correlation/request ID threaded through, actionable message.
**Step 5 — no secrets:** never log passwords, tokens, keys, or PII.

## Principles
1. **Never swallow an error** — handle, propagate, or fail; never silently drop.
2. **Fail fast on the unexpected;** recover only from what you anticipated.
3. **Preserve the cause** — wrap with context, don't discard the original.
4. **Log the right level** — ERROR for actionable failures, not for control flow.
5. **Structure and correlate** — machine-parseable fields, one ID across the request.
6. **Never log secrets or PII.**

## Decision framework
- **Failure the caller must handle routinely?** Result/error type over exception.
- **Bug or impossible state?** Fail fast — crash loud beats corrupt-and-continue.
- **Transient (network/lock)?** Bounded retry with backoff, then give up loudly.
- **Caught but can't act here?** Re-raise/wrap with context; don't log-and-swallow.
- **Level choice?** DEBUG dev detail · INFO milestones · WARN recovered/degraded ·
  ERROR needs attention · FATAL process dying.

## Common mistakes
- **Swallowed exceptions** — empty catch, `except: pass`, or catch-log-continue on a bug.
- **Catching too broad** — `except Exception`/`catch (Throwable)` hiding real faults.
- **Losing the cause** — re-throwing a new error without chaining the original.
- **Logging secrets/PII** — tokens, passwords, full request bodies.
- **Wrong level** — errors at INFO, or noisy ERROR spam that hides real ones.
- **Unstructured logs** — string-concatenated messages you can't query.
- **No correlation ID** — can't trace one request across services.

## Validation checklist
- [ ] Failure modes enumerated; fail-fast vs. recover decided per path.
- [ ] No swallowed errors; broad catches justified and narrowed where possible.
- [ ] Errors wrapped with context; original cause preserved.
- [ ] Logs structured, at correct levels, with a correlation/request ID.
- [ ] No secrets or PII in logs or error messages.
- [ ] Retries bounded with backoff; give-up path is loud.
- [ ] Tests exercise both success and failure branches.

## Edge cases
- **Libraries:** raise typed exceptions; don't log or decide policy for the caller.
- **Batch jobs:** collect and report per-item failures; don't abort the whole run silently.
- **Async/concurrent:** ensure rejected promises/tasks are awaited so errors aren't lost.
- **High-volume paths:** sample or rate-limit logs to avoid drowning signal.
- **User-facing errors:** show a safe message; log the detail server-side, not to the user.

## Related skills
- [writing-secure-code](../writing-secure-code/SKILL.md), [debugging-systematically](../debugging-systematically/SKILL.md), [designing-apis](../designing-apis/SKILL.md).
- [writing-automated-tests](../writing-automated-tests/SKILL.md), [reviewing-code](../../review/reviewing-code/SKILL.md).

## Examples
**Input:** "Our worker silently drops failed jobs — add error handling and logging."
**Output:** Found `except Exception: pass` around each job. Changed to: catch the
specific expected errors, retry transient ones 3x with backoff, and on final failure
log at ERROR with `{job_id, attempt, err}` plus the chained cause, then mark the job
failed (don't drop). Programmer errors now propagate and crash the worker loudly.
Threaded a `correlation_id` through the log fields; scrubbed the payload of API
tokens. Added tests for the retry and give-up branches.

## Automation opportunities
- Lint for empty/broad catch blocks and `except: pass`.
- Adopt a structured logger; enforce a field schema and a secret-redaction filter.
- Wire correlation-ID propagation into middleware so every log line carries it.
