# Phase 08 — Retrieval and RAG

## Purpose

Treat RAG as an information-retrieval system with a generation component, not
as `embedding → vector database → LLM`.

## WHAT / WHY / WHEN / WHERE / WHO

Retrieval supplies external evidence when model parameters are stale, lossy, or
not attributable. Use it for dynamic/private knowledge and evidence-backed
answers; do not use it to disguise an unauthoritative corpus or replace a
deterministic lookup. Indexers, retrievers, rankers, access-control filters,
context builders, generators, and evaluators own different boundaries.

## HOW

Implement and measure `documents → parsing → chunking → indexing → candidate
retrieval → ranking/reranking → evidence selection → context construction →
generation → citation`. Compare lexical, dense, ANN, hybrid, and metadata
filtering approaches. Track Recall@K, Precision@K, MRR, NDCG, hit rate, answer
correctness, and citation correctness separately.

## FAILURE

Break parsing, chunk boundaries, embedding choice/drift, filters and ACLs,
recall, ranking, context dilution, conflicting/stale evidence, poisoned
documents, citation mismatch, and generators ignoring evidence. Relevance is
not factual truth.

## VERIFY

Prerequisites: Phase 03 evaluation and Phase 07 token/context mechanics.
Enables context engineering, evidence handling, and grounded agents. Exit with
sparse+dense retrieval, no-retrieval baseline, independent retrieval metrics,
exact citation traces, and a failure-attribution report.
