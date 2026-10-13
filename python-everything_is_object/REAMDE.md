# Python - Everything is object

This project explores how Python treats everything as an object: how names
bind to objects, the difference between **equality** and **identity**,
mutable and immutable types, and how CPython manages memory for integers,
strings and tuples.

## Learning objectives

- What `id` and `type` do
- What mutable and immutable objects are
- What the difference between `==` and `is` is
- What an alias is, and how assignment binds a name to an object
- How arguments are passed to functions, and what that means for mutable
  and immutable objects
- How CPython caches small integers, interns strings and reuses the empty
  tuple

## Requirements

- Ubuntu 20.04 LTS (or WSL), Python 3 (`/usr/bin/python3`)
- Python scripts start with `#!/usr/bin/python3` and end with a new line
- Code follows the `pycodestyle` style (version 2.7.*)
- Python scripts are executable (`chmod +x <file>`)
- The answer files (`*-answer.txt` and `*-line*.txt`) contain **only** the
  answer, followed by a new line
- No module imports are allowed in any script

## Files

### Questions about objects, identity and mutability (answer files)

| Files | Topic |
|-------|-------|
| `0-answer.txt` | The function that returns the type of an object |
| `1-answer.txt` | The function that returns the identifier of an object |
| `2-answer.txt`, `3-answer.txt` | Do two names point to the same integer object? (different values vs. the same small value) |
| `4-answer.txt`, `5-answer.txt` | Aliasing with `b = a`, and what `b = a + 1` does |
| `6-answer.txt` to `9-answer.txt` | `==` versus `is` on strings |
| `10-answer.txt` to `13-answer.txt` | `==` versus `is` on lists, with equal lists and with aliases |
| `14-answer.txt`, `15-answer.txt` | `append` (mutation) versus `l1 = l1 + [4]` (rebinding) |
| `16-answer.txt` to `18-answer.txt` | Passing integers and lists to functions |
| `20-answer.txt` to `23-answer.txt` | Which expressions create a tuple (`()`, `(1, 2)`, `(1)`, `(1, )`) |
| `24-answer.txt` to `26-answer.txt` | Identity of equal integers, tuples and empty tuples |
| `27-answer.txt`, `28-answer.txt` | Does `id` change after `a = a + [5]` versus `a += [4]`? |

### Scripts

| File | Description |
|------|-------------|
| `19-copy_list.py` | `copy_list(l)`: returns a (shallow) copy of a list. Maximum 3 lines. |
| `100-magic_string.py` | `magic_string()`: returns `"BestSchool"` repeated once more on each call, joined by `", "`. Uses a mutable default argument to keep state. Maximum 4 lines. |
| `101-locked_class.py` | `LockedClass`: uses `__slots__` so that the only instance attribute that can be created is `first_name`. |

### CPython internals (answer files)

| Files | Topic |
|-------|-------|
| `103-line1.txt`, `103-line2.txt` | How many int objects does `a = 1` create? (small integer cache) |
| `104-line1.txt` to `104-line5.txt` | The life cycle of an int outside the small-integer range (`1024`): creation, `del`, and re-creation |
| `105-line1.txt` | How many int objects exist before the second line of a script runs? |
| `106-line1.txt` to `106-line5.txt` | The same life-cycle question for the string `"SCHL"` (string interning) |

## Usage

Each script comes with a main file showing how it is used:

```bash
chmod +x 19-copy_list.py 19-main.py
./19-main.py

chmod +x 100-magic_string.py 100-main.py
./100-main.py

chmod +x 101-locked_class.py 101-main.py
./101-main.py
```

Check the length limits and the style:

```bash
wc -l 19-copy_list.py 100-magic_string.py    # 3 and 4 lines
pycodestyle *.py
```

Check an answer file:

```bash
cat 3-answer.txt
```

## Key concepts

### Identity versus equality

`==` compares **values**. `is` compares **identity**, which means whether
two names point to the same object. `id(obj)` returns the identifier of an
object, which is its memory address in CPython.

```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> l1 == l2
True
>>> l1 is l2
False
```

### Mutable and immutable types

- **Mutable:** lists, dictionaries, sets. They can change in place.
- **Immutable:** integers, floats, strings, tuples, booleans. An operation
  creates a new object instead.

`l1.append(4)` changes the existing list, while `l1 = l1 + [4]` builds a new
list and rebinds the name. `a += [4]` on a list is in place and keeps the
same `id`.

### Function arguments

Python passes **references to objects**. A function that mutates a list
affects the caller's list. A function that only rebinds its parameter (`n =
v`, or `n += 1` on an integer) doesn't affect the caller.

### Tuples

The comma makes the tuple, not the parentheses. `(1)` is an integer,
`(1, )` is a tuple, and `()` is the empty tuple. CPython keeps a single
shared empty tuple, so every `()` is the same object.

### CPython optimizations

- **Small integer cache:** the integers from -5 to 256 (262 objects) are
  created at startup and reused. `NSMALLNEGINTS` is 5 and
  `NSMALLPOSINTS` is 257.
- **String interning:** short strings made of letters, digits and
  underscores are shared, so equal ones usually point to the same object.
- **Empty tuple:** a single shared instance.

### `__slots__` and `LockedClass`

Declaring `__slots__ = ["first_name"]` gives instances storage for that one
attribute only and removes the per-instance `__dict__`, so assigning any
other attribute raises `AttributeError`.

## A note on how the questions are answered

Several questions (identity of strings and tuples, `1024`, `"SCHL"`) depend
on whether the code is typed one line at a time in the interactive `>>>`
prompt or run as a script. In a script file, the compiler stores identical
constants once per code block, so two separately written equal constants can
end up as one object. The answers in this project follow the interactive,
line-by-line model, which is what the questions describe.

## Author

`set-high_level_programming` 
