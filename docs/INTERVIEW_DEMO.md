# 5-Minute Interview Demo

## 0:00-0:30 — Explain the objective

> I built this as an independent power-user QA framework for Tape AI. The idea is to evaluate not just whether an answer sounds good, but whether the entity, period, source, data, calculation, reasoning and final presentation all hold up.

## 0:30-1:15 — Show the test catalog

Open `test_cases/20_core_cases.yaml`.

Explain that the suite intentionally covers:

- fundamentals
- technical indicators
- screening
- ownership/governance
- market flows
- point-in-time research
- corporate actions
- entity resolution
- Tapetide Score
- adversarial AI quality

## 1:15-2:00 — Show the error taxonomy

Open `taxonomy/error_codes.json` or `docs/ERROR_CATALOG.md`.

Explain that TPQ-* codes are tester-defined. Give one concrete example:

> TPQ-TIME-002 means a peer comparison uses mixed reporting periods.

Then explain why the issue matters even if each individual number is correct.

## 2:00-3:00 — Show one real captured finding

Use a real Tape AI observation after you have executed the test. Show:

- exact question
- actual answer
- independent verification
- classification
- severity
- recommended fix

Never use a fabricated finding in an interview.

## 3:00-4:00 — Explain the engineering bridge

Show `src/tapetide_qa/validator.py`.

Explain:

> A good finding becomes machine-checkable. I want a confirmed issue to become a regression test so the same failure can be detected after a product change.

## 4:00-5:00 — Connect it to your background

> My software-engineering background helps me reproduce failures and think in terms of expected behavior, validation and regression testing. My market-analysis work helps me distinguish a true research error from a presentation issue or an economically inappropriate metric.

Finish with one product improvement based on evidence from your actual testing.
