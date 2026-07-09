---
name: building-google-slides
description: Build clean, consistent Google Slides decks for collaboration — using master layouts (themes), the theme builder, reusable layouts, readable typography, and purposeful visuals. Use when the user asks to "make Google Slides", "create a presentation in Slides", or turn content into a collaborative deck. Produces a professional, on-theme deck. For PowerPoint .pptx, use building-powerpoint-decks; settle the story first with crafting-presentation-narratives.
---

# Building Google Slides

## Scope
Turning approved content into a professional, collaborative Google Slides deck:
theme/master layouts, consistent typography and color, purposeful visuals, and
sharing for co-editing. Google-native counterpart to
[building-powerpoint-decks](../building-powerpoint-decks/SKILL.md).

## Purpose
Produce a consistent, readable deck built on a theme so it stays coherent across
collaborators and can be restyled centrally.

## When to use this skill
- "Make Google Slides / a presentation in Slides."
- Collaborative decks with multiple editors.
- Turning a doc/outline into a Google-native deck.
- Cleaning up an inconsistent Slides deck.

## When NOT to use this skill
- `.pptx` deliverable → [building-powerpoint-decks](../building-powerpoint-decks/SKILL.md).
- Story/argument not settled → [crafting-presentation-narratives](../crafting-presentation-narratives/SKILL.md).
- Data tables/models → [engineering-google-sheets](../engineering-google-sheets/SKILL.md).

## Inputs
- The narrative/outline (one message per slide), audience, and time limit.
- Brand theme or a clean default; data for charts (ideally linked from Sheets).
- Collaboration/sharing model.

## Outputs
- A Google Slides deck on a consistent theme with reusable layouts, one idea per
  slide, legible type, directly-labeled charts, and correct sharing.

## Workflow
```
Progress:
- [ ] 1. Lock the narrative (one message per slide)
- [ ] 2. Set the theme and edit master layouts (not individual slides)
- [ ] 3. Draft slides as takeaway headlines
- [ ] 4. Add visuals; link charts from Sheets where live data helps
- [ ] 5. Enforce consistent type, color, alignment
- [ ] 6. Add title/agenda/sections + speaker notes
- [ ] 7. Set sharing; review for legibility and count
```

**Step 1 — Narrative first.** Don't design slides before the story is set.

**Step 2 — Theme & masters.** Edit the theme's master and layouts so every slide
inherits fonts, colors, and placeholders. Change the theme once to restyle all.

**Step 3 — Takeaway titles.** The slide title states the point, not the topic.

**Step 4 — Linked visuals.** Insert charts *linked from Google Sheets* so they
update when the data changes; keep each chart to one point.

**Step 5 — Consistency.** One type system, one accent color, aligned to guides.

**Step 6 — Wayfinding & notes.** Title, agenda, section slides; detail in speaker
notes, not on the slide.

**Step 7 — Share & review.** Set edit/comment/view appropriately; read each slide
from a distance; cut slides that don't advance the argument.

## Principles
1. **One idea per slide;** the title is the message.
2. **Theme masters drive consistency,** never per-slide formatting.
3. **Link live data** from Sheets so figures stay current.
4. **Slides support the speaker;** detail goes to notes/appendix.
5. **Set permissions deliberately** before sharing.

## Decision framework
- **Live data?** Link the chart from Sheets.
- **Reusable format?** Save as a theme/template.
- **Presented vs. read?** Minimal text if presented; consider a doc if read.
- **Many editors?** Comment access for reviewers, edit for authors.

## Common mistakes
- **Per-slide formatting** instead of editing the theme's layouts.
- **Pasted static charts** that go stale — link from Sheets instead.
- **Wall-of-text slides** and topic (not takeaway) titles.
- **Everyone gets edit access** — layouts get accidentally broken.
- **Low-res images / color-only meaning** — accessibility and legibility fail.

## Validation checklist
- [ ] All slides use theme layouts; no orphan formatting.
- [ ] Every slide has one message stated in the title.
- [ ] Type, color, alignment consistent; readable from the back.
- [ ] Charts linked from Sheets (if data is live) and make one point each.
- [ ] Agenda/sections present; count fits the time (~1/min).
- [ ] Alt text on images; sufficient contrast; notes carry detail.
- [ ] Sharing permissions correct.

## Edge cases
- **PowerPoint round-trips:** exporting to `.pptx` can shift fonts/layout — re-check.
- **Cross-org sharing:** verify domain sharing policy.
- **Heavy media:** large videos/images can slow collaborative editing.
- **Offline needs:** export to `.pptx`/PDF for offline presenting.

## Related skills
- [building-powerpoint-decks](../building-powerpoint-decks/SKILL.md) — PowerPoint equivalent.
- [crafting-presentation-narratives](../crafting-presentation-narratives/SKILL.md) — story first.
- [engineering-google-sheets](../engineering-google-sheets/SKILL.md) — chart data source.

## Examples
**Input:** "Collaborative QBR deck in Slides, charts should update from our Sheet."
**Output:** Deck on a company theme; takeaway-titled slides; KPI charts linked from
the metrics Sheet so they refresh; agenda + section dividers; reviewers get comment
access, two owners get edit; detail in speaker notes.

## Automation opportunities
- Linked Sheets charts refresh figures automatically.
- Save a company theme so new decks start on-brand.
- Generate an initial deck from a structured outline, then collaborate live.
