# Tape AI Power User QA — Progress Log

This file is updated as research questions are added, executed, verified, and converted into regression tests.

## Stage 0 — Framework initialized
- QA taxonomy created
- 20 core test cases defined
- Validator and pytest suite added
- MCP testing guide added
- Tapetide Score audit added
- Interview demo added

## Stage 1 — Live Tape AI testing

### FUND-001 — TCS latest financial snapshot
**Status: VERIFIED — 1 confirmed P2 finding + 1 observation-only UX opportunity**

Observed:
- Q1 FY27, quarter ended 30 Jun 2026
- Revenue ₹72,275 Cr
- Derived EBITDA/operating-profit proxy ₹18,556 Cr
- PAT/profit for period ₹13,420 Cr
- Basic/diluted EPS ₹36.90
- Tape AI reported data refresh at 27 Sep 2026 07:47 IST

Independent verification:
- TCS official investor calendar: Q1 FY27 earnings release 09 Jul 2026.
- TCS official Q1 FY27 release: 09 Jul 2026, consolidated IFRS result for quarter ended 30 Jun 2026.
- Detailed filing: revenue ₹72,275 Cr; profit for period ₹13,420 Cr; EPS ₹36.90.

Confirmed finding:
- **TPQ-TIME-003 (P2):** Tape AI stated 10 Jul 2026 as the result-declaration date; issuer materials show 09 Jul 2026.

Observation, not defect:
- Tape AI already disclosed that ₹18,556 Cr EBITDA was derived because TCS does not publish a line called EBITDA. We will not classify this as a false positive. It can still be evaluated as a UX improvement in later repeated tests.

Positive behavior:
- Reporting period and units shown.
- Consolidated basis shown.
- Derived metric disclosed as derived.
- Single-source caveat disclosed.
- Data-refresh timestamp disclosed.

Evidence:
- reports/2026-09-27_FUND-001_TCS_Q1FY27.md
- data/captures/FUND-001_tcs_q1fy27.json
- regressions/FUND-001.md

### Next test
**FUND-002 — TCS vs Infosys comparison**
