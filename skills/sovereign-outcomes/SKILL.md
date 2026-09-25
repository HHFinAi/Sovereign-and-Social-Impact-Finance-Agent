---
name: sovereign-outcomes
description: "Perform outcome measurement and payment verification for Sovereign and Social-Impact Finance Agent; use when this bounded buy-side research task is requested, not for trading or compliance certification."
license: MIT
---

# Outcome measurement and payment verification

Read `../../prompts/stages/outcomes.md`, `../../prompts/system.md` and `../../AGENTS.md` before using this skill. The complete repository must remain available; this file alone is not the workflow or its dependencies.

Apply the stage's research instructions to the supplied issuer/instrument/portfolio evidence. Return the structured stage artifact with these sections: `theory_of_change`, `verification_and_payment`, `outcome_risk`. Follow the source, calculation, material-gap and human-review boundaries. Use the Python runtime from the repository root for enforced handoffs; text-only use is manual and does not enforce gates.

Do not auto-start a research run or call a broker. Host-specific discovery and activation are not certified. See `../../schemas/artifact.schema.json` and `../../templates/host-artifact-guide.md`.
