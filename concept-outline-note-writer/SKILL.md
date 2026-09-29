---
name: concept-outline-note-writer
description: Write concept-first Chinese LaTeX study-note sections from course materials with item-level coverage, priority labels, definitions, scope, comparisons, cases, exam cues, and common mistakes under the study-note-style-v1 contract.
---

# Concept Outline Note Writer

## Purpose

Convert textual course material into concise but complete LaTeX-ready study-note sections. Default to Chinese. Add English labels for concepts and keywords only when the user or orchestration packet explicitly asks.

Read `references/concept-patterns.md` for classification, comparison, and case-writing patterns.

This skill is coverage-id driven. Each concept, comparison, or case must map to assigned coverage item ids. When the orchestration packet specifies `study-note-style-v1`, return body content only and use its priority macros; never emit a preamble or redefine layout.

## Required Inputs

A usable orchestration packet should include:

- Batch id and coverage item ids.
- Source page/title cues and source excerpt or precise source reference.
- Expected section title.
- `importance`: `必背`, `重点`, or `了解`.
- `primary_treatment` and required treatment.
- Parent or adjacent concept sections.
- Formula, diagram, table, glossary, or later-batch cross-reference needs.
- `style_contract: study-note-style-v1` for canonical complete notes.

If source context is missing, flag it instead of replacing it with generic textbook prose.

## Section Pattern

For each concept or textual knowledge point, write:

1. Concept definition.
2. Why it matters.
3. Conditions, assumptions, or scope.
4. Relation to nearby concepts.
5. Course example or case when present.
6. Comparison dimensions in prose when concepts are easily confused; request a table only when it passes the visual gate.
7. Exam or review cue.
8. Common mistakes.

Begin each key concept with the matching canonical macro: `\PriorityMust`, `\PriorityImportant`, or `\PriorityKnow`. For named models, mechanisms, or frameworks, include actors, choices, information, result, driving parameter or institution, and relation to adjacent models before requesting a derivation or visual.

## High-Risk Omission Items

Give explicit body coverage when assigned or source-supported:

- Extensions, appendices, comparisons, intuition, limitations, and remarks.
- Model variants, parameter regimes, empirical-vs-theory conflicts, and policy implications.
- Cases, counterexamples, boundary conditions, and source topics absent from the user's outline but inside scope.

## Rules

- Synthesize; do not copy slide prose in bulk.
- Preserve source emphasis and course-specific terminology.
- Write concept prose before any table or diagram. A visual, formula sheet, or glossary entry never substitutes for body coverage.
- Use compact comparison paragraphs by default. If a table would remove substantial repetition, return its proposed dimensions and rows as a visual request; emit final table LaTeX only when the task packet explicitly delegates an already-approved table.
- Use ordinary paragraphs for cases unless the orchestrator requests a box.
- Keep boxes short. Do not put long concepts, long cases, or multiple unrelated items in one box.
- Avoid invented examples when the source has a named example; use the source example first.
- Do not claim a concept is covered only because a broader parent section exists.
- Do not let a definition replace required model setup, derivation, mechanism, diagram, or formula treatment.
- Flag missing context when a concept depends on a formula, diagram, or prior section outside the packet.

## Output Contract

Return:

- LaTeX-ready section content.
- `Handled coverage item ids: ...`
- A short coverage note for each id: definition, importance, scope, relation, example/case, exam cue, and common mistake.
- Suggested cross-references to formulas, diagrams, tables, glossary entries, or other batches.
- Any unresolved source ambiguity or missing context.

Mark any weakly handled assigned id as `weak` or `unresolved`; never silently treat it as complete.
