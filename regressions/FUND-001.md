# Regression Specification — FUND-001

## Confirmed regression

### REG-001 — Earnings release date provenance

**Given:** A company has an issuer investor calendar and an official result-release page.

**When:** The user asks for the latest earnings release date.

**Then:** The answer should use the issuer's official release date and distinguish it from:

- period end date
- filing/publication timestamp
- data refresh timestamp

**Failure code:** TPQ-TIME-003

## Observation-only UX test

### UX-001 — Derived metric transparency

Tape AI explicitly disclosed that its ₹18,556 Cr EBITDA figure was derived because TCS does not publish a line called EBITDA.

That is currently classified as **PASS / good transparency behavior**.

Future repeated tests should check whether users could still confuse:

- derived EBITDA/operating-profit proxy
- issuer-reported operating margin

No defect is recorded from FUND-001 for this item.

## Evidence

- reports/2026-09-27_FUND-001_TCS_Q1FY27.md
- data/captures/FUND-001_tcs_q1fy27.json

## Status

REG-001 documented. Future live run required to execute the regression.
