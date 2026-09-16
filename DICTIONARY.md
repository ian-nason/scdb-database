# scdb Data Dictionary

Source: [The Supreme Court Database](http://scdb.wustl.edu/data.php), modern release 2026_01 (1946-) and Legacy 07 (1791-1945).
Variable names and codes are the SCDB's; every code's label is in the `codes` table and the online code book at http://scdb.wustl.edu/documentation.php.
`v_cases` is `cases` with the most-used codes decoded.

## cases

One row per Supreme Court case by citation, 1791-present (modern 1946+ release 2026_01 plus the Legacy database): dates, citations, parties, origin, issue, decision direction, disposition, vote counts, opinion writer

Rows: 29,270

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| database | VARCHAR | 0.0% | legacy |  |
| caseId | VARCHAR | 0.0% | 1791-001 | SCDB case id (term-number); joins every case/justice table |
| docketId | VARCHAR | 0.0% | 1791-001-01 | caseId plus docket sequence; joins the *_docket tables |
| caseIssuesId | VARCHAR | 0.0% | 1791-001-01-01 | docketId plus legal-provision sequence |
| voteId | VARCHAR | 0.0% | 1791-001-01-01-01 | caseIssuesId plus vote-split sequence (and justice sequence in justice tables) |
| dateDecision | DATE | 0.0% | 1791-08-03 |  |
| decisionType | INTEGER | 0.0% | 1 |  |
| usCite | VARCHAR | 1.8% | 10 U.S. 148 |  |
| sctCite | VARCHAR | 21.3% | 1 S. Ct. 1 |  |
| ledCite | VARCHAR | 0.1% | 1 L. Ed. 2d 1 |  |
| lexisCite | VARCHAR | 0.0% | 1791 U.S. LEXIS 189 |  |
| term | INTEGER | 0.0% | 1791 | Term of Court (year the term began) |
| naturalCourt | INTEGER | 0.0% | 1001 |  |
| chief | VARCHAR | 0.0% | Burger |  |
| docket | VARCHAR | 16.7% | 00-1011 |  |
| caseName | VARCHAR | 0.0% | *WILLIAM BAILEY, PLAINTIFF IN ERROR, v. WILLIAM B. DOZIER |  |
| dateArgument | DATE | 20.0% | 1791-08-02 |  |
| dateRearg | DATE | 97.9% | 1796-08-05 |  |
| petitioner | INTEGER | 0.0% | 1 |  |
| petitionerState | INTEGER | 87.0% | 1 |  |
| respondent | INTEGER | 0.0% | 1 |  |
| respondentState | INTEGER | 78.2% | 1 |  |
| jurisdiction | INTEGER | 0.0% | 1 |  |
| adminAction | INTEGER | 75.2% | 1 |  |
| adminActionState | INTEGER | 92.3% | 1 |  |
| threeJudgeFdc | INTEGER | 0.3% | 0 |  |
| caseOrigin | INTEGER | 3.3% | 1 |  |
| caseOriginState | INTEGER | 75.3% | 1 |  |
| caseSource | INTEGER | 1.9% | 1 |  |
| caseSourceState | INTEGER | 76.2% | 1 |  |
| lcDisagreement | INTEGER | 0.2% | 0 |  |
| certReason | INTEGER | 0.3% | 1 |  |
| lcDisposition | INTEGER | 44.0% | 1 |  |
| lcDispositionDirection | INTEGER | 4.0% | 1 |  |
| declarationUncon | INTEGER | 0.0% | 1 |  |
| caseDisposition | INTEGER | 0.9% | 1 |  |
| caseDispositionUnusual | INTEGER | 0.0% | 0 |  |
| partyWinning | INTEGER | 0.1% | 0 |  |
| precedentAlteration | INTEGER | 0.0% | 0 |  |
| voteUnclear | INTEGER | 0.0% | 0 |  |
| issue | INTEGER | 0.4% | 100010 |  |
| issueArea | INTEGER | 0.4% | 1 | Issue area code; label in codes where variable = 'issueArea' |
| decisionDirection | INTEGER | 0.3% | 1 | 1 conservative, 2 liberal, 3 unspecifiable (codes table) |
| decisionDirectionDissent | INTEGER | 1.4% | 0 |  |
| authorityDecision1 | INTEGER | 0.5% | 1 |  |
| authorityDecision2 | INTEGER | 85.6% | 1 |  |
| lawType | INTEGER | 4.6% | 1 |  |
| lawSupp | INTEGER | 4.6% | 100 |  |
| lawMinor | VARCHAR | 23.2% | (Treaty) Act of August 7, 1882 |  |
| majOpinWriter | INTEGER | 7.8% | 1 |  |
| majOpinAssigner | INTEGER | 1.0% | 1 |  |
| splitVote | INTEGER | 0.0% | 1 |  |
| majVotes | INTEGER | 0.0% | 1 |  |
| minVotes | INTEGER | 0.0% | 0 |  |

## cases_docket

Modern cases split one row per docket number consolidated in the decision (1946-present)

Rows: 10,932

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| database | VARCHAR | 0.0% | modern |  |
| caseId | VARCHAR | 0.0% | 1946-001 | SCDB case id (term-number); joins every case/justice table |
| docketId | VARCHAR | 0.0% | 1946-001-01 | caseId plus docket sequence; joins the *_docket tables |
| caseIssuesId | VARCHAR | 0.0% | 1946-001-01-01 | docketId plus legal-provision sequence |
| voteId | VARCHAR | 0.0% | 1946-001-01-01-01 | caseIssuesId plus vote-split sequence (and justice sequence in justice tables) |
| dateDecision | DATE | 0.0% | 1946-11-18 |  |
| decisionType | INTEGER | 0.0% | 1 |  |
| usCite | VARCHAR | 5.6% | 329 U.S. 1 |  |
| sctCite | VARCHAR | 0.1% | 100 S. Ct. 1092 |  |
| ledCite | VARCHAR | 0.1% | 1 L. Ed. 2d 1 |  |
| lexisCite | VARCHAR | 0.0% | 1946 U.S. LEXIS 1582 |  |
| term | INTEGER | 0.0% | 1946 | Term of Court (year the term began) |
| naturalCourt | INTEGER | 0.0% | 1301 |  |
| chief | VARCHAR | 0.0% | Burger |  |
| docket | VARCHAR | 0.3% | 00-1011 |  |
| caseName | VARCHAR | 0.0% | 14 PENN PLAZA LLC et al. v. STEVEN PYETT et al. |  |
| dateArgument | DATE | 11.5% | 1944-10-08 |  |
| dateRearg | DATE | 97.9% | 1946-10-14 |  |
| petitioner | INTEGER | 0.1% | 1 |  |
| petitionerState | INTEGER | 80.3% | 1 |  |
| respondent | INTEGER | 0.1% | 1 |  |
| respondentState | INTEGER | 72.9% | 1 |  |
| jurisdiction | INTEGER | 0.0% | 1 |  |
| adminAction | INTEGER | 71.0% | 1 |  |
| adminActionState | INTEGER | 93.2% | 1 |  |
| threeJudgeFdc | INTEGER | 0.3% | 0 |  |
| caseOrigin | INTEGER | 4.0% | 1 |  |
| caseOriginState | INTEGER | 74.1% | 1 |  |
| caseSource | INTEGER | 2.4% | 1 |  |
| caseSourceState | INTEGER | 78.0% | 1 |  |
| lcDisagreement | INTEGER | 0.3% | 0 |  |
| certReason | INTEGER | 1.2% | 1 |  |
| lcDisposition | INTEGER | 14.6% | 1 |  |
| lcDispositionDirection | INTEGER | 2.1% | 1 |  |
| declarationUncon | INTEGER | 0.0% | 1 |  |
| caseDisposition | INTEGER | 1.3% | 1 |  |
| caseDispositionUnusual | INTEGER | 0.0% | 0 |  |
| partyWinning | INTEGER | 0.2% | 0 |  |
| precedentAlteration | INTEGER | 0.0% | 0 |  |
| voteUnclear | INTEGER | 0.0% | 0 |  |
| issue | INTEGER | 0.7% | 100010 |  |
| issueArea | INTEGER | 0.7% | 1 | Issue area code; label in codes where variable = 'issueArea' |
| decisionDirection | INTEGER | 0.4% | 1 | 1 conservative, 2 liberal, 3 unspecifiable (codes table) |
| decisionDirectionDissent | INTEGER | 3.5% | 0 |  |
| authorityDecision1 | INTEGER | 0.7% | 1 |  |
| authorityDecision2 | INTEGER | 82.8% | 1 |  |
| lawType | INTEGER | 13.3% | 1 |  |
| lawSupp | INTEGER | 13.3% | 100 |  |
| lawMinor | VARCHAR | 70.4% | (Treaty) Act of August 7, 1882 |  |
| majOpinWriter | INTEGER | 18.7% | 100 |  |
| majOpinAssigner | INTEGER | 2.4% | 100 |  |
| splitVote | INTEGER | 0.0% | 1 |  |
| majVotes | INTEGER | 0.0% | 3 |  |
| minVotes | INTEGER | 0.0% | 0 |  |

## cases_legal_provision

Modern cases split one row per legal provision considered (1946-present)

Rows: 14,016

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| database | VARCHAR | 0.0% | modern |  |
| caseId | VARCHAR | 0.0% | 1946-001 | SCDB case id (term-number); joins every case/justice table |
| docketId | VARCHAR | 0.0% | 1946-001-01 | caseId plus docket sequence; joins the *_docket tables |
| caseIssuesId | VARCHAR | 0.0% | 1946-001-01-01 | docketId plus legal-provision sequence |
| voteId | VARCHAR | 0.0% | 1946-001-01-01-01 | caseIssuesId plus vote-split sequence (and justice sequence in justice tables) |
| dateDecision | DATE | 0.0% | 1946-11-18 |  |
| decisionType | INTEGER | 0.0% | 1 |  |
| usCite | VARCHAR | 4.7% | 329 U.S. 1 |  |
| sctCite | VARCHAR | 0.1% | 100 S. Ct. 1092 |  |
| ledCite | VARCHAR | 0.0% | 1 L. Ed. 2d 1 |  |
| lexisCite | VARCHAR | 0.0% | 1946 U.S. LEXIS 1582 |  |
| term | INTEGER | 0.0% | 1946 | Term of Court (year the term began) |
| naturalCourt | INTEGER | 0.0% | 1301 |  |
| chief | VARCHAR | 0.0% | Burger |  |
| docket | VARCHAR | 0.2% | 00-1011 |  |
| caseName | VARCHAR | 0.0% | 14 PENN PLAZA LLC et al. v. STEVEN PYETT et al. |  |
| dateArgument | DATE | 9.5% | 1944-10-08 |  |
| dateRearg | DATE | 97.3% | 1946-10-14 |  |
| petitioner | INTEGER | 0.0% | 1 |  |
| petitionerState | INTEGER | 80.4% | 1 |  |
| respondent | INTEGER | 0.1% | 1 |  |
| respondentState | INTEGER | 72.8% | 1 |  |
| jurisdiction | INTEGER | 0.0% | 1 |  |
| adminAction | INTEGER | 70.0% | 1 |  |
| adminActionState | INTEGER | 92.3% | 1 |  |
| threeJudgeFdc | INTEGER | 0.2% | 0 |  |
| caseOrigin | INTEGER | 3.4% | 1 |  |
| caseOriginState | INTEGER | 73.6% | 1 |  |
| caseSource | INTEGER | 2.1% | 1 |  |
| caseSourceState | INTEGER | 77.9% | 1 |  |
| lcDisagreement | INTEGER | 0.2% | 0 |  |
| certReason | INTEGER | 0.9% | 1 |  |
| lcDisposition | INTEGER | 16.2% | 1 |  |
| lcDispositionDirection | INTEGER | 1.9% | 1 |  |
| declarationUncon | INTEGER | 0.0% | 1 |  |
| caseDisposition | INTEGER | 1.2% | 1 |  |
| caseDispositionUnusual | INTEGER | 0.0% | 0 |  |
| partyWinning | INTEGER | 0.1% | 0 |  |
| precedentAlteration | INTEGER | 0.0% | 0 |  |
| voteUnclear | INTEGER | 0.0% | 0 |  |
| issue | INTEGER | 0.5% | 100010 |  |
| issueArea | INTEGER | 0.5% | 1 | Issue area code; label in codes where variable = 'issueArea' |
| decisionDirection | INTEGER | 0.3% | 1 | 1 conservative, 2 liberal, 3 unspecifiable (codes table) |
| decisionDirectionDissent | INTEGER | 2.9% | 0 |  |
| authorityDecision1 | INTEGER | 0.6% | 1 |  |
| authorityDecision2 | INTEGER | 83.8% | 1 |  |
| lawType | INTEGER | 11.7% | 1 |  |
| lawSupp | INTEGER | 11.7% | 100 |  |
| lawMinor | VARCHAR | 70.7% | (Treaty) Act of August 7, 1882 |  |
| majOpinWriter | INTEGER | 16.1% | 100 |  |
| majOpinAssigner | INTEGER | 2.4% | 100 |  |
| splitVote | INTEGER | 0.0% | 1 |  |
| majVotes | INTEGER | 0.0% | 3 |  |
| minVotes | INTEGER | 0.0% | 0 |  |

## cases_vote

Modern cases split one row per issue/vote split (1946-present)

Rows: 14,090

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| database | VARCHAR | 0.0% | modern |  |
| caseId | VARCHAR | 0.0% | 1946-001 | SCDB case id (term-number); joins every case/justice table |
| docketId | VARCHAR | 0.0% | 1946-001-01 | caseId plus docket sequence; joins the *_docket tables |
| caseIssuesId | VARCHAR | 0.0% | 1946-001-01-01 | docketId plus legal-provision sequence |
| voteId | VARCHAR | 0.0% | 1946-001-01-01-01 | caseIssuesId plus vote-split sequence (and justice sequence in justice tables) |
| dateDecision | DATE | 0.0% | 1946-11-18 |  |
| decisionType | INTEGER | 0.0% | 1 |  |
| usCite | VARCHAR | 4.7% | 329 U.S. 1 |  |
| sctCite | VARCHAR | 0.1% | 100 S. Ct. 1092 |  |
| ledCite | VARCHAR | 0.0% | 1 L. Ed. 2d 1 |  |
| lexisCite | VARCHAR | 0.0% | 1946 U.S. LEXIS 1582 |  |
| term | INTEGER | 0.0% | 1946 | Term of Court (year the term began) |
| naturalCourt | INTEGER | 0.0% | 1301 |  |
| chief | VARCHAR | 0.0% | Burger |  |
| docket | VARCHAR | 0.2% | 00-1011 |  |
| caseName | VARCHAR | 0.0% | 14 PENN PLAZA LLC et al. v. STEVEN PYETT et al. |  |
| dateArgument | DATE | 9.5% | 1944-10-08 |  |
| dateRearg | DATE | 97.3% | 1946-10-14 |  |
| petitioner | INTEGER | 0.0% | 1 |  |
| petitionerState | INTEGER | 80.4% | 1 |  |
| respondent | INTEGER | 0.1% | 1 |  |
| respondentState | INTEGER | 72.9% | 1 |  |
| jurisdiction | INTEGER | 0.0% | 1 |  |
| adminAction | INTEGER | 70.0% | 1 |  |
| adminActionState | INTEGER | 92.3% | 1 |  |
| threeJudgeFdc | INTEGER | 0.2% | 0 |  |
| caseOrigin | INTEGER | 3.4% | 1 |  |
| caseOriginState | INTEGER | 73.7% | 1 |  |
| caseSource | INTEGER | 2.1% | 1 |  |
| caseSourceState | INTEGER | 78.0% | 1 |  |
| lcDisagreement | INTEGER | 0.2% | 0 |  |
| certReason | INTEGER | 0.9% | 1 |  |
| lcDisposition | INTEGER | 16.3% | 1 |  |
| lcDispositionDirection | INTEGER | 1.9% | 1 |  |
| declarationUncon | INTEGER | 0.0% | 1 |  |
| caseDisposition | INTEGER | 1.2% | 1 |  |
| caseDispositionUnusual | INTEGER | 0.0% | 0 |  |
| partyWinning | INTEGER | 0.1% | 0 |  |
| precedentAlteration | INTEGER | 0.0% | 0 |  |
| voteUnclear | INTEGER | 0.0% | 0 |  |
| issue | INTEGER | 0.5% | 100010 |  |
| issueArea | INTEGER | 0.5% | 1 | Issue area code; label in codes where variable = 'issueArea' |
| decisionDirection | INTEGER | 0.3% | 1 | 1 conservative, 2 liberal, 3 unspecifiable (codes table) |
| decisionDirectionDissent | INTEGER | 2.9% | 0 |  |
| authorityDecision1 | INTEGER | 0.6% | 1 |  |
| authorityDecision2 | INTEGER | 83.8% | 1 |  |
| lawType | INTEGER | 11.6% | 1 |  |
| lawSupp | INTEGER | 11.6% | 100 |  |
| lawMinor | VARCHAR | 70.7% | (Treaty) Act of August 7, 1882 |  |
| majOpinWriter | INTEGER | 16.1% | 100 |  |
| majOpinAssigner | INTEGER | 2.4% | 100 |  |
| splitVote | INTEGER | 0.0% | 1 |  |
| majVotes | INTEGER | 0.0% | 3 |  |
| minVotes | INTEGER | 0.0% | 0 |  |

## justice_votes

One row per justice per case, 1791-present: the case variables plus the justice's vote, opinion, direction, majority and agreement

Rows: 256,469

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| database | VARCHAR | 0.0% | legacy |  |
| caseId | VARCHAR | 0.0% | 1791-001 | SCDB case id (term-number); joins every case/justice table |
| docketId | VARCHAR | 0.0% | 1791-001-01 | caseId plus docket sequence; joins the *_docket tables |
| caseIssuesId | VARCHAR | 0.0% | 1791-001-01-01 | docketId plus legal-provision sequence |
| voteId | VARCHAR | 0.0% | 1791-001-01-01-01-01 | caseIssuesId plus vote-split sequence (and justice sequence in justice tables) |
| dateDecision | DATE | 0.0% | 1791-08-03 |  |
| decisionType | INTEGER | 0.0% | 1 |  |
| usCite | VARCHAR | 1.9% | 10 U.S. 148 |  |
| sctCite | VARCHAR | 20.2% | 1 S. Ct. 1 |  |
| ledCite | VARCHAR | 0.1% | 1 L. Ed. 2d 1 |  |
| lexisCite | VARCHAR | 0.0% | 1791 U.S. LEXIS 189 |  |
| term | INTEGER | 0.0% | 1791 | Term of Court (year the term began) |
| naturalCourt | INTEGER | 0.0% | 1001 |  |
| chief | VARCHAR | 0.0% | Burger |  |
| docket | VARCHAR | 15.6% | 00-1011 |  |
| caseName | VARCHAR | 0.0% | *WILLIAM BAILEY, PLAINTIFF IN ERROR, v. WILLIAM B. DOZIER |  |
| dateArgument | DATE | 19.9% | 1791-08-02 |  |
| dateRearg | DATE | 97.9% | 1796-08-05 |  |
| petitioner | INTEGER | 0.0% | 1 |  |
| petitionerState | INTEGER | 86.9% | 1 |  |
| respondent | INTEGER | 0.0% | 1 |  |
| respondentState | INTEGER | 78.0% | 1 |  |
| jurisdiction | INTEGER | 0.0% | 1 |  |
| adminAction | INTEGER | 74.9% | 1 |  |
| adminActionState | INTEGER | 92.2% | 1 |  |
| threeJudgeFdc | INTEGER | 0.3% | 0 |  |
| caseOrigin | INTEGER | 3.3% | 1 |  |
| caseOriginState | INTEGER | 75.1% | 1 |  |
| caseSource | INTEGER | 1.9% | 1 |  |
| caseSourceState | INTEGER | 76.0% | 1 |  |
| lcDisagreement | INTEGER | 0.2% | 0 |  |
| certReason | INTEGER | 0.3% | 1 |  |
| lcDisposition | INTEGER | 43.3% | 1 |  |
| lcDispositionDirection | INTEGER | 3.9% | 1 |  |
| declarationUncon | INTEGER | 0.0% | 1 |  |
| caseDisposition | INTEGER | 0.9% | 1 |  |
| caseDispositionUnusual | INTEGER | 0.0% | 0 |  |
| partyWinning | INTEGER | 0.1% | 0 |  |
| precedentAlteration | INTEGER | 0.0% | 0 |  |
| voteUnclear | INTEGER | 0.0% | 0 |  |
| issue | INTEGER | 0.4% | 100010 |  |
| issueArea | INTEGER | 0.4% | 1 | Issue area code; label in codes where variable = 'issueArea' |
| decisionDirection | INTEGER | 0.4% | 1 | 1 conservative, 2 liberal, 3 unspecifiable (codes table) |
| decisionDirectionDissent | INTEGER | 1.4% | 0 |  |
| authorityDecision1 | INTEGER | 0.5% | 1 |  |
| authorityDecision2 | INTEGER | 85.7% | 1 |  |
| lawType | INTEGER | 4.7% | 1 |  |
| lawSupp | INTEGER | 4.7% | 100 |  |
| lawMinor | VARCHAR | 23.6% | (Treaty) Act of August 7, 1882 |  |
| majOpinWriter | INTEGER | 7.7% | 1 |  |
| majOpinAssigner | INTEGER | 1.1% | 1 |  |
| splitVote | INTEGER | 0.0% | -99 |  |
| majVotes | INTEGER | 0.0% | 1 |  |
| minVotes | INTEGER | 0.0% | 0 |  |
| justice | INTEGER | 0.0% | -99 | Justice id; label in codes where variable = 'justice' |
| justiceName | VARCHAR | 0.0% | -99 |  |
| vote | INTEGER | 3.5% | 1 |  |
| opinion | INTEGER | 3.5% | 1 |  |
| direction | INTEGER | 16.6% | 1 |  |
| majority | INTEGER | 4.0% | 1 |  |
| firstAgreement | INTEGER | 94.3% | 0 |  |
| secondAgreement | INTEGER | 98.7% | 0 |  |

## justice_votes_docket

Justice-level rows of cases_docket (1946-present)

Rows: 97,918

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| database | VARCHAR | 0.0% | modern |  |
| caseId | VARCHAR | 0.0% | 1946-001 | SCDB case id (term-number); joins every case/justice table |
| docketId | VARCHAR | 0.0% | 1946-001-01 | caseId plus docket sequence; joins the *_docket tables |
| caseIssuesId | VARCHAR | 0.0% | 1946-001-01-01 | docketId plus legal-provision sequence |
| voteId | VARCHAR | 0.0% | 1946-001-01-01-01-01 | caseIssuesId plus vote-split sequence (and justice sequence in justice tables) |
| dateDecision | DATE | 0.0% | 1946-11-18 |  |
| decisionType | INTEGER | 0.0% | 1 |  |
| usCite | VARCHAR | 5.6% | 329 U.S. 1 |  |
| sctCite | VARCHAR | 0.1% | 100 S. Ct. 1092 |  |
| ledCite | VARCHAR | 0.1% | 1 L. Ed. 2d 1 |  |
| lexisCite | VARCHAR | 0.0% | 1946 U.S. LEXIS 1582 |  |
| term | INTEGER | 0.0% | 1946 | Term of Court (year the term began) |
| naturalCourt | INTEGER | 0.0% | 1301 |  |
| chief | VARCHAR | 0.0% | Burger |  |
| docket | VARCHAR | 0.3% | 00-1011 |  |
| caseName | VARCHAR | 0.0% | 14 PENN PLAZA LLC et al. v. STEVEN PYETT et al. |  |
| dateArgument | DATE | 11.5% | 1944-10-08 |  |
| dateRearg | DATE | 97.9% | 1946-10-14 |  |
| petitioner | INTEGER | 0.1% | 1 |  |
| petitionerState | INTEGER | 80.3% | 1 |  |
| respondent | INTEGER | 0.1% | 1 |  |
| respondentState | INTEGER | 72.9% | 1 |  |
| jurisdiction | INTEGER | 0.0% | 1 |  |
| adminAction | INTEGER | 71.0% | 1 |  |
| adminActionState | INTEGER | 93.2% | 1 |  |
| threeJudgeFdc | INTEGER | 0.3% | 0 |  |
| caseOrigin | INTEGER | 4.0% | 1 |  |
| caseOriginState | INTEGER | 74.1% | 1 |  |
| caseSource | INTEGER | 2.4% | 1 |  |
| caseSourceState | INTEGER | 78.0% | 1 |  |
| lcDisagreement | INTEGER | 0.3% | 0 |  |
| certReason | INTEGER | 1.2% | 1 |  |
| lcDisposition | INTEGER | 14.6% | 1 |  |
| lcDispositionDirection | INTEGER | 2.2% | 1 |  |
| declarationUncon | INTEGER | 0.0% | 1 |  |
| caseDisposition | INTEGER | 1.3% | 1 |  |
| caseDispositionUnusual | INTEGER | 0.0% | 0 |  |
| partyWinning | INTEGER | 0.2% | 0 |  |
| precedentAlteration | INTEGER | 0.0% | 0 |  |
| voteUnclear | INTEGER | 0.0% | 0 |  |
| issue | INTEGER | 0.7% | 100010 |  |
| issueArea | INTEGER | 0.7% | 1 | Issue area code; label in codes where variable = 'issueArea' |
| decisionDirection | INTEGER | 0.4% | 1 | 1 conservative, 2 liberal, 3 unspecifiable (codes table) |
| decisionDirectionDissent | INTEGER | 3.5% | 0 |  |
| authorityDecision1 | INTEGER | 0.7% | 1 |  |
| authorityDecision2 | INTEGER | 82.8% | 1 |  |
| lawType | INTEGER | 13.3% | 1 |  |
| lawSupp | INTEGER | 13.3% | 100 |  |
| lawMinor | VARCHAR | 70.4% | (Treaty) Act of August 7, 1882 |  |
| majOpinWriter | INTEGER | 18.6% | 100 |  |
| majOpinAssigner | INTEGER | 2.4% | 100 |  |
| splitVote | INTEGER | 0.0% | 1 |  |
| majVotes | INTEGER | 0.0% | 3 |  |
| minVotes | INTEGER | 0.0% | 0 |  |
| justice | INTEGER | 0.0% | 100 | Justice id; label in codes where variable = 'justice' |
| justiceName | VARCHAR | 0.0% | ACBarrett |  |
| vote | INTEGER | 2.6% | 1 |  |
| opinion | INTEGER | 2.7% | 1 |  |
| direction | INTEGER | 5.8% | 1 |  |
| majority | INTEGER | 3.7% | 1 |  |
| firstAgreement | INTEGER | 86.1% | 0 |  |
| secondAgreement | INTEGER | 96.9% | 0 |  |

## justice_votes_legal_provision

Justice-level rows of cases_legal_provision (1946-present)

Rows: 125,571

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| database | VARCHAR | 0.0% | modern |  |
| caseId | VARCHAR | 0.0% | 1946-001 | SCDB case id (term-number); joins every case/justice table |
| docketId | VARCHAR | 0.0% | 1946-001-01 | caseId plus docket sequence; joins the *_docket tables |
| caseIssuesId | VARCHAR | 0.0% | 1946-001-01-01 | docketId plus legal-provision sequence |
| voteId | VARCHAR | 0.0% | 1946-001-01-01-01-01 | caseIssuesId plus vote-split sequence (and justice sequence in justice tables) |
| dateDecision | DATE | 0.0% | 1946-11-18 |  |
| decisionType | INTEGER | 0.0% | 1 |  |
| usCite | VARCHAR | 4.7% | 329 U.S. 1 |  |
| sctCite | VARCHAR | 0.1% | 100 S. Ct. 1092 |  |
| ledCite | VARCHAR | 0.0% | 1 L. Ed. 2d 1 |  |
| lexisCite | VARCHAR | 0.0% | 1946 U.S. LEXIS 1582 |  |
| term | INTEGER | 0.0% | 1946 | Term of Court (year the term began) |
| naturalCourt | INTEGER | 0.0% | 1301 |  |
| chief | VARCHAR | 0.0% | Burger |  |
| docket | VARCHAR | 0.2% | 00-1011 |  |
| caseName | VARCHAR | 0.0% | 14 PENN PLAZA LLC et al. v. STEVEN PYETT et al. |  |
| dateArgument | DATE | 9.5% | 1944-10-08 |  |
| dateRearg | DATE | 97.3% | 1946-10-14 |  |
| petitioner | INTEGER | 0.1% | 1 |  |
| petitionerState | INTEGER | 80.4% | 1 |  |
| respondent | INTEGER | 0.1% | 1 |  |
| respondentState | INTEGER | 72.8% | 1 |  |
| jurisdiction | INTEGER | 0.0% | 1 |  |
| adminAction | INTEGER | 70.0% | 1 |  |
| adminActionState | INTEGER | 92.3% | 1 |  |
| threeJudgeFdc | INTEGER | 0.2% | 0 |  |
| caseOrigin | INTEGER | 3.4% | 1 |  |
| caseOriginState | INTEGER | 73.6% | 1 |  |
| caseSource | INTEGER | 2.1% | 1 |  |
| caseSourceState | INTEGER | 77.9% | 1 |  |
| lcDisagreement | INTEGER | 0.2% | 0 |  |
| certReason | INTEGER | 0.9% | 1 |  |
| lcDisposition | INTEGER | 16.2% | 1 |  |
| lcDispositionDirection | INTEGER | 1.9% | 1 |  |
| declarationUncon | INTEGER | 0.0% | 1 |  |
| caseDisposition | INTEGER | 1.2% | 1 |  |
| caseDispositionUnusual | INTEGER | 0.0% | 0 |  |
| partyWinning | INTEGER | 0.1% | 0 |  |
| precedentAlteration | INTEGER | 0.0% | 0 |  |
| voteUnclear | INTEGER | 0.0% | 0 |  |
| issue | INTEGER | 0.5% | 100010 |  |
| issueArea | INTEGER | 0.5% | 1 | Issue area code; label in codes where variable = 'issueArea' |
| decisionDirection | INTEGER | 0.3% | 1 | 1 conservative, 2 liberal, 3 unspecifiable (codes table) |
| decisionDirectionDissent | INTEGER | 2.9% | 0 |  |
| authorityDecision1 | INTEGER | 0.6% | 1 |  |
| authorityDecision2 | INTEGER | 83.8% | 1 |  |
| lawType | INTEGER | 11.7% | 1 |  |
| lawSupp | INTEGER | 11.7% | 100 |  |
| lawMinor | VARCHAR | 70.7% | (Treaty) Act of August 7, 1882 |  |
| majOpinWriter | INTEGER | 16.1% | 100 |  |
| majOpinAssigner | INTEGER | 2.4% | 100 |  |
| splitVote | INTEGER | 0.0% | 1 |  |
| majVotes | INTEGER | 0.0% | 3 |  |
| minVotes | INTEGER | 0.0% | 0 |  |
| justice | INTEGER | 0.0% | 100 | Justice id; label in codes where variable = 'justice' |
| justiceName | VARCHAR | 0.0% | ACBarrett |  |
| vote | INTEGER | 2.7% | 1 |  |
| opinion | INTEGER | 2.8% | 1 |  |
| direction | INTEGER | 5.6% | 1 |  |
| majority | INTEGER | 3.6% | 1 |  |
| firstAgreement | INTEGER | 85.9% | 0 |  |
| secondAgreement | INTEGER | 97.1% | 0 |  |

## justice_votes_vote

Justice-level rows of cases_vote (1946-present)

Rows: 126,237

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| database | VARCHAR | 0.0% | modern |  |
| caseId | VARCHAR | 0.0% | 1946-001 | SCDB case id (term-number); joins every case/justice table |
| docketId | VARCHAR | 0.0% | 1946-001-01 | caseId plus docket sequence; joins the *_docket tables |
| caseIssuesId | VARCHAR | 0.0% | 1946-001-01-01 | docketId plus legal-provision sequence |
| voteId | VARCHAR | 0.0% | 1946-001-01-01-01-01 | caseIssuesId plus vote-split sequence (and justice sequence in justice tables) |
| dateDecision | DATE | 0.0% | 1946-11-18 |  |
| decisionType | INTEGER | 0.0% | 1 |  |
| usCite | VARCHAR | 4.7% | 329 U.S. 1 |  |
| sctCite | VARCHAR | 0.1% | 100 S. Ct. 1092 |  |
| ledCite | VARCHAR | 0.0% | 1 L. Ed. 2d 1 |  |
| lexisCite | VARCHAR | 0.0% | 1946 U.S. LEXIS 1582 |  |
| term | INTEGER | 0.0% | 1946 | Term of Court (year the term began) |
| naturalCourt | INTEGER | 0.0% | 1301 |  |
| chief | VARCHAR | 0.0% | Burger |  |
| docket | VARCHAR | 0.2% | 00-1011 |  |
| caseName | VARCHAR | 0.0% | 14 PENN PLAZA LLC et al. v. STEVEN PYETT et al. |  |
| dateArgument | DATE | 9.4% | 1944-10-08 |  |
| dateRearg | DATE | 97.3% | 1946-10-14 |  |
| petitioner | INTEGER | 0.0% | 1 |  |
| petitionerState | INTEGER | 80.3% | 1 |  |
| respondent | INTEGER | 0.1% | 1 |  |
| respondentState | INTEGER | 72.9% | 1 |  |
| jurisdiction | INTEGER | 0.0% | 1 |  |
| adminAction | INTEGER | 70.0% | 1 |  |
| adminActionState | INTEGER | 92.3% | 1 |  |
| threeJudgeFdc | INTEGER | 0.2% | 0 |  |
| caseOrigin | INTEGER | 3.4% | 1 |  |
| caseOriginState | INTEGER | 73.6% | 1 |  |
| caseSource | INTEGER | 2.1% | 1 |  |
| caseSourceState | INTEGER | 77.9% | 1 |  |
| lcDisagreement | INTEGER | 0.2% | 0 |  |
| certReason | INTEGER | 0.9% | 1 |  |
| lcDisposition | INTEGER | 16.3% | 1 |  |
| lcDispositionDirection | INTEGER | 1.9% | 1 |  |
| declarationUncon | INTEGER | 0.0% | 1 |  |
| caseDisposition | INTEGER | 1.2% | 1 |  |
| caseDispositionUnusual | INTEGER | 0.0% | 0 |  |
| partyWinning | INTEGER | 0.1% | 0 |  |
| precedentAlteration | INTEGER | 0.0% | 0 |  |
| voteUnclear | INTEGER | 0.0% | 0 |  |
| issue | INTEGER | 0.5% | 100010 |  |
| issueArea | INTEGER | 0.5% | 1 | Issue area code; label in codes where variable = 'issueArea' |
| decisionDirection | INTEGER | 0.3% | 1 | 1 conservative, 2 liberal, 3 unspecifiable (codes table) |
| decisionDirectionDissent | INTEGER | 2.9% | 0 |  |
| authorityDecision1 | INTEGER | 0.6% | 1 |  |
| authorityDecision2 | INTEGER | 83.8% | 1 |  |
| lawType | INTEGER | 11.6% | 1 |  |
| lawSupp | INTEGER | 11.6% | 100 |  |
| lawMinor | VARCHAR | 70.7% | (Treaty) Act of August 7, 1882 |  |
| majOpinWriter | INTEGER | 16.0% | 100 |  |
| majOpinAssigner | INTEGER | 2.4% | 100 |  |
| splitVote | INTEGER | 0.0% | 1 |  |
| majVotes | INTEGER | 0.0% | 3 |  |
| minVotes | INTEGER | 0.0% | 0 |  |
| justice | INTEGER | 0.0% | 100 | Justice id; label in codes where variable = 'justice' |
| justiceName | VARCHAR | 0.0% | ACBarrett |  |
| vote | INTEGER | 2.7% | 1 |  |
| opinion | INTEGER | 2.8% | 1 |  |
| direction | INTEGER | 5.6% | 1 |  |
| majority | INTEGER | 3.6% | 1 |  |
| firstAgreement | INTEGER | 85.8% | 0 |  |
| secondAgreement | INTEGER | 97.1% | 0 |  |

## codes

SCDB online code book: the label for every coded value (variable, code, label; justices carry their service dates in extra)

Rows: 2,949

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| variable | VARCHAR | 0.0% | adminAction |  |
| code | VARCHAR | 0.0% | 0 |  |
| label | VARCHAR | 0.0% | 'contract clause' (No Article to be added) |  |
| extra | VARCHAR | 72.1% | Alito, Samuel ( 01/31/2006 - 00/00/0000 ) |  |
