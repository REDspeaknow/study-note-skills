# Derivation Patterns

## Generic Derivation Checklist

Include:

- Objective function, equilibrium condition, identity, or theorem statement.
- Assumptions and domain restrictions.
- Complete model setup when the formula belongs to a named model: agents, parameters, timing, information, actions, payoffs, and equilibrium concept.
- Definition of every symbol used in the derivation.
- Intermediate algebra.
- Final result.
- Interpretation and units.
- Comparative statics, boundary cases, and parameter restrictions when the lecture names them.
- Common mistakes.

Avoid:

- Jumping from assumptions to final formula.
- Changing notation from the source without saying so.
- Mixing population and sample notation.
- Treating sufficient conditions as necessary conditions.

## Optimization Pattern

1. State the objective.
2. Define choice variables and constraints.
3. Compute first-order conditions.
4. State second-order or convexity condition when relevant.
5. Solve step by step.
6. Interpret comparative statics or estimator meaning.

## Estimator Pattern

1. State the model.
2. Define data, parameters, estimator, residual, and fitted value.
3. Derive normal equations or moment conditions.
4. Show matrix form if useful.
5. State existence or rank condition.
6. Interpret orthogonality or identification.
7. Give calculation recipe.

## Variance or Distribution Pattern

1. Start from the estimator decomposition.
2. Condition on data or assumptions explicitly.
3. Apply variance rules step by step.
4. Substitute identities such as residual sum of squares, projection matrices, or auxiliary regression results.
5. State the final variance, standard error, or distribution.
6. Explain what increases or decreases precision.

## Proof QA

Before returning, check:

- Every equation follows from the prior line.
- All dimensions or summation indices are compatible.
- Each assumption is used in the correct step.
- The final formula uses the same notation as the task packet.
- Common mistakes target likely exam errors, not generic warnings.

## Economics and Finance Model Pattern

For economics, finance, econometrics, market-design, macro, banking, asset-pricing, corporate-finance, or platform mechanisms, include:

1. Full setup: agents, state variables, controls, distributions, information, constraints, timing, and payoffs/objectives.
2. Individual or institutional decision rule: consume/save/invest, price, search/stop, bid, match, borrow/lend, default, enter/exit, disclose, hire/vacancy, policy reaction, or portfolio choice.
3. Equilibrium or identifying condition: market clearing, no-arbitrage, no profitable deviation, steady-state flow balance, Euler equation, Bellman equation, orthogonality condition, moment condition, incentive compatibility, or participation constraint.
4. Closed-form or semi-closed-form result where the source provides it.
5. Boundary cases and comparisons: special case versus general case, one-period versus dynamic, representative-agent versus heterogeneous-agent, closed versus open economy, complete versus incomplete information, risk-neutral versus risk-averse, or theory versus empirical fact.
6. Parameter effects: signs and intuition for elasticities, discount factors, risk aversion, volatility, interest rates, depreciation, persistence, leverage, default risk, matching efficiency, policy intensity, pass-through, or information frictions.
7. Exam mistakes: confusing constraints with FOCs, levels with dispersion/growth/rates, partial with general equilibrium, movements along a curve with curve shifts, accounting identities with behavioral equations, or teaser topics with fully specified models.

If a task packet names a formula, theorem, estimator, equilibrium condition, price bound, probability, multiplier, valuation equation, variance formula, or comparative-static result, do not return only intuition. Derive the relationship or state exactly which source assumption is missing.
