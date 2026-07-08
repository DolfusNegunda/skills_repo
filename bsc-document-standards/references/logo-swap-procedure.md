# Client/Project Logo Swap Procedure

## Contents
- Where the logo lives inside a .docx
- Swap procedure (code)
- Format-preservation rule
- Verifying the swap

## Where the logo lives inside a .docx
A `.docx` file is a zip archive. In every BSC document template, the
client/project logo (the ONE thing that changes per project — see
[../SKILL.md](../SKILL.md) for the full logo placement table) is stored at:
```
word/media/image1.jpeg   (or image1.png, depending on the source file)
```
All other fixed BSC brand images (`image2`–`image5` in the reference
examples) must be left untouched.

Confirm which extension a given base template uses before swapping:
```python
import zipfile
with zipfile.ZipFile("base-template.docx") as z:
    image1_name = next(n for n in z.namelist() if n.startswith("word/media/image1."))
print(image1_name)   # e.g. "word/media/image1.jpeg"
```

## Swap procedure (code)
```python
import io
import zipfile
from pathlib import Path
from PIL import Image

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
        im = im.convert("RGB")   # JPEG has no alpha channel
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
```
Call this **after** saving all text/table edits with python-docx (do the
text edits first via `Document(...).save(...)`, then run `swap_logo` on the
saved file) — mixing python-docx save operations with direct zip
manipulation in the same pass causes write conflicts.

## Format-preservation rule
Always convert the new logo image to match the **existing** `image1`
extension (jpeg or png) rather than keeping the new logo's original
format. Word's relationship/content-type declarations reference the exact
filename including extension; swapping in a `.png` under a name ending in
`.jpeg` (or vice versa) produces a file that LibreOffice/Word may fail to
render the image for, even though the zip itself is technically valid.

## Verifying the swap
```python
import zipfile
with zipfile.ZipFile("output.docx") as z:
    img1 = next(n for n in z.namelist() if n.startswith("word/media/image1."))
    data = z.read(img1)
with open("verify_logo.jpeg", "wb") as f:
    f.write(data)
```
Then inspect `verify_logo.jpeg` (e.g. via an image-inspection tool) to
visually confirm the correct client logo was written, not the original
project's logo. Do not assume success from the absence of an exception —
visually confirm at least once per new document type/template.
