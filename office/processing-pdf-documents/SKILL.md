---
name: processing-pdf-documents
description: Manipulate and extract from PDF files — extract text/tables/data, split, merge, reorder, rotate, compress, fill forms, redact sensitive content, add/verify bookmarks, and convert to/from other formats. Use when the user asks to "extract text/data from a PDF", "split/merge/combine PDFs", "fill a PDF form", "redact a PDF", or process/convert PDF documents. Produces the requested PDF operation with a verification step. For scanned/image PDFs needing OCR, pair with extracting-text-with-ocr.
---

# Processing PDF Documents

## Scope
Programmatic PDF operations: extraction (text, tables, metadata), structural edits
(split, merge, reorder, rotate, crop, compress), form filling, redaction,
bookmarks, and format conversion. Scanned/image PDFs require
[extracting-text-with-ocr](../extracting-text-with-ocr/SKILL.md) first.

## Purpose
Perform the requested PDF operation reliably and verifiably — especially the
high-stakes ones (redaction, extraction accuracy) where a silent failure is costly.

## When to use this skill
- "Extract the text / tables / data from this PDF."
- "Split / merge / combine / reorder / rotate / compress these PDFs."
- "Fill this PDF form" or "flatten a filled form".
- "Redact" names/numbers, or convert PDF ↔ Word/images/text.

## When NOT to use this skill
- Scanned/image-only PDF → OCR first with [extracting-text-with-ocr](../extracting-text-with-ocr/SKILL.md).
- Authoring a new document → the relevant Word/Docs skill, export to PDF at the end.
- Diffing two PDFs' content → [comparing-documents](../comparing-documents/SKILL.md).

## Inputs
- The PDF(s) and the exact operation and parameters (page ranges, field values,
  redaction targets, output format).
- Whether the PDF is text-based or scanned (determines OCR need).
- Sensitivity/compliance constraints (for redaction).

## Outputs
- The processed PDF or extracted artifact (text, CSV/JSON of tables, images),
  plus a verification note (page counts match, redactions are irreversible, tables
  parsed correctly).

## Workflow
```
Progress:
- [ ] 1. Identify PDF type (text vs scanned) and the exact operation
- [ ] 2. For scanned input, OCR first
- [ ] 3. Perform the operation with a proven library, not by hand
- [ ] 4. Verify the result (counts, content, irreversibility)
- [ ] 5. Report what changed and any caveats
```

**Step 1 — Classify & specify.** Determine if the PDF has a real text layer or is
scanned images. Pin the exact operation and parameters before touching it. The
bundled extractor makes the text-vs-scanned call deterministically:

```bash
python scripts/extract_pdf.py path/to/file.pdf   # per-page text + has_text_layer + route
```

**Step 2 — OCR if needed.** If there's no text layer, run OCR first; extraction on
a scanned PDF returns nothing without it.

**Step 3 — Operate with tooling.** Use a robust library (e.g. `pypdf`/`pikepdf` for
structure, `pdfplumber`/`camelot` for tables, `pdf2image`+OCR for scans,
`qpdf`/`ghostscript` for compression). Ride on proven tools; never reconstruct PDF
internals by hand. **Redaction must remove the underlying content**, not draw a
black box over it.

**Step 4 — Verify.** Confirm page counts, that extracted tables preserved rows/
columns, that filled fields hold the right values, and — critically — that redacted
text cannot be selected, copied, or recovered from the file.

**Step 5 — Report.** State what was done, the output location, and any caveats
(imperfect table parsing, pages that needed OCR, fonts not embedded).

## Principles
1. **Redaction removes data,** it does not hide it. A black rectangle is not redaction.
2. **Verify extraction;** never trust that text/tables came out intact — check.
3. **Know text vs. scanned** before extracting; the wrong assumption returns silence.
4. **Preserve the original;** operate on copies.
5. **Use proven libraries;** don't hand-edit PDF byte structure.

## Decision framework
- **Text extraction:** text-based PDF → direct extraction; scanned → OCR.
- **Tables:** ruled tables → `camelot` (lattice); whitespace tables → `pdfplumber`/`camelot` (stream).
- **Merge/split/rotate:** `pypdf`/`pikepdf`.
- **Redaction:** a true-redaction tool that deletes content + flattens; then re-verify.
- **Compression:** `ghostscript`/`qpdf`; check quality after downsampling images.
- **PDF→Word:** conversion tool, then fix styles with [authoring-word-documents](../authoring-word-documents/SKILL.md).

## Common mistakes
- **Fake redaction** (black box / highlight) leaving copyable text underneath — a data breach.
- **Extracting from a scanned PDF** and getting empty output (no OCR).
- **Trusting table extraction** without checking merged/wrapped cells.
- **Losing bookmarks/metadata/forms** on merge — verify they survived.
- **Over-compressing** until images are unreadable.

## Validation checklist
- [ ] Correct PDF type identified (OCR applied if scanned).
- [ ] Operation parameters (page ranges, fields, targets) match the request.
- [ ] Output page count / structure is as expected.
- [ ] Extracted text/tables spot-checked against the source.
- [ ] Redacted content is unrecoverable (cannot select/copy; not in file text).
- [ ] Metadata/bookmarks/forms preserved where required.
- [ ] Original file untouched; output clearly named.

## Edge cases
- **Encrypted/password PDFs:** need the password; respect access restrictions.
- **Tagged/accessible PDFs:** preserve tags through edits where accessibility matters.
- **Mixed text + scanned pages:** OCR only the image pages.
- **Very large PDFs:** stream/process page-by-page to avoid memory blowups.
- **Forms:** decide whether to keep fields editable or flatten to lock values.

## Related skills
- [extracting-text-with-ocr](../extracting-text-with-ocr/SKILL.md) — for scans.
- [comparing-documents](../comparing-documents/SKILL.md) — diff two PDFs.
- [automating-document-generation](../automating-document-generation/SKILL.md) — produce PDFs at scale.
- [designing-forms](../designing-forms/SKILL.md) — for creating fillable forms.

## Reference files
- [references/pdf-operations.md](references/pdf-operations.md) — tool-by-operation guide and redaction/extraction verification.

## Scripts
- [scripts/extract_pdf.py](scripts/extract_pdf.py) — **run this** to extract PDF text
  and classify text-layer vs. scanned. Emits per-page text + char counts, encryption
  status, and a fidelity block that routes scanned/image PDFs to OCR (the classic
  empty-extraction failure). Requires `pypdf`. Structural ops (split/merge/redact) and
  table extraction still use the libraries in the operations reference.

## Examples
**Input:** "Extract the invoice tables from these 30 PDFs into one CSV."
**Output:** Per-file table extraction (lattice mode), normalized to a common schema,
concatenated to CSV, with a report of any file whose parse needed manual review and
confirmation that totals reconcile against each invoice footer.

## Automation opportunities
- Batch a folder of PDFs through one pipeline (extract → normalize → CSV/JSON).
- Chain OCR → extract → validate for scanned document intake.
- Auto-fill form templates from a data source (mail-merge for PDFs).
