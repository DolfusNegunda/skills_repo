"""Extract text from a PDF and classify text-layer vs. scanned.

The highest-value deterministic PDF step: pull the per-page text layer AND decide
whether the PDF actually has one. A scanned/image PDF returns almost no text — the
classic silent failure — so this reports `has_text_layer` and routes to OCR when the
layer is empty, instead of handing downstream an empty extraction.

Prints JSON: per-page text + char counts, encryption/metadata, and a fidelity block
with the text-layer verdict and route. Exits 0 on success, 3 if encrypted and locked.

Usage:
    python scripts/extract_pdf.py path/to/file.pdf [--chars-per-page N]
"""
import json
import sys
from pathlib import Path

from pypdf import PdfReader

MIN_CHARS_PER_PAGE = 15  # below this average -> likely scanned/image


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit("usage: python scripts/extract_pdf.py <file.pdf> [--chars-per-page N]")
    path = Path(args[0])
    if not path.exists():
        sys.exit(f"file not found: {path}")
    threshold = MIN_CHARS_PER_PAGE
    if "--chars-per-page" in args:
        threshold = int(args[args.index("--chars-per-page") + 1])

    reader = PdfReader(str(path))
    encrypted = reader.is_encrypted
    if encrypted:
        # Try an empty-password unlock (many PDFs are "encrypted" with no password).
        try:
            if reader.decrypt("") == 0:
                report = {
                    "file": str(path), "format": "pdf", "encrypted": True,
                    "fidelity": {"warnings": ["Password-protected; cannot read "
                                              "without the password."],
                                 "route": "obtain password, then re-run"},
                }
                print(json.dumps(report, indent=2))
                sys.exit(3)
        except Exception:
            pass

    pages, total_chars = [], 0
    for i, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        total_chars += len(text.strip())
        pages.append({"page": i, "n_chars": len(text.strip()), "text": text.strip()})

    n_pages = len(pages)
    avg = (total_chars / n_pages) if n_pages else 0
    has_text_layer = avg >= threshold

    warnings = []
    route = "text extracted; proceed"
    if not has_text_layer:
        warnings.append(
            f"Little/no text layer (avg {avg:.0f} chars/page < {threshold}): this PDF "
            "is likely scanned/image-only. Route to OCR before trusting extraction.")
        route = "extracting-text-with-ocr (scanned/image PDF)"

    meta = reader.metadata or {}
    result = {
        "file": str(path),
        "format": "pdf",
        "encrypted": encrypted,
        "n_pages": n_pages,
        "title": str(meta.get("/Title")) if meta.get("/Title") else None,
        "pages": pages,
        "fidelity": {
            "has_text_layer": has_text_layer,
            "avg_chars_per_page": round(avg, 1),
            "route": route,
            "warnings": warnings,
        },
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    sys.exit(0)


if __name__ == "__main__":
    main()
