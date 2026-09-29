# Orchestration Workflow

## 1. Source Inventory

Create a compact table before writing:

| id | source | page/slide | raw title or cue | type | importance | primary_treatment | assigned section | required_treatment | visual_needed | visual_reason | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

For long sources, the inventory must be saved as an explicit artifact such as `source_inventory.md` or `source_inventory.csv`. A final document appendix is not a substitute for the working inventory unless it contains item-level rows.

Use these types:

- `concept`: definitions, explanations, assumptions, institutional facts, theory statements.
- `derivation`: algebra, proofs, estimators, first-order conditions, variance formulas.
- `mixed`: a concept that needs both prose and formulas.
- `diagram`: model figures, curve shifts, graphs, timelines, flowcharts.
- `table`: comparison tables, taxonomies, cases by regime.
- `case`: examples or applications.
- `review/admin/omit-candidate`: duplicate review, course logistics, bibliography, or truly outside-scope material.

High-risk omission patterns:

- Slides named extension, appendix, comparison, intuition, between cases, summary, limitations, or remarks.
- Tables comparing model variants.
- Figures that encode a mechanism but have little text.
- A source file that was replaced after earlier extraction.
- Topics not shown in the user's outline but present inside the requested page/session range.

Inventory completeness rule:

- If extracted text contains form-feed page breaks, harvest one title cue per page or slide.
- If a page has no clear title, create a cue from the first meaningful line plus source page number.
- Do not merge dozens of slides into one inventory row. Merge only obvious continuation slides for the same proof, table, or model sequence, and keep the page range precise.

Required-treatment rule:

- `full model card`: any named model or framework, including micro, macro, finance, econometrics, industrial organization, labor, platform, auction, banking, asset-pricing, corporate-finance, and policy models.
- `full derivation`: thresholds, lower/upper bounds, probabilities, equilibrium profit, first-order conditions, Euler equations, budget constraints, law-of-motion equations, steady states, estimators, test statistics, valuation formulas, or comparative-static formulas.
- `comparison table`: model variants, assumptions, parameter regimes, empirical-vs-theory contrasts, policy tools, or easily confused concepts.
- `mechanism chain`: causal sequences, platform mechanisms, matching channels, recommendation effects, or market-integration channels.
- `case note`: empirical examples, experiments, platform cases, regulation examples.
- `empirical-vs-theory note`: slides contrasting theoretical prediction and observed reality.
- `policy note`: regulation, market design, monetary/fiscal policy, financial supervision, disclosure rules, pricing rules, competition policy, macroprudential tools, or institutional implications.

Do not assign a substantive row only to `formula sheet entry` or `glossary entry`; those are supplements, not replacements for body coverage.

Importance values are `必背`, `重点`, and `了解`. Every substantive concept receives `primary treatment: concept body` even when it also needs a derivation, comparison, case, mechanism, or figure.

Default `visual needed` to `no`. Set it to `yes` only with one recorded reason:

- `source-essential`: the source figure's geometry, axes, or movement is examinable.
- `mechanism-essential`: prose alone would materially obscure a spatial, temporal, or equilibrium mechanism.
- `comparison-efficient`: a compact table removes substantial repetitive prose across genuinely comparable items.
- `user-requested`: the user explicitly asked for a more visual treatment.

Decorative, duplicate, guessed, or coverage-only visuals are not eligible.

## 1.5 Gap Backlog From User Feedback

If the user provides a screenshot, handwritten list, reviewer comments, or any missing-topic list, create `gap_backlog.md` before modifying the note or skill.

Use this table:

| gap id | user/reviewer wording | source evidence | mapped inventory id | target section | required treatment | status |
| --- | --- | --- | --- | --- | --- | --- |

Rules:

- Treat the user's missing-topic list as a blocking audit input, not as optional suggestions.
- Search the source text for every named gap. If exact text is absent, search close terms, variables, author names, and formulas.
- If a gap is source-supported, add or revise body content until it has explicit treatment.
- If a gap is not source-supported, add a short scope note outside the final study guide, not a fabricated section.
- Do not close the task while any source-supported gap remains unresolved.

Universal gap patterns that require explicit treatment when source-supported:

