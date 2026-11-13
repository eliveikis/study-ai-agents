# P4A1 — Targeted coding practice with an HTTP reader

Use 10–20 minutes to study the example and answer the recall questions. The full activity has a 75-minute timebox, including study.

## Move the input boundary

The original reader opens a local JSONL file. Now an HTTP client requests a URL and receives a response with a status and body. A successful HTTP status tells you the request succeeded at the protocol level. The body may still be malformed JSONL. Keep transport, parsing, validation, aggregation and display distinct enough to test them separately.

Draw the path on paper: URL → client → status check → text lines → validated records → counts. Where can each failure first be detected? A timeout occurs before a complete response. A missing outcome occurs after JSON decoding. Include the line number for content errors and the relevant transport diagnostic for request failures.

## Independent implementation

Start with the most frequent mistake in your log. Give yourself a failing example before coding. Reuse the existing parsing logic by supplying lines from the response. Define the tiny client interface your reader needs. A fake client implements that interface with in-memory responses, so tests stay reproducible offline.

| Fake input | Evidence your test should assert |
| --- | --- |
| Successful response with two pass records | Exact count equals two |
| Non-success status with a text error page | Transport error remains identifiable |
| Valid JSON missing a required field other than outcome | Correct line and field name |
| Field present with incorrect type | Validation rejects it |
| Client raises a timeout | Failure reaches the caller or CLI |

Consult the project contract for blank lines and permitted field types. Test the chosen behavior explicitly. Locate fixture files relative to the test file so changing the working directory does not break the test. Check the CLI exit status for errors.

## Transfer check

Try a successful response whose last JSON record has no trailing newline. Predict whether the record should be counted and verify it. Explain which tests exercise the client boundary and which tests still provide value unchanged from the file version. Save the corrected implementation and one newly exposed mistake.
