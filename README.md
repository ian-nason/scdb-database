# The Supreme Court Database (SCDB) as a DuckDB database

Coded U.S. Supreme Court decisions and individual justices’ votes from the Supreme Court Database, combining the 1791–1945 legacy files with modern release 2026_01. Start with `v_cases` for labelled case-level analysis or `justice_votes` for voting records. Alternative docket, legal-provision and vote-split tables repeat aspects of the same decisions; do not add them together as additional cases.

<a id="quick-start"></a>

## Start querying

Show five Supreme Court case records from the 2020 term onward, with the case ID, term and recorded decision direction. The rows come from the case-level view, rather than the separate justice-vote tables.

`term` identifies the Supreme Court term. `decision_direction` is SCDB’s classification of the decision, shown as a label by `v_cases`.

Choose R or Python. Install datapond once: use `install.packages("datapond")` in R, or run `python -m pip install datapond` in a terminal.

### R

```r
library(datapond)
con <- dp_connect("scdb")
tryCatch({
  DBI::dbExecute(con, "SET threads=1")
  DBI::dbExecute(con, "SET memory_limit='128MiB'")
  DBI::dbExecute(con, "SET max_temp_directory_size='0B'")
  print(DBI::dbGetQuery(con, "SELECT caseId,term,decision_direction FROM v_cases WHERE term>=2020 ORDER BY caseId LIMIT 5"))
}, finally = dp_disconnect(con))
```

### Python

```python
import datapond
con = datapond.connect('scdb')
try:
    con.execute("SET threads=1")
    con.execute("SET memory_limit='128MiB'")
    con.execute("SET max_temp_directory_size='0B'")
    print(con.execute("""SELECT caseId,term,decision_direction FROM v_cases WHERE term>=2020 ORDER BY caseId LIMIT 5""").fetchall())
finally:
    con.close()
```

Queries run on your computer and read the byte ranges they need. A small result can still require a large scan. These examples limit DuckDB to one thread and a 128 MiB buffer pool with disk spill disabled; that is not a limit on the entire R or Python process. Larger analyses may need more memory or a local download with enough disk space.

<a id="additional-dataset-notes"></a>

## Tables, fields and joins

See the [data dictionary](https://github.com/ian-nason/scdb-database/blob/main/DICTIONARY.md) for column definitions.

Start with `v_cases`, the decoded `cases` view, or `justice_votes` for one row per justice and case. The complete online code book is loaded into `codes` so coded values can be decoded in SQL.

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

Dates are stored as `DATE`; the source uses `m/d/yyyy`.

<a id="advanced-access-quick-start"></a>

## More example queries

Count case records by term and decision direction, then compare the share of recorded votes in the majority for each justice. The vote-share query excludes missing majority values. These are additional analytical examples; apply the connection resource limits from the first query for bounded use.

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

<a id="coverage-fields-and-sources"></a>

## Sources and maintenance

### Sources and attribution

Database home: [Washington University’s Supreme Court Database](http://scdb.wustl.edu/).

Source: [The Supreme Court Database (Washington University in St. Louis)](http://scdb.wustl.edu/data.php). License: CC BY-NC 3.0.

- **License:** the SCDB is released under CC BY-NC 3.0; cite Spaeth et al. as the SCDB
  requests.

### Build

The build integer-casts every coded variable and fails if any value is not an integer.

```bash
uv sync && ./download_data.sh
uv run python scrape_codebook.py   # refresh docs/scdb_codes.csv from the online code book
uv run python build_database.py && uv run python publish_to_hf.py --verify
```

### License

Code: MIT. Data: The Supreme Court Database, Harold J. Spaeth, Lee Epstein, et al.,
CC BY-NC 3.0 (http://scdb.wustl.edu/about.php).
