# Model, Context, and AI System

## Core idea

A model is one component that transforms input into an output. Context is the
information available to the model at request time. An AI system includes the
model plus data, policy, validation, application behavior, monitoring, and
human or automated decisions.

```text
user input + instructions + history + evidence + tool results
                         ↓
                       model
                         ↓
              output validation and policy
                         ↓
                  product decision/action
```

## Model

A model may produce a class, score, prediction, embedding, or generated
content. Its output is evidence for a decision; it is not automatically the
decision itself.

Examples:

- Linear regression predicts a numeric value.
- A classifier predicts a label or probability.
- A neural network recognizes patterns in images or audio.
- An LLM predicts tokens and generates text.

## Context

Context may include:

- User input
- System instructions and product policy
- Conversation history
- Retrieved documents
- Tool results
- Metadata such as time, locale, or permissions

Context can be missing, irrelevant, stale, conflicting, malicious, or
sensitive. The same model can produce different results when its context
changes.

## AI system

The surrounding system decides:

- What context is collected
- Which model or mechanism is used
- How output is validated
- Who is allowed to act on the output
- What happens when the model fails
- How quality, cost, latency, privacy, and safety are monitored

## Decision ladder

Choose the simplest mechanism that meets the requirement:

```text
ordinary code/rules
        ↓ if rules do not generalize
classical ML
        ↓ if representation or pattern complexity requires it
deep learning
        ↓ if the task requires open-ended generation
generative AI
```

This is a decision aid, not a claim that every system must use these layers
in sequence.

## Failure questions

- Is the input available at decision time?
- Is the context relevant and trustworthy?
- Does the output mean what the product assumes it means?
- Is there a validation or approval boundary before action?
- Can the system fall back safely when the model is wrong or unavailable?
