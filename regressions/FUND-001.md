# Regression Specification — FUND-001

## Objective
Prevent recurrence of the two verified issue classes from the TCS Q1 FY27 live test.

## REG-001 — Earnings release date provenance

Given: A company has an issuer investor calendar and result-release page.
When: The user asks for the latest earnings date.
Then: The answer should prefer the issuer's official release date and distinguish it from the data refresh timestamp, filing publication timestamp, and result period end date.

Failure code: TPQ-TIME-003

## REG-002 — Derived metric labeling

Given: The requested metric is not explicitly reported by the issuer.
When: The system derives a value from reported line items.
Then: The answer should explicitly identify it as derived and should not silently equate it with a separately defined management metric.

Failure code: TPQ-CALC-007 / TPQ-UX-005

## Evidence
See reports/2026-09-27_FUND-001_TCS_Q1FY27.md and data/captures/FUND-001_tcs_q1fy27.json

## Status
Regression design recorded. Execution requires a future live product run.