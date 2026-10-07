---
name: study-note-unit-writer
description: Write one coherent Chinese study-guide unit from grouped course evidence, combining concepts, necessary derivations, cases, and justified visuals without repeating a full-document template.
---

# Study Note Unit Writer

Write **one learning unit**, not a miniature study guide. The orchestrator supplies a unit question, grouped source/coverage IDs, importance, the source excerpts, prior definitions and notation, and any must-preserve results. Read `references/unit-writing.md` for treatment choices and the handoff format.

## Deliverables

1. `<unit_id>_body.tex`: body content only. It may contain subsection headings, explanations, necessary intermediate algebra, cases, and approved local visuals. It must not contain a preamble, `\begin{document}`, a relationship map, `\section{公式速查手册}`, `FormulaSummaryTable`, a priority overview, or global mistakes. A final equation belongs beside its explanation; a short local takeaway is optional, not a required ending.
2. `<unit_id>_handoff.json`: `unit_id`, `coverage_ids`, `unresolved`, `formula_candidates`, and `continuity_updates`. Each formula candidate has `key`, `name`, `formula`, `conditions`, and `body_label`. Each continuity update identifies a new or changed definition, notation or result with its canonical name, meaning and body label. These are metadata for the orchestrator, not LaTeX for the PDF. Return empty lists when nothing needs nomination or continuity updates.

## Editorial decisions

- Group related coverage IDs around one question or model. An inventory row is evidence to account for, not a command to create a heading or paragraph.
- State each concept once, at the point needed. Use prior definitions and notation from the packet rather than reintroducing them. Cross-reference a prior unit when necessary.
- Choose treatment by need: a short definition for a simple term; one synthesis paragraph and a table for a genuine comparison; one or two sentences for an illustrative case; setup and intermediate algebra for an important model result. Do not emit fixed "why important / scope / relation / exam cue / mistakes" headings for every item.
- Show transformations a learner must understand or reproduce. Compress mechanical substitutions and repeated algebra. Explain assumptions at the step where they matter.
- Use a figure only when the source geometry is examinable or prose is materially less clear. Avoid repeating the same mechanism in prose, table, figure, and caption.
- Include a local warning only when it prevents a likely misunderstanding not already resolved by the explanation. Keep global review lists out of the unit.
- Preserve source-specific claims. Mark insufficient evidence in `unresolved` rather than filling it with generic textbook material.

Before handing off, check that every assigned ID has a traceable place in the body or a specific unresolved note; every formula candidate is already explained in the body; and no claim is restated simply to fill a template slot.
