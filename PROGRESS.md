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

### FUND-001 — TCS latest quarterly snapshot
**Status: VERIFIED — 1 confirmed P2 finding**

Confirmed:
- **TPQ-TIME-003 (P2):** Tape AI stated 10 Jul 2026; TCS issuer materials show 09 Jul 2026.

Positive behavior:
- period, units, consolidated basis, derived metric disclosure, source caveat and refresh timestamp were shown.

Evidence:
- `reports/2026-09-27_FUND-001_TCS_Q1FY27.md`
- `data/captures/FUND-001_tcs_q1fy27.json`
- `regressions/FUND-001.md`

### FUND-002 — TCS vs Infosys Q1 FY27 comparison
**Status: VERIFIED — 2 confirmed P2 findings + 1 confirmed P1 research-comparability finding**

Confirmed:
- **TPQ-TIME-003 (P2):** TCS release date stated as 10 Jul 2026; official date is 09 Jul 2026.
- **TPQ-TIME-003 (P2):** Infosys release date stated as 24 Jul 2026; official date is 23 Jul 2026.
- **TPQ-RES-001 (P1):** Infosys ₹11,409 Cr was labelled operating profit, but official consolidated operating profit is ₹10,163 Cr; ₹11,409 Cr is segment profit before ₹1,246 Cr unallocable expenses. This makes the comparison with TCS's ₹18,556 Cr provider-style operating-profit figure non-like-for-like.

Positive behavior:
- Both companies were correctly placed in Q1 FY27.
- ROE was explicitly flagged as non-quarterly/period-uncertain.
- Tape AI disclosed that some figures were derived.
- Revenue values reconcile to issuer figures.

Evidence:
- `reports/2026-09-27_FUND-002_TCS_vs_Infosys_Q1FY27.md`
- `data/captures/FUND-002_tcs_infosys_q1fy27.json`

### Key lesson from Batch 01
The highest-value failure so far is not arithmetic; it is **semantic metric mismatch**. A response can contain real numbers and still create a misleading peer comparison when the numbers have different definitions.

### Next test
**FUND-003 — TCS cash conversion**
