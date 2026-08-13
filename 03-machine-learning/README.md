# Phase 03 — Machine Learning

## Objective

Design valid learning problems and experiments before seeking sophisticated models.

## WHAT / WHY / WHEN / WHERE / WHO

Machine learning estimates patterns from data to predict, rank, cluster, compress, or decide under uncertainty. It is useful where explicit rules do not generalize economically and representative evidence exists. It sits between problem/data definition and a product decision. Domain experts define target meaning; data pipelines produce examples; learners fit parameters; evaluators estimate behavior; services and users consume predictions.

## HOW

- `fundamentals/`: task formulation, hypothesis spaces, inductive bias, generalization, bias/variance, regularization, and baselines.
- `supervised-learning/`: linear/logistic models, trees, ensembles, nearest neighbors, and probabilistic outputs.
- `unsupervised-learning/`: clustering, dimensionality reduction, anomaly detection, and representation caveats.
- `model-evaluation/`: splits, cross-validation, metrics, calibration, thresholding, slices, uncertainty, and leakage.
- `experiments/`: configuration, tracking, reproducibility, ablations, error analysis, and decision records.

Start every task with a non-ML baseline and a leakage-safe pipeline. Separate the training objective, evaluation metric, and business outcome.

## FAILURE

Label ambiguity, class imbalance, leakage, duplicate entities across splits, temporal invalidity, selection bias, shortcut features, over-tuning the test set, uncalibrated scores, misleading aggregate metrics, distribution shift, and feedback loops.

## Exit gate

Implement linear and logistic baselines from primitives; compare with a trusted library; conduct slice-based error analysis; quantify uncertainty; and make a ship/no-ship decision from predeclared gates.

