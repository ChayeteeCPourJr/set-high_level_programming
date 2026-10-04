#!/usr/bin/python3
"""Defines the MyInt class."""


class MyInt(int):
    """A rebel integer with inverted == and != operators."""

    def __eq__(self, other):
        """Return False when values are equal and True otherwise."""
        return int(self) != other

    def __ne__(self, other):
        """Return True when values are equal and False otherwise."""
        return int(self) == other
