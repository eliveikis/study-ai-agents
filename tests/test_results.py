from branch_eval.parse import parse_file

def test_valid_jsonl():
    parse_file("tests/data/results_sample.jsonl")

def test_invalid_jsonl():
    try:
        parse_file("tests/data/results_malformed.jsonl")
    except:
        pass
    else:
        raise Exception("failed to parse_file")
