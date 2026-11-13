import pytest
from branch_eval.parse import parse_file

def test_valid_jsonl():
    expected = {"pass": 4, "fail": 1, "error": 1}
    counts = parse_file("tests/data/results_sample.jsonl")
    assert len(counts) == 3
    for key, val in expected.items():
        assert counts[key] == val

def test_invalid_jsonl():
    #try:
    #    parse_file("tests/data/results_malformed.jsonl")
    #except:
    #    pass
    #else:
    #    raise Exception("failed to parse_file")
    with pytest.raises(ValueError, match="line: 3"):
        parse_file("tests/data/results_malformed.jsonl")