
# Q: **String:** given a string, return the index of its first character that
# appears only once, or -1 if there is none.

def first_unique_char(text: str) -> int:
    # todo: validation
    # if not isinstance(text, str):
    #     raise ValueError(f"str expected, got:{type(text)}")

    seen = {}
    # First, count appearances of each character.
    for index, char in enumerate(text):
        record = seen.get(char, None)
        if record is None:
            # The first time a new character is seen, store its index and a
            # counter.
            seen[char] = [index, 1]
        else:
            record[1] += 1

    # Now return the first one that was seen only once.
    for _, record in seen.items():
        if record[1] == 1:
            return record[0]
    return -1