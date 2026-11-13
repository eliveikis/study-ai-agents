
# Q: **String:** given a string, return the index of its first character that
# appears only once, or -1 if there is none.

def first_unique_char(text: str) -> int:
    # todo: validation
    # if not isinstance(text, str):
    #     raise ValueError(f"str expected, got:{type(text)}")

    seen = {}
    # First, count appearances of each character.
    for _, char in enumerate(text):
        seen[char] = seen.get(char, 0) + 1

    # Now return the first one that was seen only once.
    for index, (_, count) in enumerate(seen.items()):
        if count == 1:
            return index
    return -1