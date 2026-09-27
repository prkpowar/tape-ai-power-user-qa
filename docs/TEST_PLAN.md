# Power User Test Plan

## 1. Test objective

Evaluate whether an AI-assisted Indian-equity research workflow is:

- factually correct
- financially coherent
- period-consistent
- source-aware
- tool-correct
- point-in-time safe where historical analysis requires it
- transparent about uncertainty
- usable by a human analyst
- reproducible by another researcher

## 2. Golden rule

Never mark an answer as correct solely because it sounds plausible.

Use the sequence:

**Question -> expected evidence -> observation -> verification -> conclusion**

## 3. Test layers

### Layer A: Retrieval

Can the system find the right company and dataset?

### Layer B: Data

Are the raw values correct, complete and appropriately dated?

### Layer C: Calculation

Are ratios, returns, changes and comparisons mathematically correct?

### Layer D: Interpretation

Does the conclusion logically follow from the evidence?

### Layer E: Communication

Does the user see the period, units, uncertainty and relevant caveats?

### Layer F: Product behavior

Can another researcher reproduce the result and understand why the system reached it?

## 4. Core test matrix

| Area | Minimum tests | Main risks |
|---|---:|---|
| Entity resolution | 3 | wrong company, old symbol, ambiguity |
| Financials | 4 | period, units, standalone/consolidated |
| Ratios | 4 | formula, denominator, sign, rounding |
| Technicals | 3 | observation time, calculation, interpretation |
| Screening | 3 | filter leakage, pagination, missing values |
| Ownership/governance | 2 | event classification, dates |
| Historical/PIT | 4 | look-ahead, survivorship, adjustments |
| Tapetide Score | 4 | pillars, confidence, caps, version |
| MCP | 5 | tool selection, arguments, auth, rate limits |
| AI reasoning | 5 | hallucination, unsupported inference, overconfidence |

## 5. Positive testing

Use normal questions that a researcher would ask:

- latest company financials
- compare two companies
- find stocks matching financial conditions
- explain a technical setup
- summarize earnings calls
- investigate ownership changes

## 6. Negative/adversarial testing

Deliberately create cases where weak systems often fail:

- ambiguous company names
- renamed stocks
- mixed FY/Q periods
- negative earnings
- near-zero denominators
- missing data
- corporate actions around a price jump
- historical questions requiring point-in-time information
- financial-sector companies with industrial ratios
- contradictory signals
- requests that imply investment advice

## 7. Acceptance criteria

A research response passes when:

1. The entity is correct.
2. The relevant period/date is explicit.
3. Values are internally consistent.
4. Calculations are reproducible.
5. Claims are supported by retrieved evidence.
6. The response distinguishes facts from interpretation.
7. Material uncertainty is shown.
8. The answer does not silently mix incomparable data.
9. Historical answers do not introduce later information without disclosure.
10. Product behavior is stable under a repeated query.

## 8. Regression rule

Every P0/P1 issue gets a regression test. A fix is not complete until the original failure is reproduced as a test and passes after the change.
