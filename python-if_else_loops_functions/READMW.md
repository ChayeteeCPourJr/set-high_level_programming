# 0x01. Python - if/else, loops, functions

## Description

This project is a collection of small Python and C exercises focused on
control flow, loops, functions, string/character manipulation, bytecode
reading, and singly linked lists in C.

## Requirements

### Python Scripts

- All files are interpreted/compiled on Ubuntu using `python3` (version 3.4.3+)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/python3`
- Code follows the `pycodestyle` style guide
- All files must be executable
- The length of the files is tested using `wc`

### C Files

- Compiled on Ubuntu using `gcc`, with the flags
  `-Wall -Werror -Wextra -pedantic -std=gnu89`
- All files end with a new line
- Code follows the Betty style guide, checked with `betty-style.pl`
  and `betty-doc.pl`
- No more than 5 functions per file
- The prototypes of all functions are included in `lists.h`

## Files

| File | Description |
| --- | --- |
| `0-positive_or_negative.py` | Prints whether a random number is positive, negative, or zero |
| `1-last_digit.py` | Prints the last digit of a random number and describes it |
| `2-print_alphabet.py` | Prints the lowercase alphabet, no newline |
| `3-print_alphabt.py` | Prints the lowercase alphabet except `q` and `e` |
| `4-print_hexa.py` | Prints numbers 0-98 in decimal and hexadecimal |
| `5-print_comb2.py` | Prints numbers 00 to 99, comma-separated |
| `6-print_comb3.py` | Prints all unique two-digit combinations in ascending order |
| `7-islower.py` | `islower(c)` - checks if a character is lowercase |
| `8-uppercase.py` | `uppercase(str)` - prints a string in uppercase |
| `9-print_last_digit.py` | `print_last_digit(number)` - prints and returns the last digit of a number |
| `10-add.py` | `add(a, b)` - returns the sum of two integers |
| `11-pow.py` | `pow(a, b)` - returns `a` to the power of `b` |
| `12-fizzbuzz.py` | `fizzbuzz()` - prints numbers 1-100, replacing multiples of 3 with `Fizz`, multiples of 5 with `Buzz`, and multiples of both with `FizzBuzz` |
| `100-magic_calculation.py` | `magic_calculation(a, b, c)` - reimplements a given Python bytecode sequence |
| `101-remove_char_at.py` | `remove_char_at(str, n)` - returns a copy of a string with the character at index `n` removed |
| `102-print_reversed_alphabet.py` | Prints the alphabet in reverse order, alternating lowercase/uppercase |
| `lists.h` | Header file with the `listint_t` structure and function prototypes |
| `linked_lists.c` | Contains `print_listint`, `add_nodeint_end`, and `free_listint` |
| `13-insert_number.c` | `insert_node(listint_t **head, int number)` - inserts a number into a sorted singly linked list |

## Usage

Python scripts:

```bash
./0-positive_or_negative.py
```

C files (compile with the main test file and `linked_lists.c`):

```bash
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 13-main.c linked_lists.c 13-insert_number.c -o insert
./insert
```

## Author
