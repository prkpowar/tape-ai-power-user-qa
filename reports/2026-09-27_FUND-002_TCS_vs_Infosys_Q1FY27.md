# FUND-002 — TCS vs Infosys Q1 FY27 Comparison

## Status

**VERIFIED WITH 3 CONFIRMED P2/P1 FINDINGS**

Observation supplied from Tape AI on 27 Sep 2026.

## Exact question

> Compare TCS and Infosys on the latest reported quarter using:
> 1. Revenue
> 2. Revenue YoY growth
> 3. EBITDA / operating profit
> 4. Operating margin
> 5. PAT
> 6. PAT margin
> 7. ROE
> 
> For every metric, show reporting period, consolidated/standalone basis, unit, and whether reported or derived.

## First-pass assessment

The answer correctly identified the same quarter for both companies: Q1 FY27 ended 30 June 2026. The response also explicitly warned that ROE was not quarterly and that Infosys's basis had not yet been independently confirmed.

However, there are material comparability problems in the operating-profit section.

## Official verification

### TCS

TCS's official Q1 FY27 release is dated **9 July 2026**, reports consolidated IFRS results for the quarter ended 30 June 2026, and reports a management operating margin of **24.0%**. citeturn245734search8turn245734search3

The data-provider-style figures in the Tape AI answer (revenue ₹72,275 Cr; operating profit ₹18,556 Cr; OPM 25.67%) are also published by market-data sites using the Indian convention of revenue less operating expenses before depreciation, but that is not the same presentation as TCS management's reported IFRS operating-margin metric. citeturn660879search0turn660879search1

### Infosys

Infosys officially announced Q1 FY27 results on **23 July 2026**. Its consolidated IFRS statement reports:

- Revenue: ₹48,211 Cr
- Operating profit: ₹10,163 Cr
- Operating margin: 21.1%
- Net profit: ₹7,775 Cr
- Profit attributable to owners: ₹7,769 Cr
- Basic EPS: ₹19.19

The same filing also reports **₹11,409 Cr as Segment Profit**, not consolidated operating profit, and shows **₹1,246 Cr of unallocable expenses** between segment profit and operating profit. citeturn131763view0turn271572view0turn508265search0

## Confirmed finding #1

### TPQ-TIME-003 — TCS earnings-release date
**Severity: P2**

Tape AI: 10 Jul 2026.

Issuer: 09 Jul 2026.

Evidence: TCS investor calendar and official release. citeturn245734search3turn245734search8

## Confirmed finding #2

### TPQ-TIME-003 — Infosys earnings-release date
**Severity: P2**

Tape AI: 24 Jul 2026.

Issuer: 23 Jul 2026.

Evidence: Infosys quarterly-results page and investor calendar. citeturn943798search1turn943798search7

## Confirmed finding #3

### TPQ-RES-001 / TPQ-CALC-007 — Non-comparable operating-profit metric
**Severity: P1**

The response labels:

- TCS ₹18,556 Cr as EBITDA/operating profit
- Infosys ₹11,409 Cr as EBITDA/operating profit

But for Infosys, ₹11,409 Cr is explicitly **segment profit**, while consolidated operating profit is ₹10,163 Cr. citeturn271572view0turn271572view1

Therefore:

> TCS ₹18,556 Cr / ₹72,275 Cr = 25.67%

and

> Infosys ₹11,409 Cr / ₹48,211 Cr = 23.66%

are **not a like-for-like operating-margin comparison**.

The official company-reported operating margins are:

- TCS: **24.0%**
- Infosys: **21.1%** citeturn245734search8turn943798search4

The issue is not necessarily that either raw number is fabricated. It is that the response assigns the same metric label to values with different definitions.

## ROE handling

The response did something good here.

It explicitly stated that neither company had quarterly ROE in the dataset and that the displayed ROE values did not have a precise common period. That should be recorded as a **PASS for uncertainty disclosure**, not a defect.

However, the conclusion:

> "The comparison between the two companies still holds either way"

should be treated cautiously because the current ROE figures have different/unclear period definitions. We should test this separately.

## Other verified items

### Revenue

TCS ₹72,275 Cr and Infosys ₹48,211 Cr are confirmed. citeturn245734search8turn943798search4

### Revenue growth

TCS 13.93% is consistent with ₹72,275 Cr vs ₹63,437 Cr.

Infosys 14.03% is consistent with ₹48,211 Cr vs ₹42,279 Cr; Infosys itself reports 14.0% YoY. citeturn943798search4

### Infosys PAT

₹7,775 Cr is consolidated net profit, while ₹7,769 Cr is attributable to owners. The answer should define which one it is using. The filing supports both numbers. citeturn131763view0

## Important research-quality lesson

This test found a higher-value class of problem than a simple incorrect number:

> **metric semantic mismatch**

A researcher can receive numerically valid values and still receive a misleading comparison if the values represent different concepts.

That is exactly the type of defect this QA framework should target.

## Recommended product fix

For comparative answers, every metric should carry a machine-readable definition internally and a visible label such as:

- Reported operating profit
- Segment profit
- Derived EBITDA proxy
- Management operating margin
- IFRS operating margin

Before calculating a peer comparison, the system should confirm that both selected values use compatible definitions.

## Regression tests

1. Compare TCS and Infosys on operating profit and require both values to come from the same semantic metric.
2. If the requested term "EBITDA / operating profit" maps to different provider definitions, explicitly disclose that.
3. Verify company earnings-release dates against issuer calendars.
4. Do not call Infosys segment profit "operating profit".
5. For ROE without quarterly data, show exact period or mark the period unknown.

## Interview takeaway

> I found that the most important problem wasn't a bad arithmetic calculation. The answer mixed semantic definitions: Infosys ₹11,409 Cr was segment profit, not consolidated operating profit. That means the resulting 25.67% versus 23.66% margin comparison was not like-for-like. I would classify this as a P1 research-comparability issue because an analyst could draw a different conclusion even though the underlying numbers themselves exist in the source data.
