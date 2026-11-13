# Python through a useful program

Use 10–20 minutes to study the material below. Questions and answers are at the end, behind a spoiler warning.

## Read one trial at a time

A trial is one attempt by an agent at a scenario. JSON is a text format for values such as objects, strings, and numbers. JSONL puts a complete JSON value on each physical line, so a reader can handle one trial at a time without loading the entire file.

Trace three outcomes on paper: pass, fail, pass. Start with an empty dictionary. After the second record it maps pass to 1 and fail to 1. After the third, only the pass count changes. A missing dictionary key needs an initial count of zero.

**Default arguments are evaluated once.** Python evaluates a default value when it defines the function, not on each call. A mutable default such as `def f(counts={})` is the same dictionary object on every call, so later calls inherit earlier counts. Create fresh counts inside each invocation, or default to `None` and build the dictionary inside.

## Decoding and validating are separate steps

`json.loads` checks only that a line is well-formed JSON, and turns it into Python values. It raises `json.JSONDecodeError`, a subclass of `ValueError`, when the syntax is wrong. It knows nothing about trial records. Validation is your own code checking the decoded value against the Trial record in the project's `specs/architecture.md`: is it an object, are the required fields present, and do they have the right types? Associate every diagnostic with its physical line number, counting from one. In Python, `enumerate(lines, start=1)` supplies that number.

## What makes a test fail

pytest fails a test only when an assertion is false or an exception escapes it. A test that calls a function and checks nothing passes whatever the function returns. `pytest-basics.md` has the details.

## Rehearse the reader

1. Review your existing implementation in `src/branch_eval/parse.py`. Use the Trial record in `specs/architecture.md` for the required fields and types.
2. Keep aggregation separately callable so tests can assert exact counts. Let the CLI handle display and an unsuccessful exit. Ensure a failure midway cannot look like a complete result.
3. Run the supplied sample and malformed fixtures. Expect four passes, one failure and one error on the sample. The malformed fixture should identify line 3 and the missing outcome. Run `make check` in the project.
4. The progress log already records a working reader. Carry the deferred field-type, blank-line and CLI cases into the HTTP version of the reader (`http-results-reader.md`).

---

## ⚠️ SPOILERS: questions and answers

Prepare using only the text above this line. Everything below it asks the questions and then answers them.

### Questions

1. Why can parsing succeed and validation fail? Give a valid JSON line that isn't a valid trial record.
2. Why can a test pass even when the counts are wrong? Write one assertion that would catch a wrong count on the sample file.
3. What goes wrong with `def count_outcomes(records, counts={})` when it's called twice?
4. Trace fail, error, fail, pass. What does the dictionary hold after each record?

**Stop here.** Answer every question aloud before you read on.

### Answers

1. Parsing checks syntax; validation checks shape. `{"trial": "t-1", "scenario": "S1"}` is valid JSON with no `outcome`. So is `[1, 2]`, which isn't an object at all, and so is a record whose `outcome` is the number `5`.
2. A test that only calls the function never compares its return value, so a wrong count can't fail it. On the sample: `assert counts == {"pass": 4, "fail": 1, "error": 1}`, where `counts` is what your aggregation function returned.
3. The default dictionary is created once, when the function is defined. The second call starts from the first call's counts, so its totals come out too high.
4. `{fail: 1}`, then `{fail: 1, error: 1}`, then `{fail: 2, error: 1}`, then `{fail: 2, error: 1, pass: 1}`.
