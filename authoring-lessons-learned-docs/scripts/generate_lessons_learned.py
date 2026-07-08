
"""
generate_lessons_learned.py

Generates a branded BSC Lessons Learned .docx from a base template and a
structured data dict. Preserves all BSC header/footer/logo/theme/font
styling from the base template; only replaces cover title/date, the
metadata table, project team rows, the deliverables table (format A or B,
swapped in from a stored skeleton so both formats always render correctly
regardless of which format the base template ships with), and the
Positives/Challenges/Learnings tables.

Usage (as a script):
    python generate_lessons_learned.py --data project_data.json \
        --template lessons_learned_base_template.docx \
        --logo client_logo.png \
        --output "RI.XXXX_Lessons_Learned.docx"

Or import generate() directly from Python.

Required companion assets (ship alongside this script):
    deliverables-table-format-A.xml   Item / Deliverables (bullets; time+quality noted inline in text)
    deliverables-table-format-B.xml   Document / Status / Notes
"""
import argparse
import copy
import io
import json
import zipfile
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.oxml import parse_xml
from PIL import Image


# ---------------------------------------------------------------------------
# Low-level XML helpers (cover page uses Word content controls / sdt elements
# that are NOT reachable via doc.paragraphs, so we walk the XML directly)
# ---------------------------------------------------------------------------

def get_sdts_by_alias(doc: Document, alias_value: str) -> list:
    """Return every content-control (w:sdt) element tagged with the given alias."""
    result = []
    for sdt in doc.element.body.iter(qn("w:sdt")):
        alias = sdt.find(qn("w:sdtPr") + "/" + qn("w:alias"))
        if alias is not None and alias.get(qn("w:val")) == alias_value:
            result.append(sdt)
    return result


def set_sdt_text(sdt_element, new_text: str) -> bool:
    """Set all w:t descendants of a content control to represent new_text:
    the first w:t gets the full text, the rest are cleared (keeps formatting)."""
    t_nodes = sdt_element.findall(".//" + qn("w:t"))
    if not t_nodes:
        return False
    t_nodes[0].text = new_text
    for t in t_nodes[1:]:
        t.text = ""
    return True


# ---------------------------------------------------------------------------
# Table / cell helpers
# ---------------------------------------------------------------------------

def clone_row(table, row_idx: int):
    """Deep-clone table.rows[row_idx] and insert it immediately after, to
    preserve cell borders/shading/fonts. Returns the new row object."""
    src_tr = table.rows[row_idx]._tr
    new_tr = copy.deepcopy(src_tr)
    src_tr.addnext(new_tr)
    return table.rows[row_idx + 1]


def set_cell_text(cell, text: str) -> None:
    """Replace a cell's visible text entirely with `text`, preserving the
    first paragraph/run's formatting. Cells in these templates sometimes hold
    multiple paragraphs (multi-line comments) — all but the first are removed
    so no leftover template text survives."""
    paragraphs = cell.paragraphs
    first_p = paragraphs[0]
    if first_p.runs:
        first_p.runs[0].text = text
        for r in first_p.runs[1:]:
            r.text = ""
    else:
        first_p.add_run(text)
    for p in paragraphs[1:]:
        p._p.getparent().remove(p._p)


def remove_extra_rows(table, keep_through_idx: int) -> None:
    """Delete every row after index `keep_through_idx` (0-based, inclusive)."""
    while len(table.rows) > keep_through_idx + 1:
        table.rows[keep_through_idx + 1]._tr.getparent().remove(
            table.rows[keep_through_idx + 1]._tr
        )


def replace_table_with_skeleton(doc: Document, table_index: int, skeleton_xml_path: str):
    """Swap the entire table at `table_index` for the stored skeleton (header
    row(s) + one template data row), preserving position in the document.
    Returns the new docx.table.Table object at the same index."""
    old_tbl = doc.tables[table_index]._tbl
    with open(skeleton_xml_path, "rb") as f:
        new_tbl = parse_xml(f.read())
    old_tbl.addprevious(new_tbl)
    old_tbl.getparent().remove(old_tbl)
    return doc.tables[table_index]


# ---------------------------------------------------------------------------
# Logo swap (project/client logo lives at word/media/image1.*)
# ---------------------------------------------------------------------------

