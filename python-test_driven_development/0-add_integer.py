#!/usr/bin/python3
"""Module that defines a function to add two integers.

This module provides add_integer, a function that adds two
numbers together, casting floats to integers first.
"""


def add_integer(a, b=98):
    """Adds two integers, casting floats to ints first.

    Returns the sum of a and b as an integer."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
