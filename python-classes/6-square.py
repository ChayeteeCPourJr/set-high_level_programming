#!/usr/bin/python3
"""Defines a Square class with private size and position properties"""


class Square:
    """Represents a square

    Attributes:
        __size (private): the size of the square
        __position (private): the (x, y) position of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square

        Args:
            size: the size of the square (default 0)
            position: the (x, y) position of the square (default (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

        Args:
            value: the new size of the square

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the current position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square

        Args:
            value: the new (x, y) position of the square

        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        if (type(value) is not tuple or
                len(value) != 2 or
                type(value[0]) is not int or
                type(value[1]) is not int or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the '#' character

        If size is 0, prints an empty line instead.
        position[1] blank lines are printed first, then each row of
        the square is indented by position[0] spaces, with no
        trailing spaces after the '#' characters.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
