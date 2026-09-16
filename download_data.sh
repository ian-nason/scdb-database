#!/usr/bin/env bash
# Supreme Court Database (Washington University), modern (1946-) release 2026_01 and Legacy (1791-1945).
# http://scdb.wustl.edu/data.php  -- CSV zips, one per unit of analysis.
set -uo pipefail
cd "$(dirname "$0")"
mkdir -p data/raw
failed=0
REL=${SCDB_RELEASE:-2026_01}
LEG=${SCDB_LEGACY:-Legacy_07}
# The manifest the build uses: all eight units of the modern release, but only the two
# citation-level units of the Legacy database (the SCDB publishes no legacy docket /
# legal-provision / vote files).
MANIFEST=(
  "$REL caseCentered_Citation" "$REL caseCentered_Docket" "$REL caseCentered_LegalProvision" "$REL caseCentered_Vote"
  "$REL justiceCentered_Citation" "$REL justiceCentered_Docket" "$REL justiceCentered_LegalProvision" "$REL justiceCentered_Vote"
  "$LEG caseCentered_Citation" "$LEG justiceCentered_Citation"
)
for entry in "${MANIFEST[@]}"; do
  read -r ver unit <<< "$entry"
  {
    f="data/raw/SCDB_${ver}_${unit}.csv.zip"
    [[ -s "$f" ]] && continue
    curl --fail -L --retry 5 -sS -A "Mozilla/5.0 (datapond-maintenance)" -o "$f.part" "http://scdb.wustl.edu/_brickFiles/${ver}/SCDB_${ver}_${unit}.csv.zip" \
      && python3 -c "import zipfile,sys; sys.exit(0 if zipfile.is_zipfile('$f.part') else 1)" && mv "$f.part" "$f" && echo "ok $f $(stat -c %s "$f")" || { rm -f "$f.part"; echo "FAIL $f" >&2; failed=$((failed + 1)); }
  }
done
if [[ $failed -gt 0 ]]; then echo "$failed download(s) failed" >&2; exit 1; fi
