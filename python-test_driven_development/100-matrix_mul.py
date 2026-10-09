#!/usr/bin/python3
"""Module that defines a function to multiply two matrices.

This module provides matrix_mul, a function that returns the
matrix product of two matrices given as lists of lists of
integers or floats.
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices and returns the resulting matrix."""
    matrices = (("m_a", m_a), ("m_b", m_b))

    for name, m in matrices:
        if not isinstance(m, list):
            raise TypeError("{} must be a list".format(name))
    for name, m in matrices:
        if not all(isinstance(row, list) for row in m):
            raise TypeError("{} must be a list of lists".format(name))
    for name, m in matrices:
        if len(m) == 0 or all(len(row) == 0 for row in m):
            raise ValueError("{} can't be empty".format(name))
    for name, m in matrices:
        for row in m:
            for n in row:
                if (not isinstance(n, (int, float)) or
                        isinstance(n, bool)):
                    raise TypeError(
                        "{} should contain only integers or floats"
                        .format(name))
    for name, m in matrices:
        if any(len(row) != len(m[0]) for row in m):
            raise TypeError(
                "each row of {} must be of the same size".format(name))

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*m_b)]
            for row in m_a]
