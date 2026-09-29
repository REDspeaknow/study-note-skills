---
name: diagram-mechanism-note-writer
description: Decide whether a study-note visual is necessary, then create compact source-grounded mechanism chains, comparison tables, or editable TikZ figures with item-level coverage and QA under study-note-style-v1.
---

# Diagram Mechanism Note Writer

## Purpose

Act as a visual selector first and a visual writer second. Create LaTeX-ready mechanism explanations, adaptive core-knowledge or chapter relationship maps, and editable TikZ figures only when the visual eligibility gate passes. Default to Chinese. Add English labels only when requested.

Read `references/diagram-mechanism-patterns.md` before creating multi-curve, multi-step, or equilibrium diagrams.

This skill is coverage-id driven. Every accepted mechanism chain, table, or figure maps to assigned coverage ids, a source cue, and an already-written adjacent concept section.

## Required Inputs

A usable orchestration packet should include:

- Batch id and coverage item ids.
- Source page/figure/title cues and source excerpt or precise source reference.
- Expected section title and adjacent concept section.
- `visual_needed: yes`.
- `visual_reason`: `source-essential`, `mechanism-essential`, `comparison-efficient`, or `user-requested`.
- Known axes, variables, initial equilibrium, shifts, arrows, and labels when relevant.
- `style_contract: study-note-style-v1` and parent-document TikZ libraries.

If these inputs are insufficient, return `visual rejected` or an unresolved assumption instead of guessing.

## Visual Eligibility Gate

Accept a visual only when at least one condition holds:

- The source graph's geometry, axes, or movement is examinable.
- A spatial, temporal, or equilibrium mechanism would be materially harder to understand in prose.
- A compact comparison table removes substantial repetitive prose across genuinely comparable items.
- The user explicitly requests a more visual treatment.

Reject decorative, duplicate, coverage-only, or weakly sourced visuals. A visual never replaces concept prose.

The canonical overview map is an explicit `user-requested` navigation feature. For 1–3 substantive main sections, use `核心知识关系导图` with source-grounded concept or mechanism nodes. For 4 or more, use `各章节关系导图` with actual chapter nodes. Accept either only with a `map_contract`: every node resolves to body prose and every edge has a meaningful label and evidence cue. Do not connect items merely because they are adjacent in the source. When no genuine relationship exists, record a specific omission reason instead of drawing one.

## Mechanism Pattern

Use displayed math chains for compact mechanisms:

```latex
\[
A\uparrow \Rightarrow B\downarrow \Rightarrow C\text{ shifts left} \Rightarrow Y\downarrow.
\]
```

Then explain the initial condition, shock, timing, adjustment, final outcome, and intuition in concise prose. If a short displayed chain is sufficient, do not expand it into a full TikZ figure.

## Diagram Rules

- Prefer editable TikZ over screenshots for formulas, model diagrams, and mechanisms.
- Prefer the smallest adequate representation: prose first, then a compact math chain, then a table, and only then a full TikZ figure.
- Define axes, curve names, initial and shifted curves, equilibrium points, and arrows.
- Put equilibrium labels at actual intersections, named coordinates, or explicitly calculated coordinates.
- Do not place important points by visual guesswork.
- Check arrow direction, label collision, coordinate conventions, and model timing.
- Keep node text and captions short; put necessary interpretation in the adjacent concept prose.
- Do not repeat the same content in a mechanism chain, diagram, table, and long caption.
- Do not fabricate a diagram when source cues are insufficient.
- For either overview map, use the canonical `study map ...` styles, keep labels short, and provide a prose reading guide below the map. If the complete graph becomes unreadable, keep only high-value edges rather than shrinking text below `\footnotesize`.

## Output Contract

Return:

- Decision: `visual accepted` or `visual rejected`, with the recorded reason.
- LaTeX-ready mechanism text, compact table, and/or TikZ code when accepted.
- `Handled coverage item ids: ...`
- Source cue and adjacent concept section for each visual.
- A short QA note covering point placement, arrow direction, labels, source convention, redundancy, and unresolved assumptions.
- For an overview map: the node-to-body-target list, edge-evidence list, legend meaning when present, and confirmation that no map node or edge is being counted as sole concept coverage.

Mark any unsafe visual as `unresolved`; never silently omit it or draw by visual guesswork.
