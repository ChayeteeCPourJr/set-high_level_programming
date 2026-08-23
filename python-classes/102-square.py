#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a square."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Return True if both squares have the same area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if the squares have different areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Return True if this square has a smaller area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if this square has a smaller or equal area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Return True if this square has a greater area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if this square has a greater or equal area."""
        return self.area() >= other.area()
