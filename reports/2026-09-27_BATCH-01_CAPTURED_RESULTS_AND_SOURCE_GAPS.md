# Batch 01 — Captured Results, Independent Sources & Verification Gaps

**Date:** 27 Sep 2026

## Purpose

This document records the results available before the Tape AI daily limit was reached. A captured result is **not automatically a verified result**. Verification status below follows `docs/SOURCE_VERIFICATION_POLICY.md`.

## Batch status

| Test | Captured | Source status | Current disposition |
|---|---:|---|---|
| FUND-003 | Yes | Partial official-source corroboration | Captured; accounting reconciliation finding identified |
| FUND-004 | Yes | Incomplete independent source trail | Captured; valuation inputs/definitions need source URLs |
| FUND-005 | Yes | Strong TCS annual-report corroboration | Captured; Q1 balance sheet still unavailable |
| TECH-001 | Yes | Market-data source named, URL not supplied | Captured; manual raw-data verification pending |
| TECH-002 | Yes | Market-data source named, URL not supplied | Captured; delivery verification unavailable |
| TECH-003 | Yes | Market-data source named, URL not supplied | Captured; level methodology is judgemental |
| SCR-001 | Yes | Independent verification not completed | Captured; screen is explicitly not market-wide |
| SCR-002 | No | Daily limit | **BLOCKED / PENDING** |
| SCR-003 | No | Daily limit | **BLOCKED / PENDING** |
| OWN-001 | Yes | Secondary figures corroborate, issuer URL not captured | Captured; official filing URL still required |
| OWN-002 | Yes | No pledge event found; official filing URL not captured | Captured; absence cannot be treated as proof of zero pledge |
| EVENT-001 | Yes | Current official release available | Captured; latest-call contamination is a confirmed quality issue |
| PIT-001 | Yes | Official TCS FY25 sources available | Captured; some historical filing dates still need direct evidence |
| PIT-002 | No | Daily limit | **BLOCKED / PENDING** |
| MCP-001 | No | — | Not run |
| SCORE-001 | No | — | Not run |
| ADV-001 | No | — | Not run |
| AI-001 | No | — | Not run |

## FUND-003 — Cash Conversion

### Captured conclusion

Tape AI/Claude concluded cash conversion declined from 100.3% in Q1 FY26 to 93.0% in Q1 FY27.

### Official TCS verification

TCS's Q1 FY27 official result explicitly reports **Net Cash from Operations of US$1.31 billion, equal to 93% of Net Income**. citehttps://www.tcs.com/who-we-are/newsroom/press-release/tcs-financial-results-q1-fy-2027

TCS's Q1 FY26 official result reports **Net Cash from Operations of US$1.5 billion, equal to 100.3% of Net Income**. citehttps://www.tcs.com/who-we-are/newsroom/press-release/tcs-financial-results-q1-fy-2026

### Important reconciliation

The captured answer treated the gap between:
- management net-income basis implied by 19.2% margin
- dataset PAT of ₹13,420 Cr

as unexplained.

TCS's current official Q1 FY27 release states that the displayed net-income/net-margin figures marked with an asterisk **exclude exceptional items**. The detailed filing/PAT basis therefore needs to be kept distinct from management's headline net-income basis.

### QA disposition

**Finding: TPQ-RES-002 (P2) — incomplete accounting reconciliation**

This is not a claim that the 93% ratio is wrong. The ratio is directly supported by TCS. The quality issue is that the answer left the management-vs-PAT gap unresolved even though the source framework provides a plausible and material basis difference.

**Positive behavior:** It warned that rupee CFO was estimated, that management ratios were rounded, and that the $1.5B year-ago CFO had a currency-label problem in the dataset.

### Source

TCS Q1 FY27 official result:
https://www.tcs.com/who-we-are/newsroom/press-release/tcs-financial-results-q1-fy-2027

TCS Q1 FY26 official result:
https://www.tcs.com/who-we-are/newsroom/press-release/tcs-financial-results-q1-fy-2026

---

## FUND-004 — Valuation Comparison

### Captured result

The answer calculated/quoted:
- P/E
- P/B
- EV/EBITDA
- FCF yield

using 25 Sep 2026 prices and FY26/TTM inputs.

### Source quality

The answer itself says most values were derived from a market-data provider, that some provider fields did not reconcile, and that EBITDA's exact period was unstated.

### Independent issuer sources

TCS:
https://www.tcs.com/investor-relations

Infosys:
https://www.infosys.com/investors/reports-filings/

Infosys FY26 annual-report hub:
https://www.infosys.com/investors/reports-filings/annual-report/annual-reports.html

