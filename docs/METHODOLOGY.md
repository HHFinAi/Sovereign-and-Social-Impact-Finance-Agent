# Methodology, units and model boundaries

## Model posture
All functions are transparent, deterministic arithmetic under caller-supplied assumptions. They do not estimate missing values, fit probabilities or validate the economic model. A number can pass unit and recomputation checks while its assumptions or causal interpretation remain wrong. Inspect `sf_agent/analytics.py` and the operation registry below.

Money uses one declared three-letter currency per calculation. FX conversions must be explicit and sourced. Percentages are decimal fractions unless a field explicitly says basis points. Scalar source metrics bind to their disclosed period, entity and unit. A series supplied as an assumption must have its period convention and underlying source work explained; the v0.1 schema does not independently reconcile a time-series spreadsheet. `scale` records explicit conversion arithmetic, but a reviewer must validate the declared units and factor.

Common helpers: `npv` uses cashflows[0] at time zero followed by annual periods; it is not XNPV and ignores irregular dates. `dscr` divides supplied cash available by positive debt service and does not normalize accounting definitions. `holding_period_return` uses consistent dirty-price money amounts, income, funding and transaction costs without annualizing or adding default probabilities. `scale` applies an explicit positive conversion factor; its semantics require human review.

## Standards maintenance
`references/standards.json` is a dated metadata register, not an embedded legal database or a substitute for the source text. Edition dates known only to the month are normalized to day 01 for indexing and must not be used as exact legal effective dates. Webpage update dates are distinguished from methodology editions. Reviewed references are checked as of September 24, 2026. Applicable adopted law, proposed reforms, voluntary guidance, reporting methodology and instrument contracts must remain separate. Reverify whenever material, before historical analysis and when the configured review age expires. The runtime blocks stale considered references at approval, but does not itself recheck a website.

## Financial and sustainability judgments
Make separate conclusions for financial attractiveness, sustainability/impact evidence and mandate compatibility. Use independent evidence for market prices, legal rights and outcomes. Report unassessed exposure and confidence limits rather than imputing zero. Document how uncertainty changes the investment decision; do not solve uncertainty by adding an unsupported discount or ESG score. “All checks pass” records an analyst's attestation and required inputs, not an independent suitability determination.

## Domain operation registry

## Sovereign/social-finance boundaries
`debt_path` applies the stylized recurrence `d[t] = (1 + nominal_interest[t] + fx_share × depreciation[t]) / (1 + nominal_GDP_growth[t]) × d[t−1] − primary_surplus[t] + stock_flow_adjustment[t]`. Ratios are decimal fractions of GDP; a positive primary surplus reduces debt. FX revaluation applies only to opening foreign-currency principal, omits intra-period cross effects and assumes a constant supplied FX share. This is **not the official IMF/World Bank DSA**, a credit rating, a calibrated macro forecast or an endogenous policy model. Paths implying net public assets require a different model and are rejected rather than clamped to zero.

`swap_value` discounts four same-horizon, same-currency annual schedules starting at t=0. It reports debt-service relief, programme spending, fees and net fiscal savings separately. Headline principal cancelled is not the output. Ensure schedules cover all remaining obligations and avoid double counting replacement principal and funding. Multi-currency, contingent and irregular-date transactions need a validated full model. `blended_loss_allocation` assumes first-loss capital absorbs losses, then a capped proportional guarantee pays, with residual losses borne by investors; it assumes enforceable, timely payment and does not model correlated default or delay. `outcome_payment` is verified quantities × price subject to a cap; it does not verify outcomes or payer capacity. `mobilisation_ratio` is private capital / concessional capital, not proof of financing additionality.

### Dated framework control
The September 21, 2026 IMF release describes a reviewed LIC-DSF reform expected to become operational in H2 2027. The package records it as APPROVED_FUTURE_OPERATIONAL, not currently operative law or an implemented official DSA. Select the correct framework and actual country DSA for each run. Source: https://www.imf.org/en/news/articles/2026/09/21/pr26296-lics-imf-executive-board-reviews-the-joint-world-bank-debt-sustainability-framework

| Operation | Input unit contract | Output unit/structure |
|---|---|---|
| `npv` | `cashflows: $money`, `annual_discount: decimal` | `$money` |
| `dscr` | `cash_available: $money`, `debt_service: $money` | `multiple` |
| `scale` | `value: $input_unit`, `factor: conversion_factor` | `$output_unit` |
| `holding_period_return` | `initial_dirty_price: $money`, `exit_dirty_price: $money`, `cash_income: $money`, `funding_cost: $money`, `transaction_cost: $money` | `decimal_return` |
| `debt_path` | `initial_debt_gdp: decimal_of_gdp`, `nominal_interest: decimal`, `nominal_gdp_growth: decimal`, `primary_surplus_gdp: decimal_of_gdp`, `stock_flow_adjustment_gdp: decimal_of_gdp`, `fx_debt_share: decimal_fraction`, `fx_depreciation: decimal` | `debt_path_decimal_of_gdp` |
| `swap_value` | `debt_service_before: $money`, `debt_service_after: $money`, `program_spending: $money`, `fees: $money`, `annual_discount: decimal` | `swap_value_metrics` |
| `blended_loss_allocation` | `portfolio_loss: $money`, `first_loss_capacity: $money`, `guarantee_coverage: decimal_fraction`, `guarantee_cap: $money` | `loss_allocation_metrics` |
| `outcome_payment` | `verified_outcomes: $outcome`, `price_per_outcome: money_per_outcome`, `payment_cap: $money` | `$money` |
| `mobilisation_ratio` | `private_capital: $money`, `concessional_capital: $money` | `multiple` |

`$money` resolves to the declared currency; `$outcome` resolves to the named outcome measurement unit. Compound `money_per_outcome` resolves to currency/outcome unit. Multi-output metric dictionaries have field-level meanings described above and in the implementation. Code validates input units and recomputed results, not the scientific or economic validity of those inputs.
