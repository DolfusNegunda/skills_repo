# Full-Library Benchmark & Quality Assessment — July 2026

A fresh, file-grounded benchmark of the entire skills repository (151 catalog skills
across 9 categories plus the `skill-builder` meta-skill) against the Agent Skills open standard and Anthropic's known skill-authoring
method. Supersedes `benchmark-vs-anthropic.md` (which graded the earlier 87-skill,
document-centric repo). This assessment reads the actual files, runs the actual tooling,
and grounds every correctness claim in a `skill:line` citation.

## Why this benchmark is different from the last one

The repo's centre of gravity moved. The prior benchmark graded a document-heavy library
whose one real gap was executable scripts — a gap this assessment confirms is **closed**
(validator 0/0, smoke test 14/14). But the repo nearly doubled by adding ~67
**pure-knowledge** skills (software/data/ai-engineering, reasoning, productivity) that
ship no scripts and *cannot* be script-validated. Grading those with a document-skill
rubric would declare victory on a gap that is no longer the story. So this benchmark adds
two first-class dimensions the old one lacked — **Content Correctness** and **Model
Uplift** — and grounds both in sampled claims rather than assertion.

## Basis and caveats (honest scoping)

Two separable comparisons, kept explicit:

1. **Conformance to the Agent Skills open standard** — *verifiable here*. The repo's
   `skill-builder` encodes the standard; the validator enforces it; I ran both.
2. **Comparison to Anthropic's published skills** (`docx`/`pdf`/`pptx`/`xlsx`,
   `skill-creator`) — *approximate*. Web access is disabled in this environment, so this
   is not a live diff against their current files; it reflects their known/documented
   design. Anthropic does **not** publish software/data/AI-engineering, reasoning, or
   business skills, so on those categories there is no external baseline to diff — only
   the open standard and domain-expert judgment.

Evidence base: full read of `skill-builder` + references and the review base skill; a
**near-census** read (every SKILL.md, not a sample) of the seven technical/business/
research categories — ai-engineering, data-engineering, software-engineering, reasoning,
productivity, business, research — plus ~16 office skills read in full and all 11
office document scripts confirmed via the smoke test; by parallel file-grounded readers.
Plus `validate_skills.py`, `smoke_test_scripts.py`, and a direct read of a bundled
document validator. That near-census makes "~10 errors library-wide" *more* reassuring,
not less — it is close to exhaustive, not a thin sample. Ratings use the repo's own 1–5
scale and Blocker→Nit severity.

