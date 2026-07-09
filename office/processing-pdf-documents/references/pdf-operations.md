# PDF Operations Guide

Tool selection per operation, plus the verification each one demands. Use these
via the sandbox/execution environment; do not hand-edit PDF structure.

## Contents
- Tool map
- Text and table extraction
- Structural edits
- Form filling
- Redaction (high stakes)
- Compression and conversion

## Tool map
| Operation | Preferred tool(s) |
|---|---|
| Merge / split / rotate / reorder | `pypdf`, `pikepdf` |
| Text extraction (text PDFs) | `pdfplumber`, `pypdf` |
| Table extraction | `camelot` (lattice/stream), `pdfplumber` |
| Scanned pages → text | `pdf2image` + OCR (see OCR skill) |
| Form fill / flatten | `pypdf`, `pdfrw`, `pikepdf` |
| Redaction | a true-redaction library that removes content, then flatten |
| Compression | `ghostscript`, `qpdf` |
| Metadata / encryption | `pikepdf` |

## Text and table extraction
- Try direct text extraction first; if it returns little/nothing, the PDF is scanned → OCR.
- Tables: `camelot` **lattice** for ruled tables, **stream** for whitespace-aligned.
- Always spot-check: row/column counts, merged cells, wrapped text, numeric totals.
- Normalize multi-file output to one schema before concatenating.

## Structural edits
- Merge/split by page ranges; verify final page count and that bookmarks/metadata
  and any form fields survived.
- Rotation is per-page; confirm orientation on the affected pages only.

## Form filling
- Map field names → values; fill, then decide: keep editable or **flatten** to lock.
- Verify each field shows the intended value and required fields are populated.

## Redaction (high stakes)
1. Identify every occurrence of the sensitive content (search all pages; watch for
   the same data in headers, footers, metadata, and comments).
2. Use a tool that **deletes** the underlying text/image region, not one that draws
   a shape over it.
3. Flatten the document so no layer retains the original.
4. **Verify irreversibility:** re-open, try to select/copy under the redaction,
   search the raw file text for the sensitive string, and check metadata. If the
   string is still findable, redaction failed.

## Compression and conversion
- Compress via image downsampling; inspect quality after — over-compression ruins scans.
- PDF→Word/other conversions are approximate; expect to fix styles afterward with
  [../../authoring-word-documents/SKILL.md](../../authoring-word-documents/SKILL.md).
- Preserve/embed fonts so the output renders the same everywhere.
