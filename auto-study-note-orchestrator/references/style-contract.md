# Study Note Style Contract v1

Read this when creating or auditing a complete document. `study-note-style-v1` fixes the **visual language**, not the number of paragraphs or document modules.

## Canonical assets

Copy `assets/通用笔记模板.tex` and `assets/study-note-style.sty`. Compile with XeLaTeX. Keep the package's A4 geometry, FandolKai/FandolHei Chinese text, Times New Roman ordinary Latin text, XITS Math, priority macros, colors, boxes, and `hyperref` `hidelinks` behavior. Do not rebuild these in the main TeX.

Use `\PriorityMust`, `\PriorityImportant`, and `\PriorityKnow` to show study priority. Do not force a priority marker on every paragraph.

## Document structure

Keep a compact title block, clickable contents, and coherent main chapters. Optional modules follow their purpose:

- Add a source-grounded relationship map after the contents only when it improves navigation. Its nodes resolve to body sections and its edges express real relationships. Otherwise omit it; a comment `% study-map-omitted: <reason>` can document the decision.
- Add at most one `\section{公式速查手册}` **after all main chapters** when the guide has distinct formulas worth retrieving. Group rows by topic with `FormulaSummaryTable` and `\FormulaSummaryRow`. A row contains one canonical result and its minimum conditions/use. No intermediate algebra, worked substitution, or numerical-example step belongs here.
- Add a priority overview or global mistakes section only when it condenses cross-chapter decisions that the body does not already make easy to retrieve. Keep each brief and place it after the main body and any formula reference.

The presence or absence of optional modules does not change the style version. The unit writer does not author any of them.

## Content and visual economy

A key concept needs an accurate explanation, not a seven-heading block. A comparison may use a governing sentence plus table. A model may need a full setup once, then shorter inherited results. Put equations beside the explanation that licenses them.

Choose the smallest adequate representation: prose, compact chain, comparison table, then full diagram if spatial or equilibrium geometry matters. A figure or table must add information or reduce repetition. Do not repeat its content in a long caption and adjacent paragraph. Keep boxes short and optional.

## QA

The validator checks technical and structural invariants: style marker, A4, fonts, extractable text, link borders, references, optional module order, and unit-fragment boundaries. Editorial review checks source coverage, derivation correctness, formula provenance, and redundancy; counts are diagnostics rather than quotas.
