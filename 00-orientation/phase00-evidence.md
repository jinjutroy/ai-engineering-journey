# Phase 00 Evidence — AI System Flow

This document records understanding of the AI system flow. Code is optional;
the evidence is the explanation, diagram, use-case analysis, and failure analysis.

## 1. Chosen feature

Feature:
AI email assistant that reads, summarizes, and classifies emails, then proposes
next actions without silently sending or deleting messages.

User or business problem:
Reduce inbox triage time while avoiding missed important emails and unsafe
external actions.

Decision this feature supports:
Which emails need attention, what they mean, and whether a draft or other
follow-up should be proposed.

## 2. End-to-end flow

```text
problem → policy/risk → data/context → mechanism choice
→ model/system output → validation/decision → product action
→ monitoring/feedback → iteration
```

Feature-specific flow:
```text
email → access/policy check → context selection → model classification and
summary → evidence/policy validation → label or draft suggestion → human
approval for send/delete/open-link actions → logging and evaluation
```

## 3. Mechanism choice

- Rules or ordinary software:
- Known spam domains, explicit permissions, keyword search, approval gates, and
  “never auto-delete/auto-send” controls.
- Classical ML:
- Importance or spam classification from labeled examples and email metadata.
- Deep Learning:
- Optional learned language representation for semantic classification.
- Generative AI:
- Thread summarization and reply-draft generation; output remains a proposal.
- Hybrid option:
- Search and policy rules for deterministic boundaries, ML/GenAI for
  classification and language tasks, and human approval for risky actions.
- Why this choice is appropriate:
Use deterministic controls for safety and AI only where understanding language
or reducing repetitive review provides value. Keyword search alone is not
necessarily AI.

## 4. Model, context, and system boundary

Model input:
Email content and permitted metadata, such as sender, recipients, timestamp,
thread structure, and search results.

Request context:
The current email/thread, task instruction, relevant account or business
rules, selected related messages, and any trusted evidence required for the
decision.

Model output:
Importance/spam category, summary, rationale, confidence or uncertainty, and a
draft reply when requested.

Validation and policy layer:
Check sender and access scope, evidence for urgency, confidence thresholds,
privacy/security rules, and whether the requested action requires approval.
Model output is not automatically trusted evidence.

Final product action:
Automatically label, summarize, or create a draft. Ask the user before sending,
deleting, or opening an external link.

## 5. Prediction or request trace

Describe one request from source data to user-visible result.
For an incoming email, the system receives the message and permitted metadata,
checks access policy, selects the current thread and relevant context, then
classifies importance and generates a summary. The system displays the result,
reason/evidence, and a proposed draft. The user approves any external action;
the system records the decision and outcome for later evaluation.

## 6. Failure analysis

| Failure | Detection point | Telemetry | Owner | Safe fallback |
|---|---|---|---|---|
| Data failure: missing or malformed email metadata | Input contract | schema errors, missing-field count | Data/integration owner | Do not classify; show original email |
| Model failure: misses an important email | Validation/evaluation | recall, false-negative review, confidence | ML/system owner | Put in review queue; do not auto-archive |
| Service failure: model/API timeout | Runtime boundary | latency, timeout, availability | Service owner | Keep inbox usable; retry safely or degrade to search/rules |
| User-experience failure: summary hides a required detail | Output review | user corrections, draft rejection, complaint rate | Product owner | Show source thread and require manual review |
| Security failure: unauthorized access or unsafe link | Policy/tool boundary | access denials, tool audit log, injection alerts | Security/system owner | Block action and request human confirmation |

## 7. Build, buy, or avoid AI

Decision:
Use a hybrid assistant. Do not use AI for every email operation; use rules/search
where they are more reliable and GenAI only for language-heavy assistance.

Reasoning about quality, cost, latency, privacy, security, and maintenance:
The system should reduce triage time while preserving important-email recall,
keeping unauthorized sends/deletes at zero, limiting access to permitted mail,
and logging enough evidence to review decisions. Exact thresholds still need a
baseline and a labeled evaluation set.

## 8. What the system does not guarantee

Explain why valid model output, including valid JSON, does not automatically
prove correctness, safety, authorization, or usefulness.
Valid JSON proves only that the output follows a syntax/schema. It does not
prove that “urgent” is factually justified, that the summary is complete, that
the source is trustworthy, or that the proposed action is authorized. The
system needs evidence checks, policy checks, evaluation metrics, and human
approval for high-impact actions.

## 9. Notes-free review

Review date:
2026-09-01

What I could explain without notes:
I can distinguish traditional explicit rules from learned ML behavior; explain
that a model is one component of an AI system; distinguish data, context, state,
and memory; describe policy and approval boundaries; and trace an email from
input through model output to controlled action.

What I still confuse:
I need more practice turning the goal “save time” into concrete success
thresholds and separating model confidence from verified correctness.

Next review date:
To be scheduled after the Phase 00 knowledge check.

## 10. Session knowledge check

Oral check completed: 3/3.

- Model versus context: correct, with the refinement that a model is a learned
  mapping and context is request-time information supplied to it.
- Keyword search versus AI: correct; deterministic search can retrieve emails,
  while AI can classify, summarize, or interpret the results.
- Valid JSON versus correctness: correct; syntax validity does not prove
  factual correctness, safety, authorization, or usefulness.

This session establishes `explained` evidence. Phase 00 is not yet `verified`
until the HTML knowledge check and the remaining checklist evidence are
completed.
