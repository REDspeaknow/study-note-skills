# Concept Patterns

## Definition Pattern

Use ordinary LaTeX paragraphs unless the canonical style provides an appropriate short box:

```latex
\paragraph{概念。}
...
\paragraph{为什么重要。}
...
\paragraph{常见误区。}
...
```

Under `study-note-style-v1`, begin key concepts with `\PriorityMust`, `\PriorityImportant`, or `\PriorityKnow`. A concise definition can use `definitionbox`; core takeaways can use `takeawaybox`; mistakes can use `mistakebox`. Keep long explanations outside boxes.

## Comparison Pattern

Use compact prose first. Request a table only when two or more concepts, regimes, extensions, assumptions, or policy tools are easily confused and the table removes substantial repetitive prose. The prose definition for each concept must already exist. Emit final table LaTeX only when the orchestration packet confirms that the visual gate has approved it.

```latex
\begin{center}
\begin{tabular}{p{0.25\textwidth}p{0.32\textwidth}p{0.32\textwidth}}
\toprule
维度 & 概念 A & 概念 B \\
\midrule
含义 & ... & ... \\
适用条件 & ... & ... \\
考试提醒 & ... & ... \\
\bottomrule
\end{tabular}
\end{center}
```

## Case Pattern

For source cases:

1. State the case in one or two sentences.
2. Connect it to the concept.
3. Extract the exam-useful lesson.
4. Avoid long narrative detail.
5. List the handled coverage id.

## Coverage QA

Before returning, confirm:

- The handled coverage item ids are listed.
- The concept's definition is present.
- The concept's role in the course argument is explained.
- Similar concepts are distinguished.
- Source examples or cases are not silently dropped.
- Extensions, limitations, remarks, and policy implications are not collapsed into parent-topic mentions.
- No table, diagram, formula sheet, or glossary entry is being used as the sole concept coverage.
- No English labels are added unless requested.

## Model and Mechanism Completeness

For named textual models or mechanisms, do not write only a broad overview. Include:

- What problem the model solves.
- Who the actors are.
- What each actor knows and chooses.
- What result the model predicts.
- Which parameter or institutional feature drives the result.
- How it differs from the previous model.
- How it is used in the course's larger argument.
- Which derivation, diagram, or formula coverage ids must be handled elsewhere.

A concept definition cannot substitute for model setup, decision rules, equilibrium conditions, or algebraic derivations when the source includes them.

## Empirical, Policy, and Platform Topics

When the source includes empirical evidence, policy tools, or platform governance, give them explicit body coverage:

- For empirical-vs-theory conflict, write the theoretical prediction, the observed fact, and why they differ.
- For regulation or institutional design, distinguish private incentive, externality/market failure, policy instrument, incidence, and unintended consequence.
- For distributional or concentration effects, distinguish extensive margin, intensive margin, selection, scale economies, network effects, risk sharing, and welfare incidence.
- For market integration or segmentation, state the channel through information, logistics, finance, regulation, pricing, search, capital mobility, labor mobility, or platform governance.
- For labor, credit, banking, or matching platforms, separate matching efficiency, separation/default risk, market tightness/liquidity, screening, moral hazard, and information-channel scale from match quality.

## Economics and Finance Topic Families

Use the same completeness standard across domains:

- Micro/IO: preferences, technology, demand, cost, market structure, strategic timing, equilibrium, welfare, and comparative statics.
- Macro: households, firms, government/central bank, resource constraints, laws of motion, equilibrium, shocks, transition dynamics, and policy rules.
- Finance: cash flows, discount rates, risk measures, no-arbitrage conditions, payoff replication, capital structure, valuation method, and sensitivity analysis.
- Econometrics: estimand, estimator, assumptions, identification strategy, sampling variation, inference, diagnostics, and interpretation.
- Banking/credit: balance sheets, constraints, incentives, default/liquidity risk, regulation, and systemic channels.

If a reviewer or user names one of these topics as missing, return a patch-ready section or table; do not merely say it is "covered by" a broader section.
