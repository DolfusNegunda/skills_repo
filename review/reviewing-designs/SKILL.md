---
name: reviewing-designs
description: Review UI/UX and visual designs for usability, accessibility, visual hierarchy, consistency, and fitness to user goals — producing severity-ranked findings with specific fixes. Use when the user asks to "review this design/mockup/UI/wireframe", "usability review", "accessibility check", or critique a screen/flow before build. Inherits the shared severity/scoring model. Produces an actionable design critique grounded in heuristics, not personal taste.
---

# Reviewing Designs

## Scope
Evaluation of UI/UX and visual designs — screens, flows, mockups, wireframes — for
usability, accessibility, and fitness to user goals, anchored in recognized
heuristics rather than taste. Inherits method/severity/scoring from
[conducting-structured-reviews](../conducting-structured-reviews/SKILL.md).

## Purpose
Tell the designer whether users can accomplish their goal easily and inclusively,
and exactly what to change — grounding every finding in a principle, not "I'd prefer".

## When to use this skill
- "Review this design / mockup / UI / wireframe / prototype / screen / flow."
- "Usability review / heuristic evaluation / accessibility check."
- A design critique gate before hand-off to build.

## When NOT to use this skill
- Data-display specifically → [reviewing-dashboards](../reviewing-dashboards/SKILL.md).
- Slide design → [reviewing-presentations](../reviewing-presentations/SKILL.md).
- Creating the design → a design authoring skill.

## Inputs
- The design (screens/flow) and the user + task it serves.
- Platform (web/mobile/desktop), constraints, and any design system/brand.
- Accessibility target (e.g. WCAG AA).

## Outputs
- A review: verdict + scores, severity-ranked findings (screen/element + heuristic
  violated + fix), an accessibility list, and strengths.

## Evaluation rubric (dimensions)
1. **Usability** — Nielsen heuristics: visibility of status, match to real world,
   user control, consistency, error prevention, recognition over recall, flexibility,
   minimalist design, error recovery, help.
2. **Task fit** — the primary user goal is achievable quickly with minimal friction.
3. **Visual hierarchy** — the eye is led to what matters; clear primary action.
4. **Consistency** — patterns, components, and terminology match the system and themselves.
5. **Accessibility** — contrast, text size, touch targets, keyboard/screen-reader support, labels, no color-only meaning.
6. **Feedback & error states** — loading, empty, error, and success states designed, not just the happy path.
7. **Content** — clear, concise microcopy; labels and CTAs that make sense.

## Scoring & severity
Score 1–5; rank Blocker→Praise (see
[foundation reference](../conducting-structured-reviews/references/severity-and-scoring.md)).
Examples: **Blocker** = the primary task can't be completed, or contrast fails WCAG
so content is unreadable; **Major** = no error/empty states; **Minor** = a
low-contrast secondary label; **Nit** = inconsistent icon style.

## Workflow
```
Progress:
- [ ] 1. Confirm the user, the primary task, platform, and a11y target
- [ ] 2. Walk the primary task flow as the user — note friction
- [ ] 3. Heuristic pass across screens
- [ ] 4. Accessibility pass (contrast, targets, keyboard, labels)
- [ ] 5. Check non-happy-path states and consistency
- [ ] 6. Severity-rank, score, verdict; heuristic-anchored fixes
```

**Step 2 — walk the task.** Attempt the user's goal step by step; friction and
dead-ends surface the highest-severity findings. **Anchor every finding to a
heuristic or a11y criterion** so it's a defect, not a preference — and separate
genuine usability problems from taste.

## Recommended-improvements guidance
Cite the heuristic/criterion and give the fix: increase contrast to the ratio,
surface system status, add the missing empty/error state, make the primary action
dominant, or align the component to the design system.

## Validation checklist
- [ ] User, primary task, platform, and a11y target confirmed.
- [ ] Primary flow walked; friction points noted.
- [ ] Heuristics applied across screens with evidence.
- [ ] Accessibility checked (contrast, size, targets, keyboard, labels, color).
- [ ] Empty/loading/error/success states reviewed.
- [ ] Findings anchored to a principle + carry severity + a fix; verdict + scores given.

## Common mistakes
- **Taste-based feedback** ("I don't like the blue") with no principle.
- **Reviewing only the happy path** — ignoring empty/error states.
- **Skipping accessibility** — the most-missed, highest-liability area.
- **Praising aesthetics over task success.**
- **No user/task context** — can't judge fitness.

## Edge cases
- **Wireframes:** judge structure/flow/hierarchy, not visual polish; say so.
- **Mobile:** touch targets, thumb reach, and small-screen density matter more.
- **Design system context:** consistency findings weigh heavily; flag off-system components.
- **Localization:** check text expansion and RTL if relevant.

## Related skills
- [conducting-structured-reviews](../conducting-structured-reviews/SKILL.md), [reviewing-dashboards](../reviewing-dashboards/SKILL.md).
- [designing-forms](../../office/designing-forms/SKILL.md) — for form-specific UX.

## Examples
**Input:** "Review this checkout flow mockup (web, WCAG AA)."
**Output:** Verdict: Request changes (Accessibility 2/5, Task fit 3/5). **Blocker:**
the "Pay" button contrast is 2.1:1 — fails AA and is hard to see; fix: darken to
≥4.5:1. **Major:** no error state for a declined card. **Minor:** "Continue" and
"Next" used for the same action. **Praise:** clear progress indicator.

## Automation opportunities
- Run automated contrast/a11y checkers first; focus review on flow and heuristics.
- Reuse the heuristic + a11y checklist as a standing design-review gate.
