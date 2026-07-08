# python-docx / OOXML Editing Patterns for Branded BSC Documents

## Contents
- Why raw python-docx isn't enough
- Content-control (sdt) text replacement (cover pages)
- Safe text replacement across runs
- Clearing multi-paragraph table cells
- Cloning table rows
- Swapping an entire table structure
- Validation checklist after any edit

## Why raw python-docx isn't enough
BSC's Word templates use **cover page building blocks** (Word's built-in
"Cover Pages" gallery), which store the title and date inside **content
controls** (`w:sdt` elements) nested inside floating text boxes. These are
NOT part of `document.paragraphs` or `document.tables` — python-docx's
normal APIs cannot see or edit them. You must walk the raw document XML.

## Content-control (sdt) text replacement (cover pages)
```python
from docx import Document
from docx.oxml.ns import qn

def get_sdts_by_alias(doc: Document, alias_value: str) -> list:
    """Return every content-control (w:sdt) element tagged with the given alias."""
    result = []
    for sdt in doc.element.body.iter(qn("w:sdt")):
        alias = sdt.find(qn("w:sdtPr") + "/" + qn("w:alias"))
        if alias is not None and alias.get(qn("w:val")) == alias_value:
            result.append(sdt)
    return result

def set_sdt_text(sdt_element, new_text: str) -> bool:
    """Set all w:t descendants of a content control to new_text: the first
    w:t gets the full text, the rest are cleared (keeps formatting)."""
    t_nodes = sdt_element.findall(".//" + qn("w:t"))
    if not t_nodes:
        return False
    t_nodes[0].text = new_text
    for t in t_nodes[1:]:
        t.text = ""
    return True

# Usage: BSC cover pages use aliases "Title" and "Publish Date"
doc = Document("base-template.docx")
for s in get_sdts_by_alias(doc, "Title"):
    set_sdt_text(s, "RI.2001 Lessons Learned")
for s in get_sdts_by_alias(doc, "Publish Date"):
    set_sdt_text(s, "2026/07/08")
```
Discover the exact alias names for a new template by listing all
`w:alias` values under `w:sdt` elements before writing replacement code —
don't assume "Title"/"Publish Date" apply to every template.

## Safe text replacement across runs
Word frequently splits a single visible line across multiple `w:r` runs
(e.g. spell-check artifacts, tracked edits). A naive
`paragraph.text = paragraph.text.replace(...)` **destroys formatting**
because it collapses all runs into one. Use a run-aware replacer instead:
```python
def replace_in_paragraph(paragraph, old: str, new: str) -> bool:
    """Replace `old` with `new` across a paragraph's runs, merging as needed.
    Preserves the formatting of the first run in the matched span."""
    runs = paragraph.runs
    full_text = "".join(r.text for r in runs)
    start = full_text.find(old)
    if start == -1:
        return False
    end = start + len(old)
    positions, pos = [], 0
    for r in runs:
        positions.append((pos, pos + len(r.text)))
        pos += len(r.text)
    touched_idx = [i for i, (s, e) in enumerate(positions) if e > start and s < end]
    if not touched_idx:
        return False
    first_i, last_i = touched_idx[0], touched_idx[-1]
    first_run, last_run = runs[first_i], runs[last_i]
    prefix = first_run.text[: start - positions[first_i][0]]
    suffix = last_run.text[end - positions[last_i][0]:]
    if first_i == last_i:
        first_run.text = prefix + new + suffix
    else:
        first_run.text = prefix + new
        last_run.text = suffix
        for i in range(first_i + 1, last_i):
            runs[i].text = ""
    return True
```
Use this for one-off heading renames (e.g. standardizing "Negatives /
Challenges" to "Challenges"). For wholesale cell content replacement in a
table, use `set_cell_text` below instead — it's simpler and handles the
common multi-paragraph-cell case that `replace_in_paragraph` alone misses.

## Clearing multi-paragraph table cells
**Pitfall discovered during testing:** BSC document table cells (e.g. a
"Comment" cell holding a 3-bullet lesson) often contain **multiple
paragraphs**, not one paragraph with line breaks. Only replacing
`cell.paragraphs[0]`'s text leaves the old template's 2nd/3rd paragraphs
behind, corrupting the output with leftover source-document text. Always
clear every paragraph beyond the first:
```python
def set_cell_text(cell, text: str) -> None:
    """Replace a cell's visible text entirely with `text`, preserving the
    first paragraph/run's formatting. Removes any additional paragraphs."""
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
```

## Cloning table rows
To add N data rows to a table that ships with only one template row, clone
the template row's XML (preserves borders/shading/fonts) rather than
building a new row from scratch:
```python
import copy

def clone_row(table, row_idx: int):
    """Deep-clone table.rows[row_idx] and insert it immediately after."""
    src_tr = table.rows[row_idx]._tr
    new_tr = copy.deepcopy(src_tr)
    src_tr.addnext(new_tr)
    return table.rows[row_idx + 1]

def remove_extra_rows(table, keep_through_idx: int) -> None:
    """Delete every row after index `keep_through_idx` (0-based, inclusive)."""
    while len(table.rows) > keep_through_idx + 1:
        table.rows[keep_through_idx + 1]._tr.getparent().remove(
            table.rows[keep_through_idx + 1]._tr
        )
```
Fill the first template row directly, then `clone_row` for each additional
item, then `remove_extra_rows` to trim any leftover template rows if the
data list is shorter than expected.

## Swapping an entire table structure
Some document types have two valid table *shapes* for the same section
(discovered with BSC's deliverables table: an "Item/Deliverables" format
vs. a "Document/Status/Notes" format). Don't try to reshape one format's
XML into the other cell-by-cell — merged cells (`gridSpan`) differ between
them and this breaks silently. Instead, store both shapes as standalone
`<w:tbl>` XML skeleton files (header row(s) + one template data row each,
extracted once via `copy.deepcopy` from real source documents) and swap
the whole table element at generation time:
```python
from docx.oxml import parse_xml   # NOT lxml.etree.fromstring — see pitfall below

def replace_table_with_skeleton(doc, table_index: int, skeleton_xml_path: str):
    """Swap the table at `table_index` for a stored skeleton, in place."""
    old_tbl = doc.tables[table_index]._tbl
    with open(skeleton_xml_path, "rb") as f:
        new_tbl = parse_xml(f.read())
    old_tbl.addprevious(new_tbl)
    old_tbl.getparent().remove(old_tbl)
    return doc.tables[table_index]
```
**Pitfall:** loading the skeleton with plain `lxml.etree.fromstring` looks
like it works but produces a generic `lxml.etree._Element`, not
python-docx's registered `CT_Tbl` subclass — later code that calls
`table.rows` will crash with `AttributeError: ... has no attribute
'tr_lst'`. Always load OOXML fragments meant to go back into a python-docx
document with `docx.oxml.parse_xml`, never raw lxml.

## Validation checklist after any edit
Never assume a generation script "worked" just because it ran without
raising an exception.
- [ ] Re-open the saved file with `Document(output_path)`
- [ ] Print every table's rows and confirm no leftover source-document text
      remains in any cell (the multi-paragraph pitfall above is the most
      common cause)
- [ ] Confirm the row count in each table matches the input data length
      (no extra template rows left over, no missing rows)
- [ ] Extract `word/document.xml` from the saved `.docx` (it's a zip) and
      search for the new title/date text to confirm cover-page content
      controls were actually updated
- [ ] Confirm the swapped logo's filename inside `word/media/` still uses
      the original required extension (jpeg vs png) — see
      [logo-swap-procedure.md](logo-swap-procedure.md)
