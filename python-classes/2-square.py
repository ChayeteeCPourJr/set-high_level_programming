#!/usr/bin/python3
"""Defines a Square class with a validated private size attribute"""


class Square:
    """Represents a square

    Attributes:
        __size (private): the size of the square
    """

    def __init__(self, size=0):
        """Initialize a new Square

        Args:
            size: the size of the square (default 0)

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
