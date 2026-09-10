# 0x00. Python - Hello, World

## Description
This repository contains introductory projects for Python and C programming. It covers fundamental concepts such as Python execution, string manipulation, formatting, bytecode analysis, script compilation, standard error outputs, and C singly linked list cycle detection.

---

## Technical Specifications
* **Python Version:** Python 3.8.x / Python 3.x
* **C Compiler:** `gcc` using options `-Wall -Werror -Wextra -pedantic -std=gnu89`
* **OS / Environment:** Ubuntu 20.04 LTS / WSL
* **Style Guidelines:**
  * Python files adhere to `PEP 8` standard (`pycodestyle`).
  * C files follow the `Betty` style guide.
  * Executable files must have executable permissions (`chmod u+x`).
  * All files must end with a new line.

---

## File Summary

| File | Description | Language / Tech |
| :--- | :--- | :--- |
| `2-print_percent.py` | Prints a formatted string containing `%` characters. | Python |
| `3-print_number.py` | Prints an integer followed by a formatted string. | Python |
| `4-print_float.py` | Prints a float stored in a variable with a precision of 2 digits using f-strings. | Python |
| `5-print_string.py` | Prints 3 times a string followed by its first 9 characters without using loops. | Python |
| `6-concat.py` | Concatenates strings to print `Welcome to Elmwood Institute!`. | Python |
| `7-edges.py` | Extracts the first 3 letters, last 2 letters, and middle word of a string using slicing. | Python |
| `8-concat_edges.py` | Slices and concatenates substrings from a variable without creating new variables. | Python |
| `9-easter_egg.py` | Prints "The Zen of Python" by Tim Peters using `import this` (under 98 chars). | Python |
| `10-check_cycle.c` | Implements Floyd's Cycle Detection algorithm to check if a singly linked list has a cycle. | C |
| `100-write.py` | Writes to `sys.stderr` and exits with status code `1` using `sys.exit()`. | Python |
| `101-compile` | Script that compiles a Python script file specified by `$PYFILE`. | Bash |
| `102-magic_calculation.py` | Python function replicating given Python bytecode (`98 + (a ** b)`). | Python |

---

## How to Run & Test

### Python Tasks
Ensure execution permissions are granted before running scripts directly:

```bash
chmod u+x filename.py
./filename.py
