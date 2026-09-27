# Final Submission Report — Tape AI Power User QA

**Applicant:** Pratik Powar  
**Project:** `prkpowar/tape-ai-power-user-qa`  
**Freeze date:** 27 September 2026  
**Purpose:** Portfolio evidence for the Tapetide Stock Research Analyst application

## Executive summary

I built an independent QA framework for evaluating AI-assisted Indian-equity research.

The framework treats a stock-research answer as a chain of claims that must be checked across:

**Entity → Period → Source → Raw data → Calculation → Interpretation → Tool behavior → Reproducibility**

The live run used a 20-case starter suite. Testing was stopped when the Tape AI daily usage limit was reached.

### Final coverage

- **20** planned tests
- **13** captured/completed
- **3** blocked by the product daily limit
- **4** not run
- **5 confirmed issues** across three tests
- additional captured observations preserved with explicit verification gaps

This is a deliberate **freeze**, not an attempt to make the project look artificially complete.

---

## What the live evidence demonstrated

### 1. Metadata errors can matter

**FUND-001** found a one-day mismatch in the reported TCS earnings-release date.

- Tape AI: 10 Jul 2026
- Official TCS result/calendar: 09 Jul 2026
- TPQ: **TPQ-TIME-003**
- Severity: **P2**

This is a useful example of why an analyst should verify not just the financial number, but also the **publication metadata** around it.

### 2. A real number can still be the wrong comparison

**FUND-002** found that Tape AI labelled Infosys **₹11,409 Cr** as operating profit.

The official Infosys consolidated statement shows:

- **₹11,409 Cr — segment profit**
- **₹10,163 Cr — consolidated operating profit**

That makes the peer comparison semantically non-like-for-like even though the ₹11,409 Cr number itself is genuine.

- TPQ: **TPQ-RES-001**
- Severity: **P1**

The same test also had one-day release-date mismatches for TCS and Infosys.

### 3. “Latest” requires strict context control

**EVENT-001** was asked for the latest TCS earnings event, but parts of the response used **Q1 FY26 management commentary** while the task was framed around the latest event.

- TPQ: **TPQ-TIME-004 / TPQ-AI-004**
- Severity: **P1**

The response explicitly disclosed the context mismatch. For QA purposes, that transparency is positive, but the underlying contamination remains a material research-quality issue.

---

## What I deliberately did not overclaim

Several tests produced useful observations but did not preserve enough independent evidence to call them fully verified.

Examples include:

- technical indicators without a preserved raw market-data URL
- shareholding figures without the primary issuer/exchange filing URL in the capture
- a screener response that explicitly did **not** establish exhaustive market-wide coverage
- financial-health analysis that mixed a FY26 balance sheet with Q1 FY27 earnings context
- historical research where a remaining filing-date gap was still present

Those cases remain visible in the repository with their limitations.

That is intentional: **“captured” is not the same as “verified.”**

---

## Why the daily-limit stop is part of the evidence

The remaining live questions were not completed because the product usage limit was reached.

The repository therefore records:

- what was actually run
- what was actually observed
- what was independently verified
- what remained uncertain
- what was blocked
- what was never run

No missing answer is invented to fill the quota.

For a research/QA role, this is itself an important operating principle: **preserve evidence quality rather than fabricate completeness.**

---

## Engineering implementation

The framework turns qualitative research QA into reproducible structure:

| Component | Purpose |
|---|---|
| `test_cases/20_core_cases.yaml` | starter test catalog |
| `taxonomy/error_codes.json` | tester-defined TPQ taxonomy |
| `docs/TEST_PLAN.md` | test methodology |
| `docs/SOURCE_VERIFICATION_POLICY.md` | evidence hierarchy |
| `src/tapetide_qa/validator.py` | deterministic validation |
| `tests/` | framework tests |
| `regressions/` | regression evidence |
| `reports/` | candidate-facing findings |

The **TPQ-*** codes are tester-defined taxonomy codes for this portfolio project. They are not claimed to be Tapetide internal production error codes.

---

## Five-minute recruiter walkthrough

### 0–1 minute
Open this report and explain the objective:

> I wanted to test whether AI-assisted stock research is correct, reproducible and source-aware — not just fluent.

### 1–2 minutes
Open [FUND-002](./2026-09-27_FUND-002_TCS_vs_Infosys_Q1FY27.md).

Show how a **semantic definition mismatch** can create a bad comparison even when the number is real.

### 2–3 minutes
Open [FUND-001](./2026-09-27_FUND-001_TCS_Q1FY27.md).

Show the difference between:

- what the system said
- what the issuer source says
- the classification
- the regression idea

### 3–4 minutes
Open [TEST_PLAN.md](../docs/TEST_PLAN.md) and [SOURCE_VERIFICATION_POLICY.md](../docs/SOURCE_VERIFICATION_POLICY.md).

Explain the evidence hierarchy and the rule that Tape AI is the **system under test**, not the independent source.

### 4–5 minutes
Open [validator.py](../src/tapetide_qa/validator.py).

Connect the project to software-engineering practice:

> A useful QA finding should become reproducible, testable and capable of surviving a future product change.

---

## What this project says about my working style

I approach AI product QA as a combination of:

**Market research knowledge + data verification + software testing + product judgment**

The goal is not to criticize an AI answer because it feels wrong.

The goal is to be able to say:

> **Here is the exact question. Here is the exact answer. Here is the independent source. Here is the conflicting field. Here is the impact. Here is the severity. Here is the regression test.**

---

## Scope and limitations

This is an independent portfolio project.

It is **not**:

- an internal Tapetide audit
- an exhaustive test of Tapetide
- a claim that every captured observation is a confirmed product defect
- a statement about Tapetide's internal error codes or implementation

The live test snapshot is frozen at the evidence obtained on **27 September 2026**.

## Primary source starting points

### TCS
- Investor Relations: https://www.tcs.com/investor-relations
- Q1 FY27 result: https://www.tcs.com/who-we-are/newsroom/press-release/tcs-financial-results-q1-fy-2027
- Investor calendar: https://www.tcs.com/investor-relations/calendar

### Infosys
- Q1 FY27 results: https://www.infosys.com/investors/reports-filings/quarterly-results/2026-2027/q1.html
- Investor Relations: https://www.infosys.com/investors/reports-filings/

### Tapetide
- Stock Research Analyst role: https://career.tapetide.com/stock-research-analyst
- MCP: https://tapetide.com/mcp
- MCP server: https://mcp.tapetide.com/
- Tapetide Score public repository: https://github.com/Tapetide-hq/tapetide-score

---

## Final status

**FROZEN FOR APPLICATION SUBMISSION**

The repository is ready to be shared as a portfolio evidence snapshot. Further live testing is intentionally out of scope for this frozen version.
