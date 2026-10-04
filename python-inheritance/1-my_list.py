#!/usr/bin/python3
"""Defines a MyList class that inherits from list"""


class MyList(list):
    """Represents a list of integers, with a sorted-print method"""

    def print_sorted(self):
        """Print the list, sorted in ascending order"""
        print(sorted(self))
