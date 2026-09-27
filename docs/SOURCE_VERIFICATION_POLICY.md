# Source Verification Policy

## Purpose

The Tape AI Power User project tests AI-assisted research against independent evidence. A test is not considered verified merely because the Tape AI answer is plausible.

## Source hierarchy

### Tier 1 — Issuer / company source

Use the company's own Investor Relations site whenever the fact is company-reported:

- quarterly results
- annual reports
- financial statements
- investor presentations
- earnings-call materials
- corporate announcements
- shareholding disclosures
- governance disclosures

Examples:

- TCS Investor Relations: https://www.tcs.com/investor-relations
- Infosys Investor Relations: https://www.infosys.com/investors/reports-filings/

### Tier 2 — Exchange source

Use NSE/BSE to independently confirm:

- exchange-stamped corporate filings
- shareholding pattern
- corporate actions
- security identifiers
- market data where applicable

Examples:

- NSE corporate filings/actions: https://www.nseindia.com/companies-listing/corporate-filings-actions
- NSE shareholding patterns: https://www.nseindia.com/companies-listing/corporate-filings-shareholding-pattern

### Tier 3 — Regulatory source

Use SEBI for regulatory definitions and filings where relevant:

https://www.sebi.gov.in/curation/corporate_filings.html

### Tier 4 — Raw market data / independent calculation

Use raw exchange OHLCV/market data for computed technical indicators such as:

- RSI
- MACD
- SMA/EMA
- Bollinger Bands
- ATR
- volume statistics

The issuer website normally does not publish these computed indicators. The correct QA approach is to verify the underlying price/volume observations and recalculate where practical.

## Tapetide is the system under test

Do **not** use Tapetide itself as the independent verification source when evaluating Tape AI/Tapetide outputs.

Tapetide output:
> System under test

Issuer / NSE / BSE / SEBI / independent calculation:
> Verification evidence

## Required evidence fields

Every completed test must record:

- test ID
- exact prompt
- exact Tape AI response or relevant excerpt
- observation timestamp in IST
- company name
- NSE symbol / BSE code / ISIN when relevant
- reporting period or as-of date
- source type
- source organization
- exact URL
- date checked
- exact line/figure reconciled
- verification result: PASS / MISMATCH / NOT VERIFIABLE
- TPQ code if a failure exists
- severity
- confidence
- recommended fix
- regression test

## For comparisons

For every peer comparison, independently verify **each company's** material data.

Do not verify Company A and assume Company B is equivalent.

Also verify that the metric definitions are semantically compatible.

Example:

> Segment profit vs consolidated operating profit

is not a like-for-like comparison even if both numbers are genuine.

## For derived values

Record:

1. source inputs
2. formula
3. resulting value
4. whether the issuer reports the metric directly

Example:

> PAT margin = PAT / revenue

A derived result should never be labelled as directly reported unless the issuer actually reports it.

## For historical / point-in-time research

Record both:

- period end date
- publication/disclosure date

A later publication cannot be treated as information available at an earlier historical cutoff without evidence that the information was already public.

## Verification threshold

- **PASS:** Material claims reconcile and definitions are compatible.
- **MISMATCH:** Independent source contradicts the AI output.
- **NOT VERIFIABLE:** The source/data needed to confirm the claim is unavailable or ambiguous.
- **OBSERVATION:** A potential usability or methodology issue exists but is not sufficiently evidenced to call a defect.

## Interview rule

Never say:

> “I found an AI hallucination.”

until you have independently verified the claimed fact.

Prefer:

> “The Tape AI response conflicted with the issuer source on X. Here is the source, date, exact line and impact.”

That demonstrates disciplined research rather than subjective criticism.
