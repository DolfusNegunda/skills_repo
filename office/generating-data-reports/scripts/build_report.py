"""Build a single self-contained HTML data report from a CSV file.

Loads the CSV with pandas, computes summary statistics for every numeric
column, renders up to two matplotlib charts — a trend line when a date-like
column is found, and a category bar chart when a low-cardinality text column
is found — and writes one portable .html file. Charts are embedded as base64
PNG data URIs, so the output has no external image files.

Error handling (fails loudly with actionable messages):
  - Input file missing or unreadable -> names the path and the fix.
  - Empty or header-only CSV -> says so explicitly.
  - Object columns that are mostly numeric text ("$1,200", "3,4%") are
    coerced to numbers automatically; a dataset with no numeric columns at
    all (even after coercion) aborts with each column's dtype listed.

Usage:
    python scripts/build_report.py --data examples/sample_sales.csv \
        --title "Q2 Sales Snapshot" --out examples/output/report.html

Dependencies: pip install pandas matplotlib
"""
import argparse
import base64
import html
import io
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd
import matplotlib

matplotlib.use("Agg")  # headless backend: render to memory, never open a window
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Tunable constants (documented so nothing below is a magic number)
# ---------------------------------------------------------------------------
CHART_SIZE_INCHES = (8.0, 4.0)  # 2:1 landscape fits the report column width
CHART_DPI = 110                 # crisp on normal displays without bloating the file
MAX_CATEGORY_BARS = 12          # more bars than this is unreadable; keep the top N
DATE_PARSE_FRACTION = 0.9       # a column is "date-like" if >=90% of values parse as dates
NUMERIC_COERCE_FRACTION = 0.9   # coerce a text column to numeric if >=90% of values parse
MAX_CATEGORY_CARDINALITY = 25   # a text column with more distinct values is an ID, not a category
CHART_COLOR = "#2b6cb0"         # single accent color used by both charts


def fail(message):
    """Print an actionable error to stderr and exit non-zero."""
    sys.exit(f"error: {message}")


def load_dataset(path):
    """Load the CSV, turning file and parse problems into clear messages."""
    csv_path = Path(path)
    if not csv_path.exists():
        fail(f"data file not found: {csv_path} — check the --data path (is it relative to the wrong directory?)")
    if not csv_path.is_file():
        fail(f"--data points to a directory, not a file: {csv_path}")
    try:
        df = pd.read_csv(csv_path)
    except pd.errors.EmptyDataError:
        fail(f"{csv_path} is empty — export the data again; the file has no header row or rows.")
    except pd.errors.ParserError as exc:
        fail(f"{csv_path} could not be parsed as CSV: {exc}")
    if df.empty:
        fail(f"{csv_path} contains a header but zero data rows — nothing to report on.")
    return df


def coerce_numeric_text(df):
    """Convert text columns that are really numbers ('$1,200', '15%') in place.

    Returns the list of column names that were converted.
    """
    converted = []
    for col in df.columns:
        if df[col].dtype != object:
            continue
        cleaned = (
            df[col].astype(str).str.strip().str.replace(r"[$,%\s]", "", regex=True)
        )
        as_num = pd.to_numeric(cleaned, errors="coerce")
        non_null = df[col].notna().sum()
        if non_null and (as_num.notna().sum() / non_null) >= NUMERIC_COERCE_FRACTION:
            df[col] = as_num
            converted.append(col)
    return converted


def find_date_column(df):
    """Return (column_name, parsed_series) for the first date-like column, else (None, None)."""
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            continue
        try:
            parsed = pd.to_datetime(df[col], errors="coerce", format="mixed")
        except (TypeError, ValueError):  # pandas < 2.0 has no format="mixed"
            parsed = pd.to_datetime(df[col], errors="coerce")
        non_null = df[col].notna().sum()
        if non_null and (parsed.notna().sum() / non_null) >= DATE_PARSE_FRACTION:
            return col, parsed
    return None, None


def find_category_column(df, skip):
    """Return the first low-cardinality text column not in `skip`, else None."""
    for col in df.columns:
        if col in skip or pd.api.types.is_numeric_dtype(df[col]):
            continue
        distinct = df[col].nunique(dropna=True)
        if 1 < distinct <= MAX_CATEGORY_CARDINALITY:
            return col
    return None


