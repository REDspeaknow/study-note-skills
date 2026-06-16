---
name: diagram-mechanism-note-writer
description: Write mechanism chains, flow diagrams, and editable TikZ model figures for Chinese LaTeX study guides. Use when Codex needs to explain causal chains, policy transmission, curve shifts, equilibrium movement, model diagrams, timelines, flowcharts, or figure QA from course slides.
---

# Diagram Mechanism Note Writer

## Purpose

Create LaTeX-ready mechanism explanations and editable TikZ figures. Default to Chinese. Add English labels only when the user or orchestration packet explicitly requests them.

Read `references/diagram-mechanism-patterns.md` before creating multi-curve, multi-step, or equilibrium diagrams.

## Mechanism Pattern

Use displayed math chains for compact mechanisms:

```latex
\[
A\uparrow \Rightarrow B\downarrow \Rightarrow C\text{ shifts left} \Rightarrow Y\downarrow.
\]
```

Then explain the timing and intuition in prose.

## Diagram Rules

- Prefer editable TikZ over screenshots for formulas, model diagrams, and mechanisms.
- Define axes, curve names, initial and shifted curves, equilibrium points, and arrows.
- Put equilibrium labels at actual intersections, named coordinates, or explicitly calculated coordinates.
- Do not place important points by visual guesswork.
- Check arrow direction, label collision, coordinate conventions, and model timing.

## Output Contract

Return:

- LaTeX-ready mechanism text and/or TikZ code.
- Coverage item ids handled.
- A short diagram QA note: point placement, arrow direction, labels, and unresolved assumptions.
