---
name: math-derivation-note-writer
description: Write source-faithful Chinese LaTeX derivations attached to established concepts, with complete setup, intermediate algebra, item-level coverage, interpretation, and compact formula summaries compatible with study-note-style-v1.
---

# Math Derivation Note Writer

## Purpose

Write LaTeX-ready derivation sections for a larger study guide. Default to Chinese explanations. Add English labels for concepts, keywords, or variable names only when the user or orchestration packet explicitly requests them.

Read `references/derivation-patterns.md` when a task needs proof structure, formula expansion, or derivation QA.

This skill is coverage-id driven. A derivation is not complete unless it handles its assigned ids explicitly. Under `study-note-style-v1`, return body content only, inherit the parent concept's notation and importance, and never emit a preamble or redefine formatting.

## Required Inputs

A usable orchestration packet should include:

- Batch id and coverage item ids.
- Source page/formula cues and source excerpt or precise source reference.
- Expected section title and parent concept section.
- Required setup, formulas, assumptions, and notation when available.
- `style_contract: study-note-style-v1` for canonical complete notes.

If source evidence is insufficient, return the strongest source-faithful partial treatment and list the missing assumption instead of inventing a generic derivation.

## Section Pattern

For each derivation item, write in this order:

1. Problem or goal.
2. Full setup for a named model: agents, timing, information, constraints, objectives or payoffs, state variables, and equilibrium concept.
3. Assumptions and notation.
4. Variable definitions.
5. Step-by-step derivation with intermediate algebra.
6. Final formula or result.
7. Interpretation and intuition.
8. Calculation recipe when applicable.
9. Comparative statics, boundary cases, or parameter restrictions when source-supported.
10. Common mistakes.

## Rules

- Return section body only unless asked for a full document.
- Use LaTeX-native formulas; do not describe formulas as screenshots.
- Do not skip intermediate algebra.
- Explain why each non-mechanical transformation is valid.
- Distinguish assumptions, identities, estimators, population parameters, sample quantities, and conclusions.
- Preserve source notation unless the packet explicitly requests normalization.
- Attach the derivation after its parent concept; do not restate the complete concept section.
- Keep the derivation in ordinary prose and display math. Use `formulabox` only for a short final formula summary and `proofbox` only for a short proof takeaway; never put a long derivation in a box.
- A formula-sheet entry may summarize a derivation only after the body contains its setup and intermediate steps.
- Return each approved end-matter formula as a proposed `\FormulaSummaryRow{名称}{公式}{适用条件、用途或注意事项}` and name its topic group. The third cell must carry the relevant assumption, use, test hypothesis/distribution, priority, or concrete trap; do not use a vague note such as “重要”.
- When source material is ambiguous, preserve the course notation and add a short note for the orchestrator instead of inventing a conflicting notation.

## Output Contract

Return:

- LaTeX-ready content.
- `Handled coverage item ids: ...`
- A short note for each id covering setup, notation, intermediate algebra, final result, intuition, and common mistakes.
- A `Formula summary rows` block grouped by topic, containing only formulas already handled in the returned body and ready for the canonical page-breakable summary tables.
- Any unresolved ambiguity, missing source definition, notation conflict, or source-extraction limitation.

Mark any incomplete assigned id as `unresolved`; never quietly omit it.
