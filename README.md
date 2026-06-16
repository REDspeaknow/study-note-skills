# Study Note Skills

Codex skills for building complete LaTeX/PDF study guides from course materials.

## Skills

- `auto-study-note-orchestrator`: inventories course materials, batches long sources, dispatches specialist subagents by content type, integrates LaTeX, and runs coverage audit.
- `math-derivation-note-writer`: writes derivation-heavy and formal-reasoning sections.
- `concept-outline-note-writer`: synthesizes definitions, assumptions, cases, comparisons, empirical evidence, and policy implications.
- `diagram-mechanism-note-writer`: creates mechanism chains, diagrams, flows, and TikZ-ready visual explanations.
- `coverage-audit-note-reviewer`: audits source coverage, gap backlogs, compile logs, PDF text extraction, and final completeness.

## Install

Copy the skill folders into your Codex skills directory:

```powershell
Copy-Item -Recurse .\auto-study-note-orchestrator,.\math-derivation-note-writer,.\concept-outline-note-writer,.\diagram-mechanism-note-writer,.\coverage-audit-note-reviewer "$env:USERPROFILE\.codex\skills"
```

Then invoke:

```text
Use $auto-study-note-orchestrator to turn my selected course materials into a complete Chinese LaTeX/PDF study guide.
```

The orchestrator automatically assigns content to specialist subagents by content type unless the user explicitly opts out.
