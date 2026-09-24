# python-classes

This project is part of the Higher-Level Programming track. It
covers Python's object-oriented programming model: classes,
instances, private attributes, `@property` getters/setters,
`__str__`, comparison dunder methods, and a singly linked list
implementation.

## Learning Objectives

By the end of this project you should be able to explain, without
Google:

- Why Python programming is awesome
- What is OOP
- "First-class everything"
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are public, protected, and private attributes, and how to
  implement them
- What is a method
- What is `self`
- What is `__init__`
- What is a docstring
- What is `**kwargs` and how to use it (if covered)
- How to use `@property`, getters, and setters
- How to dynamically create arbitrary new attributes for existing
  instances of a class
- How to bind attributes to object
- What is `__str__` and how to use it
- What are comparison methods (`__eq__`, `__lt__`, etc.) and how to
  use them

## Requirements

- All scripts are interpreted on Ubuntu using `python3` and are
  compatible with Python 3.
- All files end with a new line.
- The first line of every Python file is exactly `#!/usr/bin/python3`.
- All files are executable (`chmod +x`).
- Every module, class, and method has a docstring.
- `pycodestyle` (version 2.x) style rules apply to every `.py` file.
- Unless explicitly allowed by the task, no `import` statements are
  used in these solutions.

## Files

| File | Description |
| --- | --- |
| [`0-square.py`](./0-square.py) | An empty `Square` class — the starting point for the rest of the project. |
| [`1-square.py`](./1-square.py) | Adds a private `__size` instance attribute, set via `__init__`, with no validation yet. |
| [`2-square.py`](./2-square.py) | Adds type/value validation directly in `__init__`: `size` must be a non-negative integer. |
| [`3-square.py`](./3-square.py) | Adds a public `area()` method. |
| [`4-square.py`](./4-square.py) | Replaces manual `__init__` validation with a `size` `@property` getter/setter, centralizing the validation logic in one place. |
| [`5-square.py`](./5-square.py) | Adds `my_print()`, which prints the square using `#` characters (an empty line if `size` is `0`). |
| [`6-square.py`](./6-square.py) | Adds a `position` `@property` (a validated 2-tuple of non-negative integers) and updates `my_print()` to offset the square by `position` (blank lines for the vertical offset, leading spaces for the horizontal offset, no trailing whitespace). |
| [`101-square.py`](./101-square.py) | Adds `__str__`, so `print(square)` behaves identically to `my_print()`. |
| [`102-square.py`](./102-square.py) | A simplified `Square` (no `position`) whose `size` accepts `int` or `float`, and which implements `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__` — comparing instances by their `area()`. |
| [`103-magic_class.py`](./103-magic_class.py) | `MagicClass`, reconstructed directly from its compiled bytecode disassembly. Computes the area and circumference of a circle from a `radius`. This file legitimately imports `math`, since the original bytecode does too. |
| [`0-singly_linked_list.py`](./0-singly_linked_list.py) | Defines `Node` (a private `data`/`next_node` pair, both validated via properties) and `SinglyLinkedList` (a private `__head`, with `sorted_insert()` to insert in increasing order, and `__str__` to print one value per line). |

## Usage examples

```
$ ./3-square.py    # (via a main script)
<class '3-square.Square'>
9

$ ./6-square.py
###
###
###

$ ./101-main.py
#####
#####
#####
#####
#####
--

    #####
    #####
    #####
    #####
    #####

$ ./102-main.py
Square 5 < Square 6
Square 5 <= Square 6
Square 5 != Square 6

$ ./0-main.py    # (singly linked list)
1
2
3
5
8
10
```

## Author


