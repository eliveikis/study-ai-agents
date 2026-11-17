# Layered quiz

## Activity

Phase 8, "Technical mock", run as a quiz, at the human's choice, one day before the interview. It has three layers: what things are; how and why; what breaks, and the tradeoffs. Each layer covers every topic once, in three batches of four short questions. Python questions build up to a FastAPI app with a client test.

Topics: inference and decoding, the agent loop, tool schemas and MCP, retrieval versus fine-tuning, the retrieval pipeline, context management, evals, the job service, metrics and adoption, and Python.

Each batch is a file, `l<layer>b<batch>.md`, with its questions answered in place.

## Time spent

Not reported yet.

## Review

### Layer 1, batch 1

Answered and graded in chat.

1. **Right.** At temperature 0, decoding is greedy. Not said: at 1 the model samples from its unmodified distribution, and values in between sharpen or flatten it.
2. **Partly.** The flow is right, though the question's "tool call" was vague. Wrong: the final reply to the user is plain text, not a tool call. The loop ends because the response has no tool call. Missing: the model only emits a structured request, and the harness runs it, appends the result and calls the model again.
3. **Partly.** It's missing that the model *chooses* the tool from the description and *writes the arguments* to fit the schema. That's what tells you which to fix: a wrong tool choice means the description, and bad arguments mean the schema. The output schema is right for MCP, where it's the optional `outputSchema`.
4. **Right**, though the question's "what does RAG change" was unclear. The sharper contrast: RAG changes what the model sees, the input on each request, which updates instantly. Fine-tuning changes the weights, which shapes behaviour and style and is slow to update. Retrieval needn't use embeddings: keyword search and grep count.

### Layer 1, batch 2

Answered in `l1b2.md`.

5. **Right.** The relevance reason is the main one: one vector for a whole document averages its topics, so it matches no query well. "For structure" was vague. The two concrete limits are that an embedding model has a maximum input length, so a long document can't be embedded whole, and that retrieved chunks go into the prompt, so they have to be small enough for several to fit.
6. **Right.** Sharper: compaction usually means the model summarises the older turns, or old tool results are dropped, and that replaces them in the context. The risk is a detail needed later being silently lost, like an exact error message, a file path or a constraint the user set, without the agent knowing it's gone. "Like any compression system" isn't quite true: lossless compression exists. Compaction is lossy because a summary picks what to keep.
7. **Partly.** (a) is the answer, but it comes after "it's not clear", next to points that answer other questions. Only the PRs where one agent succeeded and the other failed carry evidence. Those where both succeeded or both failed say nothing about which is better. The totals fix the net difference at 2 but not how many PRs disagree: 2 to 0 and 6 to 4 both give 16 and 14. (b) and (c) are about whether the 20 PRs are the right task set, and (d) is about other metrics. Those are fair follow-ups, but they don't say which PRs carry the evidence. The p2a4 review found the same gap: why only the disagreeing PRs count.
8. **Don't know.** Claude gave hints, not code: create a `FastAPI()` instance, decorate a function with `@app.get("/health")`, return a dict, and serve it with `fastapi dev <file>.py` or `uvicorn <module>:app`.

## Assistance used

Claude wrote the questions, and gives corrections after each batch. Batch 1 was answered in chat. Its answers are copied verbatim into `l1b1.md`. Batch 2 was answered in `l1b2.md`. For question 8, Claude gave hints but no code.
