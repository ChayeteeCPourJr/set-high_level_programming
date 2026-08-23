#!/usr/bin/python3
"""Defines a MyList class that inherits from list."""


class MyList(list):
    """A list with a method to print its sorted contents."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
