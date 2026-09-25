# Legal structure, ranking and recourse

**Agent:** Sovereign and Social-Impact Finance Agent · **Stage:** `legal` · **Audience:** buy-side analysts, portfolio managers and investment committees.

## Required context and inputs
Read the adopted system prompt, operating contract, selected route, request, evidence register and completed upstream artifacts. Confirm subject and instrument boundaries, as-of date and what the sources actually establish. Resolve this stage's requirements against the preceding work packet; do not treat downstream conclusions as prior evidence.

## Analytical task
Map creditor, debtor, guarantor, fund vehicle, programme implementer and outcome payer separately. Read governing law, currency, jurisdiction, sovereign immunity, collective action clauses, negative pledge, pari passu, transferability, security, escrow, permitted use and termination. For guarantees, inspect coverage, exclusions, cap, claim conditions, payment delays, subrogation, counterparty and expiry. Do not assume a guarantee makes the entire instrument risk-free or that development commitments rank with debt service. Model restructuring or default only from relevant contractual evidence; no legal opinion is automated. Record specialist questions and block conclusions that depend on unresolved enforceability.

## Required deliverables
- `creditor_rights`: substantive analysis, supported claim IDs, limitations and decision implications.
- `governing_law_and_restructuring`: substantive analysis, supported claim IDs, limitations and decision implications.
- `guarantee_enforceability`: substantive analysis, supported claim IDs, limitations and decision implications.

Return `schema_version`, `run_id`, `input_digest`, `stage_id`, `status`, producer identity/type, summary, typed claims, calculation records, standards considered, required sections, gaps, issues and subjective confidence with its basis. Every required section must reference actual claims, not an empty list. Add allowlisted calculations when they materially support the stage; never invent a numeric result. 

## Evidence / method anchors
- IMF-WB-SWAPS: https://www.imf.org/en/publications/policy-papers/issues/2024/08/05/debt-for-development-swaps-an-approach-framework-553146

Method references are not proof of subject facts or automatic legal compliance. Use the dated register in `references/standards.json`; document non-applicable standards rather than pretending every standard governs every instrument.

## Failure and verification checks
Return NEEDS_DATA/BLOCKED with precise missing inputs when material evidence is absent. A polished paragraph is not a substitute for evidence. Check entity, period, currency, unit, denominator, restatement, point-in-time availability and contradictory evidence. Explain the strongest plausible alternative interpretation and whether it changes the decision. Record material concerns in the issue register. Do not call the human approval action. Confidence is subjective and must state its scope, not pretend to be a calibrated probability.
