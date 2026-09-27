# MCP Testing Guide

## 1. Mental model

```text
User question
    |
    v
Intent extraction
    |
    v
Tool selection
    |
    v
Tool arguments
    |
    v
MCP execution
    |
    v
Raw result
    |
    v
AI interpretation
    |
    v
Final answer
```

A failure at any layer can produce a plausible-looking final answer.

## 2. Tool-selection tests

For every multi-step question, record:

- what data the question requires
- which tools would logically satisfy it
- which tools were actually selected, when visible
- whether independent tools could have been called in parallel
- whether all required datasets were retrieved

## 3. Argument tests

Validate:

- company identifier
- exchange
- date range
- fiscal period
- filter direction
- threshold units
- pagination/cursor
- optional flags

## 4. Result-integrity tests

Check:

- expected row count
- expected fields
- duplicate records
- missing records
- stale observations
- unexpected nulls
- cross-company contamination

## 5. Authentication tests

Test that protected tools:

- reject absent/invalid authentication clearly
- do not expose private data without authentication
- recover after re-authentication

## 6. Rate-limit tests

Tapetide's public MCP docs currently state that the free plan allows 50 successful tool calls per day and 1,000 per month, while protocol traffic, the guide call and failed calls do not consume quota. Batch quotes of up to 20 stocks count as one successful call. Test the product's handling of quota exhaustion rather than treating rate limits as data errors.

## 7. Historical safety tests

Use:

- as-of date
- historical identifiers
- past index membership
- corporate-action adjustments
- observation-status checks

Then verify that the final response does not silently use later knowledge.

## 8. Research answer contract

A high-quality answer should make it possible to answer:

1. Which company?
2. Which period/date?
3. Which dataset?
4. What value?
5. How was it calculated?
6. What evidence supports the interpretation?
7. What remains uncertain?

## 9. Interview-ready example

**Question:** Compare two companies on revenue growth and ROE.

**Failure:** The system returns correct numbers, but one company's ROE is FY2026 and the other's is TTM.

**Tester response:**

> The raw values may individually be correct, but the comparison is not like-for-like. I would classify this as TPQ-TIME-002, P1. I would preserve the exact query and output, verify the underlying periods, and recommend that the response surface the reporting basis beside every metric or normalize both companies to a common basis.
