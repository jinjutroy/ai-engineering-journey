# Glossary

Definitions are intentionally compact; concept documents contain the full seven dimensions.

- **Ablation:** controlled removal or change of one component to estimate its contribution.
- **Agent:** a bounded control loop in which a model helps select actions based on state and observations.
- **Attention:** content-dependent weighted aggregation of value vectors using query–key compatibility.
- **Backpropagation:** efficient application of the chain rule through a computational graph, usually reverse-mode automatic differentiation.
- **Baseline:** simplest credible reference system against which changes are measured.
- **Batch:** group of examples processed together for computational efficiency and a gradient estimate.
- **Bias:** systematic error from assumptions or estimator behavior; context determines the precise meaning.
- **Calibration:** agreement between predicted probabilities and observed frequencies.
- **Causal mask:** constraint preventing a sequence position from attending to future positions.
- **Checkpoint:** serialized model and training state sufficient to resume or reproduce a stage.
- **Concept drift:** change in the relationship between inputs and targets over time.
- **Context window:** maximum token sequence a model can condition on for a request.
- **Data leakage:** information unavailable at legitimate prediction time entering training or evaluation.
- **Embedding:** learned or constructed vector representation in which geometry carries useful relationships.
- **Epoch:** one logical pass over the training dataset.
- **Feature:** measurable input variable supplied to a model.
- **Gradient:** vector of partial derivatives describing local change of a scalar with respect to parameters.
- **Hallucination:** generated content unsupported by supplied evidence or relevant reality.
- **Inference:** using a fitted model to compute outputs for inputs.
- **KV cache:** stored attention keys and values that avoid recomputation during autoregressive decoding.
- **Latency:** elapsed time for an operation; report its distribution, not only its mean.
- **Loss:** differentiable training objective used to update parameters; it may differ from the business metric.
- **Model:** parameterized mapping learned or selected to solve a task under assumptions.
- **Overfitting:** fitting training-specific variation that harms generalization.
- **Parameter:** value learned during training; a hyperparameter configures training or model structure.
- **Perplexity:** exponentiated average negative log-likelihood per token; lower is better only under compatible tokenization/data.
- **RAG:** retrieval-augmented generation, where external evidence is retrieved and supplied to a generator at inference time.
- **Regularization:** constraints or penalties intended to improve generalization or stability.
- **Seed:** initializer for pseudo-random processes; fixing it helps reproduction but does not remove stochastic uncertainty.
- **Serving skew:** mismatch between training-time and inference-time data or transformations.
- **Token:** discrete unit processed by a language model, produced by a tokenizer.
- **Throughput:** amount of work completed per unit time under a stated workload.
- **Transformer:** architecture built around attention, position information, feed-forward transformations, residual paths, and normalization.
- **Vectorization:** expressing operations over arrays so optimized kernels replace interpreter-level loops.

