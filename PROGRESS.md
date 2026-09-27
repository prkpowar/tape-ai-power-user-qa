# Tape AI Power User QA — Progress Log

## Stage 0 — Framework initialized
- QA taxonomy created
- 20-case starter suite defined
- MCP testing guide added
- Tapetide Score audit added
- Interview demo added
- Source Verification Policy added

## Stage 1 — Live Tape AI testing

### FUND-001
**VERIFIED — 1 confirmed P2**

Confirmed defect:
- TPQ-TIME-003: TCS earnings-release date was stated as 10 Jul 2026; official TCS calendar/release show 09 Jul 2026.

Positive behavior:
- period/units/consolidated basis visible
- derived metric disclosed
- refresh time disclosed
- single-source caveat disclosed

### FUND-002
**VERIFIED — 2 confirmed P2 + 1 confirmed P1**

Confirmed defects:
- TPQ-TIME-003: TCS date off by one day.
- TPQ-TIME-003: Infosys date off by one day.
- TPQ-RES-001: Infosys ₹11,409 Cr was labelled operating profit; official consolidated operating profit is ₹10,163 Cr, while ₹11,409 Cr is segment profit. This creates a non-like-for-like peer comparison.

Positive behavior:
- same quarter identified
- ROE period uncertainty disclosed
- derived metrics identified
- several figures independently reconciled

### FUND-003 through PIT-001
**Captured before daily limit; independent-source audit underway**

Detailed batch audit:
- reports/2026-09-27_BATCH-01_CAPTURED_RESULTS_AND_SOURCE_GAPS.md

Notable findings/observations:
- FUND-003: 93% cash-conversion ratio is directly supported by TCS's official Q1 FY27 release; the captured analysis's unresolved net-income-vs-PAT basis difference needs clearer exceptional-item reconciliation.
- FUND-004: valuation calculations contain provider-definition/date limitations; source trail incomplete.
- FUND-005: FY26 balance-sheet figures are corroborated by TCS Annual Report; Q1 FY27 full balance sheet was not in the captured dataset.
- TECH-001/002/003: methodologies are reasonable and caveats are explicit, but raw market-data source URLs were not preserved.
- SCR-001: the response explicitly says the five names are not a comprehensive market-wide screen, so the screen result cannot yet be presented as exhaustive.
- OWN-001: shareholding figures are corroborated by secondary sources, but an issuer/exchange filing URL is still required for portfolio-quality evidence.
- OWN-002: the response correctly refused to infer zero pledge from missing data; official encumbrance source still needs to be recorded.
- EVENT-001: the answer used Q1 FY26 management commentary while being asked for the latest Q1 FY27 event. This is TPQ-TIME-004 / TPQ-AI-004, P1, despite the answer disclosing the contamination.
- PIT-001: the core historical cutoff is corroborated by TCS's official FY25 result and investor calendar; the Mar 2025 shareholding filing date remains a gap.

### Daily-limit blocked
- SCR-002
- SCR-003
- PIT-002

### Not run
- MCP-001
- SCORE-001
- ADV-001
- AI-001

## Next
When the Tape AI daily limit resets, run the three blocked tests first, then the four unrun tests. Do not fabricate missing results.