- **Model setup gaps**: missing agents, timing, information, constraints, objective functions, payoffs, state variables, equilibrium concept, or institutional environment.
- **Decision-rule gaps**: missing consumer/firm/household/investor/bank/government choice rule, threshold rule, stopping rule, portfolio rule, pricing rule, bidding rule, participation rule, or policy reaction rule.
- **Derivation gaps**: missing intermediate algebra for equilibrium, first-order conditions, Euler equations, Bellman equations, estimator formulas, variance formulas, pricing kernels, no-arbitrage relations, valuation identities, or steady-state expressions.
- **Generalization gaps**: only a special case is covered while the source includes a general `n`-agent, multi-period, heterogeneous-agent, stochastic, open-economy, multi-asset, or multi-sector version.
- **Comparative-static gaps**: missing signs and intuition for key parameters, boundary cases, welfare decomposition, pass-through, elasticity, multiplier, risk premium, matching efficiency, default probability, leverage, or policy intensity.
- **Empirical/policy gaps**: missing empirical evidence, theory-vs-fact conflict, identification caveat, institutional rule, regulation channel, market-design implication, or policy tradeoff.
- **Connection gaps**: missing relationship between adjacent models, such as benchmark vs extension, short run vs long run, partial vs general equilibrium, reduced form vs structural form, risk-neutral vs risk-averse, complete vs incomplete information, or closed vs open economy.
- **Scope gaps**: source contains a teaser or partial introduction, but the note either fabricates a full model or omits the scope limitation. Add an explicit scope note instead.

Examples from any economics or finance course may include search models, auction models, IS-LM/AD-AS, Solow/Ramsey/NK models, CAPM/APT/Black-Scholes, bond duration, DCF/WACC/APV, bank runs, credit rationing, matching models, discrete choice, panel regressions, IV, GMM, DiD, event studies, or market-design mechanisms. These examples are illustrative, not a fixed checklist.

## 2. Outline Construction

Use the canonical `study-note-style-v1` order for complete documents:

1. Compact title block, priority legend, and reading order.
2. Borderless clickable table of contents.
3. Source-grounded relationship map: core knowledge for 1–3 main sections; chapters for 4 or more.
4. Main units.
5. Topic-separated formula summary tables.
6. Memorization-priority overview.
7. Global common mistakes.
8. Closing line.

Count substantive main sections before the formula summary. Build a compact front-matter `map_contract` before drawing:

| node id | displayed concept/chapter | target body section | role | evidence cue |
|---|---|---|---|---|
| edge id | from | to | relation label | evidence cue |

For 1–3 sections, use `核心知识关系导图` and make nodes the important concepts or mechanisms. For 4 or more, use `各章节关系导图` and make nodes the actual chapters. Every node must resolve to body prose. Every edge must be supported by the source or explicit outline and use a meaningful relation label. Use `visual_reason: user-requested`; when no genuine relation can be supported, omit the map and record `% study-map-omitted: <specific reason>` in the TeX. The map is navigation, not inventory coverage.

Within each unit, place definitions, importance, conditions, adjacent-concept relations, source examples, exam cues, and local mistakes before dependent derivations or visuals. The overview map is the only front-matter exception and does not replace later concept prose.

In the final `公式速查手册`, group formula rows by chapter or conceptual family. Use the canonical page-breakable three-column interface: formula name, formula, and applicability/use/warning. Include only body-backed formulas and keep all derivation steps in their parent concept section.

The user's requested outline controls section order. The source inventory controls inclusion. If a source topic does not fit the outline, place it in the nearest relevant section or add a short supplementary subsection.

For model-heavy lectures, every major named model should have a stable subsection with this internal order:

1. Motivation and question.
2. Full setup: agents, parameters, timing, information, actions, payoffs.
3. Decision rule or equilibrium condition.
4. Derivation or proof sketch.
5. Comparative statics or parameter interpretation.
6. Relation to previous and next models.
7. Common mistakes.

Do not let a final PDF consist only of high-level survey sections plus formula sheet; that is a summary, not a complete study guide.

## 3. Auto-Batching

Use auto-batching whenever the source range is more than a small chapter, more than about three lecture files, more than about 80-120 extracted pages, or dense enough that one pass risks skipped derivations or weak audit coverage.

Create a batch plan before drafting:

| batch id | source range | outline sections | estimated density | specialist needs | agent_owner | merge dependencies | status |
| --- | --- | --- | --- | --- | --- | --- | --- |

Batching rules:

- Prefer natural boundaries: lecture, chapter, topic unit, model family, or exam module.
- Keep one proof, model, mechanism chain, comparison table, or named case in a single batch.
- Keep prerequisites before dependent sections, but allow later global reordering during integration if the user's outline requires it.
- Keep each batch small enough that its source excerpts, inventory items, specialist outputs, and mini-audit can all be reviewed together.
- Use smaller batches for derivation-heavy or diagram-heavy material; use larger batches for mostly textual review material.
- If a batch becomes too large while drafting, stop and split it into sub-batches before writing more.

Default thresholds:

