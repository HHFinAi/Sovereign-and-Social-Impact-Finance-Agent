"""Demography and policy-conditional public spending; no sovereign price forecast."""
from __future__ import annotations
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from public_case_support import value, run_cli


def mechanical_burden(ratio, employment, benefit_ratio, productivity_uplift=0, wage_indexed=False):
    if ratio < 0 or not 0 < employment <= 1 or benefit_ratio < 0 or productivity_uplift <= -1:
        raise ValueError('invalid demographic fiscal scenario')
    benefits = benefit_ratio * (1 + productivity_uplift if wage_indexed else 1)
    return ratio * benefits / (employment * (1 + productivity_uplift))


def calculate(inputs, s):
    a, rows = inputs['assumptions'], []
    for country in ('japan', 'germany', 'uk'):
        getr = lambda year: value(s, 'OECD_RATIO', country + '_' + year, 'people_65plus_per_100_people_20to64')
        getp = lambda year: value(s, 'OECD_PENSIONS', country + '_' + year, 'percent_GDP')
        r0, r1 = getr('2024'), getr('2054')
        p0, p1 = getp('base'), getp('2050')
        base = mechanical_burden(r1, a['working_age_employment_fraction'], a['pension_to_worker_output_fraction'])
        employment = mechanical_burden(r1, a['employment_reform_fraction'], a['pension_to_worker_output_fraction'])
        productivity = mechanical_burden(r1, a['working_age_employment_fraction'], a['pension_to_worker_output_fraction'], a['gdp_level_productivity_uplift'])
        indexed = mechanical_burden(r1, a['working_age_employment_fraction'], a['pension_to_worker_output_fraction'], a['gdp_level_productivity_uplift'], True)
        benefit = mechanical_burden(r1, a['working_age_employment_fraction'], a['benefit_ratio_reform_fraction'])
        rows.append({'country': country, 'ratio_2024': r0, 'ratio_2054': r1,
                     'ratio_increase_percent': round((r1 / r0 - 1) * 100, 6),
                     'public_pensions_baseline_percent_gdp': p0, 'public_pensions_2050_percent_gdp': p1,
                     'public_pensions_change_pp_gdp': round(p1 - p0, 6),
                     'mechanical_common_assumption_burden_percent_output': round(base, 6),
                     'employment_scenario_burden_percent_output': round(employment, 6),
                     'productivity_fixed_benefit_burden_percent_output': round(productivity, 6),
                     'productivity_indexed_benefit_burden_percent_output': round(indexed, 6),
                     'benefit_reform_burden_percent_output': round(benefit, 6)})
    return {'prepared_on': inputs['prepared_on'], 'countries': rows,
            'scope': 'Illustrative identity alongside official projections; demographic 2054 and pension 2050 horizons deliberately not merged.'}


def render(d):
    lines = ['# Ageing: financing pressure depends on policy', '',
             'OECD/UN demographic estimates and projections, alongside separately sourced pension-spending projections. Published 27 November 2025; retrieved 21 October 2026.', '',
             '| Country | 65+ per 100 aged 20-64: 2024 | 2054 projection | Ratio increase | Pension spending: 2023-24 (% GDP) | 2050 projection (% GDP) | Change (pp GDP) |',
             '|---|---:|---:|---:|---:|---:|---:|']
    for x in d['countries']:
        lines.append(f"| {x['country']} | {x['ratio_2024']:.1f} | {x['ratio_2054']:.1f} | {x['ratio_increase_percent']:.1f}% | {x['public_pensions_baseline_percent_gdp']:.1f} | {x['public_pensions_2050_percent_gdp']:.1f} | {x['public_pensions_change_pp_gdp']:+.1f} |")
    lines += ['', 'The dates and underlying methods differ. These columns do not identify a policy offset or establish a causal residual. Population age groups are not actual workers and pension claimants.', '',
              '| Common hypothetical burden (% output) | Baseline | Employment 75% to 80% | Output/worker +10%, benefits fixed | Output/worker +10%, benefits indexed | Benefit ratio 30% to 27% |',
              '|---|---:|---:|---:|---:|---:|']
    for x in d['countries']:
        lines.append(f"| {x['country']} 2054 | {x['mechanical_common_assumption_burden_percent_output']:.2f} | {x['employment_scenario_burden_percent_output']:.2f} | {x['productivity_fixed_benefit_burden_percent_output']:.2f} | {x['productivity_indexed_benefit_burden_percent_output']:.2f} | {x['benefit_reform_burden_percent_output']:.2f} |")
    lines += ['', 'The second table uses common analyst assumptions; it is not projected national spending. Productivity reduces this burden only when benefits do not rise proportionally. Benefit restraint also has adequacy/distributional costs. Healthcare, tax responses, debt, interest and migration are not estimated here.', '',
              'See [interpretation and limitations](README.md), [inputs](inputs.json) and [source definitions](sources.json).', '']
    return '\n'.join(lines)


if __name__ == '__main__':
    run_cli(Path(__file__).parent, calculate, render)
