---
name: auto-study-note-orchestrator
description: Turn course materials into a concise, source-traceable Chinese LaTeX/PDF study guide with coherent learning units, necessary derivations, one document-level formula reference, and PDF quality checks.
---

# Auto Study Note Orchestrator

Create a guide that a learner can review: complete in key claims and derivations, concise in presentation. Use `study-note-style-v1` for visual consistency. The source inventory tracks evidence; it does **not** prescribe one section per slide or a full template per concept. Read `references/orchestration-workflow.md` for multi-file work and `references/style-contract.md` when assembling a complete document. Copy the canonical assets instead of rebuilding the preamble.

## Roles

- The orchestrator owns source inventory, synthesis plan, notation, cross-unit continuity, formula selection, final assembly, coverage and repetition audit, compilation, and PDF validation.
- `$study-note-unit-writer` owns a coherent unit's concept explanation, necessary derivation, cases, and approved visuals together. Reuse one writer across adjacent units when supported. Do not split one unit among concept, math, and figure agents.
- `$coverage-audit-note-reviewer` is optional for a requested independent review or a concrete unresolved concern; it is not a routine drafting agent.

The user may opt out of subagents. If delegation is unavailable, follow the same unit contract locally.

## Workflow

1. **Ground the scope.** Inspect source files, page counts, existing notes, and user priorities. Extract text and inspect source figures where needed. Mark ambiguous evidence rather than filling gaps.
2. **Build an item-level source inventory for traceability.** Record substantive concepts, results, derivations, cases, and visuals with precise source cues. Mark administrative material and true duplicates. Keep it outside the PDF.
3. **Plan learning units.** Group related inventory IDs around a question or model in `synthesis_plan.md`. For each unit, state its central claim, needed setup/derivation, source IDs, prior notation, and any justified visual. Preserve the user's requested order.
4. **Draft unit bodies.** Send one bounded unit packet to `$study-note-unit-writer`; receive `<unit_id>_body.tex` and `<unit_id>_handoff.json`. The body is a fragment, never a standalone guide. Check missing IDs, algebra, unsupported claims, and repeated explanations before continuing.
5. **Assemble once.** Merge units, normalize notation and links, and remove repeated definitions, setup, cases, warnings, and boxed restatements. The orchestrator alone writes front matter and optional end matter. Collect formula candidates from handoffs, resolve duplicate keys and conflicting conditions, and select distinct high-value retrieval targets explained in the body. If useful, create **one** `\section{公式速查手册}` after all main units, with topic-grouped `FormulaSummaryTable`s. Never append a table to each unit.
6. **Verify.** Map every inventory ID to a specific body passage or justified omission. Audit repetition and information density alongside coverage. Compile until references stabilize, run `scripts/validate_study_note.py`, inspect representative PDF pages, and report source limitations.

## Boundaries

- Unit writers may propose formula candidates in JSON but may not emit document-level summary sections or `FormulaSummaryTable` in TeX fragments.
- A formula sheet, glossary, diagram, or title mention does not by itself teach a substantive claim. A comparison table plus a concise governing explanation can cover comparison dimensions without parallel prose for every cell.
- A named model warrants full setup only when the source develops it and that setup is needed for understanding or assessment. Show essential algebra; do not expand every identity into a model card.
- Do not use a page-count floor or ceiling as a completion proxy. Report page and content-count changes as diagnostics.
- Preserve source and previous outputs. Workflow files stay outside the guide.

For a complete deliverable, link the PDF, TeX, inventory, synthesis plan, and coverage/repetition audit. State when original files were unavailable and an earlier note was the only basis for revision.
