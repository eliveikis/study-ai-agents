from p1_two_sum_2.p1_two_sum_2 import group_anagrams

def test_group_anagrams():
    cases = [
        ([], []),
        (["dog"], [["dog"]]), # same length, same word
        (["dog", "dog"], [["dog"]]), # duplicate handling
        (["dog", "god"], [["dog", "god"]]), # same length & anagrams, different words
        (["dog", "god", "cat"], [["dog", "god"], ["cat"]]), # similar
        (["dog", "god", "fish"], [["dog", "god"], ["fish"]]), # different length groups
    ]
    for index, val in enumerate(cases):
        assert group_anagrams(val[0]) == val[1], f"index: {index}"

