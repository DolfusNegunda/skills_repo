---
name: extracting-text-with-ocr
description: Convert scanned documents, images, and photos of text into accurate, structured, machine-readable text using OCR. Use when the user asks to "OCR this", "extract text from a scan/image/photo", "read this receipt/invoice/ID", or turn a picture of a document into editable text or data. Handles preprocessing, layout preservation, tables, and confidence checking. Produces clean extracted text or structured fields with a quality assessment.
---

# Extracting Text with OCR

## Scope
Optical Character Recognition: turning pixels of text (scans, photos, image-only
PDFs) into accurate text or structured data, including preprocessing, layout/table
handling, and confidence assessment. Downstream PDF operations belong to
[processing-pdf-documents](../processing-pdf-documents/SKILL.md).

## Purpose
Produce the most accurate possible text from imperfect images, and — crucially —
tell the user how reliable it is, so errors are caught rather than propagated.

## When to use this skill
- "OCR this", "extract text from this scan/image/photo/screenshot".
- "Read this receipt / invoice / form / ID / business card into data."
- Image-only PDFs where direct text extraction returns nothing.
- Digitizing paper archives into searchable text.

## When NOT to use this skill
- PDF already has a text layer → extract directly with [processing-pdf-documents](../processing-pdf-documents/SKILL.md).
- Handwriting at scale or forms design → different tooling / [designing-forms](../designing-forms/SKILL.md).
- Understanding/summarizing the content once extracted → [summarizing-documents](../summarizing-documents/SKILL.md).

## Inputs
- The image(s) or scanned PDF, and the target: raw text, layout-preserved text, or
  specific structured fields (e.g. invoice number, total, date).
- Language(s) and script; expected quality of the source.

## Outputs
- Extracted text (plain or layout-preserving) or structured fields (JSON/CSV),
  each with a **confidence/quality note** and flags on low-confidence regions.

## Workflow
```
Progress:
- [ ] 1. Assess image quality and confirm the target output shape
- [ ] 2. Preprocess (deskew, denoise, threshold, upscale) if needed
- [ ] 3. Run OCR with the right language/layout settings
- [ ] 4. Post-process and structure the output
- [ ] 5. Assess confidence; flag/verify low-confidence items
```

**Step 1 — Assess & target.** Judge resolution, skew, contrast, and noise. Decide
whether you need flowing text, preserved layout, or specific fields.

**Step 2 — Preprocess.** OCR accuracy is mostly won here: deskew, increase contrast,
binarize/threshold, remove speckle, and upscale low-DPI images (aim ~300 DPI).

**Step 3 — OCR.** Set the correct language(s) and page-segmentation mode (single
column, sparse text, table). Use a capable engine (e.g. Tesseract, or a cloud/
document-AI service for tables and forms).

**Step 4 — Post-process.** Fix predictable errors (0/O, 1/l/I, rn/m), rejoin
hyphenated line breaks, and map results into the requested structure. For fields
like totals or dates, validate format and, where possible, cross-check (e.g. line
items sum to the total).

**Step 5 — Confidence.** Report an overall quality estimate and flag any low-
confidence characters, numbers, or fields for human review. **Never present OCR
output as certain** — numbers and names are exactly where OCR quietly fails.

## Principles
1. **Preprocessing beats post-fixing.** Clean the image before the engine reads it.
2. **Report confidence, always.** Silent OCR errors are the real risk.
3. **Validate numbers and dates,** which are high-impact and error-prone.
4. **Match segmentation to layout;** a table read as prose is scrambled.
5. **Keep the source image** alongside the text for audit.

## Decision framework
- **Clean printed text?** Standard OCR engine, minimal preprocessing.
- **Photo / low quality / skewed?** Heavy preprocessing first.
- **Tables/forms/receipts?** A document-AI / layout-aware service, not plain OCR.
- **Multiple languages?** Set all relevant language packs.
- **Handwriting?** A handwriting-capable model; expect lower accuracy and verify.

## Common mistakes
- **Skipping preprocessing** on poor images — garbage in, garbage out.
- **Presenting output as accurate** with no confidence flag — errors propagate.
- **Wrong page-segmentation mode** — columns/tables come out interleaved.
- **Ignoring the number/date failure modes** (O↔0, comma↔period in amounts).
- **Wrong/missing language setting** — accented and non-Latin text mangled.

## Validation checklist
- [ ] Source assessed; preprocessing applied where it helps.
- [ ] Correct language(s) and segmentation mode set.
- [ ] Output structured as requested (text / layout / fields).
- [ ] Numbers and dates validated (format; totals reconcile where possible).
- [ ] Overall confidence reported; low-confidence regions flagged for review.
- [ ] Source image retained for audit.

## Edge cases
- **Multi-column layouts:** segment per column or reading order will scramble.
- **Rotated/upside-down scans:** auto-orient before OCR.
- **Watermarks/stamps over text:** may need targeted cleanup.
- **Mixed print + handwriting:** route each region to the right model.
- **Regulated data (IDs, medical):** handle per privacy policy; minimize retention.

## Related skills
- [processing-pdf-documents](../processing-pdf-documents/SKILL.md) — for scanned PDFs and downstream ops.
- [summarizing-documents](../summarizing-documents/SKILL.md) — understand the extracted content.
- [comparing-documents](../comparing-documents/SKILL.md), [designing-forms](../designing-forms/SKILL.md).

## Examples
**Input:** "Read these 50 receipt photos into a table of vendor, date, total."
**Output:** Preprocessed images → layout-aware OCR → JSON per receipt with
vendor/date/total, each field validated (date parses, total is numeric), a
confidence score per receipt, and a shortlist of ~6 receipts flagged for manual
check where totals were low-confidence or didn't parse.

## Automation opportunities
- Batch-preprocess + OCR a folder of scans into structured records.
- Add a validation gate (totals reconcile, dates parse) that routes failures to review.
- Chain into [processing-pdf-documents](../processing-pdf-documents/SKILL.md) to build searchable PDFs.
