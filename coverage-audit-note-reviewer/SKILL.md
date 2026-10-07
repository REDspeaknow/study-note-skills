---
name: coverage-audit-note-reviewer
description: Independently review a Chinese LaTeX/PDF study guide for source coverage, correct derivations, semantic repetition, formula provenance, justified visuals, and technical PDF quality.
---

# Coverage Audit Note Reviewer

Use this skill only when the user requests an independent review or the orchestrator has a concrete unresolved coverage or correctness concern. Read `references/audit-protocol.md` and the orchestrator's `references/style-contract.md` for a complete document.

Review the source inventory, synthesis plan, body fragments, unit handoffs, final TeX/PDF, and available original materials. If originals are absent, state that raw-source completeness cannot be certified.

## Findings to report

- Every substantive inventory ID has a specific passage, an intentional omission reason, or a missing/weak finding. A title, keyword hit, or formula-sheet row alone is insufficient evidence.
- Important derivations have the correct setup, conditions, key intermediate step, and result. Do not demand a full model card for a formula that inherits earlier setup.
- Repeated claims across neighboring units, prose/table/caption/box, exam tips, local mistakes, and end matter are identified with concrete locations. Prefer one clear treatment and a cross-reference.
- Every accepted figure has a source-supported purpose and correct geometry or flow. A comparison table may carry dimensions when a short governing sentence explains the distinction.
- Unit fragments contain no document-level formula tables or summary sections. The final guide has at most one formula-reference section, after all main chapters; each retained row is body-backed and useful for retrieval.
- The PDF passes typography, link, reference, extractability, and layout checks.

Use page counts, source-to-output ratio, and content counts as diagnostics, never automatic evidence of completeness or concision. Give a short pass/revise recommendation with exact fixes rather than a long checklist of passed items.
