---
name: writing-secure-code
description: Build security into code as you write it — validate and sanitize input, prevent injection (SQL/command/XSS), authenticate and authorize correctly, manage secrets safely, apply least privilege, and keep dependencies patched with an OWASP Top-10 mindset. Use when the user asks to "make this secure", "prevent SQL injection/XSS", "handle auth", "store secrets/passwords safely", or harden a feature that touches user input, credentials, or external systems. Produces secure-by-construction code, not an after-the-fact audit.
---

# Writing Secure Code

## Scope
Applying security while authoring code that handles untrusted input, credentials,
authorization, or external calls — input validation, injection prevention, authn/authz,
secret management, least privilege, and dependency hygiene. Building it in, not
auditing it afterward.

## Purpose
Ship code that resists the common attacks by construction: treat all external input
as hostile, use APIs that make injection impossible, enforce who-can-do-what, and
keep secrets and dependencies under control — an OWASP Top-10 mindset baked into the
change.

## When to use this skill
- "Make this secure / prevent SQL injection / stop XSS / handle auth."
- "Store secrets / passwords safely" or manage keys and tokens.
- Building a feature that takes user input, credentials, files, or external calls.

## When NOT to use this skill
- Only assessing existing code, not writing it → [reviewing-code](../../review/reviewing-code/SKILL.md).
- Error/log strategy (incl. not leaking secrets in logs) → [handling-errors-and-logging](../handling-errors-and-logging/SKILL.md).
- Query construction and tuning → [authoring-sql-queries](../authoring-sql-queries/SKILL.md).

## Inputs
- The feature and its trust boundaries: what input/credentials/systems it touches.
- Who the users/roles are and what each is allowed to do.
- The secrets involved and where they should live; the dependency set and its age.

## Outputs
- Code that validates input, uses injection-safe APIs, enforces authn/authz, keeps
  secrets out of source, runs least-privileged, and depends on patched libraries.

## Workflow
```
Progress:
- [ ] 1. Map trust boundaries — where untrusted input/credentials enter
- [ ] 2. Validate and sanitize input at the boundary (allow-list, typed)
- [ ] 3. Use injection-safe APIs (parameterized queries, safe encoders)
- [ ] 4. Enforce authentication, then authorization on every protected action
- [ ] 5. Move secrets out of code; store hashes; apply least privilege
- [ ] 6. Patch/pin dependencies; verify with tests and a security lens
```

**Step 2 — validate at the edge.** Prefer allow-lists (accept known-good) over
deny-lists; validate type, range, length, and format before use. **Step 3 — never
build commands from strings:** use parameterized/prepared statements for SQL,
argument arrays (not shell strings) for OS commands, and context-aware output
encoding for HTML/JS to stop XSS. String-concatenated SQL and shelling out with
interpolated input are the classic breaches. **Step 4 — authz ≠ authn:** verify
identity, then check permission on every protected action server-side; never trust
the client or a hidden field. **Step 5 — secrets:** never hard-code them — use env/
secret manager; store passwords as salted hashes (bcrypt/argon2), never plaintext or
reversible; grant the minimum rights the code needs.

## Principles
1. **Distrust all external input** — validate and sanitize at the boundary.
2. **Make injection impossible** — parameterize; never concatenate untrusted input into queries/commands/markup.
3. **Authenticate, then authorize** — check permission server-side on every action.
4. **Keep secrets out of code** — managed store; hash passwords; rotate keys.
5. **Least privilege** — minimal scopes, roles, and permissions everywhere.
6. **Patch dependencies** — track and update known-vulnerable libraries.

## Decision framework
- **Input crosses a trust boundary?** Allow-list validate before any use.
- **Building a query/command/markup with variables?** Parameterize or safely encode — no string building.
- **Protected action?** Enforce authz server-side; deny by default.
- **Need a secret?** Env var or secret manager — never a literal in source or config-in-repo.
- **Storing a password?** Salted hash (argon2/bcrypt), never encryptable/plaintext.
- **Adding/upgrading a dependency?** Check for known CVEs; pin and keep it current.

## Common mistakes
- **String-concatenated SQL / shell commands** — the injection classic.
- **Deny-list filtering** that misses an encoding or edge case; use allow-lists.
- **Trusting client-side checks** for authorization.
- **Hard-coded secrets** in source, config, or history; committed `.env`.
- **Plaintext/reversible passwords** instead of salted hashes.
- **Reflecting user input unescaped** into HTML → XSS.
- **Over-broad permissions** — admin/root where scoped access would do.
- **Stale vulnerable dependencies** left unpatched.

## Validation checklist
- [ ] Untrusted input validated/sanitized at the boundary (allow-list, typed).
- [ ] All queries parameterized; commands use arg arrays; output context-encoded.
- [ ] Authentication enforced; authorization checked server-side per action.
- [ ] No secrets in code/config/history; passwords salted-hashed.
- [ ] Least privilege applied to DB users, tokens, roles, file access.
- [ ] Dependencies scanned, pinned, and free of known critical CVEs.
- [ ] Errors don't leak stack traces/secrets to users (see handling-errors-and-logging).

## Edge cases
- **File uploads:** validate type/size, store outside webroot, never execute; avoid path traversal.
- **Deserialization:** don't deserialize untrusted data into arbitrary types.
- **Redirects:** allow-list redirect targets to prevent open redirects.
- **Timing/enumeration:** constant-time compares for secrets; uniform auth errors.
- **SSRF:** validate/allow-list outbound URLs built from user input.

## Related skills
- [handling-errors-and-logging](../handling-errors-and-logging/SKILL.md), [authoring-sql-queries](../authoring-sql-queries/SKILL.md), [managing-dependencies](../managing-dependencies/SKILL.md).
- [designing-apis](../designing-apis/SKILL.md), [reviewing-code](../../review/reviewing-code/SKILL.md).

## Examples
**Input:** "Add a login and a search box — make it secure."
**Output:** Search uses a parameterized query (was string-concatenated → SQL
injection); input is length/type validated and results are HTML-encoded on output to
block XSS. Login authenticates, then checks role server-side per request; passwords
stored with argon2 + per-user salt. DB creds moved from code to the secret manager;
the app's DB user is read/write on its own tables only (least privilege). Added a
dependency scan to CI and bumped two libraries with known CVEs.

## Automation opportunities
- Run SAST and dependency/CVE scanning (e.g. audit tools) in CI on every PR.
- Add a secret scanner and pre-commit hook to block committed credentials.
- Add lint rules banning string-built SQL/commands and unescaped output sinks.
