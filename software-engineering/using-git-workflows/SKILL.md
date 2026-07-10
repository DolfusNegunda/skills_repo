---
name: using-git-workflows
description: Work effectively with Git — choose a branching model, make atomic commits with clear messages, open reviewable PRs, decide rebase vs merge, resolve conflicts cleanly, and undo mistakes safely (revert/reset/reflog) without rewriting shared history. Use when the user asks to "structure my commits", "write a good commit message", "rebase or merge?", "fix this merge conflict", "undo a bad commit", or "how should I branch for this work".
---

# Using Git Workflows

## Scope
The mechanics and judgment of daily Git: branching, commit hygiene, PR
preparation, integration (rebase vs merge), conflict resolution, and safe
recovery. Not the code content itself — that is
[reviewing-code](../../review/reviewing-code/SKILL.md).

## Purpose
Keep history readable, bisectable, and recoverable so reviewers and future
debuggers can trust it — while never destroying a teammate's work.

## When to use this skill
- Starting a branch and unsure of the model, or naming/scoping it.
- Structuring messy work-in-progress into atomic, reviewable commits.
- Deciding rebase vs merge, resolving a conflict, or preparing a PR.
- Recovering from a bad commit, wrong branch, or lost work.

## When NOT to use this skill
- Judging the code's correctness/design → [reviewing-code](../../review/reviewing-code/SKILL.md).
- Writing the feature → [implementing-features](../implementing-features/SKILL.md).
- Cutting a versioned release/tag → [packaging-and-releasing-software](../packaging-and-releasing-software/SKILL.md).

## Inputs
- The change in progress, target branch, and team's branching convention.
- Whether the branch is shared (pushed, others based on it) or private.
- CI/PR requirements: checks, review count, merge method the repo enforces.

## Outputs
- A clean branch of atomic commits with imperative, well-scoped messages.
- A reviewable PR: focused diff, description of what/why, linked issue.
- A safe recovery path when something went wrong.

## Workflow
```
Progress:
- [ ] 1. Pick branching model + branch off current main
- [ ] 2. Commit atomically as you work; write clear messages
- [ ] 3. Sync with main (rebase private, merge shared)
- [ ] 4. Resolve conflicts deliberately; re-test after
- [ ] 5. Prepare a focused, reviewable PR
- [ ] 6. Recover safely if something broke; never force-push shared history
```

**Step 1 — Branch.** Default to trunk-based: short-lived branches off `main`,
merged within days. Name `type/short-desc` (`feat/oauth-login`). Reserve
long-lived release branches (Git Flow) only for products shipping multiple
supported versions. Always branch from an up-to-date `main`.

**Step 2 — Commit atomically.** One logical change per commit; it should build
and pass tests on its own. Separate refactors from behavior changes. Message:
imperative subject ≤50 chars ("Add retry to upload client"), blank line, body
explaining *why* not *what*, wrapped ~72. Reference the issue. Use `git add -p`
to split unrelated hunks.

**Step 3 — Sync.** Rebase your *private* branch onto `main` to keep history
linear (`git rebase main`). Merge — never rebase — a *shared* branch others have
pulled. Never rewrite already-pushed shared history.

**Step 4 — Resolve conflicts.** Understand both sides before editing; don't blind-
accept "ours"/"theirs". Remove all markers, rebuild the intended combined logic,
then re-run tests/build. `git rerere` reuses resolutions across repeated rebases.

**Step 5 — Prepare the PR.** Keep the diff focused and small; drop debug/format
noise. Squash fixup commits so the PR reads as coherent steps. Describe what
changed, why, and how it was verified. See [writing-change-notes](../../office/writing-change-notes/SKILL.md).

**Step 6 — Recover safely.** On shared history use `git revert` (adds an undo
commit). Use `git reset` only on private commits. `git reflog` finds "lost"
commits after a bad reset/rebase. `git stash` parks work when you switched
branches too early.

## Principles
- History is a communication tool: optimize for the future reader and `git bisect`.
- Rewrite freely in private; never rewrite what others have pulled.
- Prefer `revert` over `reset` the moment a commit has been shared.
- Small, atomic, self-contained commits beat one giant "done" commit.
- Nothing is truly lost for ~90 days — reflog before you panic.

## Decision framework
- **Rebase vs merge:** private/unshared → rebase for linear history; shared or
  when the merge itself is meaningful → merge.
- **Squash vs preserve commits:** noisy WIP → squash; meaningful incremental
  steps that each pass → preserve.
- **Revert vs reset:** pushed/shared → revert; local-only mistake → reset.
- **Amend vs new commit:** last commit unpushed → `--amend`; already pushed → new commit.

## Common mistakes
- **Force-pushing a shared branch** — rewrites teammates' base; if unavoidable use
  `--force-with-lease` and coordinate first.
- **Committing everything at once** — unreviewable, unbisectable, unrevertable.
- **"Fix", "wip", "stuff"** messages — useless in `git log`/`blame`.
- **Blind conflict resolution** — accepting one side and dropping the other's logic.
- **`reset --hard` without checking reflog** — recoverable, but panic causes data loss.
- **Committing secrets/large binaries** — rewriting them out of history is painful.

## Validation checklist
- [ ] Each commit builds/tests green and is one logical change.
- [ ] Messages: imperative subject, why-focused body, issue linked.
- [ ] Rebased only private history; shared branches merged.
- [ ] Conflicts resolved deliberately and re-tested; no leftover markers.
- [ ] PR diff is focused; no debug code, secrets, or unrelated churn.
- [ ] Any undo of shared work used `revert`, not history rewrite.

## Edge cases
- **Accidental commit to main:** branch it off, then reset main to `origin/main`.
- **Wrong branch:** `git stash` or `git cherry-pick` onto the right one.
- **Huge/binary files committed:** use `git-filter-repo`; coordinate the rewrite.
- **Long-running feature branch:** rebase/merge from main often to shrink conflicts.
- **Bad commit deep in history:** `git revert <sha>`, or interactive rebase only if private.

## Related skills
- [reviewing-code](../../review/reviewing-code/SKILL.md) — judging the change's content.
- [packaging-and-releasing-software](../packaging-and-releasing-software/SKILL.md) — tagging and shipping.
- [writing-change-notes](../../office/writing-change-notes/SKILL.md) — the PR/changelog prose.

## Examples
**Input:** "I have 20 messy WIP commits and a conflict with main — how do I make this reviewable?"
**Output:** Branch is private, so `git rebase -i main`: squash the WIP into ~3
atomic commits (schema, endpoint, tests), each with an imperative message.
Resolve the conflict by rebuilding the combined logic and re-running tests. Push,
open a PR describing what/why/how-verified. Never force-push once others pull it.

## Automation opportunities
- Commit-message linting (Conventional Commits) and PR-title checks in CI.
- Pre-commit hooks: format, lint, secret-scan, block large files.
- Enable `git rerere` and branch-protection rules (no force-push to main).
- Templates for PR descriptions and commit messages.
