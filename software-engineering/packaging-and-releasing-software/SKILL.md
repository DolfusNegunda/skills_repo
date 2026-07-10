---
name: packaging-and-releasing-software
description: Package and ship a release — apply semantic versioning, produce a changelog, build reproducible artifacts, run a release checklist, tag the release, and prepare a rollback plan. Use when the user asks "how do I cut a release", "what version number", "write the changelog", "tag and publish this", "build a reproducible artifact", or "what's my rollback plan if the release breaks".
---

# Packaging and Releasing Software

## Scope
Turning finished, tested code into a versioned, distributable release: version
choice, changelog, reproducible build, tagging, publish, and rollback. Not
writing or testing the code — those are
[implementing-features](../implementing-features/SKILL.md) and
[writing-automated-tests](../writing-automated-tests/SKILL.md).

## Purpose
Ship a release users can trust and you can reverse: a correctly versioned,
reproducible artifact with a truthful changelog and a rehearsed way back.

## When to use this skill
- Cutting a release/tag and choosing the version number.
- Producing a changelog or release notes.
- Building a reproducible, distributable artifact.
- Establishing or running a release checklist and rollback plan.

## When NOT to use this skill
- The code isn't finished → [implementing-features](../implementing-features/SKILL.md).
- Tests are missing/red → [writing-automated-tests](../writing-automated-tests/SKILL.md).
- Everyday branching/commits → [using-git-workflows](../using-git-workflows/SKILL.md).

## Inputs
- The release-candidate commit, current version, and changes since last release.
- Distribution channel (registry, image, installer) and its requirements.
- Locked dependencies and a green build/test pipeline.
- Deployment/rollback capabilities of the target environment.

## Outputs
- A semver version and an annotated tag on the release commit.
- A changelog/release notes grouped by change type.
- A reproducible, verifiable artifact published to its channel.
- A documented rollback plan.

## Workflow
```
Progress:
- [ ] 1. Confirm release-ready: green CI, deps locked, code frozen
- [ ] 2. Choose the semver version from the changes
- [ ] 3. Write the changelog / release notes
- [ ] 4. Build a reproducible, verifiable artifact
- [ ] 5. Tag, publish, verify the published artifact
- [ ] 6. Prepare and document the rollback plan
```

**Step 1 — Confirm readiness.** Run the release checklist: CI green on the exact
commit, dependencies locked (see [managing-dependencies](../managing-dependencies/SKILL.md)),
migrations/config accounted for, no debug/secret leakage. Freeze the candidate.

**Step 2 — Version.** Apply semver from the actual diff: MAJOR = breaking API
change, MINOR = backward-compatible feature, PATCH = backward-compatible fix.
Pre-releases use `-rc.N`/`-beta.N`. Let the changes decide the bump, not the calendar.

**Step 3 — Changelog.** Group entries by Added/Changed/Fixed/Deprecated/Removed/
Security, written for the *consumer*, not raw commit logs. Call out breaking
changes and migration steps prominently. Keep a running `CHANGELOG`. See
[writing-change-notes](../../office/writing-change-notes/SKILL.md).

**Step 4 — Build reproducibly.** Build from the clean tagged source in CI, not a
laptop. Pin toolchain and locked deps so the same input yields the same output.
Produce checksums/signatures. Verify the artifact installs and smoke-tests clean.

**Step 5 — Tag + publish.** Create an annotated, ideally signed tag on the exact
release commit (`git tag -a v1.4.0`), push it, then publish the built artifact.
After publishing, pull it fresh and verify version + checksum match.

**Step 6 — Rollback plan.** Before/at release, know how to reverse: previous
artifact retained, deploy supports revert, DB migrations are backward-compatible
or paired with a down path. Roll out gradually (canary/staged) where possible and
define the metric that triggers rollback.

## Principles
- The version number is a contract — a MAJOR bump is the only honest place for breaks.
- Reproducible builds: same source + toolchain → identical, verifiable artifact.
- A release without a rollback plan is a bet, not a plan.
- Tag the exact commit that was built and tested — never "close enough".
- Changelogs are for humans consuming the release, not a commit dump.

## Decision framework
- **Version bump:** breaking → MAJOR; new compatible feature → MINOR; fix only → PATCH.
- **Stable vs pre-release:** unproven/risky → `-rc`/`-beta`; verified → stable.
- **Rollback vs roll-forward:** fast clean revert available → rollback; data already
  migrated forward → fix-forward with a patch release.
- **Staged vs full rollout:** high blast radius → canary/staged; low risk → full.

## Common mistakes
- **No rollback plan** — discovering the break in prod with no way back.
- **Version doesn't reflect changes** — breaking change shipped as a PATCH.
- **Building on a dev machine** — unpinned, unreproducible, "works here" artifacts.
- **Tagging the wrong/untested commit** — tag drifts from what CI verified.
- **Auto-generated changelog dump** — noise instead of consumer-facing notes.
- **Irreversible migrations at release time** — rollback becomes impossible.
- **Publishing before verifying** — broken artifact already in users' hands.

## Validation checklist
- [ ] CI green on the exact release commit; deps locked; candidate frozen.
- [ ] Version follows semver from the real diff; breaking changes flagged.
- [ ] Changelog grouped by type, consumer-facing, migration steps noted.
- [ ] Artifact built in CI from tagged source; checksums/signatures produced.
- [ ] Annotated tag on the built commit; published artifact re-verified.
- [ ] Rollback plan documented and feasible; rollout strategy chosen.

## Edge cases
- **Hotfix on old version:** branch from that tag, patch, release `x.y.(z+1)`.
- **Breaking change, want to delay MAJOR:** deprecate with warnings, keep old path one cycle.
- **Backward-incompatible DB migration:** split into expand → migrate → contract releases.
- **Published a broken version:** publish a fixed higher version; avoid mutating a released tag.
- **Monorepo with many packages:** version/tag independently or lockstep, consistently.

## Related skills
- [using-git-workflows](../using-git-workflows/SKILL.md) — tagging and branch mechanics.
- [managing-dependencies](../managing-dependencies/SKILL.md) — locking deps before build.
- [writing-change-notes](../../office/writing-change-notes/SKILL.md) — the release-note prose.

## Examples
**Input:** "I fixed a bug but also changed a public function's signature — what version and what do I do?"
**Output:** The signature change is breaking → MAJOR bump (e.g. 2.0.0), not a
PATCH. Changelog under **Changed/Removed** with a migration snippet, plus the fix
under **Fixed**. Build from CI on the frozen commit, tag `v2.0.0` annotated on it,
publish, re-pull to verify checksum. Rollback plan: keep 1.x published and
deployable; if adoption breaks, users can pin 1.x while you patch.

## Automation opportunities
- Release pipeline: build → test → tag → publish on a version tag.
- Changelog generation from Conventional Commits, then human editing.
- Automated checksums/signing/SBOM and post-publish smoke tests.
- Canary/blue-green deploy with automated rollback on health-metric breach.
