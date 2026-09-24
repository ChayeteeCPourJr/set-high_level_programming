#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integer"
            )
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using #."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return the string representation of the square."""
        if self.__size == 0:
            return ""

        result = "\n" * self.__position[1]

        for row in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size
            if row < self.__size - 1:
                result += "\n"

        return result
