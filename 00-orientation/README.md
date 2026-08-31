# Phase 00 — Orientation and AI System Flow

## Purpose

Build one stable mental model of an AI system before studying algorithms or
tools. This phase is about understanding the core problem, the system flow,
and the boundary between model output and real-world action.

Code is optional in this phase. The required evidence is a clear explanation,
diagram, use-case analysis, and failure analysis.

## Core flow

Use this flow for every AI feature:

```text
1. Problem and user decision
        ↓
2. Policy, risk, and success criteria
        ↓
3. Data and request context
        ↓
4. Choose the mechanism: rules, ML, DL, GenAI, or hybrid
        ↓
5. Model/system output
        ↓
6. Validate output and make a controlled decision
        ↓
7. Product action and user experience
        ↓
8. Monitoring, feedback, and iteration
```

For each arrow, identify the owner, contract, trust boundary, failure mode,
and fallback. A model is only one component in this flow.

## Core questions

- What problem or decision are we trying to improve?
- Why is AI needed instead of rules, search, SQL, or ordinary software?
- What input, data, and context are available at decision time?
- Is the context complete, relevant, current, and trustworthy?
- Should the system use rules, ML, DL, GenAI, or a hybrid?
- What does the model output mean, and what does it not guarantee?
- Who or what validates the output before action?
- What happens when the model is wrong, slow, unavailable, or unsafe?
- How will quality, cost, latency, privacy, and user impact be monitored?

## Study order

1. [what-is-ai.md](what-is-ai.md)
2. [ai-vs-ml-vs-dl-vs-genai.md](ai-vs-ml-vs-dl-vs-genai.md)
3. [ai-engineer-role.md](ai-engineer-role.md)
4. [ai-stack.md](ai-stack.md)

## Folder map

```text
00-orientation/
├── README.md                         # phase overview and core flow
├── what-is-ai.md                     # AI scope and purpose
├── ai-vs-ml-vs-dl-vs-genai.md        # capability boundaries
├── ai-engineer-role.md               # role and ownership
├── ai-stack.md                       # system layers and contracts
├── phase00-evidence.md               # completed learner evidence
├── concepts/                         # focused overview notes
├── practice/                         # exercises and review guidance
└── knowledge-check/index.html        # offline self-check UI
```

The root documents provide the shared vocabulary. The supporting folders keep
deeper overview notes, practice guidance, and self-assessment separate from
the phase entry point.

## Knowledge check

Complete [the Phase 00 knowledge check](knowledge-check/index.html) after
reading the four documents. The quiz checks the core mental model rather than
memorization. Aim for at least 8/10, then complete the reflection questions
and record unresolved points in [phase00-evidence.md](phase00-evidence.md).

## Required evidence

- Draw the core flow for one familiar feature.
- Trace one input from source data and context to output and product action.
- Explain the difference between AI, ML, DL, and GenAI using one example.
- Explain the difference between a model, context, and the surrounding system.
- Write five failure scenarios spanning data, model, service, user experience,
  and security.
- Explain why “the model returned JSON” does not prove the system is correct.
- Defend whether to build, buy, or avoid AI for the chosen feature.

## Deliberate break lab

Take a hypothetical content classifier and inject: a missing field, irrelevant
context, a shifted label distribution, a slow model response, an adversarial
input, and a silently stale model. For each, state where it should be detected,
what telemetry is required, who owns the response, and the safe fallback.

## Out of scope for Phase 00

Do not go deep into Linear Algebra, Calculus, prompt optimization, RAG
implementation, agent frameworks, or model serving yet. Those topics belong to
later phases after the system flow is understood.

## Exit gate

Without notes, explain the four documents in this folder and draw the complete
AI system flow. A reviewer should be able to challenge your assumptions about
AI selection, context quality, output correctness, quality, cost, latency,
privacy, security, and operations.

