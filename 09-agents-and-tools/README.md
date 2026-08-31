# Phase 09 — Agents and Tools

## Purpose

Treat an agent as a control system whose model proposes actions inside explicit
state, policy, tool, budget, and evaluation boundaries.

## WHAT / WHY / WHEN / WHERE / WHO

An agent updates state, selects an action, observes the environment, and
terminates. Use one only when deterministic code or a state machine cannot
represent the needed interaction. The model proposes; validators and policy
authorize; tools execute; state stores; monitors observe; humans approve
sensitive transitions.

## HOW

Implement a framework-free loop with typed schemas, two tools, explicit state,
allowlists, retries, timeouts, idempotency, step/token/cost budgets,
termination, deterministic replay, approval boundaries, and traces. Only then
compare a framework and document its abstraction and lost control.

## FAILURE

Break planning, tool choice, schemas, stale state, prompt injection, confused
deputy, excessive permissions, repeated actions, timeout/retry storms, loops,
context overflow, unsafe side effects, nondeterminism, and cost explosion.

## VERIFY

Prerequisites: Phase 07 inference and Phase 08 retrieval/evidence. Enables
production orchestration. Exit with adversarial tool outputs, replayable traces,
bounded termination, approval tests, and drills for every listed failure.
