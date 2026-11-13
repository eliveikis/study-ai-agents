# P4A1 — Targeted coding practice with an HTTP reader

Use 10–20 minutes to study the material below. The full activity has a 75-minute timebox, including study. Questions and answers are at the end, behind a spoiler warning.

## Move the input boundary

The original reader opens a local JSONL file. Now an HTTP client requests a URL and receives a response with a status and body. A successful HTTP status tells you the request succeeded at the protocol level. The body may still be malformed JSONL. Keep transport, parsing, validation, aggregation and display distinct enough to test them separately.

Draw the path on paper: URL → client → status check → text lines → validated records → counts. Include the line number for content errors and the relevant transport diagnostic for request failures.

## HTTP in Python

A request has a method and a URL. A response has a status code, headers and a body. Codes from 200 to 299 mean success, 400 to 499 a problem with the request (404: not found), and 500 to 599 a problem on the server.

- **Standard library.** `urllib.request.urlopen(url, timeout=5)` returns a response with `.status`. `.read()` returns bytes, which `.decode("utf-8")` turns into text. A 4xx or 5xx status raises `urllib.error.HTTPError`, whose `.code` holds the status. A network failure raises `urllib.error.URLError`. A timeout raises `TimeoutError`, or a `URLError` wrapping one, depending on when it happens.
- **`requests`**, a third-party library that isn't a project dependency: `r = requests.get(url, timeout=5)`, then `r.status_code` and `r.text`. `r.raise_for_status()` raises for 4xx and 5xx, and a timeout raises `requests.exceptions.Timeout`.
- **Text to lines.** `text.splitlines()` splits on line breaks and never yields a trailing empty string. `text.split("\n")` does when the text ends with a newline: `"a\nb\n".split("\n")` is `["a", "b", ""]`.

## Testing without the network

Pass the client into the reader instead of creating it inside. The reader then depends only on the small interface it calls, such as one function that takes a URL and returns a status and text. A **fake** is a tiny class with the same interface that returns canned responses, or raises an exception you choose, so tests run offline and give the same result every time. Python doesn't need the fake to inherit anything: any object with the right methods works. `typing.Protocol` can name the interface for type checkers.

The same idea, applied to time instead of HTTP:

```python
class FakeClock:
    def __init__(self, now):
        self._now = now

    def now(self):
        return self._now


def is_expired(deadline, clock):
    return clock.now() > deadline


def test_expired():
    assert is_expired(10, FakeClock(now=11))
```

`unittest.mock.patch` can replace a function inside a module instead, but that ties the test to where the call lives. Passing a fake in doesn't.

Two more tools you'll need:

- **Fixture paths.** `Path(__file__).parent / "data" / "results_sample.jsonl"` finds a file relative to the test file, whatever the current working directory.
- **Exit status.** A CLI signals failure with a non-zero exit status. `sys.exit(1)` exits with status 1; `sys.exit("message")` prints the message to stderr and also exits with status 1. A test can catch it with `pytest.raises(SystemExit)`, where `exc.value.code` holds whatever was passed to `sys.exit`, or run the program with `subprocess.run` and check `returncode`.

## Independent implementation

Start with the most frequent mistake in your log. Give yourself a failing example before coding. Reuse the existing parsing logic by supplying lines from the response. Define the tiny client interface your reader needs. Before writing tests, list the fake responses you'll use and what each test should assert.

Consult the project contract for blank lines and permitted field types. Test the chosen behavior explicitly. Locate fixture files relative to the test file. Check the CLI exit status for errors.

## Transfer check

Try a successful response whose last JSON record has no trailing newline. Predict whether the record should be counted, then verify. Save the corrected implementation and one newly exposed mistake.

---

## ⚠️ SPOILERS: questions and answers

Prepare and attempt using only the text above this line. Everything below it answers the exercise. Read on only once your attempt is frozen.

### Questions

1. Which fake responses would you test, and what should each test assert?
2. Along URL → client → status check → text lines → validated records → counts, where is each failure first detected: a timeout; a 500 status with an HTML error page; a line missing `outcome`?
3. The last record has no trailing newline. Should it be counted? What changes if the body does end with a newline?
4. Which tests exercise the client boundary, and which carry over unchanged from the file version?

**Stop here.** Answer every question aloud before you read on.

### Answers

1. | Fake input | Evidence your test should assert |
   | --- | --- |
   | Successful response with two pass records | Exact count equals two |
   | Non-success status with a text error page | Transport error remains identifiable |
   | Valid JSON missing a required field other than outcome | Correct line and field name |
   | Field present with incorrect type | Validation rejects it |
   | Client raises a timeout | Failure reaches the caller or CLI |
2. The timeout at the client, before a complete response exists. The 500 at the status check, before any parsing, so report it as a transport error, not as malformed JSONL. The missing `outcome` in validation, after JSON decoding, with its line number.
3. Yes: a record is complete without a trailing newline, and both `splitlines()` and iterating over a file yield it. With a trailing newline, `split("\n")` produces a final empty string, which runs into your blank-line rule; `splitlines()` doesn't.
4. The client-boundary tests are those for status errors, timeouts and the success path through the fake. Tests of parsing, validation and aggregation that take lines carry over unchanged, as long as the reader takes lines from either source.
