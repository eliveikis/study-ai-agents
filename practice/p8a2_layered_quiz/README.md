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

## Assistance used

Claude wrote the questions, and gives corrections after each batch. Batch 1 was answered in chat. Its answers are copied verbatim into `l1b1.md`.
