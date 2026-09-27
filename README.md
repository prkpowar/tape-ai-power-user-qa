# Tape AI Power User QA Framework

A research-quality testing framework for evaluating AI-assisted Indian-equity research workflows, with a focus on factual accuracy, financial-period consistency, tool/MCP behavior, calculation correctness, point-in-time safety, screeners, Tapetide Score interpretation, governance context, and actionable product feedback.

> **Important:** This repository is an independent testing framework created for portfolio/interview demonstration. The error codes below are tester-defined taxonomy codes unless explicitly marked as a documented Tapetide behavior. They are not claimed to be Tapetide's internal production error codes.

## Why this project exists

Tapetide's public careers page describes the Stock Research Analyst as a power user who evaluates the quality of AI-generated stock analysis. Tapetide's MCP currently exposes research tools for NSE/BSE stocks, including fundamentals, technicals, flows, historical research, Tapetide Score, risk/governance, portfolio and watchlist workflows.

This project demonstrates how to turn that job requirement into a reproducible QA process:

```
Research question
      |
      v
Expected behavior
      |
      v
AI / MCP observation
      |
      v
Independent verification
      |
      v
Failure classification
      |
      v
Severity + impact
      |
      v
Actionable recommendation
      |
      v
Regression test
```

## What is included

This is an independent portfolio/interview project. It contains an 85-code tester-defined error taxonomy, a 20-case starter suite, a local validator, MCP test guidance, a Tapetide Score audit, an interview glossary, and a research runbook. Public Tapetide facts are isolated in `docs/PUBLIC_PRODUCT_FACTS.md` and should be re-checked before an interview.

## Repository map

- `docs/TEST_PLAN.md` - end-to-end power-user testing methodology
- `docs/ERROR_CATALOG.md` - 85 tester-defined error codes with symptoms, checks and possible fixes
- `docs/ERROR_TAXONOMY_GUIDE.md` - how to classify failures and use the taxonomy
- `taxonomy/error_codes.json` - machine-readable taxonomy registry
- `docs/CASE_STUDIES.md` - public methodology/QA lessons from Tapetide Score
- `docs/RESEARCH_RUNBOOK.md` - one end-to-end power-user research session
- `docs/PUBLIC_PRODUCT_FACTS.md` - current public product/application facts
- `docs/BUG_REPORT_TEMPLATE.md` - engineering-ready bug-report format
- `docs/MCP_TESTING.md` - MCP-specific validation strategy
- `docs/TAPETIDE_SCORE_AUDIT.md` - methodology audit questions for deterministic scoring
- `docs/INTERVIEW_GUIDE.md` - interview definitions and explainable examples
- `test_cases/20_core_cases.yaml` - starter test suite
- `examples/sample_capture.json` - example captured research interaction
- `src/tapetide_qa/validator.py` - local deterministic checks on captured observations
- `tests/` - unit tests for the framework itself

## Scope

### Functional quality

- entity resolution
- quotes and timestamps
- financial statements
- ratios and calculations
- screeners
- technical indicators
- market flows
- ownership/governance
- Tapetide Score
- historical / point-in-time research
- portfolio/watchlist workflows

### AI quality

- hallucination
- unsupported inference
- overconfidence
- missing caveats
- conflicting evidence
- period/source ambiguity
- research completeness

### MCP/tool quality

- wrong tool selection
- invalid arguments
- partial results
- schema drift
- authentication and rate limits
- aliases/retired tools
- transport failures

## Severity model

- **P0 Critical:** materially wrong financial information, destructive action, security/privacy issue, or a failure that can fundamentally mislead research.
- **P1 Major:** materially incorrect comparison, calculation, period, entity, screening condition, or historical context that can change a research conclusion.
- **P2 Moderate:** incomplete or misleading presentation with a reasonable workaround.
- **P3 Minor:** cosmetic, wording, discoverability or low-impact usability issue.

## Reproducibility rule

Every serious finding should preserve:

1. exact user question
2. date/time of observation
3. company/symbol/identifier
4. reporting period or observation date
5. tools used, when visible
6. raw returned data or screenshot
7. expected result
8. actual result
9. independent verification source
10. classification + severity
11. proposed fix
12. regression test idea

## Current Tapetide product context

The public Tapetide MCP documentation currently describes approximately 8,200 NSE/BSE stocks, a 326-ratio fundamental screener, 20+ technical indicators, 55 registered tool names including setup/aliases, historical research tools, the Tapetide Score, governance/risk tools, and a free tier of 50 successful calls/day and 1,000/month. Data freshness varies by dataset, and index option chains are described as end-of-day snapshots. The MCP docs also state that the system provides historical research inputs but does not run trading-strategy backtests.

## Usage

This repository does not require a live Tapetide connection to run its local validator. Capture observations manually from the product/MCP and place them into JSON following `examples/sample_capture.json`.

Example:

```bash
python -m tapetide_qa.validator examples/sample_capture.json
```

## Validation

```bash
pytest -q
python scripts/validate_test_catalog.py test_cases/20_core_cases.yaml
```

## Interview positioning

The core message is:

> I evaluate the answer, the data, the reporting period, the tool path, the calculation, the reasoning, and the user's ability to reproduce the result. When something fails, I turn it into a precise bug report and a regression test.

## Sources

- Tapetide careers: https://career.tapetide.com/stock-research-analyst
- Tapetide MCP: https://tapetide.com/mcp
- Tapetide MCP reference: https://mcp.tapetide.com/
- Tapetide Score public repository: https://github.com/Tapetide-hq/tapetide-score
- Model Context Protocol: https://modelcontextprotocol.io/


## Publish

See `docs/GITHUB_PUBLISH.md` for the exact commands to publish this repository under the `prkpowar/tape-ai-power-user-qa` GitHub namespace after authenticating to GitHub. See `docs/TAPE_AI_PROJECT.md` and `docs/QUICKSTART.md` for the project workflow.
```