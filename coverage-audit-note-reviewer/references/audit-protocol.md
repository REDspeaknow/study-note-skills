# Audit Protocol

## Inputs

Expected inputs:

- Source inventory table (`source_inventory.md` or `.csv` for long sources).
- Batch plan and batch mini-audits for long sources.
- Generated `.tex`.
- Canonical `study-note-style.sty` when `study-note-style-v1` applies.
- Compiled `.pdf`.
- LaTeX `.log`, when available.
- Extracted PDF text, when available.
- User's requested scope and language rule.
- Gap backlog when user/reviewer missing topics were supplied.
- Output of `validate_study_note.py` for canonical notes.

## Commands

```powershell
pdfinfo '.\notes.pdf'
pdftotext -layout -enc UTF-8 '.\notes.pdf' '.\notes_extracted.txt'
Select-String -Path '.\notes.log' -Pattern 'Error|Warning|Overfull|Underfull'
pdftoppm -png -r 120 -f 1 -l 3 '.\notes.pdf' '.\qa_page'
```

## Coverage Procedure

1. Read the source inventory.
2. Confirm it is item-level and every substantive row has importance, primary treatment, and visual fields.
3. Read the batch plan and confirm every row is assigned; inspect each mini-audit.
4. Read the table of contents and extracted PDF text.
5. Search for each major title, concept, model, formula cue, table, diagram cue, case, extension, limitation, remark, and policy implication.
6. Assign one status to each item.
7. For missing or weak items, say exactly where they should be added.
8. For intentionally omitted items, confirm the reason is valid.

For long sources, also verify:

- The source inventory is item-level, not broad page ranges.
- The batch plan exists and covers all inventory rows.
- Each batch has a mini-audit.
- The final global audit reports counts for all statuses.
- The final PDF length is plausible for the requested deliverable. If final pages are below `source_pages / 8`, or below 25 pages for a 200+ page source, recommend `revise` unless the user requested a compressed summary. These are short-output red flags, not maximum-page limits.
- User- or reviewer-supplied missing topics have a gap backlog with source evidence, target section, required treatment, and closure status.
- The final PDF does not contain workflow-only sections such as source inventory, batch plan, mini-audit summary, subagent merge area, or global coverage audit, unless the user asked for an audit appendix.

## Gap Backlog Audit

When reviewing a screenshot or missing-topic list:

1. Transcribe each listed item into a gap row.
2. Search source text for exact and approximate evidence.
3. Search final PDF text for the same topic, variables, author names, formulas, and close synonyms.
4. Mark each item:
   - `resolved`: explicit body coverage exists.
   - `weak`: only parent-topic or passing mention exists.
   - `missing`: no meaningful coverage exists.
   - `out of scope`: not supported by the provided source range.
5. Recommend `revise` if any source-supported item is `weak` or `missing`.

Named-topic patterns that require explicit coverage when source-supported:

- Complete model setup: agents, timing, information, objectives, constraints, payoff/utility/profit functions, equilibrium concept, and institutional background.
- Decision rule: threshold, stopping, participation, pricing, investment, portfolio, bidding, matching, default, disclosure, policy, or estimation rule.
- General model version: if the source includes a general `n`-agent, multi-period, stochastic, heterogeneous-agent, multi-asset, open-economy, or multi-sector case, a special-case-only note is weak.
- Key formula or theorem: lower/upper bound, probability, multiplier, elasticity, risk premium, valuation identity, FOC, Euler equation, Bellman equation, estimator, variance, test statistic, or steady-state formula.
- Comparative statics: key parameter signs, boundary cases, welfare effects, pass-through, sensitivity, and intuition.
- Empirical and policy content: theory-vs-fact conflict, institutional rule, identification caveat, regulation channel, market-design implication, and tradeoff.
- Connection across models: benchmark vs extension, partial vs general equilibrium, short run vs long run, reduced form vs structural, complete vs incomplete information, risk-neutral vs risk-averse, accounting identity vs behavioral equation.
- Scope note: when the source only teases a later model or gives partial materials, the note must say so rather than fabricate or silently omit.

Illustrative examples may come from search/auction/platform models, IS-LM/AD-AS, growth and business-cycle models, asset pricing, derivatives, corporate valuation, banking and credit, labor matching, discrete choice, panel regression, IV/GMM/DiD/event studies, or any course-specific model. The audit should generalize from the source, not rely on a fixed topic list.

## Quality Procedure

Check:

- PDF exists, has pages, and text extracts.
- Chinese text is readable.
- TOC includes all major units.
- Formulas are native LaTeX and not screenshots.
- Derivations show setup, notation, intermediate algebra, final result, and intuition.
- Diagrams are eligible, source-grounded, editable or justified if not, and adjacent to concept prose.
- Equilibrium points and arrows are correct.
- Approved boxes are used consistently.
- Formula sheet, memorization-priority overview, and global mistakes reflect the main body content and occur in canonical order.
- Workflow artifacts are absent from the final PDF body unless the user requested an audit appendix.

## Canonical Style Gate

For `study-note-style-v1`:

1. Confirm the TeX loads `study-note-style.sty` and the style declares `study-note-style-v1`.
2. Confirm ordinary Latin text fonts include embedded Times New Roman and mathematics includes XITS Math.
3. Confirm PDF link annotations have zero-width borders and the table of contents remains clickable.
4. Reject missing-font or font-substitution messages, unresolved references, non-A4 pages, or unreadable text.
5. Confirm priority markers use the canonical macros and render as stars rather than missing-glyph boxes.
6. Render and visually inspect the title/TOC, a concept-heavy page, a formula page, the priority overview, and the global mistakes section.
7. Inspect the front-matter relationship map: for 1–3 main sections require core knowledge nodes, and for 4 or more require chapter nodes. Check node-to-body resolution, edge evidence, short labels, readable type, and legend consistency. If omitted, verify the recorded source-grounded reason.
8. Inspect every formula-summary topic table: repeated three-column headers, clean page breaks, body provenance, and specific applicability/use/warning notes.

## Content-Balance Gate

For every substantive concept, locate explicit prose containing its definition and role. Tables, diagrams, formula summaries, glossaries, and boxes are supplements only.

For every visual, require:

- One allowed `visual_reason`.
- Source page/figure/title cue.
- Coverage ids.
- Adjacent concept section.
- A QA note and no redundant nearby representation.

Visual counts are diagnostic, not a fixed quota. Recommend `revise` whenever visuals are decorative, repetitive, guessed, disproportionately expanded, or used in place of concepts.

## Recommendation

Use:

- `pass`: no substantive missing items, all gates pass, and only harmless warnings remain.
- `pass with notes`: minor warnings or justified omissions.
- `revise`: missing content, weak derivation, unjustified visual, cleanliness failure, implausibly short PDF, or important warning.
- `block`: compile failure, unreadable PDF, missing required fonts, visible link borders, missing long-source artifacts, or major scope omission.

Block or revise when:

- The source has 120+ pages and no explicit inventory artifact.
- The source has 120+ pages and no batch plan.
- The audit appendix uses only broad source ranges without item-level coverage.
- Substantive slide titles, proofs, examples, or comparison tables are absent from the PDF text and have no justified omission note.
- A user-provided missing-topic list contains unresolved source-supported items.
- The final PDF includes workflow artifacts as numbered study-guide sections without explicit user request.
