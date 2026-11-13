import pytest
from p1_two_sum.p1_two_sum import first_unique_char

def test_p1_two_sum():
    cases = {
        "": -1,
        #None: -1 # leaving out for now, requires checking error, or returning -1
        "a": 0,
        "aa": -1,
        "aba": 1,
        "abab": -1
    }
    index = 0
    for k, v in cases.items():
        assert first_unique_char(k) == v, f"index: {index}"
        index += 1

