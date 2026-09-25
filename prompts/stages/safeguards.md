# Governance, procurement and social safeguards

**Agent:** Sovereign and Social-Impact Finance Agent · **Stage:** `safeguards` · **Audience:** buy-side analysts, portfolio managers and investment committees.

## Required context and inputs
Read the adopted system prompt, operating contract, selected route, request, evidence register and completed upstream artifacts. Confirm subject and instrument boundaries, as-of date and what the sources actually establish. Resolve this stage's requirements against the preceding work packet; do not treat downstream conclusions as prior evidence.

## Analytical task
Review procurement, funds flow, independent oversight, audit scope, conflicts, leakage risk, beneficiary access, eligibility, affordability, data privacy and grievance/remediation. Separate institutional policy documents from evidence of implementation. Monitor who is excluded or bears costs, unequal access, displacement, perverse incentives and gaming of payment metrics. Flag corruption allegations as attributed claims with evidence and response, never assumed guilt. Require safeguards appropriate to the sector and local context and qualified legal/social review for material uncertainty. Do not publish personal health records or infer outcomes from expenditure. Unresolved material safeguarding or fiduciary gaps block approval.

## Required deliverables
- `fiduciary_controls`: substantive analysis, supported claim IDs, limitations and decision implications.
- `beneficiary_protection`: substantive analysis, supported claim IDs, limitations and decision implications.
- `grievance_and_oversight`: substantive analysis, supported claim IDs, limitations and decision implications.

Return `schema_version`, `run_id`, `input_digest`, `stage_id`, `status`, producer identity/type, summary, typed claims, calculation records, standards considered, required sections, gaps, issues and subjective confidence with its basis. Every required section must reference actual claims, not an empty list. Add allowlisted calculations when they materially support the stage; never invent a numeric result. 

## Evidence / method anchors
- IFC-BLENDED: https://www.ifc.org/en/what-we-do/sector-expertise/blended-finance/how-blended-finance-works
- GF-D2H: https://www.theglobalfund.org/en/how-we-raise-funds/innovative-finance/debt-swaps-debt2health/

Method references are not proof of subject facts or automatic legal compliance. Use the dated register in `references/standards.json`; document non-applicable standards rather than pretending every standard governs every instrument.

## Failure and verification checks
Return NEEDS_DATA/BLOCKED with precise missing inputs when material evidence is absent. A polished paragraph is not a substitute for evidence. Check entity, period, currency, unit, denominator, restatement, point-in-time availability and contradictory evidence. Explain the strongest plausible alternative interpretation and whether it changes the decision. Record material concerns in the issue register. Do not call the human approval action. Confidence is subjective and must state its scope, not pretend to be a calibrated probability.
