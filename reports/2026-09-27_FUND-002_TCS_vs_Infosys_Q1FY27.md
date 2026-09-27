# FUND-002 — TCS vs Infosys Q1 FY27 Comparison

## Status

**VERIFIED WITH 2 CONFIRMED P2 FINDINGS + 1 CONFIRMED P1 COMPARABILITY FINDING**

## Exact test

> Compare TCS and Infosys on the latest reported quarter using revenue, revenue YoY growth, EBITDA / operating profit, operating margin, PAT, PAT margin and ROE. For every metric, show reporting period, consolidated/standalone basis, unit, and whether the value is reported or derived.

## Independent-source requirement

This test was manually reconciled against **issuer/company sources**, not against Tapetide or another secondary data provider.

### TCS official sources

- TCS Q1 FY27 official result: https://www.tcs.com/who-we-are/newsroom/press-release/tcs-financial-results-q1-fy-2027
- TCS Investor FAQ: https://www.tcs.com/investor-relations/investor-faqs
- TCS Investor Relations: https://www.tcs.com/investor-relations

TCS's official Q1 release is dated **9 July 2026** and reports consolidated IFRS results for the quarter ended 30 June 2026. It gives a 24.0% operating margin and related financial disclosures. citeturn175228search2turn175228search6

### Infosys official sources

- Infosys Q1 FY27 results: https://www.infosys.com/investors/reports-filings/quarterly-results/2026-2027/q1.html
- Infosys Investor Relations: https://www.infosys.com/investors/reports-filings/
- Infosys Annual Reports: https://www.infosys.com/investors/reports-filings/annual-report/annual-reports.html

Infosys's official Q1 page says results for the quarter ended 30 June 2026 were announced on **23 July 2026** and provides standalone and consolidated financial statements, including IFRS INR statements. citeturn175228search8turn175228search7

## Verified core facts

Both companies' latest reported quarter was Q1 FY27 ended 30 June 2026.

### TCS

Tape AI returned revenue ₹72,275 Cr, revenue growth 13.93%, provider-style/derived operating-profit figure ₹18,556 Cr, derived margin 25.67%, PAT ₹13,420 Cr, PAT margin 18.57%, and ROE 45.59% with no exact ROE period stated.

TCS's issuer materials confirm the quarter and consolidated basis. citeturn175228search2turn175228search6

### Infosys

Tape AI returned revenue ₹48,211 Cr, revenue growth 14.03%, ₹11,409 Cr labelled operating profit, derived margin 23.66%, PAT ₹7,775 Cr, PAT margin 16.13%, and ROE 31.59% with no exact ROE period stated.

Infosys's official Q1 page provides the consolidated IFRS INR statements for the quarter. citeturn175228search8

## Confirmed finding #1

### TPQ-TIME-003 — TCS release-date metadata
**Severity: P2**

Tape AI stated **10 Jul 2026**.

TCS official result is dated **9 Jul 2026**. citeturn175228search2

## Confirmed finding #2

### TPQ-TIME-003 — Infosys release-date metadata
**Severity: P2**

Tape AI stated **24 Jul 2026**.

Infosys official results page states the Q1 FY27 results were announced on **23 Jul 2026**. citeturn175228search8

## Confirmed finding #3

### TPQ-RES-001 — Semantic operating-profit mismatch
**Severity: P1**

Tape AI labelled Infosys ₹11,409 Cr as operating profit. Infosys's official consolidated statement identifies ₹11,409 Cr as **segment profit**, while consolidated operating profit is lower after unallocable expenses.

Therefore the derived comparison using TCS ₹18,556 Cr and Infosys ₹11,409 Cr is not a like-for-like operating-profit comparison.

This is a **semantic/comparability defect**, not simply a bad arithmetic result.

## ROE handling

The response correctly warned that ROE was not quarterly and that the period for the current ROE was not stated. That is a **positive uncertainty disclosure**.

We are not classifying ROE as a confirmed defect from this test. A separate ROE-period test is needed.

## Source protocol

For company financials, record the issuer page/document, URL, date checked, and exact line/field reconciled.

For technical indicators, company investor-relations sites are generally not sufficient because RSI/MACD/EMA are computed from market data. Verify raw NSE/BSE price/volume data (or another explicitly named independent market-data source) and recalculate where practical.

For ownership/corporate actions, use issuer disclosures plus exchange filings.

For historical research, record both reporting period and publication/disclosure date to establish what was actually knowable at the requested time.

## Regression tests

- Latest earnings date must match issuer source.
- Comparative metrics must have compatible semantic definitions before peer calculations.
- Segment profit must not be silently labelled consolidated operating profit.
- ROE with unclear period must remain period-uncertain.
- Every cited company number in the final response must be traceable to a named source.

## Evidence

- data/captures/FUND-002_tcs_infosys_q1fy27.json
- reports/2026-09-27_FUND-002_TCS_vs_Infosys_Q1FY27.md

## Interview takeaway

> I manually opened the issuer sources and reconciled the underlying figures before classifying the answer. The key defect was semantic: the system used a real Infosys number but attached the wrong metric meaning to it for the peer comparison. That can produce a misleading comparison even when the raw numbers themselves exist.

## Sources

- TCS Q1 FY27: https://www.tcs.com/who-we-are/newsroom/press-release/tcs-financial-results-q1-fy-2027
- TCS Investor FAQ: https://www.tcs.com/investor-relations/investor-faqs
- TCS Investor Relations: https://www.tcs.com/investor-relations
- Infosys Q1 FY27: https://www.infosys.com/investors/reports-filings/quarterly-results/2026-2027/q1.html
- Infosys Investor Relations: https://www.infosys.com/investors/reports-filings/
- Infosys Annual Reports: https://www.infosys.com/investors/reports-filings/annual-report/annual-reports.html