Infosys's official FY26 annual-report site provides consolidated financial statements and financial-data sections. citehttps://www.infosys.com/investors/reports-filings/annual-report/annual-reports/ar-2025-26.html

### QA disposition

**Captured — independent source trail incomplete.**

Do not publish the provider-derived P/E, P/B, EV/EBITDA or FCF-yield figures as "company verified" until the following are manually reconciled:

- price date
- shares used
- TTM profit basis
- book value basis
- EBITDA period/definition
- FCF definition
- cash/investment treatment in EV

The answer correctly recognized these limitations. That is a positive research-quality behavior.

### Interview lesson

A valuation multiple without a clear numerator date, denominator period and metric definition is not fully reproducible.

---

## FUND-005 — Financial Health

### Official TCS source

TCS FY26 Annual Report:
https://www.tcs.com/content/dam/tcs/investor-relations/financial-statements/2025-26/ar/annual-report-2025-2026.pdf

The official consolidated balance sheet reports:
- Cash and cash equivalents ₹6,417 Cr
- Other bank balances ₹6,491 Cr
- Current investments ₹33,770 Cr
- Non-current investments ₹218 Cr
- Total current assets ₹1,35,705 Cr
- Total current liabilities ₹60,914 Cr
- Non-current lease liabilities ₹9,453 Cr
- Current lease liabilities ₹1,830 Cr
- Total equity ₹1,08,478 Cr
- Goodwill ₹9,108 Cr

These figures are independently corroborated by the official annual report. citeturn138454search57

### Q1 FY27 source

TCS's official Q1 FY27 release confirms Q1 operating cash flow and operating metrics but does not provide the full quarterly balance sheet in the captured source set. citeturn138454search0

### QA disposition

**Captured — strong FY26 source verification; Q1 balance-sheet limitation correctly disclosed.**

The answer should continue to distinguish:
- Q1 FY27 P&L/current operating metrics
- FY26 audited balance sheet

This is a good example of temporal separation.

---

## TECH-001 — RSI + MACD + Moving Averages

### Captured result

The answer reports daily TCS indicators as of the 25 Sep 2026 close:
- RSI 32.23
- MACD -58.64
- signal -43.14
- histogram -15.50
- SMA20 2,222.40
- SMA50 2,290.85
- SMA200 2,541.33
- EMA20/50/200 = 2,189.64 / 2,244.39 / 2,507.28

It independently recomputed SMA20 and SMA50 close to the retrieved values.

### Source protocol

The captured answer names "price history and technical scanner" but does not include a public URL or exchange-download reference.

**Issuer website is not the appropriate authoritative source for RSI/MACD/SMA/EMA.**

Manual verification should use raw NSE/BSE OHLCV data or another explicitly named market-data source and reproduce the calculation.

NSE's TCS page confirms TCS is an active listed security and provides market/quote infrastructure. citeturn898121search0

### QA disposition

**Captured — source URL missing.**

Do not call any indicator "company-verified".

---

## TECH-002 — Volume Confirmation

### Captured result

The answer identifies 18 Sep 2026 as the latest >3% anomaly move:
- close-to-close move -3.88%
- volume 6.875M
- 20-day average 2.655M
- volume ratio 2.59x

### QA disposition

The methodology is reproducible from OHLCV, but:
- the raw source URL was not preserved
- delivery percentage was not retrieved
- trigger/news was not independently verified

The answer correctly says volume confirmation does **not** prove the cause of the move.

**Status: captured; independent source trail incomplete.**

---

## TECH-003 — Support / Resistance

### Captured result

The answer identifies S1/S2 and R1-R4 zones from retrieved daily OHLCV and explicitly states the zones are its own grouping/judgement rather than direct tool output.

### QA disposition

**Good tester behavior:** source-vs-judgement separation is explicit.

Remaining requirement:
- preserve exact raw-data URL/export
- preserve the calculation/grouping rule
- repeat on a second sample to test reproducibility

**Status: captured; source URL incomplete.**

---

## SCR-001 — Fundamental + Technical Screen

### Captured result

Deepseek returned:
- TCS
- Asian Paints
- Infosys
- Wipro
- Hindustan Unilever

with ROE >15%, Debt/Equity <1 and RSI <40.

### Important limitation

The answer explicitly says:

> "This is NOT a comprehensive market-wide screen"

and instead describes the five names as prominent companies that happen to qualify.

Therefore this is **not evidence that a full NSE/BSE universe screen was successfully executed**.

### QA disposition

**Captured — not independently verified.**

