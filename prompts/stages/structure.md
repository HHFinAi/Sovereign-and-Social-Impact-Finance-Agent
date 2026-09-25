# Financing structure and sources/uses

**Agent:** Sovereign and Social-Impact Finance Agent · **Stage:** `structure` · **Audience:** buy-side analysts, portfolio managers and investment committees.

## Required context and inputs
Read the adopted system prompt, operating contract, selected route, request, evidence register and completed upstream artifacts. Confirm subject and instrument boundaries, as-of date and what the sources actually establish. Resolve this stage's requirements against the preceding work packet; do not treat downstream conclusions as prior evidence.

## Analytical task
Reconstruct the full transaction: retired liabilities, replacement finance, guarantees, concessional tranches, upfront fees, reserves, programme commitments, repayment and verification costs. Distinguish debt-for-development swaps, sovereign social bonds, blended funds and outcome contracts; a bilateral Debt2Health agreement is not automatically a traded bond. Compare the same economic objective through grants, ordinary refinancing, loans and guarantees as descriptive financing scenarios, not political-policy endorsements. Reconcile currencies, dates, leverage and double counting between new financing and debt service. State payment priorities and which party bears each loss, outcome failure or cost overrun. Flag missing side letters and confidentiality-limited evidence.

## Required deliverables
- `transaction_map`: substantive analysis, supported claim IDs, limitations and decision implications.
- `sources_uses_and_waterfall`: substantive analysis, supported claim IDs, limitations and decision implications.
- `alternative_structures`: substantive analysis, supported claim IDs, limitations and decision implications.

Return `schema_version`, `run_id`, `input_digest`, `stage_id`, `status`, producer identity/type, summary, typed claims, calculation records, standards considered, required sections, gaps, issues and subjective confidence with its basis. Every required section must reference actual claims, not an empty list. Add allowlisted calculations when they materially support the stage; never invent a numeric result. 

## Evidence / method anchors
- IMF-WB-SWAPS: https://www.imf.org/en/publications/policy-papers/issues/2024/08/05/debt-for-development-swaps-an-approach-framework-553146
- IFC-BLENDED: https://www.ifc.org/en/what-we-do/sector-expertise/blended-finance/how-blended-finance-works
- GF-D2H: https://www.theglobalfund.org/en/how-we-raise-funds/innovative-finance/debt-swaps-debt2health/

Method references are not proof of subject facts or automatic legal compliance. Use the dated register in `references/standards.json`; document non-applicable standards rather than pretending every standard governs every instrument.

## Failure and verification checks
Return NEEDS_DATA/BLOCKED with precise missing inputs when material evidence is absent. A polished paragraph is not a substitute for evidence. Check entity, period, currency, unit, denominator, restatement, point-in-time availability and contradictory evidence. Explain the strongest plausible alternative interpretation and whether it changes the decision. Record material concerns in the issue register. Do not call the human approval action. Confidence is subjective and must state its scope, not pretend to be a calibrated probability.
