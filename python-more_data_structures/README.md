# python-more_data_structures

This project is part of the Higher-Level Programming track. It builds
on `python-data_structures` and covers Python's `set` and `dict`
types, functional tools like `map`, and a deeper dive into CPython's
C API for lists and bytes objects.

## Learning Objectives

By the end of this project you should be able to explain, without
Google:

- What are sets, and common methods and how to use them
- When to use sets versus lists
- What are dictionaries, and common methods and how to use them
- When to use dictionaries versus lists or sets
- What is a key in a dictionary as long as it's hashable
- How to iterate over a dictionary
- What is `**kwargs` and how to use it (if covered)
- Why Python programming is awesome
- How to access CPython's internal `PyListObject` and
  `PyBytesObject` structures from C

## Requirements

- All scripts are interpreted on Ubuntu using `python3` and are
  compatible with Python 3.
- All files end with a new line.
- The first line of every Python file is exactly `#!/usr/bin/python3`.
- All files are executable (`chmod +x`).
- Every module and function has a docstring.
- `pycodestyle` (version 2.x) style rules apply to every `.py` file.
- Unless explicitly allowed by the task, no `import` statements are
  used in these solutions.

## Python files

| File | Description |
| --- | --- |
| [`14-square_matrix_simple.py`](./14-square_matrix_simple.py) | Computes the square of every integer in a matrix, returning a new matrix. The original is not modified. |
| [`15-search_replace.py`](./15-search_replace.py) | Replaces all occurrences of an element by another, returning a new list. |
| [`16-uniq_add.py`](./16-uniq_add.py) | Adds all unique integers in a list, counting each value only once. |
| [`17-common_elements.py`](./17-common_elements.py) | Returns the set intersection of two sets. |
| [`18-only_diff_elements.py`](./18-only_diff_elements.py) | Returns the symmetric difference of two sets (elements in exactly one set). |
| [`19-number_keys.py`](./19-number_keys.py) | Returns the number of keys in a dictionary. |
| [`20-print_sorted_dictionary.py`](./20-print_sorted_dictionary.py) | Prints a dictionary's `key: value` pairs sorted by key (top level only). |
| [`21-update_dictionary.py`](./21-update_dictionary.py) | Replaces or adds a key/value pair in a dictionary, in place. |
| [`22-simple_delete.py`](./22-simple_delete.py) | Deletes a key from a dictionary, if it exists. |
| [`23-multiply_by_2.py`](./23-multiply_by_2.py) | Returns a new dictionary with every value doubled. |
| [`24-best_score.py`](./24-best_score.py) | Returns the key with the highest value in a dictionary, or `None` if empty. |
| [`25-multiply_list_map.py`](./25-multiply_list_map.py) | Multiplies every value in a list by a number, using `map()` only (no loops), in 3 lines. |
| [`100-roman_to_int.py`](./100-roman_to_int.py) | Converts a Roman numeral string to an integer. Returns `0` for non-string/`None` input. |
| [`101-weight_average.py`](./101-weight_average.py) | Computes the weighted average of a list of `(score, weight)` tuples. |
| [`102-square_matrix_map.py`](./102-square_matrix_map.py) | Same as task 14, but using nested `map()` calls only — no loops, 3 lines max. |
| [`103-complex_delete.py`](./103-complex_delete.py) | Deletes every key in a dictionary whose value matches a given value. |

## C files

| File | Description |
| --- | --- |
| [`103-python.c`](./103-python.c) | `void print_python_list(PyObject *p);` and `void print_python_bytes(PyObject *p);` — CPython C-API functions that inspect a list's or bytes object's internal structure directly (without `Py_SIZE`, `Py_TYPE`, `PyList_GetItem`, `PyBytes_AS_STRING`, or `PyBytes_GET_SIZE`), printing size, allocation, per-element types, and up to 10 raw bytes in hex. Compiled as a shared library and called from Python via `ctypes`. |

## Usage examples

```
$ ./14-square_matrix_simple.py    # (via a main script)
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]

$ ./15-search_replace.py
[1, 2, 3, 4, 5, 2]
[1, 100, 3, 4, 5, 100]

$ ./17-common_elements.py
{3, 4, 5}

$ ./18-only_diff_elements.py
{1, 2, 6, 7}

$ ./20-print_sorted_dictionary.py
a: ['Best', 'School']
b: 89
c: is fun

$ ./24-best_score.py
John

$ ./25-multiply_list_map.py
[1, 2, 3, 4, 5]
[3, 6, 9, 12, 15]

$ ./100-roman_to_int.py
16
1994

$ ./101-weight_average.py
7.166666666666667

$ python3 103-tests.py   # using libPython.so built from 103-python.c
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
...
```

## Compiling 103-python.c

```bash
# Adjust the -I path to match YOUR installed Python version:
#   python3-config --includes
gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so \
    -o libPython.so -fPIC -I/usr/include/python3.12 103-python.c
```

**Note:** this file accesses CPython's internal struct fields
directly (`ob_size`, `ob_type`, `ob_item`, `ob_sval`, `allocated`)
rather than through the `Py_SIZE`/`Py_TYPE` macros, per the task's
constraints. These fields are laid out differently between Python
3.4 (flat fields) and Python 3.10+ (nested under `ob_base`), so this
file is written for — and should be tested against — an actual
Python 3.4 environment to match the grading target exactly.

## Author

