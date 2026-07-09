# Report Structure and Chart Selection

## Contents
- Recommended report sections (in order)
- Choosing a chart type for the data
- One metric, one chart
- Sizing and readability rules the script encodes
- When to add no chart at all

## Recommended report sections (in order)

The generated report follows this order deliberately — readers scan top-down
and should hit conclusions before raw material:

1. **Title + metadata line.** The user's brief becomes the title. The metadata
   line (generation timestamp, row count, column count) lets a reader judge
   freshness and scale at a glance.
2. **Summary statistics.** One table, numeric columns only: count, mean,
   std, min, quartiles, max. This answers "what is typical and what is the
   spread?" before any picture does.
3. **Charts.** At most two, each answering a single question (see below).
4. **Data preview.** The first 10 rows, so a reader can sanity-check what the
   statistics were computed over without opening the CSV.
5. **Notes.** Anything the pipeline did on the reader's behalf: text columns
   coerced to numbers, columns excluded from statistics, charts skipped.

## Choosing a chart type for the data

Ask two questions about the dataset, in this order:

| Question | If yes | Chart |
| -------- | ------ | ----- |
| Is there a date or time column? | Show change over time | **Line chart**: x = date, y = sum of the headline metric per date |
| Is there a text column with few distinct values (a category, not an ID)? | Compare groups | **Bar chart**: one bar per category, sorted descending by total |

Other shapes, for when the script is extended or a chart is built by hand:

- **Two numeric columns, suspected relationship** → scatter plot.
- **One numeric column, distribution question** ("are values clustered?") →
  histogram.
- **Part-of-whole with 5 or fewer slices** → a sorted bar chart still beats a
  pie chart; use a pie only if the audience explicitly expects one.

What disqualifies a text column from being a "category": high cardinality.
If nearly every row has a distinct value (names, emails, order IDs), grouping
by it produces one bar per row — noise, not comparison. The script treats
more than 25 distinct values as an identifier and skips it.

## One metric, one chart

Each chart plots exactly one numeric column (the first numeric column in the
file, treated as the headline metric). Resist overlaying several metrics with
different units on one axis — if two metrics both matter, that is two charts,
and this report format intentionally caps at two. Reorder the CSV's columns
to change which metric leads.

## Sizing and readability rules the script encodes

- Bar charts are capped at the top 12 categories; a long tail of slivers hides
  the comparison the chart exists to make.
- Charts render at 8 x 4 inches, 110 DPI — wide enough for date labels,
  small enough that the base64 payload keeps the HTML portable.
- Category labels rotate 30 degrees so long names do not overlap.
- One accent color throughout; color should carry no meaning the caption
  does not state.

## When to add no chart at all

If the dataset has neither a date-like column nor a usable category column
(for example, a single column of measurements), the report ships with tables
only and says so in the Notes section. A forced chart of unordered row
indices communicates nothing and undermines trust in the rest of the report.
