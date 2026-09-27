# Tapetide Score Methodology Audit Checklist

This is an independent audit checklist based on the public Tapetide Score concept and public product documentation. It is not a claim about internal implementation details that are not publicly exposed.

## 1. Determinism

Question:

> If the same frozen inputs and formula version are used twice, is the result identical?

Test:

- capture all inputs
- run twice
- compare pillar and final score

Failure:

TPQ-SCORE-001

## 2. Pillar reconciliation

The current public Tapetide Score product presents six pillar dimensions:

- Quality
- Valuation
- Growth
- Financial Health
- Momentum
- Ownership

Test whether the displayed final score can be reconciled to its published methodology and metadata.

## 3. Sector applicability

Ask:

> Are all metrics economically meaningful for banks, NBFCs and other financial companies?

A ratio can be mathematically calculable but economically inappropriate.

Example:

Using an industrial cash-flow or enterprise-value metric blindly for a bank can create a false sense of precision.

## 4. Negative and unstable ratios

Test:

- negative earnings
- zero/near-zero denominators
- negative book value
- extreme P/E
- extreme P/B

Expected principle:

Do not transform a mathematically unstable value into a seemingly precise quality signal without an explicit rule.

## 5. Missing data

Test whether missing data is distinguished from poor performance.

Example:

A company with unavailable FCF data should not automatically be interpreted as having bad FCF.

## 6. Governance controls

Check whether material governance signals can be hidden by strong financial metrics.

Document:

- the underlying governance event
- event date
- classification
- any multiplier/cap behavior visible in the product

## 7. Versioning

A deterministic score is only reproducible when the formula/reference version and inputs are known.

Ask:

> Can another analyst reproduce the score from the published specification and the same inputs?

## 8. Historical caveats

Do not assume that an historical displayed score automatically represents an exact point-in-time backtest. Verify what data was actually known at the historical date.

## 9. Factor validation questions

When evaluating a proposed factor:

- What is the exact definition?
- What is the direction of the signal?
- Is the relationship cross-sectional and date-specific?
- Are observations independent?
- Was there a holdout/out-of-sample test?
- How correlated is the factor with existing factors?
- Does residual information remain after controlling for existing factors?
- Is the effect concentrated in one sector or market-cap bucket?

## 10. Interview phrasing

Say:

> I would not argue that a factor belongs in the score because it sounds economically intuitive. I would define it precisely, test it cross-sectionally, control for overlap with existing factors, validate it out of sample where possible, and document limitations.
