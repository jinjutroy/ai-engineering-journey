# The AI System Stack

## WHAT

The AI stack is the set of layers required to turn a goal and evidence into a maintained behavior. A practical decomposition is: product policy, data, representation/features, model, training, evaluation, inference, application orchestration, platform, observability, and governance/security.

## WHY

Layering localizes responsibility and failures. “The AI is wrong” is not actionable; “the online tokenizer version differs from training” is. Without explicit boundaries, teams cannot reproduce results, secure trust transitions, estimate cost, or decide where to intervene.

## WHEN

Use this map during design reviews, debugging, build-versus-buy decisions, incident response, and ownership planning. Do not mistake it for a fixed vendor architecture; small systems may combine layers, while large systems split them into many services.

## WHERE

```text
Goal, policy, and risk constraints
              ↓
Raw sources → validation → versioned data → features/tokens
              ↓                         ↓
        training pipeline → model artifact + metadata
                                   ↓
evaluation sets → quality/safety gates → registry
                                   ↓
request → auth/validation → inference → policy/grounding → product action
              ↘ logs/traces/feedback/outcomes ↙
                    monitoring and iteration
```

## WHO

Producers include users, sensors, operational databases, annotators, and upstream services. Consumers include training jobs, evaluators, inference services, policy components, product interfaces, analysts, and monitors. Owners must be explicit for datasets, models, services, evaluation suites, and incident response.

## HOW

Each boundary needs a versioned contract:

- **Data:** schema, semantics, lineage, consent, retention, freshness, and quality checks.
- **Representation:** deterministic transformation version, vocabulary, normalization statistics, and unknown handling.
- **Model artifact:** architecture, weights, dependencies, training configuration, and provenance.
- **Evaluation:** immutable test identity, slice definitions, metrics, uncertainty, and acceptance thresholds.
- **Inference:** request/response schema, resource limits, batching, timeout, idempotency, and fallback.
- **Observability:** correlation ID, versions, latency, resource use, quality proxies, outcomes, and privacy-safe samples.
- **Governance/security:** identity, least privilege, audit, deletion, content/data boundaries, and human approval.

An output should be traceable to input version, transformation version, model version, configuration, and relevant external evidence. This is the AI equivalent of a debuggable distributed system.

## FAILURE

- Schema drift is accepted silently and changes feature meaning.
- Training and serving transformations diverge.
- Test data leaks into tuning or becomes stale relative to production.
- A model registry stores weights but not tokenizer/configuration.
- Retry storms amplify slow inference; batching improves throughput but violates latency SLOs.
- Cached outputs ignore model or knowledge version.
- Logs capture sensitive prompts or labels without retention controls.
- Feedback loops learn from model-influenced outcomes and reinforce mistakes.
- A generated string crosses into SQL, shell, HTML, or a tool call without validation and authorization.

## Architecture exercise

Design an AI-assisted search box. Specify every contract, version, trust boundary, metric, owner, timeout, and fallback. Then remove the model and determine which layers still remain; most of them should.

