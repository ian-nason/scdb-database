# The Supreme Court Database (SCDB) as a DuckDB database

Every U.S. Supreme Court decision from 1791 to the present, from Washington University's
[Supreme Court Database](http://scdb.wustl.edu/): the modern database (1946 term onward,
release 2026_01) and the Legacy database (1791-1945), at both the case and the justice level,
with the entire online code book loaded as a table so every code can be decoded in SQL.

| Table | One row per | Rows | Coverage |
|-------|-------------|-----:|----------|
| `cases` | case (by citation) | 29,270 | 1791-2025 terms (modern + legacy) |
| `cases_docket` | docket consolidated in a decision | 10,932 | 1946- |
| `cases_legal_provision` | legal provision considered | 14,016 | 1946- |
| `cases_vote` | issue/vote split | 14,090 | 1946- |
| `justice_votes` | justice x case: vote, opinion, direction, majority, agreements | 256,469 | 1791- (modern + legacy) |
| `justice_votes_docket` / `_legal_provision` / `_vote` | justice-level rows of the split tables | 97,918 / 125,571 / 126,237 | 1946- |
| `codes` | (variable, code, label) from the online code book | 2,949 | 44 variables |

`database` says `modern` or `legacy` on every row. Keys: `caseId` (`term-number`),
`docketId`, `caseIssuesId`, `voteId`, `justice`. `v_cases` is `cases` with issue area,
issue, decision direction, decision type, winning party and opinion writer decoded.
Columns and null rates: `DICTIONARY.md`; variable definitions: the
[online code book](http://scdb.wustl.edu/documentation.php).

## Quick start

```python
import datapond
con = datapond.connect("scdb")
con.sql("""
    SELECT term, decision_direction, COUNT(*) AS n
    FROM v_cases WHERE term >= 2015 GROUP BY 1, 2 ORDER BY 1, 2
""").show()
```

```sql
-- share of votes in the majority for every justice who voted in the 2020 term or later
-- (includes justices who have since left the Court, e.g. Breyer)
SELECT k.label AS justice, COUNT(*) AS votes, ROUND(AVG((j.majority = 2)::INTEGER) * 100, 1) AS pct_in_majority
FROM justice_votes j JOIN codes k ON k.variable = 'justice' AND k.code = j.justice::VARCHAR
WHERE j.term >= 2020 AND j.majority IS NOT NULL GROUP BY 1 ORDER BY 3 DESC;
```

## Researcher caveats

- **Units of analysis.** The SCDB publishes the same cases four ways (by citation, docket,
  legal provision, vote split). `cases` and `justice_votes` are the citation-level files most
  analyses use; the split tables repeat case variables across their rows, so do not add them.
- **Codes are integers; labels live in `codes`.** Justice ids, issue codes (278), parties
  (311), lower-court dispositions and so on are all there. `-99` in `justice_votes.justice`
  is the SCDB's own "unknown" in a few legacy rows.
- **Legacy vs modern.** The Legacy database has the two citation-level units only, and its
  justice-centered file carries 25 cases (1896-1931) that its case-centered file lacks; they
  are kept as published. Some variables are coded less completely before 1946.
- The build integer-casts every coded variable and fails if any value is not an integer;
  dates are `DATE` (`m/d/yyyy` in the source).
- **License:** the SCDB is released under CC BY-NC 3.0; cite Spaeth et al. as the SCDB
  requests.

## Build

```bash
uv sync && ./download_data.sh
uv run python scrape_codebook.py   # refresh docs/scdb_codes.csv from the online code book
uv run python build_database.py && uv run python publish_to_hf.py --verify
```

## License

Code: MIT. Data: The Supreme Court Database, Harold J. Spaeth, Lee Epstein, et al.,
CC BY-NC 3.0 (http://scdb.wustl.edu/about.php).
