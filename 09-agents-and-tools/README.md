# Phase 09 — Agents and Tools

## Seven-dimension map

**WHAT:** an agent is a bounded loop that updates state, chooses actions, observes results, and terminates. **WHY:** some tasks require interaction with changing external systems. **WHEN:** use only when the workflow cannot be represented more safely as deterministic code or a state machine; do not grant open-ended authority for high-impact actions. **WHERE:** in the orchestration layer above models and below product policy. **WHO:** a model proposes, validators authorize, tools execute, state stores record, monitors observe, and humans approve sensitive transitions. **HOW:** implement explicit state, typed tool schemas, allowlists, budgets, idempotency, retries, termination, traces, and eval scenarios before adopting an agent framework. **FAILURE:** prompt injection, confused deputy, excessive permissions, retry duplication, loops, stale state, hidden tool errors, cost explosion, nondeterminism, and irreversible actions.

## Exit gate

Implement a framework-free tool loop with two tools, deterministic replay, a step/time/cost budget, approval boundary, adversarial outputs, and safe termination.

