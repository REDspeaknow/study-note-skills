# Diagram and Mechanism Patterns

## Selection Ladder

Choose the smallest representation that materially improves understanding:

1. Ordinary concept prose.
2. A compact displayed mechanism chain.
3. A comparison table when it removes substantial repetition.
4. A full TikZ diagram only for genuine spatial, temporal, curve-shift, flow, or equilibrium structure.

Record the coverage ids, source cue, adjacent concept section, and one allowed visual reason. Reject decorative, duplicate, guessed, and coverage-only visuals.

## Overview Relationship Map Pattern

For a complete guide, the user-requested front-matter map summarizes genuine relationships. With 1–3 substantive main sections, map core concepts or mechanisms; with 4 or more, map chapters. Before drawing, return a compact contract:

```text
Nodes: node id -> exact body target -> role -> evidence cue
Edges: edge id -> from -> to -> relation label -> evidence cue
Visual reason: user-requested
```

Use the canonical `study map ...` styles. Prefer a small number of high-value labeled edges: prerequisite, extension/application, assumption failure, remedy, or synthesis. Every node must resolve to body prose (a concept for 1–3 main sections, an actual chapter for 4+); every edge needs evidence. Add `\StudyMapLegend` when its color roles apply, and always include a short prose reading guide. The map appears after the table of contents, but it remains navigation rather than concept coverage. If no defensible edge exists, return an omission reason for `% study-map-omitted: ...` instead.

## Mechanism Chain

Use a chain when a sequence is the main lesson:

```latex
\[
\text{shock}
\Rightarrow \text{intermediate channel}
\Rightarrow \text{curve shift or behavior change}
\Rightarrow \text{new outcome}.
\]
```

Add a short paragraph that states:

- Coverage item id, source cue, and adjacent concept section.
- Initial condition.
- Shock.
- Short-run movement.
- Adjustment process.
- Final outcome.
- Any convention ambiguity.

## TikZ Intersection Pattern

For two-curve equilibrium diagrams:

```latex
\begin{tikzpicture}[>=Stealth, scale=0.9]
  \draw[->] (0,0) -- (6.5,0) node[right] {$X$};
  \draw[->] (0,0) -- (0,4.5) node[above] {$Y$};
  \draw[name path=Acurve, thick] (0.8,3.8) -- (5.8,0.8) node[right] {$A$};
  \draw[name path=Bcurve, thick] (0.8,0.8) -- (5.8,3.8) node[right] {$B$};
  \path[name intersections={of=Acurve and Bcurve, by=E}];
  \fill (E) circle (2pt) node[above right] {$E$};
\end{tikzpicture}
```

Use `\usetikzlibrary{intersections,arrows.meta,positioning}` in the parent document.

## Figure QA Checklist

Before returning:

- Handled coverage item ids, visual reason, source cue, and adjacent concept section are listed.
- Axes are named and match the course convention.
- Curves and shifted curves are labeled.
- Equilibrium points sit on relevant curves or intersections.
- Arrows match the mechanism.
- Labels avoid collisions.
- The surrounding prose explains the sequence.
- Any convention ambiguity is reported to the orchestrator.
- The visual does not duplicate a nearby chain, table, or long caption.
- For either overview map, every node resolves to body prose and every labeled edge appears in the edge-evidence list.

If point placement, arrow direction, or curve shift cannot be inferred from the source packet, do not guess. Return an unresolved assumption.

## Flowchart Pattern

For non-coordinate mechanisms, prefer a displayed math chain. Use a simple TikZ node chain only when branching or layout carries meaning. Keep node text short and put longer interpretation in the adjacent concept prose.