- 1-3 lecture files: one batch unless derivation-heavy.
- 4-8 lecture files: split by lecture group or topic unit.
- More than 8 lecture files or a full-course folder: first produce only inventory, outline, and batch plan; then draft batch by batch.
- One dense mathematical chapter can be split by theorem, estimator, model, or proof sequence even if it is a single PDF.

Hard gates:

- Over 120 source PDF pages, 4 lecture files, or 60 inventory rows: create `batch_plan.md` before drafting.
- Over 200 source PDF pages: use at least 4 batches unless the source is mostly administrative or explicitly requested as a short summary.
- Over 200 source PDF pages: final output under 25 PDF pages is a coverage red flag and requires a deeper item-level audit before delivery.
- Do not mark the task complete with only a final `.tex` and PDF. Keep or report the inventory, batch plan, and audit artifacts.

Each batch must end with a mini-audit:

1. All batch inventory items have a status.
2. Derivations in the batch show intermediate algebra.
3. Diagrams or mechanism chains are present when required.
4. New symbols are added to the global symbol list.
5. Cross-references to other batches are recorded.

Do not merge batches until their mini-audits pass or their open issues are explicitly recorded.

## 4. Specialist Delegation Requirements

Specialist delegation is the default architecture of this skill. Invoking `$auto-study-note-orchestrator` should be treated as authorization to use the specialist subagents named by this skill, unless the user explicitly opts out. Do not require the user's prompt to separately say "use subagents".

The architecture is content-type based rather than course-specific. Do not hard-code a course, lecture, textbook, model family, or local folder as the delegation logic. First classify inventory rows by required treatment, then assign owners from the universal role set:

- `formal-reasoning`: formulas, derivations, proofs, algorithms, optimization, statistics, quantitative examples, formal model setup, inference, equilibrium, valuation, and computation.
- `concept-synthesis`: definitions, assumptions, textual theory, taxonomy, cases, institutional context, empirical findings, policy/managerial implications, and comparison dimensions in prose.
- `visual-mechanism`: justified comparison or process tables, mechanism chains, graphs, diagrams, timelines, flows, model movement, and visual QA after the concept body is complete.
- `orchestrator`: planning, inventory, batching, integration, style normalization, cross-reference consolidation, source inventory closure, gap backlog closure, compile/PDF QA, final item-level completeness checks, and final assembly.

For long sources, or any batch with a non-`orchestrator` owner, subagent delegation is mandatory when the environment provides subagent tools:

- `formal-reasoning` batch: delegate to `$math-derivation-note-writer`.
- `concept-synthesis` batch: delegate to `$concept-outline-note-writer`.
- `visual-mechanism` batch: delegate to `$diagram-mechanism-note-writer`.

Automatic ownership rules:

- `formal-reasoning`: any batch or section whose required treatment includes full derivation, proof, FOC, Euler equation, Bellman equation, estimator, variance, equilibrium formula, probability, bound, comparative-static formula, valuation formula, algorithm, quantitative example, or steady-state formula.
- `concept-synthesis`: any batch or section dominated by definitions, assumptions, institutional context, empirical evidence, policy implications, cases, concept distinctions, or comparison dimensions in prose.
- `visual-mechanism`: any batch or section with an approved comparison/process table or requiring mechanism chains, model diagrams, curve shifts, timelines, market-design flows, matching flows, decision trees, causal graphs, Sankey-like flows, platform ranking flows, or TikZ QA.
- `orchestrator`: glue work, style normalization, cross-reference consolidation, preamble integration, coverage and gap closure, deterministic validation, and final assembly.

Coverage review is not a subagent role. The orchestrator performs the item-level status pass and all deterministic compile/PDF gates. When the user explicitly invokes `$codex-with-chatgpt`, use ChatGPT for one independent semantic review at each agreed checkpoint (normally after a completed batch or after the final local validation). ChatGPT reads the inventory and outputs through the workspace connection; do not paste source files, diffs, or logs, and do not dispatch a second coverage-review specialist for the same checkpoint. Without C2C, the orchestrator performs the semantic coverage pass locally.

Mixed batches should be split into multiple task packets and dispatched in dependency order: concept body first, formal reasoning second, and an optional visual packet last. Do not create a visual packet unless `visual_needed: yes` has a valid `visual_reason`.

Owner assignment should be regenerated for every new course or folder. Never reuse a prior course's batch plan, model list, or owner map unless the user explicitly asks to continue that exact project.

If no subagent tool is available, record this exact note in the batch log and delivery note:

```text
Subagent delegation was required by the long-source workflow but no subagent tool was available; local fallback was used.
```

Do not silently skip delegation on a long source.

If the user explicitly opts out of subagents, keep the same ownership table but mark each non-orchestrator row as `local fallback by <owner role>`, then perform the role locally and state that subagents were intentionally disabled.

