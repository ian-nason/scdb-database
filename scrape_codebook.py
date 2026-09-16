#!/usr/bin/env python3
"""Scrape the SCDB online code book (http://scdb.wustl.edu/documentation.php) into docs/scdb_codes.csv:
one row per (variable, code, label) for every variable that has a code table. Run when the SCDB
publishes a new release; the build loads the CSV into the `codes` table."""
import csv, html, re, urllib.request

BASE = "http://scdb.wustl.edu/documentation.php"


def fetch(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=60).read().decode("latin-1")


index = fetch(BASE)
variables = sorted(set(re.findall(r"documentation\.php\?var=([A-Za-z0-9_]+)", index)))
rows = []
for var in variables:
    page = fetch(f"{BASE}?var={var}")
    m = re.search(r"Normalizations\s*(?:</[^>]+>\s*)*(\d+)", re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", page)))
    tables = re.findall(r"<table.*?</table>", page, flags=re.S)
    best = None
    for t in tables:
        trs = re.findall(r"<tr[^>]*>(.*?)</tr>", t, flags=re.S)
        parsed = []
        for tr in trs:
            cells = [html.unescape(re.sub(r"<[^>]+>", "", c)).strip() for c in re.findall(r"<td[^>]*>(.*?)</td>", tr, flags=re.S)]
            cells = [re.sub(r"\s+", " ", c) for c in cells]
            if len(cells) >= 2 and cells[0] and cells[1]:
                parsed.append(cells)
        if parsed and (best is None or len(parsed) > len(best)):
            best = parsed
    if not best or len(best) < 2 or var in ("caseName", "docket", "usCite", "sctCite", "ledCite", "lexisCite", "dateDecision", "dateArgument", "dateRearg", "term"):
        print(f"{var}: no code table"); continue
    for cells in best:
        rows.append((var, cells[0], cells[1], cells[2] if len(cells) > 2 else ""))
    print(f"{var}: {len(best)} codes")
with open("docs/scdb_codes.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["variable", "code", "label", "extra"]); w.writerows(rows)
print(f"wrote docs/scdb_codes.csv: {len(rows)} rows, {len({r[0] for r in rows})} variables")
