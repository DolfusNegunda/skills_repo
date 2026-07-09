# Authoring Checklist

Run through this before publishing a skill to the repo.

## Discovery (does it trigger?)
- [ ] `description` states both **what** the skill does and **when** to use it
- [ ] `description` is third person (not "I can..." / "You can...")
- [ ] `description` includes the concrete terms a user would actually say
- [ ] `name` is lowercase-hyphens, ≤64 chars, gerund/noun-phrase, no `claude`/`anthropic`

## Frontmatter (does it parse?)
- [ ] Opens and closes with `---`
- [ ] Only `name` + `description` unless a specific optional field is needed
- [ ] Extra fields nested under `metadata` (not top-level author/version/tags)
- [ ] 2-space indentation, no tabs, no trailing whitespace, ends with one newline
- [ ] Confirmed against [frontmatter.md](frontmatter.md) rules

## Content (is it lean and clear?)
- [ ] `SKILL.md` body under ~500 lines
- [ ] No content Claude already knows (no explaining what a PDF/JSON/SQL is)
- [ ] Consistent terminology throughout (pick one term per concept)
- [ ] Concrete examples, not abstract descriptions
- [ ] No time-sensitive info (or isolated in an "old patterns" section)
- [ ] Freedom level matches task fragility (exact commands where it's fragile)

## Structure (is it navigable?)
- [ ] Long material split into `references/`, linked from `SKILL.md`
- [ ] All reference links are **one level deep** (no chains of references)
- [ ] Reference files >100 lines start with a "Contents" list
- [ ] Forward slashes in every path (`references/x.md`, not `references\x.md`)
- [ ] Scripts marked as **execute** vs. **read**; required packages listed

## Testing (does it work?)
- [ ] Tested on a realistic request with a fresh Claude — it triggered
- [ ] It found and used the right reference files
- [ ] Output was correct; fragile steps had a validation/feedback loop
- [ ] If it didn't trigger, the description was tightened first
