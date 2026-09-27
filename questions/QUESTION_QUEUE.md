# Tape AI Live Question Queue — Frozen

**Freeze date: 27 September 2026**

The live question queue is closed for this application snapshot.

No additional Tape AI questions are required for submission. The remaining cases below are preserved only to show the intended coverage and the exact point where testing stopped.

| ID | Area | Status at freeze |
|---|---|---|
| FUND-001 | Fundamentals | VERIFIED — 1 P2 finding |
| FUND-002 | Fundamentals | VERIFIED — 2 P2 + 1 P1 findings |
| FUND-003 | Fundamentals | CAPTURED — corroborated; reconciliation/source-check gap remains |
| FUND-004 | Valuation | CAPTURED — source trail incomplete |
| FUND-005 | Financial health | CAPTURED — FY26 balance-sheet evidence; Q1 limit disclosed |
| TECH-001 | Technicals | CAPTURED — raw market-data source still needed |
| TECH-002 | Technicals | CAPTURED — delivery/source evidence still needed |
| TECH-003 | Technicals | CAPTURED — raw price-history source still needed |
| SCR-001 | Screener | CAPTURED — not proven market-wide |
| SCR-002 | Screener | BLOCKED — daily limit |
| SCR-003 | Screener | BLOCKED — daily limit |
| OWN-001 | Ownership | CAPTURED — primary filing URL still needed |
| OWN-002 | Governance | CAPTURED — primary pledge/encumbrance evidence still needed |
| EVENT-001 | Events | CAPTURED — P1 context-contamination finding |
| PIT-001 | Historical | CAPTURED — largely corroborated; filing-date gap remains |
| PIT-002 | Historical | BLOCKED — daily limit |
| MCP-001 | MCP | NOT RUN |
| SCORE-001 | Tapetide Score | NOT RUN |
| ADV-001 | AI reasoning | NOT RUN |
| AI-001 | AI reasoning | NOT RUN |

## Verification standard

For every portfolio-quality claim, record:

- exact Tape AI prompt/response
- observation timestamp in IST
- company/identifier
- reporting period or as-of date
- independent source checked
- source URL
- exact field/line reconciled
- PASS / MISMATCH / NOT VERIFIABLE
- TPQ code and severity
- recommended fix
- regression idea

## Why the remaining tests are not run

The live Tape AI daily usage limit was reached. They are **not failures** and they are **not presented as completed**.

The repository is frozen rather than extended beyond the evidence actually obtained.
