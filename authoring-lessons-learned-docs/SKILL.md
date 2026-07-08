---
name: authoring-lessons-learned-docs
description: Generate a standardized Lessons Learned project document (.docx) for any organization by asking the required clarifying questions and filling a validated, brand-agnostic template. Use when the user asks to write, create, draft, or generate a lessons learned document, project retrospective, or post-project review, for any company or team deployment.
---

# Authoring Lessons Learned Docs

Produces a Lessons Learned `.docx` for a completed (or completing) project, following a standardized section skeleton that stays identical across organizations. Works with **any** company's branding by design — this skill ships a generic, neutrally-branded default template and reads company-specific branding from a swappable [branding profile](../document-branding-standards/SKILL.md), never from hardcoded content.

## When to use this skill
- "Write a lessons learned document for [project]"
- "Create a post-project retrospective for [client]"
- Any request for a project close-out / lessons learned deliverable, for any organization or team this skill has been deployed for

## Core principles
1. **Ask before drafting.** Never invent project details, team members, or lessons.
2. **One standard skeleton, two deliverables-table formats, any branding.**
3. **Generate the real file, don't describe it.**
4. **Never hardcode a company's branding into this skill.**
5. **Preserve the standard vocabulary.** Use *Challenges*, not *Negatives*.

## Standard document skeleton
1. Cover — `{ORG_NAME}` header/logo, `{PROJECT_CODE} Lessons Learned` title, cover date
2. Project identity table — Project Name, Project Code, Project Manager, Date
3. **Project Team**
4. **Deliverables**
5. **Commentary on Project Execution**
   - **Positives**
   - **Challenges**
6. **Learnings and Suggestions**

## Process
- Confirm which branding profile applies (generic default, or an onboarded org profile)
- Ask for project identity + team
- Ask for the organization/project logo image if not already set in the profile
- Ask which deliverables format fits (A or B)
- Ask for deliverables, positives, challenges, learnings
- Assemble the data dict and run `scripts/generate_lessons_learned.py`
- Validate the output
- Deliver the `.docx`

## Reference files
- `references/data-schema.md`
- `scripts/generate_lessons_learned.py`
- `assets/lessons-learned-base-template-generic.docx`
- `assets/deliverables-table-format-A.xml`
- `assets/deliverables-table-format-B.xml`
- `assets/placeholder-logo.png`
- `examples/bsc-profile/`
