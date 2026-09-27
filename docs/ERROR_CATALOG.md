# Error & Problem Catalog

## How to read this file

The codes in this document are an **independent tester-defined taxonomy** for organizing findings. They are intentionally human-readable and are not claimed to match Tapetide's internal production error codes.

## Severity

- P0 = Critical
- P1 = Major
- P2 = Moderate
- P3 = Minor

## Entity / Identifier

| Code | Problem | Example | First check | Possible solution |
|---|---|---|---|---|
| TPQ-ID-001 | Wrong entity | A brand name resolves to a different listed entity | Compare name, symbol, ISIN | Improve identifier resolution and show resolved identifier |
| TPQ-ID-002 | Ambiguous entity | Two companies share a similar name | Search results and identifiers | Ask for clarification or return disambiguation |
| TPQ-ID-003 | Renamed symbol mismatch | Historical symbol no longer resolves | Check symbol/ISIN as-of date | Use historical identifier mapping |
| TPQ-ID-004 | Exchange mismatch | NSE result used where BSE-specific result was requested | Verify exchange field | Expose exchange and keep routing explicit |
| TPQ-ID-005 | Duplicate entity | Same company appears twice with different aliases | Compare ISIN | Canonicalize by stable identifier |

## Time / Period

| Code | Problem | Example | First check | Possible solution |
|---|---|---|---|---|
| TPQ-TIME-001 | Missing reporting period | "PAT rose 20%" with no comparison period | Inspect raw financial rows | Require period in response |
| TPQ-TIME-002 | Mixed periods | Company A FY2026 vs Company B FY2025 | Compare period labels | Align periods or flag mismatch |
| TPQ-TIME-003 | Wrong observation date | Quote described as current but is stale | Check timestamp | Show observed-at time |
| TPQ-TIME-004 | Publication-date leakage | Historical research uses a report published later | Compare reporting and publication dates | Enforce as-of cutoff |
| TPQ-TIME-005 | Calendar/session error | Weekend treated as trading day | Observation-status check | Use trading-session calendar |
| TPQ-TIME-006 | Fiscal-year confusion | Q1 FY27 interpreted as calendar Q1 2026 | Inspect fiscal definition | Normalize labels |
| TPQ-TIME-007 | TTM/FY confusion | TTM EPS compared with full-year EPS | Check metric definition | Label period basis beside every value |
| TPQ-TIME-008 | YoY/QoQ confusion | 15% QoQ reported as 15% YoY | Check comparator | Explicitly state comparator |

## Data Quality

| Code | Problem | Example | First check | Possible solution |
|---|---|---|---|---|
| TPQ-DATA-001 | Stale data | Latest price is from an earlier session | Timestamp | Surface freshness |
| TPQ-DATA-002 | Missing required field | Debt/equity absent | Schema completeness | Return missing-state instead of inventing value |
| TPQ-DATA-003 | Unit mismatch | ₹ crore compared with ₹ million | Unit metadata | Normalize or display units |
| TPQ-DATA-004 | Duplicate observation | Same quarterly row appears twice | Unique keys | Deduplicate upstream |
| TPQ-DATA-005 | Corporate-action distortion | Split creates fake 60% return | Adjustment factors | Apply adjustment or explain raw price |
| TPQ-DATA-006 | Restatement mismatch | Historical number differs after filing restatement | Compare versions | Preserve version/date metadata |
| TPQ-DATA-007 | Missing-vs-zero confusion | No dividend data interpreted as zero dividend | Raw presence flag | Preserve null semantics |
| TPQ-DATA-008 | Source conflict | Two sources disagree | Compare source/date | Surface conflict and preferred source |
| TPQ-DATA-009 | Denominator near zero | P/E becomes enormous | Check denominator | Treat unstable ratio as unavailable/flagged |
| TPQ-DATA-010 | Sign inversion | Negative debt/cash-flow metric scored as favorable | Inspect sign | Add domain-specific validation |

## Calculations