Required next work:
- verify every company on issuer sources for ROE/debt basis
- verify RSI from raw market data
- confirm the screen universe and whether the product actually supports the requested full-universe operation

Do not claim the five returned names are a complete market-wide answer.

---

## SCR-002 / SCR-003

**BLOCKED — Tape AI daily limit**

No result exists.

Do not create findings.

---

## OWN-001 — TCS Shareholding

### Captured result

Jun 2026:
- Promoter 71.77%
- FII 9.06%
- DII 13.47%
- Public 4.92%

The figures are corroborated by multiple secondary datasets, including Jun 2026 shareholding summaries. citeturn898121search1turn898121search4

NSE's current TCS page also displays promoter holding and exchange corporate-announcement infrastructure. citeturn898121search0

TCS's Investor Relations page provides the official filing archive and governance/investor documentation. citeturn505028search5

### QA disposition

**Captured — issuer filing URL not preserved.**

For interview evidence, manually open the actual Jun 2026 exchange/company filing and record the filing URL/date. Secondary confirmation is useful but does not replace the issuer/exchange source trail.

---

## OWN-002 — Promoter Pledge / Release

The captured response correctly avoids claiming that "no result retrieved" means "zero pledge."

It also correctly distinguishes:
- promoter ownership
- pledge
- pledge release
- sale

The response says no pledge event was found in its retrieved sources.

### QA disposition

**Captured — not sufficient to establish zero pledge.**

Next manual verification should open the relevant NSE/BSE encumbrance/shareholding disclosure and record:
- filing URL
- filing date
- pledged %
- event type

This is an excellent negative-evidence test.

---

## EVENT-001 — Latest TCS Earnings Event

### Confirmed quality problem

The answer was asked for the latest Q1 FY27 earnings event but admitted that sections B-D were taken from the **Q1 FY26 call from July 2025**, not the latest Q1 FY27 call.

This is a research-context contamination issue.

### Current official source

TCS's Q1 FY27 official release is dated **9 July 2026** and contains current Q1 FY27 operating metrics and management commentary. citeturn138454search0

TCS's Investor Relations page currently exposes the Q1 FY27 earnings call audio/transcript under the Q1 results area. citeturn505028search5

### QA disposition

**TPQ-TIME-004 / TPQ-AI-004 — P1**

The answer mixed the requested current event with a prior-year event.

The disclosure that it had done so is good transparency, but the answer still fails the requested "latest earnings event" requirement.

**Regression requirement:** A latest-event query must constrain the result to the latest period/event and reject or clearly isolate older conference calls.

---

## PIT-001 — Historical Research

### Captured conclusion

The response claims that, as of 30 June 2025, the latest published TCS financial results covered the quarter/year ended 31 March 2025, with Q4/FY25 results declared 10 Apr 2025, while Q1 FY26 results had not yet been published.

### Official sources

TCS's official Q4/FY25 result is dated **10 Apr 2025**, covering the quarter and full year ending 31 Mar 2025. citeturn505028search0turn505028search34

TCS's official investor calendar lists **10 Jul 2025** as the Q1 FY26 earnings release date, supporting the historical-cutoff conclusion that the June 2025 quarter results were not yet available on 30 Jun 2025. citeturn505028search4

TCS's official Q1 FY26 schedule also lists its earnings conference call for 10 Jul 2025. citeturn505028search35

### QA disposition

**Captured — largely corroborated by official issuer sources.**

Remaining caveat:
- exact Mar 2025 shareholding filing/broadcast date was not preserved, so that specific claim remains unverified.

The answer correctly warns that later restatements can affect historical point-in-time reconstruction.

---

## PIT-002

**BLOCKED — Tape AI daily limit**

No result exists.

---

## Remaining unrun tests

These remain **PENDING**, not failed:

- MCP-001
- SCORE-001
- ADV-001
- AI-001

They should be run only after the daily limit resets.

## Batch lessons

The first batch has now demonstrated several different QA classes:

1. **Metadata error** — wrong earnings-release date.
2. **Semantic metric mismatch** — segment profit presented as operating profit.
3. **Accounting reconciliation gap** — management net-income basis not fully reconciled with PAT.
4. **Research-context contamination** — current-event question answered partly from the prior-year call.
5. **Coverage limitation** — screener explicitly not market-wide.
6. **Source-trace weakness** — several calculations lacked a preserved independent URL.
7. **Good uncertainty behavior** — several answers explicitly disclosed missing data or unclear periods.

## Rule for the next batch

No result will be labelled **VERIFIED** until the report contains the independent source organization, URL, date checked, exact field reconciled, and verification result.
