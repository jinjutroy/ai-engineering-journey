# Phase 08 — Retrieval and RAG

## Seven-dimension map

**WHAT:** retrieval finds evidence relevant to an information need; RAG conditions generation on retrieved evidence. **WHY:** model parameters are lossy, stale, and difficult to attribute. **WHEN:** use for dynamic or private knowledge and evidence-backed answers; avoid when the corpus is not authoritative or deterministic lookup suffices. **WHERE:** between request understanding and generation. **WHO:** indexers produce searchable representations; retrievers/rerankers select evidence; generators and users consume it. **HOW:** study lexical scoring, embeddings, approximate nearest neighbors, chunking, metadata filters, reranking, context construction, and separate retrieval/generation evaluation. **FAILURE:** missing/poisoned corpus, bad chunk boundaries, embedding drift, filter bugs, recall loss, citation mismatch, prompt injection inside documents, access-control leaks, and generators ignoring evidence.

## Exit gate

Build a small sparse and dense retriever, evaluate recall independently, compare with a no-retrieval baseline, trace citations to exact chunks, and defend trust boundaries.

