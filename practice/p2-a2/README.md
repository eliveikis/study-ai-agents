# Retrieval versus fine-tuning

## Activity

Phase 2, "Retrieval versus fine-tuning": explain what retrieval-augmented generation supplies at request time and what fine-tuning changes, and discuss why retrieval is a plausible starting point for a private codebase that changes daily. It is evidence for the completion item "Can say what retrieval and fine-tuning each change, and why retrieval suits a codebase that changes daily."

## Time spent

5–10 minutes.

## Review

What it gets right:

- **The retrieval pipeline, in order:** split the corpus into chunks, one embedding vector per chunk, find the chunks most similar to the query, then rerank the top candidates against the query.
- **Cost and freshness as the tradeoff:** the index has to be updated when the code changes, and how much that matters depends on how often it changes and how long a delay is acceptable.
- **Size matters:** "for a codebase of sufficient size" hints at the point that a small enough corpus can go into the prompt whole, with no retrieval.

What's missing or wrong:

- **Fine-tuning isn't covered.** Half the question is what fine-tuning changes: it keeps training the model on examples and changes its weights. That suits teaching a behavior or a format, not facts that change daily. Asked after the review, the human said they had read "fine-tuning" in the question as tuning the RAG pipeline, since the sentence opens with RAG, and described it as setting chunking, chunk size and vector size. Those are retrieval-pipeline settings, which change what the model is given, not the model itself: the distinction Phase 5's item "Can distinguish retrieval-pipeline tuning from model fine-tuning" checks for. In an LLM context, "fine-tuning" alone means training the model further; when a question is ambiguous, ask which is meant.
- **What RAG supplies is wrong.** It supplies the retrieved text itself, put into the model's context with the question, not links to sources. The generation step is missing: the model answers from that text, and can cite the file and revision it came from.
- **"Why retrieval for daily changes" has no comparison.** The argument needs the alternative. A daily change means re-embedding only the changed files' chunks, which is cheap and incremental. Fine-tuning would mean retraining to absorb every change, and weights can't cite a source or check who may read a file. Calling re-indexing an "offline process" whose value "depends on how frequently code is changing" points the wrong way: frequent change is the case where retrieval beats fine-tuning.
- **The query is embedded too.** Similarity is computed between the query's vector and each chunk's vector, not between a chunk and "a given set of tokens".
- **No exact-text search.** In code, identifiers, error strings and config keys need exact matches, which embeddings can miss. Keyword search, alongside embeddings or instead of them, covers that.
- **Reranking is thin.** The reason for the second step is missing: a reranker reads the query and each chunk together, which is more accurate but too slow to run on the whole corpus, so it only reorders a short list.

Verdict: **doesn't meet the item yet.** Fine-tuning is missing, RAG's output is described as links rather than context for generation, and the case for retrieval with daily changes isn't made against the alternative. The pipeline description is a sound base to build on.

## Assistance used

For the first attempt: not reported. After the review, Claude explained fine-tuning and listed the retrieval pipeline's settings.