def swap_logo(docx_path: str, new_logo_path: str) -> None:
    """Replace the project logo image (word/media/image1.*) in-place."""
    with zipfile.ZipFile(docx_path, "r") as zin:
        names = zin.namelist()
        image1_name = next(n for n in names if n.startswith("word/media/image1."))
    ext_needed = image1_name.rsplit(".", 1)[-1].lower()

    im = Image.open(new_logo_path)
    buf = io.BytesIO()
    fmt = "JPEG" if ext_needed in ("jpg", "jpeg") else "PNG"
    if fmt == "JPEG" and im.mode in ("RGBA", "P"):
        im = im.convert("RGB")
    im.save(buf, format=fmt)
    new_bytes = buf.getvalue()

    tmp_path = docx_path + ".tmp"
    with zipfile.ZipFile(docx_path, "r") as zin, zipfile.ZipFile(tmp_path, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == image1_name:
                data = new_bytes
            zout.writestr(item, data)
    Path(tmp_path).replace(docx_path)


# ---------------------------------------------------------------------------
# Main generation function
# ---------------------------------------------------------------------------

def generate(
    data: dict,
    template_path: str,
    output_path: str,
    logo_path: str | None = None,
    assets_dir: str = ".",
) -> str:
    """Generate a branded Lessons Learned .docx.

    `data` keys (see references/data-schema.md for the full field list):
      project_code, project_name, project_manager, cover_date, metadata_date,
      team (list of {name, position, allocation?}),
      deliverables_format ("A" or "B"), deliverables (list matching the format),
      positives (list of {title, comment}),
      challenges (list of {title, comment}),
      learnings (list of {title, actions}).

    `assets_dir` must contain deliverables_table_format_A.xml and
    deliverables-table-format-B.xml (the stored table skeletons).
    """
    import shutil
    shutil.copy(template_path, output_path)
    doc = Document(output_path)

    # --- Cover page ---
    for s in get_sdts_by_alias(doc, "Title"):
        set_sdt_text(s, f"{data['project_code']} Lessons Learned")
    for s in get_sdts_by_alias(doc, "Publish Date"):
        set_sdt_text(s, data.get("cover_date", data.get("metadata_date", "")))

    # --- Metadata table (table 0): Project Name / Project Code / Project Manager / Date ---
    t0 = doc.tables[0]
    set_cell_text(t0.rows[0].cells[1], data["project_name"])
    set_cell_text(t0.rows[1].cells[1], data["project_code"])
    set_cell_text(t0.rows[2].cells[1], data["project_manager"])
    set_cell_text(t0.rows[3].cells[1], data["metadata_date"])

    # --- Project Team table (table 1): header row 0, data rows 1..n ---
    t1 = doc.tables[1]
    has_allocation = len(t1.rows[0].cells) >= 3 and any(
        m.get("allocation") for m in data["team"]
    )
    for i, member in enumerate(data["team"]):
        row = t1.rows[1] if i == 0 else clone_row(t1, i)
        set_cell_text(row.cells[0], member["name"])
        set_cell_text(row.cells[1], member["position"])
        if has_allocation and len(row.cells) >= 3:
            set_cell_text(row.cells[2], member.get("allocation", ""))
    remove_extra_rows(t1, len(data["team"]))

    # --- Deliverables table (table 2): always swap in the correct skeleton for
    #     the requested format first, so Format A works even if the base
    #     template shipped with Format B's table structure (or vice versa) ---
    fmt = data.get("deliverables_format", "A")
    skeleton_filename = "deliverables-table-format-A.xml" if fmt == "A" else "deliverables-table-format-B.xml"
    skeleton_path = str(Path(assets_dir) / skeleton_filename)
    t2 = replace_table_with_skeleton(doc, 2, skeleton_path)
    header_rows = 2 if fmt == "A" else 1
    deliverables = data["deliverables"]
    for i, item in enumerate(deliverables):
        row = t2.rows[header_rows] if i == 0 else clone_row(t2, header_rows + i - 1)
        if fmt == "A":
            # Real-world Format A data rows have 2 physical cells: Item, and a
            # Deliverables description where time/quality status is noted
            # inline (e.g. "SOW Document: ... \u2022 Delivered on time, met quality bar.")
            set_cell_text(row.cells[0], item["item"])
            description = item["description"]
            status_note = item.get("status_note")
            if status_note:
                description = f"{description}\n\u2022 {status_note}"
            set_cell_text(row.cells[1], description)
        else:
            set_cell_text(row.cells[0], item["document"])
            set_cell_text(row.cells[1], item.get("status", ""))
            set_cell_text(row.cells[2], item.get("notes", ""))
    remove_extra_rows(t2, header_rows + len(deliverables) - 1)

    # --- Positives table (table 3): Title / Comment ---
    t3 = doc.tables[3]
    for i, item in enumerate(data["positives"]):
        row = t3.rows[1] if i == 0 else clone_row(t3, i)
        set_cell_text(row.cells[0], item["title"])
        set_cell_text(row.cells[1], item["comment"])
    remove_extra_rows(t3, len(data["positives"]))

    # --- Challenges table (table 4): Title / Comment ---
    t4 = doc.tables[4]
    for i, item in enumerate(data["challenges"]):
        row = t4.rows[1] if i == 0 else clone_row(t4, i)
        set_cell_text(row.cells[0], item["title"])
        set_cell_text(row.cells[1], item["comment"])
    remove_extra_rows(t4, len(data["challenges"]))

    # --- Learnings and Suggestions table (table 5): Title / Learnings-Suggestions-Actions ---
    t5 = doc.tables[5]
    for i, item in enumerate(data["learnings"]):
        row = t5.rows[1] if i == 0 else clone_row(t5, i)
        set_cell_text(row.cells[0], item["title"])
        set_cell_text(row.cells[1], item["actions"])
    remove_extra_rows(t5, len(data["learnings"]))

    doc.save(output_path)

    if logo_path:
        swap_logo(output_path, logo_path)

    return output_path


def main():
    parser = argparse.ArgumentParser(description="Generate a BSC Lessons Learned document.")
    parser.add_argument("--data", required=True, help="Path to a JSON file matching the data schema.")
    parser.add_argument("--template", required=True, help="Path to lessons_learned_base_template.docx")
    parser.add_argument("--logo", default=None, help="Path to the client/project logo image (optional).")
    parser.add_argument("--output", required=True, help="Output .docx path.")
    parser.add_argument("--assets-dir", default=".", help="Directory containing the deliverables table skeleton XML files.")
    args = parser.parse_args()

    with open(args.data, "r", encoding="utf-8") as f:
        data = json.load(f)

    out = generate(data, args.template, args.output, args.logo, args.assets_dir)
    print(f"Generated: {out}")


if __name__ == "__main__":
    main()
