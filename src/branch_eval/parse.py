# Phase 1 task 1 implementation using more low-level Python to help learn.

import sys
import json

def require(d: dict, k: str) -> bool:
    try:
        d[k]
    except KeyError:
        return False
    return True

def validate(result: dict):
    required_keys = [ "trial", "scenario", "config", "attempt", "outcome", "elapsed_s"]
    failed_keys = []
    for key in required_keys:
        if not require(result, key):
            failed_keys.append(key)

    if len(failed_keys) > 0:
        raise KeyError(f"missing keys: {failed_keys}")

    outcome = result["outcome"]
    if outcome not in(("pass", "fail", "error")):
        raise ValueError(f"invalid outcome: {outcome}")

    # optional keys
    #error = result.get()

def parse_file(filename) -> dict:
    with open(filename, encoding=("utf-8")) as file:
        counts = {"pass": 0, "fail": 0, "error": 0}
        for line_number, line in enumerate(file, start=1):
            try:
                result = json.loads(line)
                validate(result)
            except Exception as err:
                raise ValueError(f"line: {line_number}, invalid result: {result} with exception:{err}") from err
            else:
                outcome = result["outcome"]
                counts[outcome] += 1
        return counts

def main():
    if len(sys.argv) < 2:
        raise ValueError("missing argument")
    filename = sys.argv[1]
    counts = parse_file(filename)
    for key, val in counts.items():
        print(f"{key}: {val}")

if __name__ == "__main__":
    main()