#!/usr/bin/env python3
"""Build scdb.duckdb from the Supreme Court Database (Washington University in St. Louis).
Sources (http://scdb.wustl.edu/data.php; run ./download_data.sh):
    SCDB_<release>_<unit>.csv.zip      modern database, 1946 term to present (release 2026_01)
    SCDB_Legacy_07_<unit>.csv.zip      legacy database, 1791-1945 (citation-level units only)
Units of analysis become tables; where the legacy database has the unit, its rows are unioned
in with `database = 'legacy'`:
    cases                    caseCentered_Citation      one row per case (by citation)         modern + legacy
    cases_docket             caseCentered_Docket        one row per docket                     modern
    cases_legal_provision    caseCentered_LegalProvision one row per legal provision           modern
    cases_vote               caseCentered_Vote          one row per issue/vote split           modern
    justice_votes            justiceCentered_Citation   one row per justice per case           modern + legacy
    justice_votes_docket / justice_votes_legal_provision / justice_votes_vote   (modern)
    codes                    the online code book (docs/scdb_codes.csv, scrape_codebook.py)
Variable names are the SCDB's (camelCase); code values are integers, labels live in `codes`.
"""
from __future__ import annotations

import argparse
import sys
import time
import zipfile
from pathlib import Path

from datapond_build import Checker, build_columns_table, ensure_metadata, export_dictionary
from datapond_build.session import connect

RAW = Path("data/raw")
DEFAULT_OUTPUT = "scdb.duckdb"
RELEASE = "2026_01"
LEGACY = "Legacy_07"
SOURCE_URL = "http://scdb.wustl.edu/data.php"
UNITS = {
    "cases": "caseCentered_Citation",
    "cases_docket": "caseCentered_Docket",
    "cases_legal_provision": "caseCentered_LegalProvision",
    "cases_vote": "caseCentered_Vote",
    "justice_votes": "justiceCentered_Citation",
    "justice_votes_docket": "justiceCentered_Docket",
    "justice_votes_legal_provision": "justiceCentered_LegalProvision",
    "justice_votes_vote": "justiceCentered_Vote",
}
TABLE_DESCRIPTIONS = {
    "cases": "One row per Supreme Court case by citation, 1791-present (modern 1946+ release 2026_01 plus the Legacy database): "
             "dates, citations, parties, origin, issue, decision direction, disposition, vote counts, opinion writer",
    "cases_docket": "Modern cases split one row per docket number consolidated in the decision (1946-present)",
    "cases_legal_provision": "Modern cases split one row per legal provision considered (1946-present)",
    "cases_vote": "Modern cases split one row per issue/vote split (1946-present)",
    "justice_votes": "One row per justice per case, 1791-present: the case variables plus the justice's vote, opinion, direction, majority and agreement",
    "justice_votes_docket": "Justice-level rows of cases_docket (1946-present)",
    "justice_votes_legal_provision": "Justice-level rows of cases_legal_provision (1946-present)",
    "justice_votes_vote": "Justice-level rows of cases_vote (1946-present)",
    "codes": "SCDB online code book: the label for every coded value (variable, code, label; justices carry their service dates in extra)",
}
JOIN_HINTS = {
    "caseId": "SCDB case id (term-number); joins every case/justice table",
    "docketId": "caseId plus docket sequence; joins the *_docket tables",
    "caseIssuesId": "docketId plus legal-provision sequence",
    "voteId": "caseIssuesId plus vote-split sequence (and justice sequence in justice tables)",
    "justice": "Justice id; label in codes where variable = 'justice'",
    "issueArea": "Issue area code; label in codes where variable = 'issueArea'",
    "decisionDirection": "1 conservative, 2 liberal, 3 unspecifiable (codes table)",
    "term": "Term of Court (year the term began)",
}
TEXT_COLS = {"caseId", "docketId", "caseIssuesId", "voteId", "usCite", "sctCite", "ledCite", "lexisCite", "chief", "docket", "caseName",
             "lawMinor", "justiceName"}
DATE_COLS = {"dateDecision", "dateArgument", "dateRearg"}


def extract(name: str) -> Path:
    z = RAW / f"{name}.csv.zip"
    out = RAW / f"{name}.csv"
    if not out.exists():
        with zipfile.ZipFile(z) as zf:
            zf.extract(f"{name}.csv", RAW)
    return out


