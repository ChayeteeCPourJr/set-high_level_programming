# Python - Test-driven development

This project covers writing Python functions together with the tests that
prove they work. Each function is documented with module and function
docstrings, and is tested with either **doctest** (interactive tests in
`.txt` files) or **unittest** (test classes in `.py` files).

## Learning objectives

- What the Python docstring is, and how to write one
- What a module docstring is, and how to write one
- How to write interactive tests with `doctest`
- How to write unit tests with `unittest`
- How to cover edge cases: invalid types, empty input, boundary values
- Why testing exception types and messages matters

## Requirements

- Ubuntu 20.04 LTS (or WSL), Python 3 (`/usr/bin/python3`)
- All files end with a new line and start with `#!/usr/bin/python3`
- Code follows the `pycodestyle` style (version 2.7.*)
- All files are executable (`chmod +x <file>`)
- All modules, classes and functions have docstrings
- No module imports are allowed, except `numpy` in task 101
- Every function task ships with a doctest file (`tests/<name>.txt`),
  and task 6 ships with a unittest file

## Installation

Only task `101-lazy_matrix_mul.py` needs an extra package:

```bash
pip3 install numpy
```

> The project brief mentions `numpy==1.15.0`, which predates recent Python
> versions and may not install on Python 3.12. A current NumPy works too:
> the tests for task 101 check the kind of exception raised, not its exact
> message, because NumPy's messages differ between versions.

## Files

| Task | File | Description | Tests |
|------|------|-------------|-------|
| 0 | `0-add_integer.py` | `add_integer(a, b=98)`: adds two integers or floats (floats are cast to int). Raises `TypeError` with `a must be an integer` / `b must be an integer`. | `tests/0-add_integer.txt` |
| 2 | `2-matrix_divided.py` | `matrix_divided(matrix, div)`: returns a new matrix with every element divided by `div`, rounded to 2 decimals. Validates the matrix, the row sizes, and `div` (including division by zero). | `tests/2-matrix_divided.txt` |
| 3 | `3-say_my_name.py` | `say_my_name(first_name, last_name="")`: prints `My name is <first name> <last name>`. Both arguments must be strings. | `tests/3-say_my_name.txt` |
| 4 | `4-print_square.py` | `print_square(size)`: prints a square of `#`. Raises `TypeError` for a non-integer (including negative floats) and `ValueError` for a negative integer. | `tests/4-print_square.txt` |
| 5 | `5-text_indentation.py` | `text_indentation(text)`: prints text with 2 new lines after each `.`, `?` and `:`, with no leading or trailing spaces on each line. | `tests/5-text_indentation.txt` |
| 6 | `6-max_integer.py` | `max_integer(list=[])`: returns the largest element, or `None` for an empty list. This task is about **writing the tests**. | `tests/6-max_integer_test.py` |
| 100 | `100-matrix_mul.py` | `matrix_mul(m_a, m_b)`: multiplies two matrices without any module. Validates both matrices in a fixed order, each with its own message. | `tests/100-matrix_mul.txt` |
| 101 | `101-lazy_matrix_mul.py` | `lazy_matrix_mul(m_a, m_b)`: multiplies two matrices with `numpy.matmul`. | `tests/101-lazy_matrix_mul.txt` |

Each task also has a `*-main.py` file with the example from the project
brief (for example `0-main.py`, `2-main.py`).

## Usage

Run a main file to see a function in action:

```bash
./0-main.py
./2-main.py
./5-main.py | cat -e
./100-main.py
./101-main.py
```

## Running the tests

### Doctests (tasks 0, 2, 3, 4, 5, 100, 101)

```bash
python3 -m doctest -v ./tests/0-add_integer.txt
python3 -m doctest -v ./tests/2-matrix_divided.txt
python3 -m doctest -v ./tests/3-say_my_name.txt
python3 -m doctest -v ./tests/4-print_square.txt
python3 -m doctest -v ./tests/5-text_indentation.txt
python3 -m doctest -v ./tests/100-matrix_mul.txt
python3 -m doctest -v ./tests/101-lazy_matrix_mul.txt
```

Run them all at once:

```bash
for f in tests/*.txt; do python3 -m doctest "$f" && echo "OK  $f"; done
```

A doctest run prints nothing when everything passes. Add `-v` to see each
test and the final `N passed and 0 failed` summary.

### Unittests (task 6)

```bash
python3 -m unittest tests.6-max_integer_test
```

Expected result: `Ran 23 tests` followed by `OK`.

### Style check

```bash
pycodestyle *.py tests/*.py
```

## Test coverage summary

| File | Number of tests |
|------|-----------------|
| `tests/0-add_integer.txt` | 9 |
| `tests/2-matrix_divided.txt` | 10 |
| `tests/3-say_my_name.txt` | 8 |
| `tests/4-print_square.txt` | 10 |
| `tests/5-text_indentation.txt` | 9 |
| `tests/6-max_integer_test.py` | 23 |
| `tests/100-matrix_mul.txt` | 20 |
| `tests/101-lazy_matrix_mul.txt` | 19 |

## Notes on tricky behaviour

- **Docstring length (task 0):** the module docstring must print as 5 lines
  and the function docstring as 3 lines with
  `python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l`.
- **Trailing spaces in doctests (task 3):** the expected output
  `My name is Bob ` ends with a space. If your editor trims trailing
  whitespace on save, that test will fail. Check with
  `cat -e tests/3-say_my_name.txt`.
- **Float vs `ValueError` (task 4):** a negative float raises `TypeError`,
  not `ValueError`, because the type check runs before the value check.
- **No trailing newline (task 5):** `text_indentation` ends without a final
  new line, so the shell prompt follows the last word directly.
- **Validation order (task 100):** each requirement is checked for `m_a`
  and then `m_b` before moving to the next requirement, so
  `matrix_mul([], [1])` raises `m_b must be a list of lists`, not
  `m_a can't be empty`.
- **`bool` values:** `True` and `False` are rejected as numbers in tasks 2,
  4 and 100, since they are almost certainly unintended input there. Task 0
  follows the spec literally and accepts them, because `bool` is a subtype
  of `int`.

## Author
FIT
