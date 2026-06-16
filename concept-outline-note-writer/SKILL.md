---
name: concept-outline-note-writer
description: Write Chinese concept-focused LaTeX study note sections from course materials. Use when Codex needs to extract and synthesize textual knowledge points, definitions, assumptions, mechanisms in prose, comparisons, typologies, cases, tables, exam summaries, and common mistakes for a complete study guide.
---

# Concept Outline Note Writer

## Purpose

Convert textual course material into concise but complete LaTeX-ready study-note sections. Default to Chinese. Add English labels for concepts and keywords only when the user or orchestration packet explicitly asks.

Read `references/concept-patterns.md` for classification, comparison, and case-writing patterns.

## Section Pattern

For each concept or textual knowledge point, write:

1. Concept definition.
2. Why it matters.
3. Conditions, assumptions, or scope.
4. Relation to nearby concepts.
5. Course example or case when present.
6. Exam or review cue.
7. Common mistakes.

## Rules

- Synthesize; do not copy slide prose in bulk.
- Preserve source emphasis and course-specific terminology.
- Use comparison tables for easily confused concepts.
- Use ordinary paragraphs for cases unless the orchestrator requests a box.
- Avoid invented examples when the source has a named example; use the source example first.
- Flag missing context when a concept depends on a formula, diagram, or prior section outside the packet.

## Output Contract

Return:

- LaTeX-ready section content.
- Coverage item ids handled.
- Any suggested cross-reference to formulas, diagrams, tables, or glossary entries.
