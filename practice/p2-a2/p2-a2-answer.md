## Q

Explain what retrieval-augmented generation supplies at request time and what fine-tuning changes. Discuss why retrieval is a plausible starting point for a private codebase that changes daily.

## A

RAG provides links to relevant sources, e.g. documents, or urls, or whatever the target corpus is to search, which are most relevant to a query. It does this by a process which breaks the corpus down into chunks, which are then used to create vector embeddings which include a single vector for each chunk, which can be used to calculate it's approximate "distance" or relevance to a given set of tokens (i.e. a user query). The lookup process returns a list of most-similar chunks, which can then be re-ranked by comparing the original query again to the top chunks, to further refine the results.

For a codebase of sufficient size, RAG can provide inexpensive results to find relevant parts of the code. When the corpus changes, the underlying chunks and vector embeddings must be updated, which is an offline process, so the value of the RAG approach depends on how frequently code is changing, available compute, and how much delay is acceptable for updated results.