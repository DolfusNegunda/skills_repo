---
name: designing-apis
description: Design clear, evolvable HTTP/REST APIs — model resources, choose methods and status codes, name consistently, plan versioning, pagination, filtering, idempotency, error shape, and auth, contract-first with OpenAPI. Use when the user asks to "design an API", "define endpoints", "write an OpenAPI spec", pick REST verbs/status codes, or plan API versioning and pagination before code exists.
---

# Designing APIs

## Scope
Designing the external contract of an HTTP/REST API before implementation: resource
model, methods, status codes, naming, versioning, pagination, filtering, idempotency,
error shape, and auth — captured as an OpenAPI document. Not the server code behind it.

## Purpose
Produce an API that is predictable to call, safe to evolve without breaking clients, and
honest about failure — so integrators succeed without reading your source.

## When to use this skill
- "Design an API / define the endpoints / write the OpenAPI spec."
- Choosing REST verbs, status codes, URL structure, or an error format.
- Planning versioning, pagination, filtering, or idempotency for a new or growing API.

## When NOT to use this skill
- Building against an existing contract → [implementing-features](../implementing-features/SKILL.md).
- Reviewing a proposed system/API design → [reviewing-architecture](../../review/reviewing-architecture/SKILL.md).
- Publishing/versioning the artifact that ships → [packaging-and-releasing-software](../packaging-and-releasing-software/SKILL.md).

## Inputs
- The domain nouns and the client use cases (who calls what, and why).
- Consumers (internal, partner, public) and expected scale/latency.
- Auth context, existing API conventions to stay consistent with, and hard constraints.

## Outputs
- An OpenAPI document: resources, paths, methods, status codes, request/response schemas,
  error shape, auth scheme, pagination/filter params, and versioning note.
- A short rationale for the non-obvious choices.

## Workflow
```
Progress:
- [ ] 1. Map use cases to resources (nouns), not RPC verbs
- [ ] 2. Assign methods + status codes per resource; decide collection vs item
- [ ] 3. Fix naming, pagination, filtering, and the error shape as global rules
- [ ] 4. Decide idempotency, auth, and the versioning strategy
- [ ] 5. Write it contract-first as OpenAPI; validate against use cases
- [ ] 6. Dry-run the common client flows; check evolvability
```

**Step 1 — Model resources.** Extract nouns from use cases; expose resources and
sub-resources, not actions. `POST /transfers`, not `POST /doTransfer`. Reserve
non-CRUD "action" endpoints (`POST /orders/{id}/cancel`) for genuine state transitions
that aren't a field write.

**Step 2 — Methods and status codes.** GET (safe, no body effect), PUT (full replace,
idempotent), PATCH (partial), POST (create/action, not idempotent by default), DELETE
(idempotent). Use 200/201/204, 400/401/403/404/409/422, 429, 500/503 precisely — 201
with `Location` on create, 204 for empty success, 409 for conflicts, 422 for semantic
validation failure, 404 vs 403 to avoid leaking existence.

**Step 3 — Global rules.** Pick one convention and hold it everywhere: plural nouns
(`/users/{id}/orders`), lowercase-hyphen paths, a single JSON casing. Standardize
cursor pagination (`?limit=&cursor=`) over offset for large/mutating sets. Define one
error envelope for the whole API (see Principles).

**Step 4 — Idempotency, auth, versioning.** Support an `Idempotency-Key` header for
POST that creates money/side effects. Choose an auth scheme (OAuth2/bearer, API key) and
mark scopes per operation. Choose a versioning strategy up front (URL `/v1` is simplest
and most visible) and write down what counts as breaking.

**Step 5 — Contract-first.** Author the OpenAPI document as the source of truth before
any handler. Define reusable `components/schemas`, shared error and pagination shapes,
and examples. The spec, not the code, is the contract.

**Step 6 — Validate.** Walk each client use case through the paths end to end. Confirm
every added field/param is optional and additive so v1 clients keep working.

