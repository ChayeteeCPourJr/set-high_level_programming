# python-import_modules

This project is part of the Higher-Level Programming track. It covers how
Python modules work: importing functions and variables between files,
reading command-line arguments, reconstructing a function from its
compiled bytecode, and writing constrained one-liners.

## Learning Objectives

By the end of this project you should be able to explain, without Google:

- Why Python programming is awesome
- What is a module and how to use one
- What is the purpose of `if __name__ == "__main__":`
- How to use System's arguments in a Python script (`sys.argv`)
- How to read Python bytecode with `dis`

## Requirements

- All scripts are interpreted/compiled on Ubuntu 24.04 LTS using
  `python3` (version 3.8.x for the tasks that read compiled `.pyc`
  files, since bytecode format is version-specific).
- All files end with a new line.
- The first line of every file is exactly `#!/usr/bin/python3`.
- All files are executable (`chmod +x`).
- Every module and function has a docstring.
- No file may execute its top-level logic when it is imported — this is
  enforced with `if __name__ == "__main__":`.
- `*` and `__import__` are never used for importing.

## Files

| File | Description |
| --- | --- |
| [`add_0.py`](./add_0.py) | Defines `add(a, b)`. |
| [`0-add.py`](./0-add.py) | Imports `add` from `add_0` and prints `1 + 2 = 3`. |
| [`calculator_1.py`](./calculator_1.py) | Defines `add`, `sub`, `mul`, `div`. |
| [`1-calculator.py`](./1-calculator.py) | Imports all four functions from `calculator_1` and prints the result of each operation on `10` and `5`. |
| [`2-args.py`](./2-args.py) | Prints the number of command-line arguments and lists each one with its position. |
| [`3-infinite_add.py`](./3-infinite_add.py) | Prints the sum of all command-line arguments, cast to `int` (supports arbitrarily large integers). |
| [`4-hidden_discovery.py`](./4-hidden_discovery.py) | Imports the compiled module `hidden_4.pyc` and prints every top-level name that doesn't start with `__`, one per line, sorted alphabetically. Must be run with Python 3.8.x, the version `hidden_4.pyc` was compiled with. |
| [`variable_load_5.py`](./variable_load_5.py) | Defines the variable `a = 98`. |
| [`5-variable_load.py`](./5-variable_load.py) | Imports `a` from `variable_load_5` and prints its value. |
| [`100-my_calculator.py`](./100-my_calculator.py) | A basic CLI calculator: `./100-my_calculator.py <a> <operator> <b>`. Supports `+`, `-`, `*`, `/`. Validates argument count and operator, exiting with status `1` on error. |
| [`101-easy_print.py`](./101-easy_print.py) | Prints `#pythoniscool` in 2 lines, without using `print`, `eval`, `open`, or `import sys`. |
| [`magic_calculation_102.py`](./magic_calculation_102.py) | Defines `add` and `sub`, used by `102-magic_calculation.py`. |
| [`102-magic_calculation.py`](./102-magic_calculation.py) | Defines `magic_calculation(a, b)`, reconstructed by reading its compiled bytecode with `dis`. |
| [`103-fast_alphabet.py`](./103-fast_alphabet.py) | Prints the uppercase alphabet in 2 lines, without loops, conditionals, `str.join()`, string literals, or system calls. |

## Usage examples

```
$ ./0-add.py
1 + 2 = 3

$ ./1-calculator.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2

$ ./2-args.py Hello World
2 arguments:
1: Hello
2: World

$ ./3-infinite_add.py 79 10 -40 -300 89
-162

$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school

$ ./5-variable_load.py
98

$ ./100-my_calculator.py 3 + 5
3 + 5 = 8

$ ./101-easy_print.py
#pythoniscool

$ ./103-fast_alphabet.py
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

## Author

