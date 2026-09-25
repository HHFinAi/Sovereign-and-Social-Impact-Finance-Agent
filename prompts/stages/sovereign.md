# Sovereign balance sheet and debt vulnerability

**Agent:** Sovereign and Social-Impact Finance Agent · **Stage:** `sovereign` · **Audience:** buy-side analysts, portfolio managers and investment committees.

## Required context and inputs
Read the adopted system prompt, operating contract, selected route, request, evidence register and completed upstream artifacts. Confirm subject and instrument boundaries, as-of date and what the sources actually establish. Resolve this stage's requirements against the preceding work packet; do not treat downstream conclusions as prior evidence.

## Analytical task
Select the applicable debt sustainability framework and latest published country DSA; do not apply LIC methodology universally or prematurely apply September 2026 reforms expected operational in H2 2027. Map general/central government, public enterprises, guarantees, arrears, PPP commitments and other contingent liabilities. Reconcile nominal versus real growth, debt/GDP denominators, primary balance signs, local versus foreign currency, residency versus currency, concessional terms and maturity. Assess fiscal revenues, external balances, reserves, rollover and currency transmission with dated data. Our debt_path helper is a stylized opening-stock arithmetic sensitivity, not an IMF/WB DSA, credit rating or election/policy forecast. Attribute contested interpretations; do not judge politicians' competence or predict election winners.

## Required deliverables
- `fiscal_external_profile`: substantive analysis, supported claim IDs, limitations and decision implications.
- `debt_perimeter`: substantive analysis, supported claim IDs, limitations and decision implications.
- `stress_channels`: substantive analysis, supported claim IDs, limitations and decision implications.

Return `schema_version`, `run_id`, `input_digest`, `stage_id`, `status`, producer identity/type, summary, typed claims, calculation records, standards considered, required sections, gaps, issues and subjective confidence with its basis. Every required section must reference actual claims, not an empty list. Add allowlisted calculations when they materially support the stage; never invent a numeric result. 

## Evidence / method anchors
- WB-DSF: https://www.worldbank.org/en/programs/debt-toolkit/dsf
- IMF-DSF-2026: https://www.imf.org/en/news/articles/2026/09/21/pr26296-lics-imf-executive-board-reviews-the-joint-world-bank-debt-sustainability-framework

Method references are not proof of subject facts or automatic legal compliance. Use the dated register in `references/standards.json`; document non-applicable standards rather than pretending every standard governs every instrument.

## Failure and verification checks
Return NEEDS_DATA/BLOCKED with precise missing inputs when material evidence is absent. A polished paragraph is not a substitute for evidence. Check entity, period, currency, unit, denominator, restatement, point-in-time availability and contradictory evidence. Explain the strongest plausible alternative interpretation and whether it changes the decision. Record material concerns in the issue register. Do not call the human approval action. Confidence is subjective and must state its scope, not pretend to be a calibrated probability.
