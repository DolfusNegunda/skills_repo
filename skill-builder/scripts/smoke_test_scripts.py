"""Smoke-test every bundled skill script against generated fixtures.

Proves the document scripts actually run and behave as documented (right exit codes,
right verdicts) — reproducibly, in CI or by hand. Generates real .xlsx/.docx/.pptx/
.pdf/.csv fixtures, runs each validator/extractor, and asserts the outcome.

Run from the repo root:
    python skill-builder/scripts/smoke_test_scripts.py

Requires: openpyxl, python-docx, python-pptx, pypdf, reportlab.
Exits non-zero if any script is missing, errors unexpectedly, or gives a wrong verdict.
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
results = []


def run(script_rel, arg):
    """Run a bundled script; return (exit_code, parsed_json_or_None)."""
    script = ROOT / script_rel
    if not script.exists():
        return None, None
    proc = subprocess.run([sys.executable, str(script), str(arg)],
                          capture_output=True, text=True)
    data = None
    try:
        data = json.loads(proc.stdout)
    except (ValueError, json.JSONDecodeError):
        pass
    return proc.returncode, data


def check(name, cond):
    results.append((name, bool(cond)))
    print(f"  {'PASS' if cond else 'FAIL'}  {name}")


def make_fixtures(tmp):
    from openpyxl import Workbook
    from docx import Document
    from pptx import Presentation
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter

    # xlsx: bad (error value + placeholder) and good
    wb = Workbook(); ws = wb.active; ws["A1"] = "TBD"; ws["A2"] = "#DIV/0!"
    wb.save(tmp / "bad.xlsx")
    wb2 = Workbook(); wb2.active["A1"] = "clean"; wb2.save(tmp / "good.xlsx")
    (tmp / "data.csv").write_text("a,b\n1,2\n", encoding="utf-8")

    # docx: bad (tag) and good (heading)
    b = Document(); b.add_paragraph("Hi {{ name }}"); b.save(tmp / "bad.docx")
    g = Document(); g.add_heading("Title", 1); g.add_paragraph("ok"); g.save(tmp / "good.docx")

    # pptx: bad (lorem) and good
    pb = Presentation(); s = pb.slides.add_slide(pb.slide_layouts[0])
    s.shapes.title.text = "Lorem ipsum"; pb.save(tmp / "bad.pptx")
    pg = Presentation(); sg = pg.slides.add_slide(pg.slide_layouts[0])
    sg.shapes.title.text = "Real Title"; pg.save(tmp / "good.pptx")

    # pdf: text layer and 'scanned' (rectangle only)
    c = canvas.Canvas(str(tmp / "text.pdf"), pagesize=letter)
    c.drawString(72, 720, "Real text content here."); c.showPage(); c.save()
    c2 = canvas.Canvas(str(tmp / "scan.pdf"), pagesize=letter)
    c2.rect(72, 600, 200, 100, fill=1); c2.showPage(); c2.save()


def main():
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        make_fixtures(tmp)

        print("engineering-excel-workbooks/validate_workbook.py")
        rc, d = run("office/engineering-excel-workbooks/scripts/validate_workbook.py", tmp / "bad.xlsx")
        check("excel validator fails on bad workbook", rc == 1 and d and d["status"] == "FAILED")
        rc, d = run("office/engineering-excel-workbooks/scripts/validate_workbook.py", tmp / "good.xlsx")
        check("excel validator passes clean workbook", rc == 0 and d and d["status"] == "OK")

        print("processing-excel-files/extract_workbook.py")
        rc, d = run("office/processing-excel-files/scripts/extract_workbook.py", tmp / "data.csv")
        check("excel extractor reads csv", rc == 0 and d and d["format"] == "csv")

        print("processing-word-documents/extract_docx.py")
        rc, d = run("office/processing-word-documents/scripts/extract_docx.py", tmp / "good.docx")
        check("docx extractor returns markdown", rc == 0 and d and "Title" in d["markdown"])

        print("authoring-word-documents/validate_docx.py")
        rc, d = run("office/authoring-word-documents/scripts/validate_docx.py", tmp / "bad.docx")
        check("docx validator fails on unfilled tag", rc == 1 and d and d["status"] == "FAILED")
        rc, d = run("office/authoring-word-documents/scripts/validate_docx.py", tmp / "good.docx")
        check("docx validator passes clean doc", rc == 0 and d and d["status"] == "OK")

        print("processing-powerpoint-files/extract_pptx.py")
        rc, d = run("office/processing-powerpoint-files/scripts/extract_pptx.py", tmp / "good.pptx")
        check("pptx extractor returns slides", rc == 0 and d and d["slides"][0]["title"] == "Real Title")

        print("building-powerpoint-decks/validate_pptx.py")
        rc, d = run("office/building-powerpoint-decks/scripts/validate_pptx.py", tmp / "bad.pptx")
        check("pptx validator fails on lorem", rc == 1 and d and d["status"] == "FAILED")
        rc, d = run("office/building-powerpoint-decks/scripts/validate_pptx.py", tmp / "good.pptx")
        check("pptx validator passes clean deck", rc == 0 and d and d["status"] == "OK")

        print("processing-pdf-documents/extract_pdf.py")
        rc, d = run("office/processing-pdf-documents/scripts/extract_pdf.py", tmp / "text.pdf")
        check("pdf extractor finds text layer", rc == 0 and d and d["fidelity"]["has_text_layer"])
        rc, d = run("office/processing-pdf-documents/scripts/extract_pdf.py", tmp / "scan.pdf")
        check("pdf extractor flags scanned -> OCR", rc == 0 and d and not d["fidelity"]["has_text_layer"])

        print("processing-documents/detect_type.py")
        rc, d = run("office/processing-documents/scripts/detect_type.py", tmp / "good.docx")
        check("type detector identifies docx", rc == 0 and d and d["detected_type"] == "docx")

    passed = sum(1 for _, ok in results if ok)
    total = len(results)
    print(f"\n{passed}/{total} checks passed")
    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()
