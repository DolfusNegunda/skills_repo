---
name: writing-reports
description: Write structured analytical, status, and business reports — with an executive summary, clear findings backed by evidence, analysis, and actionable recommendations. Use when the user asks to "write a report", "create a status/analysis/research report", "put this analysis into a report", or turn findings into a structured document. Separates findings from interpretation from recommendations. Produces a decision-useful report, not a data dump.
---

# Writing Reports

## Scope
Structured reporting: analytical reports, status reports, research write-ups, and
business reports that move from findings → analysis → recommendations. Uses
[writing-executive-summaries](../writing-executive-summaries/SKILL.md) for the
front page and [authoring-word-documents](../authoring-word-documents/SKILL.md) for
the artifact. Data-driven HTML alternative: [generating-data-reports](../generating-data-reports/SKILL.md).

## Purpose
Turn information into a document that supports a decision: the answer up front, the
evidence organized, the interpretation distinct from the facts, and clear
recommendations someone can act on.

## When to use this skill
- "Write a report" — analysis, status, research, incident, or business report.
- Turning findings, data, or investigation into a structured document.
- A recurring report (weekly/monthly/quarterly) that needs consistent structure.

## When NOT to use this skill
- Persuading an external buyer → [writing-proposals](../writing-proposals/SKILL.md).
- Just a summary of a source → [summarizing-documents](../summarizing-documents/SKILL.md).
- Status reports specifically → [writing-status-reports](../writing-status-reports/SKILL.md) (RAG format).
- A live data dashboard → [designing-dashboards](../designing-dashboards/SKILL.md).

## Inputs
- The findings/data/analysis and the question the report answers.
- Audience and the decision it informs; required length/format.
- Any recurring template to follow.

## Outputs
- A report: executive summary, background/scope, findings (evidence), analysis
  (interpretation), recommendations (actions with owners), and appendices —
  structured for the reader's decision.

## Workflow
```
Progress:
- [ ] 1. Define the question the report answers and the decision it serves
- [ ] 2. Draft the executive summary (answer first)
- [ ] 3. State background, scope, and method
- [ ] 4. Present findings — facts and evidence, clearly separated from opinion
- [ ] 5. Analyze — what the findings mean, implications, causes
- [ ] 6. Recommend — specific actions with owners and priority
- [ ] 7. Add appendices; verify every claim is supported
```

**Step 1 — Question & decision.** A report answers a question for a decision. Name
both; otherwise it becomes an unfocused data dump.

**Step 2 — Executive summary first.** Lead with the answer and key recommendations
(see [writing-executive-summaries](../writing-executive-summaries/SKILL.md)).

**Step 3 — Background & method.** Give only the context and methodology the reader
needs to trust the findings.

**Step 4 — Findings = facts.** Present what the data/investigation shows, with
evidence (numbers, sources, examples). Keep this section free of interpretation.

**Step 5 — Analysis = interpretation.** Separately, explain what the findings *mean*
— implications, causes, patterns, uncertainty. Keeping facts and interpretation
distinct lets the reader judge your reasoning.

**Step 6 — Recommendations = actions.** Specific, prioritized, with owners and,
ideally, expected impact. "Consider improving X" is not a recommendation; "Assign Y
to do Z by Q3" is.

**Step 7 — Support & appendices.** Detail, data tables, and methodology go to
appendices. Verify every claim in the body traces to evidence.

## Principles
1. **Answer first.** Executive summary leads; conclusions aren't saved for the end.
2. **Separate facts, interpretation, and recommendations.** The reader must tell them apart.
3. **Evidence for every claim.** No unsupported assertions in the body.
4. **Recommendations are actionable** — specific, owned, prioritized.
5. **Structure serves the decision,** not the chronology of your work.

## Decision framework
- **Recurring status?** Use [writing-status-reports](../writing-status-reports/SKILL.md) (RAG format).
- **One-off analysis?** Full findings → analysis → recommendations structure.
- **Data-heavy, visual?** [generating-data-reports](../generating-data-reports/SKILL.md) or add a dashboard.
- **Incident/postmortem?** Timeline → impact → root cause → actions (blameless).

## Common mistakes
- **Data dump** with no clear question or takeaway.
- **Mixing facts and opinion** so the reader can't tell evidence from inference.
- **Conclusions buried** at the end instead of the summary.
- **Vague recommendations** with no owner, priority, or impact.
- **Unsupported claims** — assertions with no evidence.
- **Chronological structure** ("what we did") instead of decision structure.

## Validation checklist
- [ ] The question the report answers is explicit.
- [ ] Executive summary leads with the answer and key recommendations.
- [ ] Findings are factual and evidenced; interpretation is separated.
- [ ] Analysis explains meaning, causes, and uncertainty.
- [ ] Recommendations are specific, prioritized, and owned.
- [ ] Every body claim traces to evidence/appendix.
- [ ] Consistent structure and formatting; charts labeled.

## Edge cases
- **Bad-news reports:** state it plainly in the summary; separate cause from blame.
- **Uncertain data:** state confidence and limitations; don't overclaim.
- **Mixed audiences:** exec summary for leaders, detail in body/appendix for specialists.
- **Regulated/audit reports:** follow the mandated structure exactly; keep an evidence trail.

## Related skills
- [writing-executive-summaries](../writing-executive-summaries/SKILL.md), [writing-business-prose](../writing-business-prose/SKILL.md).
- [writing-status-reports](../writing-status-reports/SKILL.md), [generating-data-reports](../generating-data-reports/SKILL.md).
- [authoring-word-documents](../authoring-word-documents/SKILL.md), [designing-dashboards](../designing-dashboards/SKILL.md).

## Examples
**Input:** "Write a report on last quarter's customer churn analysis."
**Output:** Exec summary (churn rose to 6.2%, driven by onboarding gaps —
recommend three fixes), background/method, findings (churn by segment/cohort with
charts, facts only), analysis (onboarding drop-off is the leading cause, with
evidence), recommendations (owned, prioritized, expected impact), and an appendix
with the full data and methodology.

## Templates
- [templates/report-structure.md](templates/report-structure.md) — analytical report skeleton.

## Automation opportunities
- Standardize recurring report structures as templates.
- Generate data sections from a source with [generating-data-reports](../generating-data-reports/SKILL.md).
- Auto-assemble the report and render it via [automating-document-generation](../automating-document-generation/SKILL.md).
