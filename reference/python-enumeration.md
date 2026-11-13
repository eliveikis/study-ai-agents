# Python enumeration

Use `for item in values` for items alone. Use `for i, item in enumerate(values)` for a counter and an item. The counter starts at 0. Pass `start=1` for human-readable numbering.

| Type | Loop | What you get |
|---|---|---|
| List, tuple | `for i, x in enumerate(seq):` | Index and element |
| String | `for i, ch in enumerate(text):` | Index and character |
| Range | `for i, n in enumerate(range(10, 20, 2)):` | Counter and number, starting with `(0, 10)` |
| Set, frozenset | `for i, x in enumerate(s):` | Counter and element in unspecified order |
| Dict | `for key in d:` | Key |
| Dict | `for key, val in d.items():` | Key and value |
| Dict | `for i, key in enumerate(d):` | Counter and key |
| Dict | `for i, val in enumerate(d.values()):` | Counter and value |
| Dict | `for i, (key, val) in enumerate(d.items()):` | Counter, key, and value |
| Bytes, bytearray | `for i, b in enumerate(data):` | Index and integer byte (0–255) |
| Generator, iterator | `for i, x in enumerate(it):` | Counter and next item |

**Text file** — count lines from 1 while reading:

```python
with open("notes.txt", encoding="utf-8") as f:
    for line_no, line in enumerate(f, start=1):
        print(line_no, line.rstrip("\n"))
```

Numbers, booleans, and `None` aren't iterable. To loop a given number of times, use `for i in range(n):`.
