#!/usr/bin/python3
"""Defines a Square class with a private size attribute"""


class Square:
    """Represents a square

    Attributes:
        __size (private): the size of the square
    """

    def __init__(self, size):
        """Initialize a new Square

        Args:
            size: the size of the square
        """
        self.__size = size
