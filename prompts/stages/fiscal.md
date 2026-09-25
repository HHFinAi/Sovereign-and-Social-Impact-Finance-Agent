# Net fiscal economics and debt-service savings

**Agent:** Sovereign and Social-Impact Finance Agent · **Stage:** `fiscal` · **Audience:** buy-side analysts, portfolio managers and investment committees.

## Required context and inputs
Read the adopted system prompt, operating contract, selected route, request, evidence register and completed upstream artifacts. Confirm subject and instrument boundaries, as-of date and what the sources actually establish. Resolve this stage's requirements against the preceding work packet; do not treat downstream conclusions as prior evidence.

## Analytical task
Compare counterfactual and transaction debt-service schedules over the full life using common dates, currency and discount conventions. Include fees, guarantees, insurance, reserve funding, verification, transaction costs, legally committed development spending and remaining obligations; distinguish transfers from economic resource costs. Face-value debt reduction is not net fiscal savings, and a lower coupon is not savings if tenor, principal or risk changes. Show debt-service relief, new programme resources and net fiscal value separately, including discounted and undiscounted schedules. Prevent double counting loan proceeds, principal replacement and contingent guarantees. Use scenarios for uncertain exchange rates and contingent payments; require a full professional cash-flow model beyond the bounded annual helper.

## Required deliverables
- `debt_service_comparison`: substantive analysis, supported claim IDs, limitations and decision implications.
- `fees_and_commitments`: substantive analysis, supported claim IDs, limitations and decision implications.
- `net_fiscal_value`: substantive analysis, supported claim IDs, limitations and decision implications.

Return `schema_version`, `run_id`, `input_digest`, `stage_id`, `status`, producer identity/type, summary, typed claims, calculation records, standards considered, required sections, gaps, issues and subjective confidence with its basis. Every required section must reference actual claims, not an empty list. At least one allowlisted, independently recomputed calculation is required for COMPLETE. 

## Evidence / method anchors
- IMF-WB-SWAPS: https://www.imf.org/en/publications/policy-papers/issues/2024/08/05/debt-for-development-swaps-an-approach-framework-553146

Method references are not proof of subject facts or automatic legal compliance. Use the dated register in `references/standards.json`; document non-applicable standards rather than pretending every standard governs every instrument.

## Failure and verification checks
Return NEEDS_DATA/BLOCKED with precise missing inputs when material evidence is absent. A polished paragraph is not a substitute for evidence. Check entity, period, currency, unit, denominator, restatement, point-in-time availability and contradictory evidence. Explain the strongest plausible alternative interpretation and whether it changes the decision. Record material concerns in the issue register. Do not call the human approval action. Confidence is subjective and must state its scope, not pretend to be a calibrated probability.
