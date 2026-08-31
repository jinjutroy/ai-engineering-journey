# Phase 03 — Machine Learning

## Purpose

Turn a product question into a valid learning experiment before selecting a
sophisticated model.

## WHAT / WHY / WHEN / WHERE / WHO

The core loop is `Data → Representation → Model → Prediction → Loss →
Optimization → Evaluation → Generalization`. ML is appropriate when
representative data and a learnable signal exist; explicit rules, lookup, or no
AI may be safer. Domain owners define target meaning, data pipelines produce
examples, models estimate parameters, and evaluators estimate behavior.

## HOW

Implement linear regression and logistic regression from primitives, then
compare with trusted libraries. Cover classification, generative versus
discriminative modeling, MLE/MAP, splits, baselines, regularization,
bias/variance, calibration, uncertainty, thresholding, slices, error analysis,
and business metrics. Separate training objective, evaluation metric, and
product outcome.

## FAILURE

Break label definitions, class balance, temporal splits, entity duplicates,
leakage, selection bias, shortcut features, test-set over-tuning, calibration,
aggregate metrics, distribution shift, and feedback loops.

## VERIFY

Prerequisites: Phase 02 probability, statistics, and optimization. Enables
neural-network objectives and reliable model selection. Exit with a non-ML
baseline, from-scratch baselines, leakage audit, slice/error report,
uncertainty estimate, and evidence-backed ship/no-ship decision.