def fig_to_data_uri(fig):
    """Render a matplotlib figure to a base64 PNG data URI and close it."""
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=CHART_DPI, bbox_inches="tight")
    plt.close(fig)
    encoded = base64.b64encode(buf.getvalue()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def build_charts(df):
    """Return a list of (caption, data_uri) chart tuples — zero, one, or two."""
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if not numeric_cols:
        return []
    metric = numeric_cols[0]  # first numeric column is the headline metric
    charts = []

    date_col, parsed_dates = find_date_column(df)
    if date_col is not None:
        trend = (
            df.assign(_date=parsed_dates)
            .dropna(subset=["_date"])
            .groupby("_date")[metric]
            .sum()
            .sort_index()
        )
        fig, ax = plt.subplots(figsize=CHART_SIZE_INCHES)
        ax.plot(trend.index, trend.values, marker="o", color=CHART_COLOR)
        ax.set_title(f"{metric} over {date_col}")
        ax.set_xlabel(date_col)
        ax.set_ylabel(metric)
        ax.grid(True, alpha=0.3)
        fig.autofmt_xdate()
        charts.append((f"Total {metric} by {date_col}", fig_to_data_uri(fig)))

    cat_col = find_category_column(df, skip={date_col})
    if cat_col is not None:
        totals = (
            df.groupby(cat_col)[metric]
            .sum()
            .sort_values(ascending=False)
            .head(MAX_CATEGORY_BARS)
        )
        fig, ax = plt.subplots(figsize=CHART_SIZE_INCHES)
        ax.bar(totals.index.astype(str), totals.values, color=CHART_COLOR)
        ax.set_title(f"{metric} by {cat_col}")
        ax.set_xlabel(cat_col)
        ax.set_ylabel(metric)
        ax.grid(True, axis="y", alpha=0.3)
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
        charts.append((f"Total {metric} by {cat_col} (top {MAX_CATEGORY_BARS})", fig_to_data_uri(fig)))

    return charts


def build_html(df, title, charts, coerced_cols):
    """Assemble the full report as a single HTML string."""
    numeric = df.select_dtypes(include="number")
    non_numeric = [c for c in df.columns if c not in numeric.columns]

    stats_html = numeric.describe().round(2).to_html(border=0)
    preview_html = df.head(10).to_html(border=0, index=False)

    notes = []
    if coerced_cols:
        notes.append(
            "Columns converted from text to numbers: " + ", ".join(map(html.escape, coerced_cols))
        )
    if non_numeric:
        notes.append(
            "Non-numeric columns (excluded from the statistics table): "
            + ", ".join(map(html.escape, non_numeric))
        )
    if not charts:
        notes.append("No date-like or category column was found, so no charts were generated.")
    notes_html = "".join(f"<li>{n}</li>" for n in notes)

    chart_html = "".join(
        f'<figure><img alt="{html.escape(caption)}" src="{uri}">'
        f"<figcaption>{html.escape(caption)}</figcaption></figure>"
        for caption, uri in charts
    )

    generated = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>
  body {{ font-family: Georgia, "Times New Roman", serif; max-width: 60rem;
         margin: 2rem auto; padding: 0 1rem; color: #1a202c; line-height: 1.5; }}
  h1 {{ border-bottom: 3px solid {CHART_COLOR}; padding-bottom: .4rem; }}
  h2 {{ color: {CHART_COLOR}; margin-top: 2rem; }}
  table {{ border-collapse: collapse; width: 100%; font-size: .9rem;
           font-family: system-ui, sans-serif; }}
  th, td {{ padding: .4rem .7rem; text-align: right; border-bottom: 1px solid #cbd5e0; }}
  th {{ background: #edf2f7; }}
  figure {{ margin: 1.5rem 0; text-align: center; }}
  img {{ max-width: 100%; height: auto; }}
  figcaption {{ font-size: .85rem; color: #4a5568; margin-top: .3rem; }}
  .meta {{ color: #4a5568; font-size: .9rem; }}
</style>
</head>
<body>
<h1>{html.escape(title)}</h1>
<p class="meta">Generated {generated} &middot; {len(df)} rows &middot; {len(df.columns)} columns</p>
<h2>Summary statistics</h2>
{stats_html}
<h2>Charts</h2>
{chart_html or "<p>No charts for this dataset.</p>"}
<h2>Data preview (first 10 rows)</h2>
{preview_html}
<h2>Notes</h2>
<ul>{notes_html or "<li>None.</li>"}</ul>
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser(
        description="Build a self-contained HTML report (tables + embedded charts) from a CSV."
    )
    parser.add_argument("--data", required=True, help="path to the input CSV file")
    parser.add_argument("--title", required=True, help="report title, e.g. from the user's brief")
    parser.add_argument("--out", required=True, help="path of the .html file to write")
    args = parser.parse_args()

    df = load_dataset(args.data)
    coerced = coerce_numeric_text(df)

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if not numeric_cols:
        dtypes = ", ".join(f"{c} ({df[c].dtype})" for c in df.columns)
        fail(
            "no numeric columns found, so there is nothing to summarize or chart. "
            f"Columns are: {dtypes}. Add or fix a numeric column (values like "
            "'1,200' or '$50' are converted automatically, but this file had none)."
        )

    charts = build_charts(df)
    report = build_html(df, args.title, charts, coerced)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report, encoding="utf-8")
    print(
        f"Report written: {out_path} "
        f"(rows: {len(df)}, numeric columns: {len(numeric_cols)}, charts: {len(charts)})"
    )


if __name__ == "__main__":
    main()