## Principles
- **Resources over actions.** URLs name things; methods name what you do to them.
- **Design for the client, not the table.** Shape responses around use cases, not schema rows.
- **One error shape, everywhere.** e.g. `{ "error": { "code": "...", "message": "...", "details": [...] } }` — machine `code`, human `message`, field-level `details`.
- **Additive is safe; removal/rename/retype is breaking.** New optional fields and new endpoints don't need a version bump; anything a client could already depend on does.
- **Idempotent by contract.** GET/PUT/DELETE must be safely retryable; make risky POSTs idempotent with a key.
- **Pagination and filtering are defaults, not features.** Any list that can grow needs a bounded page and a stable sort.

## Decision framework
- **PUT vs PATCH?** Full-object replace → PUT; partial update → PATCH.
- **Sub-resource vs query param?** Ownership/hierarchy → path (`/users/{id}/orders`); optional narrowing → query (`?status=open`).
- **Action endpoint vs field?** A pure field write → PATCH; a real state machine transition with side effects → `POST /{id}/{action}`.
- **URL vs header versioning?** Public/visible/cache-friendly → URL `/v1`; fine-grained content negotiation → header. Pick one; don't mix.
- **Offset vs cursor pagination?** Small stable data → offset is fine; large or concurrently-mutating → cursor.

## Common mistakes
- **RPC-in-REST** — verbs in URLs (`/getUser`, `/createOrder`) instead of resources.
- **200-for-everything** — success status on errors, forcing clients to parse the body to detect failure.
- **Leaking the database** — exposing internal IDs, column names, and join tables as the API.
- **Breaking changes disguised as fixes** — renaming a field, tightening a type, or making an optional field required without a version bump.
- **Unbounded lists** — no default page size, no max, no stable sort → timeouts and inconsistent pages.
- **Inconsistent errors** — a different error format per endpoint.

## Validation checklist
- [ ] Every endpoint maps to a resource; actions are justified state transitions.
- [ ] Methods match semantics; idempotent methods are actually idempotent.
- [ ] Status codes are specific (201+Location, 204, 4xx split, 429, 5xx).
- [ ] One error envelope and one naming/casing convention used throughout.
- [ ] Lists are paginated with a bounded default and stable sort; filters documented.
- [ ] Auth scheme and per-operation scopes defined; versioning strategy chosen.
- [ ] OpenAPI validates; examples present; every client use case is reachable.

## Edge cases
- **Bulk operations:** decide partial-success semantics (207-style multi-status body) up front.
- **Long-running work:** return 202 + a status resource to poll, not a blocked request.
- **Money/side effects:** require an idempotency key and document retry behavior.
- **Public APIs:** stability and deprecation policy matter more than elegance; announce and sunset with headers.

## Related skills
- [implementing-features](../implementing-features/SKILL.md) — building against the contract you designed.
- [applying-design-patterns](../applying-design-patterns/SKILL.md), [handling-errors-and-logging](../handling-errors-and-logging/SKILL.md), [writing-secure-code](../writing-secure-code/SKILL.md).
- [reviewing-architecture](../../review/reviewing-architecture/SKILL.md), [writing-technical-documentation](../../office/writing-technical-documentation/SKILL.md).

## Examples
**Input:** "Design an API for orders and their line items; clients need to list, create, and cancel orders."
**Output:** Resources `/orders`, `/orders/{id}`, `/orders/{id}/items`. `GET /orders?status=&limit=&cursor=` (cursor pagination, `created_at` sort); `POST /orders` → 201 + `Location`, accepts `Idempotency-Key`; `POST /orders/{id}/cancel` → 200 or 409 if already shipped. One error envelope; bearer auth with `orders:write` scope; URL-versioned `/v1`. Delivered as an OpenAPI document with shared schemas and examples.

## Automation opportunities
- Lint the OpenAPI spec (Spectral) for naming, error-shape, and status-code rules in CI.
- Generate client SDKs and server stubs from the spec so code can't drift from the contract.
- Run a contract/diff check on each PR to flag breaking changes before merge.