| Code | Problem | Example | First check | Possible solution |
|---|---|---|---|---|
| TPQ-CALC-001 | Arithmetic error | 100 to 120 described as +30% | Recalculate | Add deterministic calculation test |
| TPQ-CALC-002 | Wrong formula | ROE uses wrong denominator | Compare formula definition | Centralize metric definitions |
| TPQ-CALC-003 | Percentage vs percentage-point error | Margin 20% to 25% called +25% | Recalculate both forms | State pp vs % explicitly |
| TPQ-CALC-004 | CAGR error | 100 to 121 over 2 years called 10% CAGR | Recalculate | Unit-test CAGR |
| TPQ-CALC-005 | Return-basis error | Simple return used where log return expected | Check specification | Label return type |
| TPQ-CALC-006 | Rounding error | 9.995 shown as 9.95 | Re-run full precision | Round only at presentation |
| TPQ-CALC-007 | Cross-company mismatch | Different ratio definitions used for peers | Compare definitions | Normalize definitions |
| TPQ-CALC-008 | Invalid negative valuation | Negative P/E treated as "cheap" | Check earnings sign | Exclude or flag mathematically invalid ratio |

## Tool / MCP

| Code | Problem | Example | First check | Possible solution |
|---|---|---|---|---|
| TPQ-MCP-001 | Authentication failure | Protected tool call returns auth error | Token/OAuth status | Re-authenticate, surface clear error |
| TPQ-MCP-002 | Wrong tool selected | Financial comparison routed to unrelated tool | Trace requested capability | Improve tool descriptions/routing prompts |
| TPQ-MCP-003 | Invalid arguments | Tool receives wrong symbol/date format | Inspect request | Add schema validation and examples |
| TPQ-MCP-004 | Partial tool result | Multi-company query silently omits one company | Count expected vs returned | Return completeness status |
| TPQ-MCP-005 | Schema drift | Field renamed and parser still expects old name | Compare schema | Version schema / contract tests |
| TPQ-MCP-006 | Rate limit | Successful-call quota is exhausted | Usage/reset info | Backoff, batching, explain retry time |
| TPQ-MCP-007 | Timeout/network error | Tool doesn't return within expected time | Request timing | Retry safely and surface status |
| TPQ-MCP-008 | Alias/retired tool mismatch | Old tool name invoked | Tool catalog | Use current tool; test compatibility path |
| TPQ-MCP-009 | Parallel-call failure | Independent tools run serially causing avoidable delay | Trace timing | Parallelize independent calls |
| TPQ-MCP-010 | Tool-result contamination | Data from one company leaks into another | Compare raw result IDs | Strict request/result correlation |

## AI / Reasoning

| Code | Problem | Example | First check | Possible solution |
|---|---|---|---|---|
| TPQ-AI-001 | Hallucinated fact | Company event invented | Source verification | Ground claims in retrieved data |
| TPQ-AI-002 | Unsupported inference | High ROE => "excellent business" | Evidence chain | Phrase inference as interpretation |
| TPQ-AI-003 | Overconfidence | Unknown value stated as exact | Missing-data state | Express uncertainty |
| TPQ-AI-004 | Contradictory answer | Summary conflicts with table | Cross-check response sections | Add consistency pass |
| TPQ-AI-005 | Missing material caveat | High debt omitted from risk discussion | Compare evidence set | Require risk/context checklist |
| TPQ-AI-006 | Prompt ambiguity ignored | "Best stock" answered with unstated criteria | Inspect assumptions | Ask clarification or state criteria |
| TPQ-AI-007 | Citation mismatch | Claim cites unrelated metric/source | Verify source linkage | Bind citations to claims/data points |
| TPQ-AI-008 | Reasoning leap | One indicator used as full thesis | Inspect evidence coverage | Require multi-factor reasoning |
| TPQ-AI-009 | Retrieval contamination | Answer mixes information from similar companies | Entity trace | Entity-aware context isolation |
| TPQ-AI-010 | Advice-language violation | Data presented as a direct buy/sell instruction | Policy/disclaimer check | Reframe as analysis and evidence |

## Research / Screening

| Code | Problem | Example | First check | Possible solution |
|---|---|---|---|---|
| TPQ-RES-001 | Peer-group mismatch | Bank compared with industrials for EV/EBITDA | Industry/sector | Sector-aware comparison |
| TPQ-RES-002 | Incomplete research | Valuation discussed without growth context | Checklist | Minimum research schema |
| TPQ-RES-003 | Signal conflation | RSI treated as proof of value | Separate factor types | Explain signal role |
| TPQ-SCR-001 | Filter leakage | Results violate a requested threshold | Recalculate filters | Apply filters after retrieval and validate |
| TPQ-SCR-002 | False positive | Stock appears despite missing required value | Inspect null handling | Null-aware filtering |
| TPQ-SCR-003 | False negative | Stock should qualify but is missing | Compare universe | Audit pagination/universe/filters |
| TPQ-SCR-004 | Pagination truncation | Only first page considered | Inspect cursor/page state | Iterate until complete or disclose limit |
| TPQ-SCR-005 | Filter semantic mismatch | "Debt low" interpreted with wrong ratio | Metric mapping | Show exact ratio used |

