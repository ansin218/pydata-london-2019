# How to Validate Your Client Churn Model
By Elena Sharova

Audience level: Intermediate

## Description

Accurately predicting when clients churn is valuable to many businesses. This talk will cover validation techniques that can be used to assess the adequacy of a client churn model. After reviewing how to fit the Cox Proportional Hazard model with the lifelines library, we will focus on the model validation techniques, such as proportional assumptions, Schoenfeld, martingale and score residuals.

## Abstract

Survival analysis models have been successfully applied to predict the ‘time to churn’ in subscription-based businesses. Nowadays there are a number of Python libraries that allow data scientists to quickly build a ‘churn’ model. However, unlike in a typical linear regression, a proportional hazard model does not easily lend itself to the ‘observed minus predicted’ residuals metric. However, certain regression modelling assumptions like additivity, linearity and distributional assumptions extend to the proportional hazard model and must be examined.

The main objective of this talk is to provide and intuitive explanation of the metrics that can be used to assess the adequacy of a client churn model. The talk will cover mathematical definitions and Python implementation of such metrics. It will cover:

1. The fundamentals of the Cox Proportional Hazard (CPH) model.
2. A brief overview of how to use the lifelines package to fit a CPH model to your data. A brief overview of validation tools currently available in the lifelines package.
3. Practical ideas for selecting covariates and the interactive terms when developing a CPH model.
4. Description of the residuals designed for measuring a CPH model adequacy, how to calculate and interpret them using Python.
5. Overview of alternative to lifelines Python packages (scikit-survival, tick).