# python-data_structures

This project is part of the Higher-Level Programming track. It covers
Python's built-in data structures — lists and tuples — how CPython
implements them under the hood, and a classic linked-list algorithm
in C.

## Learning Objectives

By the end of this project you should be able to explain, without
Google:

- What is a list and how to use it
- What are the differences and similarities between lists and
  strings
- What is a tuple
- How to use tuples to swap values without using a third variable
- When to use tuples vs. lists
- How does Python allocate memory for a list

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
| [`0-print_list_integer.py`](./0-print_list_integer.py) | Prints all integers of a list, one per line, using `str.format()`. |
| [`1-element_at.py`](./1-element_at.py) | Retrieves an element from a list by index, C-style: returns `None` for negative or out-of-range indices. |
| [`2-replace_in_list.py`](./2-replace_in_list.py) | Replaces an element in a list at a given index, in place. Leaves the list untouched for invalid indices. |
| [`3-print_reversed_list_integer.py`](./3-print_reversed_list_integer.py) | Prints all integers of a list in reverse order, one per line. |
| [`4-new_in_list.py`](./4-new_in_list.py) | Replaces an element at a given index **without** modifying the original list — always returns a copy. |
| [`5-no_c.py`](./5-no_c.py) | Removes every `c` and `C` character from a string, without using `str.replace()`. |
| [`6-print_matrix_integer.py`](./6-print_matrix_integer.py) | Prints a matrix of integers, one row per line, values space-separated. |
| [`7-add_tuple.py`](./7-add_tuple.py) | Adds two tuples element-wise, padding missing values with `0` and ignoring anything past the first two elements. |
| [`8-multiple_returns.py`](./8-multiple_returns.py) | Returns a tuple of a string's length and its first character (`None` if the string is empty). |
| [`9-max_integer.py`](./9-max_integer.py) | Finds the biggest integer in a list, without using the builtin `max()`. |
| [`100-max_integer.py`](./100-max_integer.py) | Finds the biggest integer in a list, using the builtin `max()`. |
| [`10-divisible_by_2.py`](./10-divisible_by_2.py) | Returns a list of booleans marking which integers in the input list are multiples of 2. |
| [`11-delete_at.py`](./11-delete_at.py) | Deletes the item at a given index in a list, without using `pop()`. Leaves the list untouched for invalid indices. |
| [`12-switch.py`](./12-switch.py) | A 5-line script that swaps two variables using tuple-unpacking assignment (`a, b = b, a`), no temporary variable. |

## C files

| File | Description |
| --- | --- |
| [`lists.h`](./lists.h) | Header defining the `listint_t` singly linked list struct and function prototypes. |
| [`linked_lists.c`](./linked_lists.c) | Helper functions: `print_listint`, `add_nodeint_end`, `free_listint`. |
| [`13-is_palindrome.c`](./13-is_palindrome.c) | `int is_palindrome(listint_t **head);` — checks whether a singly linked list is a palindrome, using a recursive approach that never modifies the list. An empty list is considered a palindrome. |
| [`100-print_python_list_info.c`](./100-print_python_list_info.c) | `void print_python_list_info(PyObject *p);` — a CPython C-API function that inspects a Python list's internal `PyListObject` structure and prints its size, allocated capacity, and the type of each element. Compiled as a shared library (`libPyList.so`) and called from Python via `ctypes`. |

## Usage examples

```
$ ./0-print_list_integer.py    # (via a main script importing the function)
1
2
3
4
5

$ ./3-print_reversed_list_integer.py
5
4
3
2
1

$ ./6-print_matrix_integer.py
1 2 3
4 5 6
7 8 9

$ ./7-add_tuple.py
(4, 6)

$ ./9-max_integer.py
91

$ ./12-switch.py
a=10 - b=89

$ ./palindrome   # compiled from 13-is_palindrome.c + linked_lists.c + 13-main.c
1
17
972
50
98
98
50
972
17
1
Linked list is a palindrome

$ python3 100-test_lists.py   # using libPyList.so built from 100-print_python_list_info.c
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: str
Element 1: str
...
```

## Compiling the C files

```bash
# Palindrome checker
gcc -Wall -Werror -Wextra -pedantic 13-main.c linked_lists.c 13-is_palindrome.c -o palindrome

# Python list internals (CPython C API)
# Adjust the -I path to match YOUR installed Python version:
#   python3-config --includes
gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList \
    -o libPyList.so -fPIC -I/usr/include/python3.12 100-print_python_list_info.c
```

## Author

