---
name: math-derivation-note-writer
description: Write derivation-heavy Chinese LaTeX study note sections from course materials. Use when Codex needs to expand mathematical, statistical, econometric, economic, finance, or management-science formulas, proofs, first-order conditions, estimators, variance formulas, model derivations, calculation recipes, and common algebra mistakes for a larger study guide.
---

# Math Derivation Note Writer

## Purpose

Write LaTeX-ready derivation sections for a larger study guide. Default to Chinese explanations. Add English labels for concepts, keywords, or variable names only when the user or orchestration packet explicitly requests them.

Read `references/derivation-patterns.md` when a task needs proof structure, formula expansion, or derivation QA.

## Section Pattern

For each derivation, write in this order:

1. Problem or goal.
2. Assumptions and notation.
3. Variable definitions.
4. Step-by-step derivation with intermediate algebra.
5. Final formula.
6. Interpretation.
7. Calculation recipe when applicable.
8. Common mistakes.

## Rules

- Return section body only unless asked for a full document.
- Use LaTeX-native formulas; do not describe formulas as screenshots.
- Do not skip intermediate algebra.
- Explain why each transformation is valid.
- Distinguish assumptions, identities, estimators, population parameters, sample quantities, and conclusions.
- Use `proofbox` only when the surrounding document has that box defined; otherwise use `\paragraph{推导}` or ordinary subsections.
- When source material is ambiguous, preserve the course notation and add a short note for the orchestrator instead of inventing a conflicting notation.

## Output Contract

Return:

- LaTeX-ready content.
- A short coverage note listing handled coverage item ids.
- Any unresolved ambiguity, missing source definition, or notation conflict.
