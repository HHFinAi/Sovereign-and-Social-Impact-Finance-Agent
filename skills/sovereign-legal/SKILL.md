---
name: sovereign-legal
description: "Perform legal structure, ranking and recourse for Sovereign and Social-Impact Finance Agent; use when this bounded buy-side research task is requested, not for trading or compliance certification."
license: MIT
---

# Legal structure, ranking and recourse

Read `../../prompts/stages/legal.md`, `../../prompts/system.md` and `../../AGENTS.md` before using this skill. The complete repository must remain available; this file alone is not the workflow or its dependencies.

Apply the stage's research instructions to the supplied issuer/instrument/portfolio evidence. Return the structured stage artifact with these sections: `creditor_rights`, `governing_law_and_restructuring`, `guarantee_enforceability`. Follow the source, calculation, material-gap and human-review boundaries. Use the Python runtime from the repository root for enforced handoffs; text-only use is manual and does not enforce gates.

Do not auto-start a research run or call a broker. Host-specific discovery and activation are not certified. See `../../schemas/artifact.schema.json` and `../../templates/host-artifact-guide.md`.
