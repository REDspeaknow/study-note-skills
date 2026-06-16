# Audit Protocol

## Inputs

Expected inputs:

- Source inventory table.
- Generated `.tex`.
- Compiled `.pdf`.
- LaTeX `.log`, when available.
- Extracted PDF text, when available.
- User's requested scope and language rule.

## Commands

```powershell
pdfinfo '.\notes.pdf'
pdftotext -layout -enc UTF-8 '.\notes.pdf' '.\notes_extracted.txt'
Select-String -Path '.\notes.log' -Pattern 'Error|Warning|Overfull|Underfull'
pdftoppm -png -r 120 -f 1 -l 3 '.\notes.pdf' '.\qa_page'
```

## Coverage Procedure

1. Read the source inventory.
2. Read the table of contents and extracted PDF text.
3. Search for each major source title, model name, formula cue, table name, and case.
4. Assign one status to each item.
5. For missing items, say exactly where they should be added.
6. For intentionally omitted items, confirm the reason is valid.

For long sources, also verify:

- The source inventory is item-level, not broad page ranges.
- The batch plan exists and covers all inventory rows.
- Each batch has a mini-audit.
- The final global audit reports counts for all statuses.
- The final PDF length is plausible for the requested deliverable. If a 200+ page source produces fewer than 25 PDF pages, recommend `revise` unless the user requested a compressed summary.
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
- Derivations show intermediate algebra.
- Diagrams are editable or justified if not.
- Equilibrium points and arrows are correct.
- Approved boxes are used consistently.
- Formula sheet and mistake checklist reflect the main content.

## Recommendation

Use:

- `pass`: no substantive missing items and only harmless warnings.
- `pass with notes`: minor warnings or justified omissions.
- `revise`: missing content, weak derivation, diagram issue, or important warning.
- `block`: compile failure, unreadable PDF, or major scope omission.

Block or revise when:

- The source has 120+ pages and no explicit inventory artifact.
- The source has 120+ pages and no batch plan.
- The audit appendix uses only broad source ranges without item-level coverage.
- Substantive slide titles, proofs, examples, or comparison tables are absent from the PDF text and have no justified omission note.
- A user-provided missing-topic list contains unresolved source-supported items.
- The final PDF includes workflow artifacts as numbered study-guide sections without explicit user request.
