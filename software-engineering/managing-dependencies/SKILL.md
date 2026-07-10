---
name: managing-dependencies
description: Add and maintain third-party dependencies safely — prefer minimal well-maintained libraries, pin via lockfiles, reason about semver ranges, update deliberately, watch transitive deps, and respond to vulnerabilities. Use when the user asks "should I add this library", "how do I pin/lock deps", "is this update safe", "what does this semver range mean", "audit my dependencies", or "there's a CVE in a package I use".
---

# Managing Dependencies

## Scope
Choosing, pinning, updating, and securing third-party packages across an
application or library. Not writing the application code that uses them — that is
[implementing-features](../implementing-features/SKILL.md).

## Purpose
Get needed functionality without importing risk: minimize the dependency surface,
make builds reproducible, and keep known-vulnerable or abandoned code out of
production.

## When to use this skill
- Evaluating whether to add a library vs write it yourself.
- Setting up or fixing pinning/lockfiles for reproducible builds.
- Planning a deliberate dependency update or major-version bump.
- Responding to a CVE, audit alert, or transitive-dep surprise.

## When NOT to use this skill
- Writing the feature that consumes the dep → [implementing-features](../implementing-features/SKILL.md).
- Shipping the release once deps are settled → [packaging-and-releasing-software](../packaging-and-releasing-software/SKILL.md).
- Security review of your own code → [writing-secure-code](../writing-secure-code/SKILL.md).

## Inputs
- The capability needed and candidate libraries.
- Ecosystem tooling and manifest/lockfile (e.g. package + lock, or equivalent).
- Whether the artifact is an app (pin exact) or a library (declare ranges).
- Current advisories/audit output and update cadence.

## Outputs
- A justified add/build decision and chosen library.
- A committed lockfile and sane version constraints.
- A remediation plan for vulnerabilities and a repeatable update process.

## Workflow
```
Progress:
- [ ] 1. Decide: real need? build vs buy?
- [ ] 2. Vet candidates (maintenance, security, license, size)
- [ ] 3. Add with correct constraint; commit the lockfile
- [ ] 4. Inspect transitive deps introduced
- [ ] 5. Update deliberately; test after every bump
- [ ] 6. Monitor advisories; remediate on a schedule
```

**Step 1 — Decide.** Confirm the need is real and non-trivial. A one-liner you
can own beats a dependency; a hard, well-solved problem (crypto, parsing, dates)
favors a mature library. Weigh the maintenance and supply-chain cost of every add.

**Step 2 — Vet.** Check recent commits/releases, open-issue responsiveness, number
of maintainers (bus factor), download trend, and a compatible license. Skim the
code size and its own dependency count. Avoid packages with a single unresponsive
maintainer or a bloated transitive tree.

**Step 3 — Add + pin.** Apps: pin exact and commit the lockfile so every
environment resolves identically. Libraries: declare the widest *safe* semver
range so consumers can dedupe. Always commit the lockfile; never `.gitignore` it
for an app.

**Step 4 — Inspect transitive deps.** One add can pull dozens of indirect
packages — the real attack/bloat surface. Review the resolved tree, watch for
duplicate/conflicting versions, and prefer deps with shallow trees.

**Step 5 — Update deliberately.** Patch/minor: batch regularly, let CI verify.
Major: read the changelog/migration guide, bump in isolation, run the full suite.
Never blanket-bump everything blind before a release.

**Step 6 — Monitor + remediate.** Run an audit tool in CI. On a CVE, check
whether the vulnerable path is actually reachable, then upgrade to the patched
version; if none exists, pin a safe version, apply an override, or replace the dep.

## Principles
- Every dependency is a liability you now maintain and trust — add reluctantly.
- Lockfiles make builds reproducible; ranges express intended compatibility.
- Semver is a promise, not a guarantee — test even "safe" patch bumps.
- Transitive deps are your deps: they run with your privileges.
- Update in small, frequent increments; giant batched upgrades hide the breaker.

## Decision framework
- **Build vs buy:** trivial/owned logic → build; hard, security-sensitive, well-
  maintained → buy.
- **Pin exact vs range:** deployable app → pin (+lockfile); published library → range.
- **Patch/minor vs major update:** batch small ones; isolate and migration-test majors.
- **CVE response:** reachable & fix exists → upgrade; no fix → override/pin/replace;
  unreachable → schedule, don't scramble.

## Common mistakes
- **Not committing the lockfile** — "works on my machine", non-reproducible prod.
- **Unpinned/`latest` in production** — silent breakage on the next install.
- **Adding a heavy dep for one function** — bloat and supply-chain risk.
- **Ignoring transitive deps** — the vulnerability is usually indirect.
- **Blind bulk upgrades before a release** — one bump breaks and you can't isolate it.
- **Chasing every CVE alert** without checking reachability — noise over signal.
- **Abandonware** — depending on a package with no release in years.

## Validation checklist
- [ ] Each dependency is justified vs building it or an existing dep.
- [ ] Candidates vetted for maintenance, license, and size.
- [ ] Lockfile committed; app deps pinned, library deps ranged.
- [ ] Transitive tree reviewed; no duplicate/conflicting versions.
- [ ] Tests green after every add/update.
- [ ] Audit runs in CI; known CVEs triaged with a plan.

## Edge cases
- **No patched version for a CVE:** override the transitive pin, fork/patch, or replace.
- **Diamond/version conflict:** align on one version; use resolutions/overrides.
- **License incompatibility (e.g. copyleft in proprietary):** reject or isolate.
- **Native/binary deps:** verify platform builds and reproducibility.
- **Deprecated package:** plan migration before it becomes an emergency.

## Related skills
- [packaging-and-releasing-software](../packaging-and-releasing-software/SKILL.md) — shipping with locked deps.
- [writing-secure-code](../writing-secure-code/SKILL.md) — supply-chain and code-level security.
- [implementing-features](../implementing-features/SKILL.md) — the code that uses the deps.

## Examples
**Input:** "An audit flags a critical CVE in a package I don't import directly — what do I do?"
**Output:** It's transitive. Trace which direct dep pulls it and whether the
vulnerable code path is reachable. If the direct dep has a release requiring the
patched version, bump it and test. If not, add a resolution/override forcing the
patched transitive version, verify the tree resolves, run the suite, and file an
upstream issue. Document the override so it isn't lost on the next update.

## Automation opportunities
- Dependency-update bots (grouped patch/minor PRs) plus CI gates.
- `audit`/SCA scanning and license checks in the pipeline.
- Renovate/Dependabot config, lockfile-drift checks, SBOM generation.
- Fail CI on missing lockfile or unpinned production deps.
