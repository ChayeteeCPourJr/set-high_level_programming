#!/usr/bin/python3
"""Module that defines a function to divide all elements of a matrix.

This module provides matrix_divided, a function that returns a new
matrix with every element divided by a given number, rounded to 2
decimal places.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Returns a new matrix with every element rounded to 2 decimals."""
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix) or
            not all(
                isinstance(n, (int, float)) and not isinstance(n, bool)
                for row in matrix for n in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(n / div, 2) for n in row] for row in matrix]
