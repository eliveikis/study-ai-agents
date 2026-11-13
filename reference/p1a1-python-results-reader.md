# P1A1 — Python through a useful program

Use 10–20 minutes to study the example and answer the recall questions. The full activity has a 90-minute timebox, including study.

## Read one trial at a time

A trial is one attempt by an agent at a scenario. JSON is a text format for values such as objects, strings, and numbers. JSONL puts a complete JSON value on each physical line, so a reader can handle one trial at a time without loading the entire file.

Trace three outcomes on paper: pass, fail, pass. Start with an empty dictionary. After the second record it maps pass to 1 and fail to 1. After the third, only the pass count changes. A missing dictionary key needs an initial count of zero. If a function uses a mutable dictionary as a default argument, later calls can accidentally inherit earlier counts. Create fresh counts inside each invocation.

## Rehearse the reader

1. Review your existing implementation in `src/branch_eval/parse.py`. Use the Trial record in the project’s `specs/architecture.md` for the required fields and types.
2. Explain the boundary between decoding JSON and validating a record. A well-formed object can still lack its outcome. Associate every diagnostic with its physical line number, counting from one. In Python, `enumerate(lines, start=1)` supplies that number.
3. Keep aggregation separately callable so tests can assert exact counts. Let the CLI handle display and an unsuccessful exit. Ensure a failure midway cannot look like a complete result.
4. Run the supplied sample and malformed fixtures. Expect four passes, one failure and one error on the sample. The malformed fixture should identify line 3 and the missing outcome. Run `make check` in the project.

## Recall and evidence

Why can parsing succeed and validation fail? Give a valid JSON object with the wrong shape. Why can a test pass even when the counts are wrong? A test that only calls the function may never compare its return value. Save one assertion that would catch a wrong count. The progress log already records a working reader. Carry the deferred field-type, blank-line and CLI cases into P4A1.