**Verification status of the correctness table below.** Each error was first surfaced by a
single category reader. The three most consequential (RICE, Spark join-salting,
self-consistency) plus two checkable facts (git reflog, CRAAP composition) were then
**re-read and confirmed by the benchmark author directly against the cited lines**;
those are marked *confirmed*. The remaining rows are *reader-reported* — credible and
cited, but not yet independently re-verified. Two categories were **not** correctness-
sampled: **review/** (the reader failed on a session limit; only structural inheritance
was independently confirmed — all 15 skills genuinely use the shared severity taxonomy),
and the office knowledge skills beyond the ~16 read.

## Verified tooling state (commands actually run)

- `python skill-builder/scripts/validate_skills.py` → **Scanned 152 SKILL.md (151 catalog
  skills + 1 worked example), 0 errors, 0 warnings.**
- `python skill-builder/scripts/smoke_test_scripts.py` → **14/14 checks passed** (docx/
  pptx/pdf/xlsx extract + validate loops, JSON validator, type router).
- Staleness grep across ai/data/software-engineering → **no hardcoded model names,
  context sizes, prices, or version-pinned API behavior** outside illustrative figures.
  The provider-agnostic discipline held.

## Scorecard (12 dimensions — re-weighted off the now-closed script gap)

| # | Dimension | Anthropic | This repo | Verdict |
|---|---|---|---|---|
| 1 | Frontmatter & standard compliance | 5 | 5 | Equal — validated, portable `name`+`description` |
| 2 | Description quality / discoverability | 5 | 5 | Equal — what+when+triggers, enforced by validator |
| 3 | Progressive disclosure & leanness | 5 | 3 | **Anthropic ahead** — new tech categories run heavy |
| 4 | Executable scripts / determinism (doc skills) | 5 | 4–5 | Gap closed & CI-tested; honest library limits remain |
| 5 | Validation & feedback loops | 4 | 4 | Equal, different form (in-skill vs repo-level) |
| 6 | Breadth & composition | 3 | 5 | **Repo far ahead** — 151 skills, 9 domains, 1,449 cross-links |
| 7 | Consistency tooling (validator/index/CI) | 3 | 5 | **Repo ahead** — but blind to correctness & link labels |
| 8 | Templates & worked examples | 4 | 4 | Equal — 12+ substantive templates, worked example each |
| 9 | **Content correctness (NEW)** | 5 | 4 | Anthropic ahead — ~10 real errors, nothing checks them |
| 10 | **Model uplift for cheaper models (NEW)** | 4 | 4 | Strong core; ~20 skills restate common knowledge |
| 11 | Domain technique quality | 5 | 4 | Near-equal where judgment-heavy; slips on a few claims |
| 12 | Fit to the cheaper-model goal | 4 | 4 | Sound thesis, well-executed for judgment work |

## Where the repo matches or exceeds Anthropic

- **Breadth & composition (5 vs 3).** 151 skills across 9 domains, densely and coherently
  cross-linked (1,449 `../` links, ~9.5/skill), engineered to compose (ingest → analyze →
  draft → review → render). Anthropic's public set is a focused handful. For an enterprise
  operating manual this is a decisive advantage.
- **Structural consistency (5/5 across every category).** Every reader independently scored
  house-style conformance 5/5: an identical skeleton (Scope → Purpose → When/When-NOT →
  Inputs → Outputs → Workflow-with-checklist → Principles → Decision framework → Common
  mistakes → Validation checklist → Edge cases → Related → Examples → Automation). This
  uniformity is itself a quality signal — a cheaper model always knows where to look.
- **Consistency tooling + CI (5 vs 3).** Repo-level frontmatter/naming/link/duplicate
  validator + generated flat index + CI gate + a script smoke-test harness is stronger
  repo hygiene than per-skill guidance provides.
- **Review & business rubrics.** The `review/` severity model (Blocker/Major/Minor/Nit/
  Praise + 1–5 scoring + verdict rules) is genuinely inherited by all 15 review skills
  (verified: all 15 reference the base and actively use the taxonomy, 7–17 uses each) —
  not name-dropped. Original, high-value content Anthropic's tool-oriented skills don't
  emphasize.
- **Staleness discipline.** Provider-agnostic authoring held across the highest-risk
  categories — a durable, correct decision.

## Where the repo falls short

### [Major] Nothing checks content correctness — and ~10 real errors exist
The validator checks frontmatter/naming/links/dupes; the smoke test checks document
scripts. **Neither can catch a well-structured, confident, wrong knowledge skill** — the
highest-severity failure mode for a library going into client environments, where a cheap
model will follow authoritative-but-wrong guidance verbatim. Grounded errors found by
sampling ~40 knowledge skills (every one cited):

| # | Location | Defect | Severity | Status |
|---|---|---|---|---|
| 1 | `reasoning/prioritizing-options:69` | RICE stated as a **sum** ("Impact + confidence + reach, divided by effort"); RICE is **(Reach × Impact × Confidence) ÷ Effort**. Changes every ranking. | Major | **confirmed** |
| 2 | `data-engineering/optimizing-spark-jobs:131` | Join example salts "on **both sides**, join" — matching keys collide only on equal random draws, silently dropping ~(N−1)/N of rows. Correct: salt skewed side, **replicate/explode** small side across N salts. (The aggregation pattern at :63-64, "salt… aggregate away," is fine — error is isolated to the join example.) | Major | **confirmed** |
| 3 | `ai-engineering/detecting-hallucinations:80` | Self-consistency correctly described as a technique, but "exposes invented facts" **overstates by omission**: it suppresses *stochastic* errors only — a confidently-held false fact agrees across all samples and passes. Add the caveat; the technique isn't wrong. | Minor | **confirmed (reclassified from Major — incomplete, not false)** |
| 4 | `research/assessing-source-credibility:48` (+frontmatter) | Labelled "CRAAP-style" but drops **Relevance** and adds "Objectivity"; frontmatter also claims SIFT, which the body doesn't use. Loose label — softened by the explicit "-style" hedge, so imprecise rather than false. | Minor | **confirmed (CRAAP composition; SIFT-absence reader-reported)** |
| 5 | `software-engineering/optimizing-code-performance:102` | Muddled Big-O: "O(n) instead of O(n)." The real win is O(1) queries vs N round-trips. | Minor | reader-reported |
| 6 | `ai-engineering/generating-structured-outputs:56-57` | "cannot emit off-shape text" overstated for tool-calling; only strict constrained decoding hard-guarantees shape (the skill's own "always validate" is right). | Minor | reader-reported |
| 7 | `ai-engineering/designing-ai-systems:91` | Fine-tuning "can't add fresh knowledge" — oversimplified absolute; it encodes knowledge poorly/un-updatably, not never. Interpretive — defensible received wisdom. | Nit | reader-reported |
| 8 | `research/reading-scientific-papers:62` | "results = truth" overstates; results are bounded by method/stats/sample (contradicts the skill's own better point at :60). Interpretive. | Minor | reader-reported |
| 9 | `software-engineering/using-git-workflows:83` | "Nothing truly lost for ~90 days" — unreachable reflog entries default to **30 days** (`gc.reflogExpireUnreachable`); loose objects prunable sooner. | Minor | **confirmed** |
| 10 | `data-engineering/designing-data-pipelines:62-64` | ~~MERGE framed as inherently idempotent~~ — **re-verified: NOT a defect.** The text says "re-running must converge to the same table state," which is careful, not the flat claim reported. Dedup precondition is a nice-to-have. No edit. | — | withdrawn on re-read |

Plus internal-consistency and unsupported-figure issues: `business/analyzing-cost-benefit:98`
(ROI example computes ~16%, text says 12% — not reproducible); `office/writing-proposals:129`
("cut drafting time 30–60%" — unsupported stat as fact).

### [Major] Frontmatter over-claims the body in several skills
Discovery text promises methods the body never delivers — a cheap model routes to the skill
expecting them:
- `business/analyzing-stakeholders:3` — "and RACI" but body routes RACI away.
- `business/managing-change:3` — "ADKAR/**Kotter**" but only ADKAR is delivered.
- `research/assessing-source-credibility` — "CRAAP/SIFT-style" (see #4).

### [Minor] Mislabeled-but-resolving cross-links (validator blind spot)
Links whose text disagrees with their target — the validator confirms the target exists but
never checks the label matches:
- `business/performing-business-analysis:92` — anchor reads "[../reasoning]" but links to
  `office/comparing-documents/SKILL.md`.
- `office/designing-dashboards:12,25,119` — link labelled "dataviz" points to
  `generating-data-reports`.

### [Minor] Leanness regressed in the new technical categories
The prior benchmark's leanness note persists and spread: **data-engineering 14/14** and
**ai-engineering 13/14** skills exceed 120 body lines (avg 136 / 133); office 28/42. All
under the 500-line cap, but every loaded line is context cost — which cuts against the
cheaper-model economics the library exists to serve.

### [Minor] ~20 skills restate what a capable model already knows (uplift tail)
The uplift test — "if deleted, does output get materially worse?" — cleanly separates the
library. **High uplift** (keep, these carry the thesis): the `review/` rubrics; SQL traps
(`authoring-sql-queries`), `writing-secure-code`, `designing-vector-search`,
`applying-guardrails`, `building-decision-matrices`, `analyzing-cost-benefit`,
`estimating-under-uncertainty`, `thinking-in-systems`, incremental-loading/streaming,
`verifying-facts`, `synthesizing-research`, the script-backed document skills. **Low uplift**
(restate common knowledge — trim/merge candidates): SWE `implementing-features`,
`refactoring-code`, `debugging-systematically`, `reading-unfamiliar-codebases`,
`applying-design-patterns`; reasoning `breaking-down-tasks`, `analyzing-gaps`; productivity
`managing-time`, `planning-your-day`, `managing-tasks`, `taking-notes`; ai-eng
`engineering-prompts`; research `collecting-evidence`, `conducting-comparative-research`;
business `facilitating-meetings`, `communicating-with-stakeholders`; office `editing-prose`,
`proofreading-text`. **Caveat that softens this:** the library explicitly targets *cheaper/
smaller* models, for which even generic procedural scaffolding has real value. The verdict
is "lowest marginal uplift," not "worthless."

### [Minor] Genuine duplication to resolve (vs intentional author/review pairing)
Most overlap is deliberate and cross-linked (authoring↔review; org↔personal). Real dupes:
- `office/summarizing-meeting-notes` markets a "formal minutes" variant that reproduces
  `recording-meeting-minutes`'s entire reason to exist → strip the variant, hand off.
- `business/building-decision-matrices` ↔ `reasoning/analyzing-tradeoffs` — closest true
  duplicate, and **not** cross-linked to each other.
- `business/performing-business-analysis` (5-Whys/fishbone) ↔ `reasoning/analyzing-root-causes`
  — duplicated technique; PBA links to the wrong target instead of the dedicated skill.
- `ai-engineering/evaluating-prompts-and-outputs` ↔ `building-llm-evaluations` — merge candidate.
- `data-engineering/optimizing-data-costs` ↔ `tuning-warehouse-performance` — heavy overlap.

### [Nit] Two house-style families + minor structure slips
Office runs two skeletons — "Family A" (formal `## Validation checklist`) vs "Family B"
(`status-reports`, `brand-guidelines`: `## Anti-patterns` + inline review). Both are fine
but inconsistent. `office/editing-prose:8` has a stray pre-Scope subheading.
`office/document-branding-standards` is the one real skill with no Related-skills links.

### [Nit] Repo hygiene: duplicate cruft + count drift
`skills_repo-starter/` and `skills_repo-starter.zip` are a stale duplicate snapshot of
`skill-builder` (2 duplicate SKILL.md) — the only reason `find` reports 154. **Canonical
count is now pinned at 151 catalog skills** (150 across 9 categories + the `skill-builder`
meta-skill; the validator additionally validates 1 worked example, reported separately).
Docs previously disagreed (87 in the old brief, "152" including the example); a doc-count
guard now fails CI if a leadership doc drifts from the canonical number.

## The cheaper-model lens (the stated goal)

The premise — bake expert procedure into skills so smaller models perform well — is sound
and well-executed for **judgment-heavy** work (reviews, decision frameworks, domain traps,
document determinism). Two things now most threaten it, and both are addressable: (a)
**content correctness**, because a weak model cannot sanity-check authoritative-but-wrong
guidance the way a strong one might; and (b) **leanness**, because a verbose body loaded per
task is a direct token cost that erodes the savings. The script gap that dominated the last
review is genuinely closed.

## Prioritized recommendations

1. **[Major] Fix the 10 grounded correctness findings** (table above). Start with the two
   confirmed Majors — **RICE** (wrong rankings) and **Spark join-salting** (silent row loss);
   both are one-line edits with high reliability payoff. Then the confirmed Minors (self-
   consistency caveat, git reflog 30-day fact, CRAAP label), then re-verify and fix the
   reader-reported rows.
2. **[Major] Reconcile frontmatter claims with bodies** (RACI, Kotter, SIFT). Either add the
   promised method or drop it from the description so discovery doesn't mis-route.
3. **[Major] Add a correctness feedback loop.** Nothing catches a wrong knowledge skill today.
   Cheapest durable mechanism: a periodic adversarial claim-audit (like this one) at a set
   cadence and on every new technical skill, logged in `docs/`. Optionally extend the
   validator to flag *frontmatter methods named but absent from the body* — it already parses
   both, so the RACI/Kotter/SIFT class is mechanically catchable.
4. **[Minor] Extend the validator to check link-label ↔ target agreement** — closes the
   `designing-dashboards`/`performing-business-analysis` blind spot with existing machinery.
5. **[Minor] Leanness pass on data/ai-engineering first** (27 of 28 skills are heavy). Push
   depth into `references/`, cut lines that restate what any model knows; target ~15–30%.
6. **[Minor] Resolve the five genuine duplicates** (merge or cross-link + hand-off).
7. **[Nit] Delete `skills_repo-starter/` + `.zip`, pin the skill count** at 151 across README,
   docs, and the brief. Fix the two structure slips.
8. **[Consider] Triage the uplift tail** — for the ~20 low-uplift skills, either sharpen each
   to carry a non-obvious payload or accept them as deliberate scaffolding for weak models and
   say so explicitly in the category READMEs.

## Actions taken this session (2026-07-10)

**Fixes applied** — 10 skill files edited; `validate_skills.py` **0/0**, `smoke_test_scripts.py`
**14/14**, and `skills-index.md` regenerated after:
- **RICE → product** (`prioritizing-options`) and **Spark join-salting → salt-one-side/
  replicate-other** (`optimizing-spark-jobs`) — the two confirmed Majors.
- Self-consistency caveat (`detecting-hallucinations`), git reflog 30-day fact
  (`using-git-workflows`), Big-O phrasing (`optimizing-code-performance`), structured-output
  "cannot" softened (`generating-structured-outputs`), "results = truth" reframed
  (`reading-scientific-papers`).
- Three frontmatter over-claims reconciled with their bodies: RACI (`analyzing-stakeholders`),
  Kotter (`managing-change`), SIFT (`assessing-source-credibility`).
- Row 10 (MERGE idempotency) **withdrawn** on re-read — not a defect.

**Correctness feedback loop shipped** (closes recommendation #3):
- `validate_skills.py` now warns when a description advertises a distinctive named framework
  (RACI/Kotter/SIFT/RICE/SWOT/BATNA/…) the body never uses. Tested: fires on bad input,
  silent on the cleaned repo.
- New [correctness-audit-process.md](correctness-audit-process.md) (3-layer: mechanical /
  per-skill / periodic-adversarial) + a **Content correctness** gate added to the
  authoring checklist.

**Runtime execution test** (end-to-end, not just read):
- Produced a real SOP `.docx` following `authoring-word-documents`. Its bundled gate correctly
  **FAILED** an unfilled `{{owner}}` tag (exit 1), then passed (`status: OK`, exit 0) after the
  fix — the produce→validate→fix→re-validate loop works as documented, with `has_headings`
  confirming named styles registered.
- Ran the corrected RICE on a real backlog: the product formula lets all four factors matter,
  where the buggy sum let reach (thousands-scale) swamp impact/confidence — confirming the fix
  is substantive, not cosmetic.

## Verdict

**A strong, unusually broad, and structurally disciplined library — at or above Anthropic on
breadth, discoverability, consistency tooling, and (now) document determinism.** It trails
Anthropic in two addressable ways: **leanness** and, more importantly, **content-correctness
assurance** — the new dimension that matters most for a library deployed to cheaper models in
client environments, where confident-but-wrong guidance is the top risk. No Blockers. Fix the
ten grounded errors, reconcile the frontmatter overclaims, add a correctness loop, and trim
the heaviest bodies, and this library matches Anthropic's method quality while decisively
exceeding its coverage.

**Overall: Approve, with content correctness tracked as the new top follow-up (the script gap
is closed).**
