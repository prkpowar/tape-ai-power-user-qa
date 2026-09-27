# Tape AI Live Question Queue

**Verification standard:** Every completed test must record (1) exact Tape AI prompt/response, (2) observation timestamp, (3) company/identifier, (4) reporting period/as-of date, (5) **independent source checked**, (6) source URL, (7) exact field/line reconciled, (8) result, (9) TPQ code if any, (10) severity, (11) recommended fix, and (12) regression test.

**Source hierarchy:** issuer/company Investor Relations first for company-reported financials, earnings, presentations and disclosures; NSE/BSE corporate filings for exchange-stamped confirmation/shareholding/corporate actions; raw exchange price/volume or independently recalculated indicators for technicals; SEBI for regulatory definitions. Tapetide/MCP is the system under test, not the independent verification source.

| ID | Area | Question | Required independent verification | Status |
|---|---|---|---|---|
| FUND-001 | Fundamentals | Latest TCS quarterly revenue, EBITDA/operating profit, PAT, EPS with period/units | TCS Q1 FY27 official release + filing | VERIFIED — 1 P2 |
| FUND-002 | Fundamentals | TCS vs Infosys Q1 FY27 revenue, growth, operating profit, margin, PAT, PAT margin, ROE | TCS IR + Infosys IR / official filings | VERIFIED — 2 P2 + 1 P1 |
| FUND-003 | Fundamentals | TCS latest-quarter cash conversion using CFO/PAT and year-ago comparison | TCS Q1 FY27 release + detailed financial statements | PENDING |
| FUND-004 | Valuation | Compare TCS and Infosys on P/E, P/B, EV/EBITDA and FCF yield; show definition, date, source and whether reported/derived | TCS/Infosys IR for shares/financials; cross-check calculation | PENDING |
| FUND-005 | Financial health | Identify TCS balance-sheet risks from latest quarter/year: debt, cash, interest, working capital | TCS Q1 FY27 filing + FY26 annual report | PENDING |
| TECH-001 | Technicals | Explain TCS current RSI, MACD, 20/50/200 MA structure with observation time | Raw NSE/BSE price history or independently recalculated indicators; issuer site is not sufficient for computed indicators | PENDING |
| TECH-002 | Technicals | Does recent TCS price movement have volume/delivery confirmation? | NSE/BSE raw market data / delivery data | PENDING |
| TECH-003 | Technicals | Identify TCS support/resistance and show the exact price history used | NSE/BSE price history + reproducible calculation | PENDING |
| SCR-001 | Screener | Find up to 5 NSE/BSE stocks with ROE >15%, Debt/Equity <1 and RSI <40; show every filter value | For every returned company: issuer IR/annual or quarterly data + raw price source for RSI | PENDING |
| SCR-002 | Screener | Verify every SCR-001 result independently and identify any false positive/false negative | Issuer IR + raw market data | PENDING |
| SCR-003 | Screener | Test pagination/universe completeness on a screen; repeat with page/cursor changes | Tapetide result set + independent spot checks | PENDING |
| OWN-001 | Ownership | TCS latest promoter/FII/DII/public ownership and quarterly change | TCS investor disclosure + NSE/BSE shareholding filing | PENDING |
| OWN-002 | Governance | TCS promoter pledge/release events and date; distinguish pledge, release and sale | TCS disclosures + NSE/BSE/SEBI filing | PENDING |
| EVENT-001 | Events | Summarize TCS latest earnings event: facts, guidance, risks, and interpretation | TCS official result release + investor presentation/concall transcript | PENDING |
| PIT-001 | Historical | What information about TCS was available as of 30 Jun 2025? Separate period end vs publication date | TCS IR archive/annual & quarterly reports + exchange filing dates | PENDING |
| PIT-002 | Historical | Answer using only information published on/before 30 Jun 2025; explicitly flag anything unavailable | TCS official archived disclosures + exchange timestamps | PENDING |
| MCP-001 | MCP | Use a multi-constraint research request and inspect whether the correct tool(s), parameters and completeness are used | Tapetide MCP tool catalogue + raw tool behavior; validate returned company data independently | PENDING |
| SCORE-001 | Score | Explain TCS Tapetide Score, six pillars, confidence, coverage and governance flags; do not turn it into a buy/sell instruction | Tapetide Score public methodology + product output | PENDING |
| ADV-001 | AI reasoning | “Is TCS fundamentally strong?” Require criteria, evidence, uncertainty and no unsupported conclusion | TCS IR/annual report + official filings | PENDING |
| AI-001 | AI quality | Ask Tape AI to provide source/period for every financial number and identify unverifiable claims | Manually open the cited issuer sources and reconcile each number | PENDING |

## Official source starting points

### TCS
- Investor FAQs: https://www.tcs.com/investor-relations/investor-faqs
- Quarterly result Q1 FY27: https://www.tcs.com/who-we-are/newsroom/press-release/tcs-financial-results-q1-fy-2027
- Annual Report FY2025-26: https://www.tcs.com/content/dam/tcs/investor-relations/financial-statements/2025-26/ar/annual-report-2025-2026.pdf
- Investor relations: https://www.tcs.com/investor-relations

### Infosys
- Quarterly result Q1 FY27: https://www.infosys.com/investors/reports-filings/quarterly-results/2026-2027/q1.html
- Investor financials: https://www.infosys.com/investors/reports-filings/
- Annual reports: https://www.infosys.com/investors/reports-filings/annual-report/annual-reports.html

### Exchange/regulatory
- NSE corporate filings/shareholding: https://www.nseindia.com/companies-listing/corporate-filings-shareholding-pattern
- NSE corporate filings/actions: https://www.nseindia.com/companies-listing/corporate-filings-actions
- NSE corporate actions: https://www.nseindia.com/static/investor-relations/corporate-actions
- SEBI corporate-filings directory: https://www.sebi.gov.in/curation/corporate_filings.html

### Tapetide
- MCP/tool reference: https://tapetide.com/mcp
- MCP server reference: https://mcp.tapetide.com/
- Careers/application: https://career.tapetide.com/stock-research-analyst

**Important:** Technical indicators such as RSI/MACD/EMA are calculated values. A company investor-relations page generally will not be the authoritative source for the computed indicator. For those tests, verify the underlying OHLCV data from NSE/BSE (or another independently identified market-data source) and recalculate the indicator where practical.