# Quality Benchmark: this repo vs. Anthropic's Skills approach

An honest assessment of how this repo's skills compare, in method and quality, to
Anthropic's own Agent Skills — scored per dimension, with gaps rated by severity and
prioritized fixes.

## Basis and caveats

Compared against: (a) the **Agent Skills open standard** (agentskills.io) that this
repo's `skill-builder` encodes; (b) Anthropic's **documented skill-authoring
guidance** (the philosophy captured in `skill-builder/references/`); and (c) the
**known design of Anthropic's published skills** — the `docx`/`pdf`/`pptx`/`xlsx`
document skills and `skill-creator` — from training knowledge. This is **not a live
fetch** (web access is disabled in this environment), so statements about Anthropic's
skills are to the best of documented/known design, not a line-by-line diff. Ratings
use this repo's own 1–5 scale and severity taxonomy (Blocker→Nit).

## Update — iteration 2 (script gap: pilot closed, propagation started)

Acting on this benchmark's top finding, the executable-script pattern is now proven
in-repo on three document skills, each with a **tested** script wired into a loop:

- `office/engineering-excel-workbooks` — `scripts/validate_workbook.py`: fails on stray
  Excel error values (`#REF!`/`#DIV/0!`/…) and leftover placeholders, warns on merged
  cells / empty sheets / external links; emits JSON; wired as a produce → validate →
  fix → re-validate loop (Workflow Step 8). Tested against defective + clean workbooks.
  Caveat: the error-value check reads *cached* results, so the formula-error branch
  self-closes only after Excel/LibreOffice recalculates (openpyxl doesn't compute
  formulas); the placeholder / merged-cell / empty-sheet checks work unconditionally.
- `office/processing-excel-files` — `scripts/extract_workbook.py`: deterministic
  `.xlsx`/`.csv` → per-sheet JSON (typed, ISO dates, formula results, merged/error
  flags) + a fidelity block. Tested on a dated/merged/error workbook and a semicolon+BOM CSV.
- `office/processing-word-documents` — `scripts/extract_docx.py`: `.docx` → Markdown
  (heading hierarchy, tables) + fidelity (tracked changes, comments, footnotes, images).
  Tested on real repo `.docx` samples.

Durable follow-through so the standard propagates: a **"Determinism"** section in
`authoring-checklist.md`, a script-bundling note in `skill-template.md`, and a **scoped
validator warning** (`validate_skills.py`) that flags file-producing/processing skills
shipping no `scripts/` (currently 7 advisory hits — the propagation backlog).

**Still open (tracked):** PowerPoint (`building-powerpoint-decks`,
`processing-powerpoint-files`) and PDF scripts are deferred **because there is no real
`.pptx`/`.pdf` sample in the repo and no generator library installed to test against** —
and an untested script is worse than prose. `authoring-word-documents` and the
Google-API skills are the remaining candidates. Deferred by user direction: the leanness
trim (quality/delivery must not be sacrificed for lean).

## Scorecard

| Dimension | Anthropic | This repo | Verdict |
|---|---|---|---|
| 1. Frontmatter & standard compliance | 5 | 5 | Equal — validated, portable `name`+`description` |
| 2. Description quality / discoverability | 5 | 4–5 | Near-equal; enforced by validator heuristic |
| 3. Progressive disclosure & leanness | 5 | 3 | **Anthropic ahead** — theirs is leaner |
| 4. Executable scripts / determinism | 5 | 3 | Gap narrowing — pattern proven on 3 skills; propagation tracked |
| 5. Validation & feedback loops | 4 | 4 | Equal, different form (theirs in-skill; ours repo-level) |
| 6. Breadth & composition | 3 | 5 | **This repo ahead** — 87 cross-linked skills |
| 7. Consistency tooling (validator, index, CI) | 3 | 5 | **This repo ahead** |
| 8. Templates & worked examples | 4 | 4 | Equal |
| 9. Domain technique quality | 5 | 4 | Anthropic slightly ahead where it ships tools |
| 10. Fit to the cheaper-model goal | 4 | 3–4 | Mixed — see below |

## Where this repo matches or exceeds Anthropic

- **Breadth and composition (5 vs 3).** Anthropic's public skills are a focused set
  (document formats, skill-creator, a handful of others). This repo spans 87 skills
  across office, review, business, and research, deliberately cross-linked so they
  compose (ingest → summarize → draft → review → render). For an "enterprise
  operating manual," this coverage is a genuine advantage.
