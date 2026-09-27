# Tape AI Power User QA — Frozen Progress

**Freeze date: 27 September 2026**

This repository is now a **frozen portfolio/application snapshot**. No additional live Tape AI tests are planned for this submission.

## Final test status

| Status | Count | Meaning |
|---|---:|---|
| Captured / completed | 13 | Tape AI response was obtained and preserved |
| Blocked | 3 | Live testing stopped because the Tape AI daily limit was reached |
| Not run | 4 | Deliberately left unclaimed; no result was fabricated |
| **Planned** | **20** | Full starter suite |

## Fully verified findings

### FUND-001
**1 confirmed P2 finding**

- **TPQ-TIME-003:** TCS Q1 FY27 result date stated as 10 Jul 2026 vs official TCS date of 09 Jul 2026.

### FUND-002
**2 confirmed P2 + 1 confirmed P1 finding**

- **TPQ-TIME-003:** TCS release date off by one day.
- **TPQ-TIME-003:** Infosys release date off by one day.
- **TPQ-RES-001:** Infosys ₹11,409 Cr was labelled operating profit, but the official consolidated figure is ₹10,163 Cr; ₹11,409 Cr is segment profit.

## Additional captured P1 finding

### EVENT-001

The answer was asked to summarize the latest TCS earnings event but used **Q1 FY26 management commentary** while framing the task around the latest event.

- **TPQ-TIME-004 / TPQ-AI-004:** research-context / period contamination
- **Severity:** P1

The response disclosed the contamination. That disclosure is itself useful evidence of uncertainty handling, but it does not remove the underlying quality issue.

## Captured cases with source/verification gaps

The following were preserved but are **not promoted to fully verified findings** unless the evidence standard is satisfied:

- FUND-003 — official TCS cash-conversion corroboration; accounting-basis reconciliation needs clearer treatment
- FUND-004 — valuation definitions/source trail incomplete
- FUND-005 — FY26 balance-sheet evidence available; full Q1 FY27 balance sheet not captured
- TECH-001 — technical calculation method/caveats captured; raw market-data URL still required
- TECH-002 — price/volume move captured; delivery/source evidence still required
- TECH-003 — support/resistance method captured; raw price-history source still required
- SCR-001 — five names returned, but response explicitly says it was not a comprehensive market-wide screen
- OWN-001 — shareholding figures captured and secondary-corroborated; primary filing URL still required
- OWN-002 — response correctly did not infer zero pledge from missing pledge data; primary filing evidence still required
- PIT-001 — core historical cutoff corroborated by official TCS sources; one filing-date gap remains

## Daily-limit blocked

- SCR-002
- SCR-003
- PIT-002

These are recorded as **blocked**, not failed.

## Not run

- MCP-001
- SCORE-001
- ADV-001
- AI-001

No result is claimed for these cases.

## Evidence standard

Every serious finding should preserve:

1. exact question
2. observation timestamp in IST
3. company/identifier
4. reporting period or as-of date
5. raw returned data
6. independent source
7. exact field/figure reconciled
8. result
9. TPQ code + severity
10. recommended fix
11. regression test idea

## Freeze decision

The live test run stopped for a genuine product-usage limit. Continuing would have required spending more time waiting for/resetting the quota rather than improving the portfolio evidence.

The correct portfolio representation is therefore:

> **Frozen evidence snapshot — transparent about coverage, explicit about limitations, and no fabricated completion.**

See [reports/FINAL_SUBMISSION.md](./reports/FINAL_SUBMISSION.md) for the recruiter-facing summary.
