# Tape AI Power User QA

> **Independent research-quality QA framework for AI-assisted Indian-equity research**

[![Status](https://img.shields.io/badge/status-frozen%20for%20submission-2ea44f)](./reports/FINAL_SUBMISSION.md)
[![Evidence](https://img.shields.io/badge/live%20tests-13%20captured-blue)](./PROGRESS.md)
[![Blocked](https://img.shields.io/badge/daily%20limit-3%20blocked-lightgrey)](./questions/QUESTION_QUEUE.md)

This repository is a **portfolio demonstration for the Stock Research Analyst role at Tapetide**.

It shows how I approach AI-assisted stock research as a power user: not by judging whether an answer *sounds* convincing, but by checking the **company, period, source, data, calculation, reasoning, reproducibility and product behavior**.

## Start here

### 1. [Final Submission Report](./reports/FINAL_SUBMISSION.md)
The recruiter-facing summary: what was tested, what was verified, what failed, what could not be completed, and what the project demonstrates.

### 2. [Five-Minute Interview Demo](./docs/INTERVIEW_DEMO.md)
A guided walkthrough for explaining the project quickly.

### 3. [Test Plan](./docs/TEST_PLAN.md)
The methodology behind the test suite.

### 4. [Live Test Progress](./PROGRESS.md)
The frozen state of the actual Tape AI testing run.

### 5. [20-Case Test Catalog](./test_cases/20_core_cases.yaml)
The original research and QA questions used for the live evaluation.

## What I tested

The framework covers the analyst workflow end to end:

| Area | Examples |
|---|---|
| Fundamentals | quarterly results, cash conversion, financial health |
| Valuation | P/E, P/B, EV/EBITDA, FCF yield, definition matching |
| Technicals | RSI, MACD, moving averages, price/volume confirmation |
| Screening | multi-condition filters, verification, pagination |
| Ownership & governance | shareholding, promoter pledge/events |
| Earnings & events | facts vs commentary vs interpretation |
| Point-in-time research | publication-date cutoffs and look-ahead risk |
| MCP / tools | tool selection, arguments, limits and reproducibility |
| Tapetide Score | pillars, coverage, governance controls and methodology |
| AI quality | hallucination, unsupported inference, uncertainty, source traceability |

## My QA model

The core workflow is:

**Question → Expected evidence → Tape AI observation → Independent verification → Failure classification → Severity → Product recommendation → Regression test**

A research answer passes only when the material claims are supportable and the definitions are compatible.

### Independent verification rule

Tape AI is the **system under test**.

For company-reported facts I prefer:

1. issuer Investor Relations / filings
2. NSE / BSE exchange records
3. SEBI for regulatory definitions
4. raw market data + independent recalculation for technical indicators

This prevents the common mistake of “verifying” an AI answer against the same data source that produced it.

## Frozen live-test result

**Freeze date: 27 September 2026**

- **20** planned core tests
- **13** captured/completed before the live daily limit was reached
- **3** blocked by the Tape AI daily limit
- **4** not run
- **2** tests fully independently verified with concrete findings
- **1** additional captured test contains a documented P1 research-context contamination finding
- Remaining captured cases are deliberately marked with source gaps or verification requirements rather than being overstated as verified

The incomplete cases are **not hidden**. The final report explains exactly why they remain incomplete.

## Confirmed findings

### FUND-001 — release-date metadata mismatch
Tape AI stated TCS's Q1 FY27 result date as **10 Jul 2026**; the official TCS result/calendar shows **09 Jul 2026**.

**Classification:** TPQ-TIME-003 · P2

### FUND-002 — peer-comparison semantic mismatch
Tape AI labelled Infosys **₹11,409 Cr** as operating profit. The official Infosys consolidated statement identifies that amount as **segment profit**, while consolidated operating profit is **₹10,163 Cr**.

**Classification:** TPQ-RES-001 · P1

The same test also contained one-day release-date mismatches for TCS and Infosys.

### EVENT-001 — latest-event context contamination
The response was asked for the latest TCS earnings event but used **Q1 FY26 management commentary** while presenting the task as a latest-event review.

**Classification:** TPQ-TIME-004 / TPQ-AI-004 · P1

The important QA behavior was that the contamination was explicitly disclosed rather than silently presented as current.

## Engineering bridge

This is not only a checklist. Confirmed observations are designed to become machine-checkable regression cases.

- `src/tapetide_qa/validator.py` — deterministic validation logic
- `tests/` — framework tests
- `taxonomy/error_codes.json` — tester-defined TPQ taxonomy
- `regressions/` — concrete regression evidence
- `reports/` — candidate-facing research audits

The **TPQ-*** codes are my own tester-defined taxonomy. They are not claimed to be Tapetide's internal production error codes.

## Why this is relevant to the role

My software-engineering background supports the **reproduction, validation, debugging and regression** side of the work.

My stock-market development and research work supports the **financial-data, market-context and metric-definition** side.

The project is meant to demonstrate the combination: **market understanding + technical QA discipline + AI product judgment**.

## Review path for a recruiter

Open this repository in this order:

**[Final Submission Report](./reports/FINAL_SUBMISSION.md) → [Verified findings](./reports/) → [Test Plan](./docs/TEST_PLAN.md) → [Error Catalog](./docs/ERROR_CATALOG.md) → [Validator](./src/tapetide_qa/validator.py)**

That path is intentionally short; the rest of the repository is supporting evidence.

## Important scope note

This is an **independent portfolio/interview project**, not an internal Tapetide audit and not a claim of exhaustive product coverage.

Because the live product testing run hit its daily usage limit, the repository is frozen at the evidence actually obtained on 27 September 2026. No missing result is presented as tested.

## Source links

- [Tapetide Stock Research Analyst role](https://career.tapetide.com/stock-research-analyst)
- [Tapetide MCP](https://tapetide.com/mcp)
- [Tapetide MCP reference](https://mcp.tapetide.com/)
- [Tapetide Score public repository](https://github.com/Tapetide-hq/tapetide-score)
- [Model Context Protocol](https://modelcontextprotocol.io/)

---

**Submission note:** This repository is intentionally frozen as a transparent snapshot of the live test run. The goal is to demonstrate **how I test and reason about AI-assisted research**, not to maximize the number of test cases completed.
