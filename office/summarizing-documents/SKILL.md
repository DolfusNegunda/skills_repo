---
name: summarizing-documents
description: Reads long documents (contracts, reports, policies, PDFs including scanned ones) and produces executive summaries, key points, and risk/obligation reviews at a requested length, plus grounded answers to targeted questions. Use when the user asks to summarize, condense, review, or extract key points, risks, obligations, or answers from a document or PDF.
---

# Summarizing Documents

## Overview
This skill turns long documents — contracts, reports, policies, and PDFs — into
concise, decision-ready output: an executive summary, key points, and a review of
risks and obligations, sized to whatever length the user asks for. It also answers
targeted questions about the document, with every answer traceable back to the
source text.

## When to use this skill
- "Summarize this contract / report / policy / PDF"
- "Give me the key points" or "What do I need to know from this?"
- "What are the risks or obligations in this agreement?"
- "TL;DR this in one paragraph" / "Give me a one-pager"
- "Does this document say anything about X?" (targeted question over a document)
- "Compare/synthesize these documents" (multiple documents provided)

## Core principles
1. **Read natively**: Claude reads provided documents and PDFs directly —
   including scanned or image-based PDFs, which it reads visually. No extraction
   tooling is needed or permitted.
2. **Ground every claim**: every statement in the summary must be traceable to a
   specific place in the source (section, clause number, page, or heading). If it
   cannot be pointed to, it does not go in.
3. **Never invent**: do not fabricate clauses, figures, dates, parties, or terms.
   If the document is silent on something the user asked about, say so plainly.
4. **Flag uncertainty**: mark anything ambiguous, partially legible, or open to
   interpretation as uncertain, and quote the problematic passage rather than
   guessing.
5. **Match the requested length**: honor one-line, one-paragraph, or one-page
   requests exactly; when no length is given, default to one page or less and
   offer to expand.
6. **Surface what matters to the reader**: lead with decisions, money, deadlines,
   liabilities, and termination rights — not with the document's own ordering.

## Workflow

Copy this checklist and track progress through it:

```
Summary progress:
- [ ] Step 1: Confirm scope — document(s), summary type, target length, audience
- [ ] Step 2: Read the full document (all pages, including schedules/annexes)
- [ ] Step 3: Map the structure — parties, purpose, key sections, defined terms
- [ ] Step 4: Draft the summary at the requested length
- [ ] Step 5: Extract risks/obligations with source references
- [ ] Step 6: Verify grounding — recheck each claim against the source
- [ ] Step 7: Deliver, noting gaps, ambiguities, and unread/illegible portions
```

**Step 1 — Confirm scope.** Identify what was provided and what is wanted: which
document(s), which summary type (see [references/summary-types.md](references/summary-types.md)),
the target length, and who will read it. If the user gave no length, plan for one
page or less.

**Step 2 — Read everything.** Read the whole document before writing anything,
including schedules, annexes, exhibits, and footnotes — key obligations often
hide there. For long PDFs, read in page ranges until complete. Note any pages
that are illegible or missing.

**Step 3 — Map the structure.** Identify parties, effective dates, purpose,
governing sections, and defined terms whose meaning changes the reading (e.g.
"Services", "Confidential Information"). This map anchors the references used in
later steps.

**Step 4 — Draft the summary.** Write to the requested length and type. Lead
with the most consequential facts. Attach a source anchor to each key point
(e.g. "§4.2", "p. 12", "Schedule B").

**Step 5 — Extract risks and obligations.** For contracts and policies, list who
must do what, by when, and what happens on failure — payment terms, liability
caps, indemnities, termination triggers, auto-renewals, notice periods. Cite the
clause for each item.

**Step 6 — Verify grounding.** Recheck the draft claim by claim against the
source. Remove or soften anything not directly supported. Downgrade inferences
to explicitly labeled inferences ("the document implies…, based on §7").

**Step 7 — Deliver and disclose limits.** Present the output, then state what
the document does *not* cover from the user's question, anything uncertain or
partially legible, and any assumptions made.

For targeted Q&A: answer only from the document, quote or cite the supporting
passage, and if the document does not answer the question, say exactly that
rather than filling the gap from general knowledge.

## Examples
See [examples/example-contract-summary.md](examples/example-contract-summary.md)
for a full worked example: a contract excerpt as input, followed by an executive
summary, a risks/obligations table with clause citations, and grounded Q&A.

Mini illustration of length control on the same source:

**One-line:** "Two-year managed-services agreement at $18k/month with a 90-day
termination notice and an auto-renewal clause (§9)."

**One-paragraph:** the same facts plus liability cap, SLA credits, and the two
obligations most likely to be missed — each with a clause reference.

## Anti-patterns
- **Summarizing from the table of contents or first pages only** — key
  obligations often sit in schedules and annexes. Instead: read the entire
  document before drafting.
- **Stating a clause exists without citing where** — unverifiable output is
  untrustworthy output. Instead: anchor every key point to a section, clause,
  or page.
- **Filling gaps with plausible boilerplate** ("the contract likely includes a
  standard indemnity") — this invents terms. Instead: report that the document
  is silent, and say so explicitly.
- **Presenting an interpretation as a fact** — ambiguous drafting cut both ways.
  Instead: quote the ambiguous text and flag it as uncertain.
- **Ignoring the requested length** — a one-page answer to a "one line, please"
  request fails the user. Instead: hit the requested size, then offer more depth.
- **Reaching for extraction tools or MCP servers to read PDFs** — unnecessary.
  Instead: read the file directly; scanned pages are read visually.

## Related skills
- **summarizing-meeting-notes** — for condensing meeting transcripts and notes
  into decisions and action items rather than reviewing formal documents.
- **generating-data-reports** — for producing analytical reports from data
  sources; use it when the input is data, not prose documents.

## Reference files
- [references/summary-types.md](references/summary-types.md) — the summary
  types (executive summary, risk/obligation review, targeted extraction,
  multi-document synthesis) and length controls, with output templates.