- **Consistency tooling (5 vs 3).** A repo-level `validate_skills.py` (frontmatter,
  naming, link integrity, duplicate detection) + a generated `skills-index.md` +
  a CI gate is stronger *repo hygiene* than Anthropic's per-skill guidance provides.
  This is the right machinery for a growing shared library.
- **Review/knowledge-work rubrics.** The `review/` and `business/` skills encode
  scored evaluation rubrics and decision frameworks that Anthropic's tool-oriented
  document skills don't emphasize. This is original, high-value content.
- **Frontmatter/discoverability parity.** Descriptions follow the what+when+triggers
  recipe and pass an automated check — on par with Anthropic's discovery discipline.

## Where this repo falls short

**[Major] Little to no executable code — the defining gap.**
Anthropic's document skills ship **working scripts** (e.g. unpack/repack OOXML, fill
and flatten PDF forms, manipulate `.docx`/`.xlsx` deterministically). The model calls
a tested tool instead of reasoning through a fragile operation. This repo's document
skills — including the new `processing-*` ingestion skills — currently *describe* the
right library and steps in prose but **bundle almost no runnable scripts** (only
`generating-data-reports` and `producing-branded-documents` ship code). Failure
scenario: a cheap model told "use python-docx to preserve headings and tables" may
still produce a lossy extraction, whereas running a bundled, tested `extract_docx.py`
would be deterministic. **This is the most important gap to close, and it matters most
precisely because of the cheaper-model goal.**

**[Minor] Verbosity vs. the leanness principle.**
Anthropic's guidance (which this repo's own `anti-patterns.md` repeats) is "Claude is
smart — add only what it doesn't know; keep `SKILL.md` lean." This repo's skills use a
richer ~17-section structure and occasionally restate general knowledge (what a PDF is,
generic best practices). Every loaded line competes for context — and context is cost,
which cuts against the very goal. Bodies are all under the 500-line cap, but several
could shed 15–30% by pushing depth into `references/`.

**[Minor] Token cost of the heavy format is in tension with the cost goal.**
The library is designed to let cheap models work well, but a verbose `SKILL.md` loaded
per task raises the token bill. The mitigations (index-first loading, one skill at a
time) are in place, but leaner bodies would compound the savings.

**[Nit] Uneven script-intent signalling.**
Anthropic is explicit about run-vs-read for scripts. This repo mostly has no scripts to
signal; as scripts are added, each should say "run" vs "read" (the `skill-builder`
template already prescribes this).

## The cheaper-model lens (the stated goal)

The core premise — bake expert procedure into skills so smaller models perform well —
is sound and well-executed for **judgment-heavy** work (reviews, writing genres,
analysis), where explicit rubrics and checklists genuinely uplift a weak model. It is
**under-executed for mechanical document operations**, where the highest-reliability
uplift for a weak model is a *deterministic script it runs*, not prose it must
interpret. Anthropic optimized exactly that half. Closing the script gap is what would
take this library from "great guidance" to "great guidance + reliable tools."

## Prioritized recommendations

1. **[Major] Ship scripts with the document skills.** Add tested, self-contained
   extractors/generators to `processing-word-documents` (`docx→markdown+tables`),
   `processing-powerpoint-files` (`pptx→per-slide JSON`), `processing-excel-files`
   (`xlsx/csv→clean tables`), and the PDF skill (extraction/redaction/forms). Mark
   them "run this," list dependencies. This directly serves the cost/quality goal.
2. **[Minor] Trim for leanness.** Pass over the heaviest `SKILL.md` bodies; move
   deep material to `references/`, cut lines that restate what any model knows. Target
   the biggest office/review files first.
3. **[Minor] Add a token-budget note to `skill-builder`.** Codify "lean body, depth in
   references, scripts for determinism" as an explicit authoring rule, since the whole
   library's economics depend on it.
4. **[Nit] Add per-skill "smoke tests"** for skills that ship scripts, so CI runs them
   (extends the existing validator/CI foundation you already lead on).

## Verdict

**Strong library, clearly above baseline on breadth, discoverability, and repo
consistency — at or above Anthropic on those axes.** It trails Anthropic in one
material way: **executable, deterministic tooling for document operations**, plus some
avoidable verbosity. Neither is a Blocker; both are addressable. Close the script gap
on the `processing-*`/document skills and trim the heaviest bodies, and the library
would match Anthropic's method quality while exceeding its coverage — and, importantly,
better deliver the cheaper-model cost/quality goal it was built for.

Overall: **Approve, with the script gap tracked as the top follow-up.**
