# Diagram and Mechanism Patterns

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

- Initial condition.
- Shock.
- Short-run movement.
- Adjustment process.
- Final outcome.

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

- Axes are named and match the course convention.
- Curves and shifted curves are labeled.
- Equilibrium points sit on relevant curves or intersections.
- Arrows match the mechanism.
- Labels avoid collisions.
- The surrounding prose explains the sequence.
- Any convention ambiguity is reported to the orchestrator.

## Flowchart Pattern

For non-coordinate mechanisms, use a simple TikZ node chain with arrows. Keep node text short and put longer interpretation in prose.