## Tapetide Score / Deterministic Research

| Code | Problem | Example | First check | Possible solution |
|---|---|---|---|---|
| TPQ-SCORE-001 | Pillar inconsistency | Final score doesn't reconcile to pillar inputs | Recompute | Publish calculation trace |
| TPQ-SCORE-002 | Version mismatch | Same score compared across formula versions | Check version metadata | Show formula/reference version |
| TPQ-SCORE-003 | Confidence inconsistency | Sparse data shown with unjustified high confidence | Coverage vs confidence | Recalculate confidence |
| TPQ-SCORE-004 | Governance cap missing | Score doesn't reflect documented cap/red flag | Inspect governance layer | Enforce post-score controls |
| TPQ-SCORE-005 | Inapplicable metric | Industrial metric applied to financial company | Sector template | Sector-specific eligibility |
| TPQ-SCORE-006 | Missing-data treated as poor performance | No data lowers score like bad data | Compare null semantics | Separate missing from negative |
| TPQ-SCORE-007 | Smoothing threshold bug | Hysteresis behaves differently from specification | Compare raw vs smoothed delta | Add boundary regression tests |
| TPQ-SCORE-008 | Factor-validation error | A factor is promoted without out-of-sample support | Validation report | Require documented evidence |
| TPQ-SCORE-009 | Universe eligibility error | Sparse/illiquid company receives a full score | Eligibility rules | Apply liquidity/coverage gate |
| TPQ-SCORE-010 | Reproducibility failure | Same frozen inputs produce different scores | Run twice | Lock formula/reference/input versions |

## Point-in-Time / Historical

| Code | Problem | Example | First check | Possible solution |
|---|---|---|---|---|
| TPQ-PIT-001 | Look-ahead bias | Historical answer uses later publication | Publication dates | Enforce cutoff |
| TPQ-PIT-002 | Survivorship bias | Historical universe contains only current survivors | Historical constituents | Use as-of membership |
| TPQ-PIT-003 | Historical identifier drift | Current symbol used for past date | Identifier history | Resolve identifier as-of date |
| TPQ-PIT-004 | Corporate-action leakage | Adjusted price history changes historical interpretation | Adjustment metadata | Keep raw/adjusted basis explicit |
| TPQ-PIT-005 | Restatement leakage | Restated figures used for prior-date research | Filing versions | Use version available at cutoff |

## Governance / Ownership

| Code | Problem | Example | First check | Possible solution |
|---|---|---|---|---|
| TPQ-GOV-001 | Pledge misclassification | Pledged shares interpreted as selling | Event type | Separate pledge/release/sale |
| TPQ-GOV-002 | Insider-activity misclassification | Routine event treated as discretionary sale | Event label | Normalize event taxonomy |
| TPQ-GOV-003 | Governance date mismatch | Current governance event applied to earlier snapshot | Event date | Apply as-of event logic |
| TPQ-GOV-004 | Missing material flag | Serious governance event omitted | Cross-check disclosures | Add governance checklist |

## UX / Operations

| Code | Problem | Example | First check | Possible solution |
|---|---|---|---|---|
| TPQ-UX-001 | Period hidden | User cannot tell which period supports a number | Response labels | Display period next to metric |
| TPQ-UX-002 | Unit hidden | ₹ crore vs ₹ million unclear | Metadata | Display units |
| TPQ-UX-003 | Freshness hidden | User cannot tell when market data was updated | Timestamp | Display last updated |
| TPQ-UX-004 | Caveat hidden | Material limitation buried | Response layout | Surface caveat near claim |
| TPQ-OPS-001 | Silent partial run | Incomplete dataset published without warning | Row-count checks | Gate publication |
| TPQ-OPS-002 | Duplicate run | Same job publishes duplicate records | Run ID | Idempotent write |
| TPQ-OPS-003 | Failed retry corruption | Retry creates mixed-version output | Run metadata | Atomic publish and versioning |
| TPQ-OPS-004 | Monitoring blind spot | Critical failure produces no alert | Logs/metrics | Add health checks |

---

## Rule

**Never treat a TPQ code as an official Tapetide internal error code.** This catalog is an independent portfolio/tester taxonomy.