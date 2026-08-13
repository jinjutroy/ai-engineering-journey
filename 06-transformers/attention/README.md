# Scaled Dot-Product Attention

## WHAT

Attention maps queries to weighted sums of values. Weights are normalized query–key compatibility scores. Scaled dot-product attention uses \(QK^T/\sqrt{d_k}\), an optional mask, and row-wise softmax.

## WHY

Fixed-size recurrence or pooling creates an information bottleneck. Attention lets each query select different information from the available keys. Scaling prevents dot-product variance from growing with key dimension and pushing softmax into saturated, low-gradient regions.

## WHEN

Use it when content-dependent interaction among elements is valuable and its compute/memory fit the workload. Avoid full attention for very long sequences when quadratic score matrices exceed the budget, or when a simpler local/structured operator provides the needed inductive bias.

## WHERE

It is the information-routing sublayer inside transformers and is also used for cross-attention between different sources. Projection layers create Q/K/V; masks encode visibility; residual/normalization paths consume its output.

## WHO

Queries represent information needs, keys represent addresses, and values carry content. Token/position representations produce them; later layers consume the mixed output. Serving engines may cache keys and values during autoregressive decoding.

## HOW

For \(Q\in\mathbb{R}^{n_q\times d_k}\), \(K\in\mathbb{R}^{n_k\times d_k}\), and \(V\in\mathbb{R}^{n_k\times d_v}\):

\[
S=QK^T/\sqrt{d_k}+M,\quad A=\operatorname{softmax}_{rows}(S),\quad O=AV
\]

Therefore \(S,A\in\mathbb{R}^{n_q\times n_k}\) and \(O\in\mathbb{R}^{n_q\times d_v}\). Subtract each row maximum before exponentiation. A causal mask allows key positions \(j\le i\). Complexity is \(O(n_qn_kd)\) compute and \(O(n_qn_k)\) score memory, ignoring projections.

The executable reference is `src/ai_journey/attention.py`.

## FAILURE

Wrong mask polarity, a mask that broadcasts along the wrong axis, fully masked rows producing NaNs, omitted scaling, unstable softmax, swapped sequence/feature dimensions, padding leakage, incorrect causal boundary, quadratic OOM, stale/corrupt KV caches, and interpreting attention weights as faithful causal explanations.

## Lab

Verify row sums and causal invariance; make future values extremely large and prove earlier outputs do not change; remove scaling and measure entropy as \(d_k\) grows; compare against a trusted implementation using fixed arrays.

