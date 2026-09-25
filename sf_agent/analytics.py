"""Transparent scenario arithmetic, NOT the official IMF/WB DSA template."""
from __future__ import annotations
from .maths import COMMON_OPERATIONS, checked, fraction, number, operation, positive, require, series, npv

@operation({"initial_debt_gdp": "decimal_of_gdp", "nominal_interest": "decimal", "nominal_gdp_growth": "decimal", "primary_surplus_gdp": "decimal_of_gdp", "stock_flow_adjustment_gdp": "decimal_of_gdp", "fx_debt_share": "decimal_fraction", "fx_depreciation": "decimal"}, "debt_path_decimal_of_gdp")
def debt_path(initial_debt_gdp: float, nominal_interest: list[float], nominal_gdp_growth: list[float],
              primary_surplus_gdp: list[float], stock_flow_adjustment_gdp: list[float],
              fx_debt_share: float, fx_depreciation: list[float]) -> list[float]:
    """Opening debt revaluation, uniform interest; primary surplus positive.

FX term is opening foreign-currency principal revaluation only. It excludes
within-period currency/interest cross effects and endogenous policy responses.
"""
    debt = checked(initial_debt_gdp, "initial_debt_gdp", 0)
    interest = series(nominal_interest, "nominal_interest")
    growth = series(nominal_gdp_growth, "nominal_gdp_growth")
    primary = series(primary_surplus_gdp, "primary_surplus_gdp")
    sfa = series(stock_flow_adjustment_gdp, "stock_flow_adjustment_gdp")
    fx = series(fx_depreciation, "fx_depreciation")
    share = fraction(fx_debt_share, "fx_debt_share")
    require(len({len(x) for x in (interest, growth, primary, sfa, fx)}) == 1, "scenario series length mismatch")
    result = [debt]
    for r, g, pb, adjust, depreciation in zip(interest, growth, primary, sfa, fx):
        require(r > -1 and g > -1 and depreciation > -1, "interest, growth and FX change must exceed -100%")
        debt = (1 + r + share * depreciation) / (1 + g) * debt - pb + adjust
        require(debt >= 0, "path implies net public assets; use a net-asset model rather than silently clamping debt")
        result.append(number(debt, "debt ratio"))
    return result

@operation({"debt_service_before": "$money", "debt_service_after": "$money", "program_spending": "$money", "fees": "$money", "annual_discount": "decimal"}, "swap_value_metrics")
def swap_value(debt_service_before: list[float], debt_service_after: list[float], program_spending: list[float],
               fees: list[float], annual_discount: float) -> dict:
    """All arrays have t=0 followed by annual periods, same currency and horizon."""
    before = series(debt_service_before, "debt_service_before")
    after = series(debt_service_after, "debt_service_after")
    programs = series(program_spending, "program_spending")
    costs = series(fees, "fees")
    require(len({len(x) for x in (before, after, programs, costs)}) == 1, "cashflow horizons must match")
    require(all(x >= 0 for xs in (before, after, programs, costs) for x in xs), "cost schedules must be nonnegative")
    relief = npv([a - b for a, b in zip(before, after)], annual_discount)
    spending = npv(programs, annual_discount)
    fee_pv = npv(costs, annual_discount)
    return {"pv_debt_service_relief": relief, "pv_program_commitment": spending,
            "pv_fees": fee_pv, "net_fiscal_savings": relief - spending - fee_pv}

@operation({"portfolio_loss": "$money", "first_loss_capacity": "$money", "guarantee_coverage": "decimal_fraction", "guarantee_cap": "$money"}, "loss_allocation_metrics")
def blended_loss_allocation(portfolio_loss: float, first_loss_capacity: float,
                            guarantee_coverage: float, guarantee_cap: float) -> dict:
    loss = checked(portfolio_loss, "portfolio_loss", 0)
    first = min(loss, checked(first_loss_capacity, "first_loss_capacity", 0))
    coverage = fraction(guarantee_coverage, "guarantee_coverage")
    cap = checked(guarantee_cap, "guarantee_cap", 0)
    guarantee = min((loss - first) * coverage, cap)
    return {"first_loss_absorbed": first, "guarantee_payment": guarantee, "residual_investor_loss": loss - first - guarantee}

@operation({"verified_outcomes": "$outcome", "price_per_outcome": "money_per_outcome", "payment_cap": "$money"}, "$money")
def outcome_payment(verified_outcomes: float, price_per_outcome: float, payment_cap: float) -> float:
    outcomes = checked(verified_outcomes, "verified_outcomes", 0)
    price = checked(price_per_outcome, "price_per_outcome", 0)
    cap = checked(payment_cap, "payment_cap", 0)
    return min(outcomes * price, cap)

@operation({"private_capital": "$money", "concessional_capital": "$money"}, "multiple")
def mobilisation_ratio(private_capital: float, concessional_capital: float) -> float:
    """Simple ratio, not proof that concessional support caused mobilisation."""
    return checked(private_capital, "private_capital", 0) / positive(concessional_capital, "concessional_capital")

OPERATIONS = dict(COMMON_OPERATIONS)
OPERATIONS.update({f.__name__: f for f in (debt_path, swap_value, blended_loss_allocation, outcome_payment, mobilisation_ratio)})
