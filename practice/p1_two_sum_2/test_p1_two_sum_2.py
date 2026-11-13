import pytest
from p1_two_sum_2.p1_two_sum_2 import group_anagrams

def test_group_anagrams():
    cases = [
        (["dog", "god"], [["dog", "god"]]),
    ]
    for index, val in enumerate(cases):
        assert group_anagrams(val[0]) == val[1], f"index: {index}"

