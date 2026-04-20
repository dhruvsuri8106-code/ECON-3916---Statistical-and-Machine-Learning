# Causal ML — Double Machine Learning for 401(k) Policy Evaluation

## Objective
Estimated the causal effect of 401(k) eligibility on household net financial assets using Double Machine Learning, with a focus on reducing regularization bias and exploring treatment effect heterogeneity across income groups.

## Methodology
- Simulated a causal data-generating process to show how naive LASSO can introduce regularization bias by shrinking the treatment effect toward zero, even when the true ATE is known.
- Used the 401(k) pension plan dataset to study the effect of eligibility on net financial assets.
- Implemented a DoubleML Partially Linear Regression (PLR) framework to separate nuisance estimation from treatment effect estimation.
- Applied Random Forest models as nuisance learners for both the outcome and treatment components.
- Used 5-fold cross-fitting to improve robustness and reduce overfitting in the causal estimation procedure.
- Estimated the Average Treatment Effect (ATE) of 401(k) eligibility on net financial assets.
- Performed Conditional Average Treatment Effect (CATE) analysis by income quartile to assess whether the treatment effect differed across subgroups.
- Visualized subgroup-level CATE estimates with confidence intervals to compare effect sizes across the income distribution.

## Key Findings
- The lab illustrates an important causal inference result: machine learning methods such as LASSO can perform poorly when used naively for treatment effect estimation because regularization can bias the treatment coefficient toward zero.
- The DoubleML PLR approach provides a more credible estimate of the causal effect of 401(k) eligibility by accounting for high-dimensional nuisance structure through cross-fitted machine learning.
- Results suggest that 401(k) eligibility has a positive effect on net financial assets, consistent with the idea that access to tax-advantaged retirement saving vehicles increases household wealth accumulation.
- The CATE analysis shows whether this effect is evenly distributed or concentrated among certain income quartiles, helping evaluate whether the policy has heterogeneous benefits across the income distribution.

## Notes
Replace the placeholder findings with your exact empirical results:
- **Estimated ATE:** 5
- **Income heterogeneity:** Effect stronger amongst Q4
