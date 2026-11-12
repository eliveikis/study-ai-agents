# Phase 1 task 1 implementation using more low-level Python to help learn.

import sys
import json

def require(d: dict, k: str) -> bool:
    try:
        d[k]
    except KeyError as err:
        return False
    return True

def validate(result: dict):
    required_keys = [ "trial", "scenario", "config", "attempt", "outcome", "elapsed_s"]
    failed_keys = []
    for key in required_keys:
        if not require(dict, key):
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
        for line in file:
            result = json.loads(line)
            try:
                validate(result)
            except Exception as err:
                raise Exception(f"invalid result: {result} with exception:{err}")
            outcome = result["outcome"]
            counts[outcome] += 1
        print(f"pass: {counts["pass"]}, {counts["fail"]}, {counts["error"]}")

def main():
    if len(sys.argv) < 2:
        raise ValueError("missing argument")
    filename = sys.argv[1]
    parse_file(filename)

if __name__ == "__main__":
    main()