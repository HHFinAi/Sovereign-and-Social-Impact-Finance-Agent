# Financing and social additionality

**Agent:** Sovereign and Social-Impact Finance Agent · **Stage:** `additionality` · **Audience:** buy-side analysts, portfolio managers and investment committees.

## Required context and inputs
Read the adopted system prompt, operating contract, selected route, request, evidence register and completed upstream artifacts. Confirm subject and instrument boundaries, as-of date and what the sources actually establish. Resolve this stage's requirements against the preceding work packet; do not treat downstream conclusions as prior evidence.

## Analytical task
Test what would occur without the financing, transaction or investor. Separate cheaper funding, extended maturity, expanded programme resources, capital mobilisation and incremental social outcomes. Assess why concessional capital is needed, whether less could achieve the objective, allocation of subsidy, crowding-in versus displacement and commercial sustainability. Mobilisation ratios are descriptive, not proof of causality or appropriate subsidy. Document counterfactual uncertainty, donor/creditor/debtor perspectives and opportunity costs without inventing social-return multiples. Public-policy comparisons must be neutral, sourced and descriptive; do not endorse political actors, legislation or electoral choices.

## Required deliverables
- `financing_counterfactual`: substantive analysis, supported claim IDs, limitations and decision implications.
- `concessionality_and_crowding_in`: substantive analysis, supported claim IDs, limitations and decision implications.
- `distribution_and_tradeoffs`: substantive analysis, supported claim IDs, limitations and decision implications.

Return `schema_version`, `run_id`, `input_digest`, `stage_id`, `status`, producer identity/type, summary, typed claims, calculation records, standards considered, required sections, gaps, issues and subjective confidence with its basis. Every required section must reference actual claims, not an empty list. Add allowlisted calculations when they materially support the stage; never invent a numeric result. 

## Evidence / method anchors
- IFC-BLENDED: https://www.ifc.org/en/what-we-do/sector-expertise/blended-finance/how-blended-finance-works
- IMF-WB-SWAPS: https://www.imf.org/en/publications/policy-papers/issues/2024/08/05/debt-for-development-swaps-an-approach-framework-553146

Method references are not proof of subject facts or automatic legal compliance. Use the dated register in `references/standards.json`; document non-applicable standards rather than pretending every standard governs every instrument.

## Failure and verification checks
Return NEEDS_DATA/BLOCKED with precise missing inputs when material evidence is absent. A polished paragraph is not a substitute for evidence. Check entity, period, currency, unit, denominator, restatement, point-in-time availability and contradictory evidence. Explain the strongest plausible alternative interpretation and whether it changes the decision. Record material concerns in the issue register. Do not call the human approval action. Confidence is subjective and must state its scope, not pretend to be a calibrated probability.