def load_unit(con, table: str, unit: str) -> dict[str, int]:
    counts = {}
    for db, ver, enc in (("modern", RELEASE, "utf-8"), ("legacy", LEGACY, "latin-1")):
        z = RAW / f"SCDB_{ver}_{unit}.csv.zip"
        if not z.exists():
            continue
        path = extract(f"SCDB_{ver}_{unit}")
        con.execute(f"CREATE OR REPLACE TABLE _raw AS SELECT * FROM read_csv('{path}', all_varchar=true, header=true, sample_size=-1, encoding='{enc}')")
        header = [r[0] for r in con.execute("DESCRIBE _raw").fetchall()]
        exprs = [f"'{db}' AS database"]
        for h in header:
            clean = f'NULLIF(TRIM("{h}"), \'\')'
            if h in DATE_COLS:
                exprs.append(f"TRY_STRPTIME({clean}, '%m/%d/%Y')::DATE AS {h}")
            elif h in TEXT_COLS:
                exprs.append(f"{clean} AS {h}")
            else:
                exprs.append(f"TRY_CAST({clean} AS INTEGER) AS {h}")
                bad = con.execute(f"SELECT COUNT(*) FROM _raw WHERE {clean} IS NOT NULL AND TRY_CAST({clean} AS INTEGER) IS NULL").fetchone()[0]
                if bad:
                    raise RuntimeError(f"{table}/{db}: {bad} non-integer values in {h}")
        sel = ", ".join(exprs)
        if db == "modern":
            con.execute(f"CREATE OR REPLACE TABLE {table} AS SELECT {sel} FROM _raw")
        else:
            con.execute(f"INSERT INTO {table} BY NAME SELECT {sel} FROM _raw")
        counts[db] = con.execute("SELECT COUNT(*) FROM _raw").fetchone()[0]
        con.execute("DROP TABLE _raw")
        path.unlink()
    return counts


