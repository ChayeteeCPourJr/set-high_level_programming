#!/usr/bin/python3
"""Module that defines a function to multiply two matrices with NumPy.

This module provides lazy_matrix_mul, a function that returns the
matrix product of two matrices using the NumPy module.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using numpy.matmul and returns the result."""
    return np.matmul(m_a, m_b)
