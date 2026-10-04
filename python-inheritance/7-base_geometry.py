#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """Represents a base for other geometry classes"""

    def area(self):
        """Raise an exception; area computation must be implemented
        by a subclass

        Raises:
            NotImplementedError: always
        """
        raise NotImplementedError("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer

        Args:
            name: the name of the attribute being validated
            value: the value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
