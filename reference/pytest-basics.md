# pytest basics

Install once per environment with `python -m pip install pytest`. Run tests with `python -m pytest -q`. Python’s `-m` runs the pytest module using that interpreter. The pytest flag `-q` shortens the output.

## Write and run a test

Save this as `test_math.py`. pytest discovers functions whose names start with `test_`.

```python
def double(n):
    return n * 2

def test_double():
    assert double(3) == 6
```

Run just this test with `python -m pytest -q test_math.py::test_double`. A false assertion or an unexpected exception fails the test.

## Expect an exception

```python
import pytest

def test_missing_key():
    data = {}
    with pytest.raises(KeyError) as exc:
        data["email"]
    assert exc.value.args == ("email",)
```

If the lookup returns normally, pytest reports `DID NOT RAISE`. An unrelated exception also fails the test. To check text, use `pytest.raises(KeyError, match="email")`; the pattern is a regular expression.

## Handle exceptions manually

- `except KeyError as err` catches the error so you can inspect it. Catching and only printing it can let a test pass. A bare `raise` re-raises it.
- `else` runs if the `try` block finishes normally. In a manual expected-error test, put `pytest.fail("Expected KeyError")` here.
- `finally` runs for cleanup even when an error propagates or the function returns. Code after the block runs only if control reaches it.
- Raise an exception object such as `KeyError(key)`. To add context while preserving the original error, use `raise RuntimeError("Lookup failed") from err`. The traceback shows both errors. The new exception’s `__cause__` holds the original.

## Debug one test in VS Code

Set a breakpoint by clicking beside a line number. Right-click the test’s ▶ icon and choose **Debug Test**. Inspect variables when execution pauses, then press **F5** to continue. If no test icon appears, open **Python: Configure Tests** from the Command Palette and select **pytest**.