## 5. Delegation Packet

When using subagents, send a bounded packet:

```text
Use $<specialist-skill> to write the following LaTeX-ready section.
Batch id: ...
Coverage item ids: ...
Agent owner: formal-reasoning | concept-synthesis | visual-mechanism
Style contract: study-note-style-v1
Importance: 必背 | 重点 | 了解
Primary treatment: concept body | derivation | comparison | case | mechanism | ...
Parent concept section: ...
Visual needed: yes | no
Visual reason: source-essential | mechanism-essential | comparison-efficient | user-requested | blank
Expected section title: ...
Language rule: Chinese by default; add English labels only if requested.
Source excerpt: ...
Required output: ...
Style constraints: use ctex-compatible LaTeX, no full document preamble, no unsupported boxes.
Return: section body plus any coverage notes or unresolved source ambiguity.
```

Do not ask specialists to solve the whole document. Give each specialist a disjoint section or content class.

## 6. Batch Integration Template

Store or clearly mark batch fragments with stable names such as:

- `batch_01_learning_map_and_basics.tex`
- `batch_02_core_model_derivations.tex`
- `batch_03_applications_and_cases.tex`

During integration:

1. Preserve the master outline order.
2. Resolve duplicated definitions by keeping the earliest complete definition and replacing later repeats with cross-references.
3. Normalize notation across batches.
4. Consolidate formula sheets, mistakes, and glossary entries.
5. Run a global coverage validation after the merge, not only batch mini-audits. When C2C is active, follow it with one independent ChatGPT semantic review and resolve any findings locally.

Workflow artifacts stay outside the final PDF by default:

- `source_inventory.md`
- `batch_plan.md`
- `batch_*_mini_audit.md`
- `global_coverage_audit.md`
- `gap_backlog.md`
- subagent handoff logs

These files should be linked in the delivery note, not inserted as numbered sections in the study guide, unless the user explicitly asks for an audit appendix.

## 7. Integration Template

Use a new file name such as `course_range_complete_study_guide.tex`. Copy the canonical `assets/通用笔记模板.tex` and `assets/study-note-style.sty` into the output project and integrate content into that skeleton. Do not construct a substitute preamble or duplicate style declarations in the main document.

The style package owns A4 geometry, the supplied colors, FandolKai/FandolHei Chinese fonts, Times New Roman ordinary Latin text, XITS Math, code monospace, heading spacing, priority symbols, light breakable boxes, page numbering, and borderless clickable links.

Default end matter is formula quick reference, memorization-priority overview, and global common mistakes in that order. Add a glossary only when useful or requested; add bilingual entries only when requested.

## 8. Compile and Coverage Audit

Run `scripts/compile_study_note.py --tex <entrypoint>.tex`; it performs one XeLaTeX pass and reruns only while the table of contents, bookmarks, or references are stale. If the bounded retries cannot stabilize them, report a failure. Then audit:

1. PDF exists and has pages.
2. Text extracts in Chinese.
3. TOC contains all major units.
4. Every inventory item has one status: represented, represented indirectly, intentionally omitted, missing.
5. Each missing substantive item is either added or explicitly justified.
6. Complex diagrams render and labels do not collide.
7. Formula-heavy sections do not contain skipped algebra.
8. No disallowed box names appear in new notes.
9. Every substantive concept has prose body coverage before visual support.
10. Every visual has a valid reason, source cue, coverage ids, and adjacent concept section.
11. The PDF embeds Times New Roman and XITS Math, has no visible link borders, and contains no font-substitution warnings.

Run the canonical validator after compilation:

```powershell
python scripts/validate_study_note.py --tex '.\notes.tex' --pdf '.\notes.pdf' --log '.\notes.log' --inventory '.\source_inventory.md'
```

Long-source audit must include:

- Source page count and final PDF page count.
- Inventory row count.
- Batch count and mini-audit status for each batch.
- Number of represented, indirectly represented, intentionally omitted, and missing items.
- A sample of source slide/page titles searched in the output PDF text.

Reject these as insufficient:

- A small appendix with broad ranges such as `pages 1--30 covered`.
- A final PDF with no separate inventory or batch plan for a 120+ page source.
- A claim of completeness when most source slide titles or title cues cannot be found directly or indirectly in the PDF.
- A claim that a model is covered when its setup, decision rule, equilibrium result, and comparative statics are not all represented.
- A claim that user-identified missing topics are resolved without a `gap_backlog.md` or equivalent item-level closure list.

Delivery must include absolute links to the final PDF and TeX source, plus a short note about any intentional omissions or unavailable QA steps.
