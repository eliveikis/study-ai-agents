# Q: **List/dictionary:** given a list of words, return them grouped so that
# each group holds words that are anagrams of each other.

def group_anagrams(input: list[str]) -> list[list[str]]:
    # properties:
    #   - same length
    #   - same letters
    #   - any order

    # so, could start with length and make buckets of words with same length
    # probably a regular expression would really help...but my regex is long gone.
    # i would check with AI naturally for a regex...in the old days I would use
    # an online regex tool and fiddle with it.
    # but let's try the spirit of it

    # dict of buckets of a particular word length containing groups of anagrams.
    buckets_by_len = {}
    for _, val in enumerate(input):
        sorted_val = "".join(sorted(val))
        val_len = len(val)
        # if no buckets for this word length.
        anagram_groups = buckets_by_len.get(val_len, None)
        if anagram_groups is None:
            # add this length with a map of this sorted letter combination to a
            # group of anagrams.
            buckets_by_len[val_len] = {sorted_val: [val]}
        else:
            # see if this letter combo has been entered
            group = anagram_groups.get(sorted_val, None)
            if group is None:
                # add the first one
                anagram_groups[sorted_val] = [val]
            else:
                # append
                group = group.append(val)

    # transform to group of groups
    result: list[list[str]] = []
    for _, anagram_maps in buckets_by_len.items():
        for _, group in anagram_maps.items():
            result.append(group)

    return result


