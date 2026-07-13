"""Force a real formula recalculation of an .xlsx before validating it.

WHY THIS EXISTS: `validate_workbook.py` reads *cached* formula results via openpyxl,
which does not compute formulas. So an error like `#DIV/0!` is only catchable if some
application already recalculated and cached it. This step closes that gap by driving a
headless LibreOffice pass that recomputes every formula and writes fresh cached values,
so the subsequent validate step checks real results, not whatever was last saved.

Pipeline:  produce -> recalculate (this) -> validate_workbook.py -> fix -> re-validate

Usage:
    python scripts/recalculate_workbook.py <input.xlsx> [output.xlsx]
    # default output: <input>.recalc.xlsx next to the input

Behaviour and exit codes (machine-readable JSON on stdout):
    RECALCULATED       engine found, workbook recomputed and written   -> exit 0
    SKIPPED_NO_ENGINE  no LibreOffice on this machine; nothing changed  -> exit 0
    ERROR              input missing, or engine present but failed      -> exit 1

The SKIPPED path is a deliberate graceful degradation for restricted runtimes: the
caller should then validate the original file and treat "no cached values" as the known
limitation, not a pass. A SKIPPED result must never be reported as a successful recalc.

NOTE ON THOROUGHNESS: LibreOffice recomputes formulas on load when "recalculate on file
load" is in effect for foreign (xlsx) formats. If your environment disables that, enable
it (Tools > Options > Calc > Formula > Recalculation on File Load) or the resaved file may
carry forward stale cached values. This is an environment-level caveat, documented, not
silently assumed.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def find_engine():
    """Locate a LibreOffice/OpenOffice headless binary, or return None."""
    env = os.environ.get("SOFFICE_BIN")
    if env and Path(env).exists():
        return env
    for name in ("soffice", "libreoffice"):
        found = shutil.which(name)
        if found:
            return found
    candidates = [
        r"C:\Program Files\LibreOffice\program\soffice.exe",
        r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
        "/Applications/LibreOffice.app/Contents/MacOS/soffice",
        "/usr/bin/soffice",
        "/usr/bin/libreoffice",
        "/opt/libreoffice/program/soffice",
    ]
    for c in candidates:
        if Path(c).exists():
            return c
    return None


def recalculate(engine, src, dst):
    """Convert src -> xlsx via LibreOffice (forces a recompute), write to dst.

    Returns (ok, message). LibreOffice writes <stem>.xlsx into the out dir; we move it
    to the requested dst path.
    """
    with tempfile.TemporaryDirectory() as td:
        # A private user profile keeps the run deterministic and avoids clobbering any
        # real LibreOffice profile on the machine.
        profile = Path(td) / "profile"
        proc = subprocess.run(
            [engine, "--headless", "--calc",
             f"-env:UserInstallation=file://{profile.as_posix()}",
             "--convert-to", "xlsx:Calc MS Excel 2007 XML",
             "--outdir", td, str(src)],
            capture_output=True, text=True, timeout=180,
        )
        if proc.returncode != 0:
            return False, f"LibreOffice exited {proc.returncode}: {proc.stderr.strip()[:300]}"
        produced = Path(td) / (Path(src).stem + ".xlsx")
        if not produced.exists():
            return False, f"LibreOffice produced no output ({proc.stdout.strip()[:300]})"
        shutil.copyfile(produced, dst)
        return True, "recomputed via LibreOffice headless convert"


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit("usage: python scripts/recalculate_workbook.py <input.xlsx> [output.xlsx]")
    src = Path(sys.argv[1])
    if not src.exists():
        print(json.dumps({"file": str(src), "status": "ERROR",
                          "message": "input file not found"}, indent=2))
        sys.exit(1)
    dst = Path(sys.argv[2]) if len(sys.argv) == 3 else src.with_suffix(".recalc.xlsx")

    engine = find_engine()
    if not engine:
        print(json.dumps({
            "file": str(src),
            "status": "SKIPPED_NO_ENGINE",
            "recalculated": False,
            "engine": None,
            "message": ("No LibreOffice found. Formulas were NOT recomputed; validate the "
                        "original file and treat 'no cached values' as the known limitation."),
        }, indent=2))
        sys.exit(0)

    ok, message = recalculate(engine, src, dst)
    if not ok:
        print(json.dumps({"file": str(src), "status": "ERROR", "engine": engine,
                          "recalculated": False, "message": message}, indent=2))
        sys.exit(1)
    print(json.dumps({
        "file": str(src),
        "status": "RECALCULATED",
        "recalculated": True,
        "engine": engine,
        "output": str(dst),
        "message": message + f". Now run: validate_workbook.py {dst}",
    }, indent=2))
    sys.exit(0)


if __name__ == "__main__":
    main()
