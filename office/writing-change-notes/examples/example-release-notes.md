# Worked Example: Commit List → Software Release Notes

## Input

The user provides the previous version (`2.1.3`) and this raw commit list from
`git log --oneline v2.1.3..HEAD`:

```
9f3d21a Merge pull request #241 from feature/saved-filters
e8c4b70 feat: saved filters on the transactions list (#241)
b2a9d55 fix typo in README
4d1e0c9 feat!: remove legacy /v1/export endpoint (#236)
a77f3e2 fix: PDF statements rendered blank for accounts with no activity (#238)
c90b114 refactor: extract StatementRenderer into its own module
5e2d8aa fix: session token not refreshed after password change (#233)
1b6f472 deps: bump openssl wrapper to patch CVE-2026-1187 (#244)
88ac310 feat: add `--quiet` flag to the CLI sync command (#229)
0d4e9c1 Revert "feat: experimental dark mode" 
73aa20f feat: experimental dark mode
```

## Reasoning applied

- Filtered out: the merge commit (duplicate of #241), the README typo fix
  (no user-visible product effect), the pure refactor (behavior unchanged),
  and the dark-mode commit plus its revert (net zero within the window).
- `feat!` marks a breaking removal → goes to Removed and forces a major bump.
- The CVE dependency bump has a security effect → Security, not omitted.
- The session-token fix protects account integrity but fixes intended
  behavior → Fixed (the CVE entry alone carries Security).
- Version: breaking removal present → major bump, `3.0.0`.

## Output

```markdown
## [3.0.0] - 2026-07-08

**Breaking:** The legacy `/v1/export` endpoint has been removed. Migrate to
`/v2/export`, which accepts the same query parameters and returns paginated
JSON (#236).

### Added
- Saved filters on the transactions list — save, name, and reapply filter
  combinations (#241)
- `--quiet` flag on the CLI `sync` command to suppress per-record progress
  output (#229)

### Removed
- Legacy `/v1/export` endpoint; use `/v2/export` instead (#236)

### Fixed
- PDF statements no longer render blank for accounts with no activity in the
  period (#238)
- Session tokens are now refreshed immediately after a password change (#233)

### Security
- Updated the OpenSSL wrapper to address CVE-2026-1187 (#244)
```

**Version recommendation:** `3.0.0` — the removal of `/v1/export` is
backward-incompatible, so a major bump is required regardless of the
accompanying features and fixes.
