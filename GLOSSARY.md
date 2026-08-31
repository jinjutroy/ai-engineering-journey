# Glossary

Definitions are intentionally compact; concept documents contain the full
WHAT / WHY / WHEN / WHERE / WHO / HOW / FAILURE / VERIFY treatment.

- **Abstention:** intentionally refusing to answer or act when evidence, confidence, or authorization is insufficient.
- **Ablation:** controlled removal or change of one component to estimate its contribution.
- **Agent:** a bounded control loop in which a model helps select actions based on state and observations.
- **Attention:** content-dependent weighted aggregation of value vectors using query–key compatibility.
- **Backpropagation:** efficient application of the chain rule through a computational graph, usually reverse-mode automatic differentiation.
- **Baseline:** simplest credible reference system against which changes are measured.
- **Calibration:** agreement between predicted probabilities and observed frequencies.
- **Causal mask:** constraint preventing a sequence position from attending to future positions.
- **Context:** selected, ordered information supplied to a model for one task or decision; it is not the same as a database or memory.
- **Context engineering:** selecting, prioritizing, compressing, ordering, and budgeting context for a model or agent.
- **Cross-entropy:** expected negative log probability assigned to the observed target; common classification and language-model objective.
- **Data leakage:** information unavailable at legitimate prediction time entering training or evaluation.
- **Embedding:** learned or constructed vector representation in which geometry carries useful relationships.
- **Evidence:** an observation or source that supports, contradicts, or limits a claim; it requires provenance and does not guarantee truth.
- **Gradient:** vector of partial derivatives describing local change of a scalar with respect to parameters.
- **Hallucination:** generated content unsupported by supplied evidence or relevant reality.
- **Inference:** using a fitted model to compute outputs for inputs.
- **KL divergence:** asymmetric measure of how one probability distribution differs from another.
- **KV cache:** stored attention keys and values that avoid recomputation during autoregressive decoding.
- **Memory engineering:** externalizing, retrieving, correcting, consolidating, and expiring experience outside model weights.
- **Model:** parameterized mapping learned or selected to solve a task under assumptions; one component of an AI system.
- **MLE / MAP:** maximum likelihood estimation / maximum a posteriori estimation; optimization with likelihood alone or likelihood plus a prior.
- **MRR / NDCG:** ranking metrics measuring reciprocal rank and graded relevance with position discount.
- **Overfitting:** fitting training-specific variation that harms generalization.
- **Parameter:** value learned during training; a hyperparameter configures training or model structure.
- **Perplexity:** exponentiated average negative log-likelihood per token; comparable only under compatible tokenization and data.
- **Provenance:** trace linking a claim, memory, or context item to its source, time, transformation, and access policy.
- **Prompt injection:** untrusted content attempting to override instructions or obtain unauthorized behavior.
- **RAG:** retrieval-augmented generation, where external evidence is retrieved and supplied to a generator at inference time.
- **Recall@K:** fraction of relevant items found among the top K retrieved candidates.
- **Regularization:** constraints or penalties intended to improve generalization or stability.
- **State:** current task variables, observations, decisions, and control metadata needed to continue a workflow.
- **Token:** discrete unit processed by a language model, produced by a tokenizer.
- **Tool:** typed capability that lets a model or agent observe or change an external environment.
- **Transformer:** architecture built around attention, position information, feed-forward transformations, residual paths, and normalization.
- **Vectorization:** expressing operations over arrays so optimized kernels replace interpreter-level loops.