def run_validation(con) -> int:
    ck = Checker("Validation")
    ck.query(con, "cases: caseId unique", "SELECT COUNT(*) - COUNT(DISTINCT caseId) FROM cases", lambda n: n == 0, str)
    ck.query(con, "cases: legacy + modern present", "SELECT COUNT(DISTINCT database) FROM cases", lambda n: n == 2, str)
    ck.query(con, "cases: terms 1791..2025", "SELECT MIN(term) || '-' || MAX(term) FROM cases", lambda s: s.startswith("1791-") and s >= "1791-2025", str)
    ck.query(con, "cases: dateDecision parsed (> 99.9%)", "SELECT COUNT(dateDecision) * 1.0 / COUNT(*) FROM cases", lambda v: v > 0.999, lambda v: f"{v:.3%}")
    ck.query(con, "cases: latest decision in the current release year", "SELECT MAX(dateDecision) FROM cases", lambda d: str(d) >= "2025-06-01", str)
    # the Legacy justice-centered file carries 25 cases (1896-1931) absent from the Legacy case-centered file; kept as published
    ck.query(con, "justice_votes: every modern caseId exists in cases",
             "SELECT COUNT(*) FROM justice_votes j LEFT JOIN cases c USING (caseId) WHERE c.caseId IS NULL AND j.database = 'modern'", lambda n: n == 0, str)
    ck.query(con, "justice_votes: legacy caseIds missing from cases stay a known handful (<= 30)",
             "SELECT COUNT(*) FROM justice_votes j LEFT JOIN cases c USING (caseId) WHERE c.caseId IS NULL AND j.database = 'legacy'", lambda n: n <= 30, str)
    ck.query(con, "justice_votes: (caseId, justice) unique", "SELECT COUNT(*) - COUNT(DISTINCT (caseId, justice)) FROM justice_votes", lambda n: n == 0, str)
    ck.query(con, "justice_votes: ~9 justices per modern case", "SELECT COUNT(*) * 1.0 / COUNT(DISTINCT caseId) FROM justice_votes WHERE database = 'modern'", lambda v: 8.5 < v < 9.2, lambda v: f"{v:.2f}")
    for t in ("cases_docket", "cases_legal_provision", "cases_vote"):
        ck.query(con, f"{t}: rows >= modern cases", f"SELECT (SELECT COUNT(*) FROM {t}) >= (SELECT COUNT(*) FROM cases WHERE database = 'modern')", lambda v: v, str)
    ck.query(con, "codes: every issueArea value has a label",
             "SELECT COUNT(*) FROM (SELECT DISTINCT issueArea FROM cases WHERE issueArea IS NOT NULL) v LEFT JOIN codes k ON k.variable = 'issueArea' AND k.code = v.issueArea::VARCHAR WHERE k.code IS NULL",
             lambda n: n == 0, str)
    ck.query(con, "codes: every justice has a label (-99 = SCDB unknown)",
             "SELECT COUNT(*) FROM (SELECT DISTINCT justice FROM justice_votes WHERE justice <> -99) v LEFT JOIN codes k ON k.variable = 'justice' AND k.code = v.justice::VARCHAR WHERE k.code IS NULL",
             lambda n: n == 0, str)
    ck.query(con, "v_cases runs", "SELECT COUNT(*) FROM v_cases", lambda n: n > 29000, lambda n: f"{n:,}")
    return ck.report()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=Path(DEFAULT_OUTPUT))
    a = ap.parse_args()
    t0 = time.time()
    con = connect(a.output, fresh=True, memory_limit="2GB", threads=2)
    counts = {}
    for table, unit in UNITS.items():
        c = load_unit(con, table, unit)
        counts[table] = sum(c.values())
        print(f"  {table}: " + ", ".join(f"{k} {v:,}" for k, v in c.items()))
    con.execute("CREATE OR REPLACE TABLE codes AS SELECT variable, code, label, NULLIF(extra, '') AS extra FROM read_csv('docs/scdb_codes.csv', all_varchar=true, header=true)")
    counts["codes"] = con.execute("SELECT COUNT(*) FROM codes").fetchone()[0]
    print(f"  codes: {counts['codes']:,}")
    con.execute("""
        CREATE VIEW v_cases AS
        SELECT c.caseId, c.database, c.term, c.dateDecision, c.usCite, c.caseName, c.chief,
               ia.label AS issue_area, i.label AS issue_label, dd.label AS decision_direction, dt.label AS decision_type,
               pw.label AS party_winning, c.majVotes, c.minVotes, mw.label AS maj_opinion_writer
        FROM cases c
        LEFT JOIN codes ia ON ia.variable = 'issueArea' AND ia.code = c.issueArea::VARCHAR
        LEFT JOIN codes i ON i.variable = 'issue' AND i.code = c.issue::VARCHAR
        LEFT JOIN codes dd ON dd.variable = 'decisionDirection' AND dd.code = c.decisionDirection::VARCHAR
        LEFT JOIN codes dt ON dt.variable = 'decisionType' AND dt.code = c.decisionType::VARCHAR
        LEFT JOIN codes pw ON pw.variable = 'partyWinning' AND pw.code = c.partyWinning::VARCHAR
        LEFT JOIN codes mw ON mw.variable = 'majOpinWriter' AND mw.code = c.majOpinWriter::VARCHAR""")
    print("\nMetadata + dictionary")
    ensure_metadata(con, descriptions=TABLE_DESCRIPTIONS, tables=list(counts), source_url=SOURCE_URL, license="CC BY-NC 3.0 (SCDB)", replace=True)
    build_columns_table(con, join_hints=JOIN_HINTS, tables=list(counts))
    export_dictionary(con, Path("DICTIONARY.md"), title="scdb Data Dictionary",
                      intro=[f"Source: [The Supreme Court Database]({SOURCE_URL}), modern release {RELEASE} (1946-) and {LEGACY.replace('_', ' ')} (1791-1945).",
                             "Variable names and codes are the SCDB's; every code's label is in the `codes` table and the online code book at http://scdb.wustl.edu/documentation.php.",
                             "`v_cases` is `cases` with the most-used codes decoded."],
                      style="registry", tables=list(counts))
    con.execute("CHECKPOINT")
    failures = run_validation(con)
    con.close()
    print(f"\nBUILD DONE in {time.time() - t0:.0f}s; " + ", ".join(f"{k} {v:,}" for k, v in counts.items()) + f"; {a.output.stat().st_size / 1024**2:.0f} MB")
    if failures:
        print(f"BUILD FAILED: {failures} check(s) failed -- do not publish this file")
        sys.exit(1)


if __name__ == "__main__":
    main()
