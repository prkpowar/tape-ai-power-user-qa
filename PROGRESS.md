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
**Status: VERIFIED — 2 P2 findings**

Observed:
- Q1 FY27, quarter ended 30 Jun 2026
- Revenue ₹72,275 Cr
- Derived EBITDA/operating-profit proxy ₹18,556 Cr
- PAT/profit for period ₹13,420 Cr
- Basic/diluted EPS ₹36.90
- Tape AI reported data refresh at 27 Sep 2026 07:47 IST

Verification:
- TCS official investor calendar shows Q1 FY27 earnings release on 09 Jul 2026.
- TCS official Q1 FY27 release is dated 09 Jul 2026 and identifies the quarter ending 30 Jun 2026 as consolidated IFRS results.
- Detailed Q1 filing data supports revenue ₹72,275 Cr, profit for period ₹13,420 Cr and EPS ₹36.90.

Findings:
- **TPQ-TIME-003 (P2):** Tape AI said results were declared on 10 Jul 2026. The issuer calendar/release show 09 Jul 2026.
- **TPQ-CALC-007 / TPQ-UX-005 (P2):** ₹18,556 Cr is useful as a derived operating-profit/EBITDA proxy, but the answer should more clearly distinguish a derived figure from TCS's separately reported operating-margin presentation.

Positive behavior:
- Reporting period and units shown.
- Reported vs estimated status distinguished.
- Derived EBITDA was disclosed as derived.
- Single-source caveat disclosed.
- Data refresh timestamp disclosed.

Evidence:
- `reports/2026-09-27_FUND-001_TCS_Q1FY27.md`
- `data/captures/FUND-001_tcs_q1fy27.json`

### Next test
**FUND-002 — TCS vs Infosys comparison**
