# Tape AI Live Question Queue

**Verification standard:** Every completed test must record (1) exact Tape AI prompt/response, (2) observation timestamp, (3) company/identifier, (4) reporting period/as-of date, (5) **independent source checked**, (6) source URL, (7) exact field/line reconciled, (8) result, (9) TPQ code if any, (10) severity, (11) recommended fix, and (12) regression test.

**Source hierarchy:** issuer/company Investor Relations first for company-reported financials, earnings, presentations and disclosures; NSE/BSE corporate filings for exchange-stamped confirmation/shareholding/corporate actions; raw exchange price/volume or independently recalculated indicators for technicals; SEBI for regulatory definitions. Tapetide/MCP is the system under test, not the independent verification source.

| ID | Area | Question | Status |
|---|---|---|---|
| FUND-001 | Fundamentals | Latest TCS quarterly revenue, EBITDA/operating profit, PAT, EPS with period/units | VERIFIED — 1 P2 finding |
| FUND-002 | Fundamentals | TCS vs Infosys Q1 FY27 revenue, growth, operating profit, margin, PAT, PAT margin, ROE | VERIFIED — 2 P2 + 1 P1 findings |
| FUND-003 | Fundamentals | TCS latest-quarter cash conversion using CFO/PAT and year-ago comparison | CAPTURED — official TCS corroboration; applicant source-check record still needed |
| FUND-004 | Valuation | Compare TCS and Infosys on P/E, P/B, EV/EBITDA and FCF yield; show definition, date, source and whether reported/derived | CAPTURED — source trail incomplete |
| FUND-005 | Financial health | Identify TCS balance-sheet risks from latest quarter/year: debt, cash, interest, working capital | CAPTURED — official FY26 annual-report corroboration; Q1 balance-sheet limit disclosed |
| TECH-001 | Technicals | Explain TCS current RSI, MACD and 20/50/200 MA structure with observation time | CAPTURED — market-data source URL still needed |
| TECH-002 | Technicals | Does recent TCS price movement have volume/delivery confirmation? | CAPTURED — market-data source URL and delivery evidence needed |
| TECH-003 | Technicals | Identify TCS support/resistance and show the exact price history used | CAPTURED — market-data source URL needed |
| SCR-001 | Screener | Find NSE/BSE stocks with ROE > 15%, Debt/Equity < 1 and RSI < 40 | CAPTURED — not market-wide; all returned names need manual verification |
| SCR-002 | Screener | Verify every SCR-001 result independently and identify any false positive/false negative | BLOCKED — Tape AI daily limit |
| SCR-003 | Screener | Test pagination/universe completeness on a screen | BLOCKED — Tape AI daily limit |
| OWN-001 | Ownership | TCS latest promoter/FII/DII/public ownership and quarterly change | CAPTURED — secondary corroboration; official filing URL still needed |
| OWN-002 | Governance | TCS promoter pledge/release events and date; distinguish pledge, release and sale | CAPTURED — absence not proof of zero; official filing URL still needed |
| EVENT-001 | Events | Summarize TCS latest earnings event: facts, guidance, risks, and interpretation | CAPTURED — P1 context-contamination issue |
| PIT-001 | Historical | What information about TCS was available as of 30 Jun 2025? | CAPTURED — largely corroborated by official TCS sources; shareholding filing date gap remains |
| PIT-002 | Historical | Answer using only information published on/before 30 Jun 2025 | BLOCKED — Tape AI daily limit |
| MCP-001 | MCP | Test whether a multi-constraint research question resolves to correct tool(s)/parameters | PENDING — not run |
| SCORE-001 | Tapetide Score | Explain current score, pillars, coverage and eligibility/limitations | PENDING — not run |
| ADV-001 | AI reasoning | Is this company fundamentally strong? Define criteria before answering | PENDING — not run |
| AI-001 | AI reasoning | Give source/period for every financial number and identify unverifiable claims | PENDING — not run |

## Applicant manual-source checklist

Before calling a captured test "VERIFIED" for portfolio purposes, manually open the independent source and record the exact page/document and field reconciled in the test report.

## Official source starting points

### TCS
- Investor Relations: https://www.tcs.com/investor-relations
- Q1 FY27 result: https://www.tcs.com/who-we-are/newsroom/press-release/tcs-financial-results-q1-fy-2027
- FY25 result: https://www.tcs.com/who-we-are/newsroom/press-release/tcs-financial-results-q4-fy-2025
- Investor calendar: https://www.tcs.com/investor-relations/calendar
- FY26 Annual Report: https://www.tcs.com/content/dam/tcs/investor-relations/financial-statements/2025-26/ar/annual-report-2025-2026.pdf

### Infosys
- Q1 FY27 results: https://www.infosys.com/investors/reports-filings/quarterly-results/2026-2027/q1.html
- Investor Relations: https://www.infosys.com/investors/reports-filings/
- Annual reports: https://www.infosys.com/investors/reports-filings/annual-report/annual-reports.html

### Exchange/regulatory
- NSE corporate filings/actions: https://www.nseindia.com/companies-listing/corporate-filings-actions
- NSE shareholding: https://www.nseindia.com/companies-listing/corporate-filings-shareholding-pattern
- SEBI corporate filings: https://www.sebi.gov.in/curation/corporate_filings.html

### Tapetide
- MCP: https://tapetide.com/mcp
- MCP server: https://mcp.tapetide.com/
- Stock Research Analyst application: https://career.tapetide.com/stock-research-analyst
