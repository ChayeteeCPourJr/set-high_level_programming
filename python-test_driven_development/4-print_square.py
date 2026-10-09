#!/usr/bin/python3
"""Module that defines a function to print a square.

This module provides print_square, a function that prints a
square of a given size using the character '#'.
"""


def print_square(size):
    """Prints a square of size `size`, using the character '#'."""
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
