#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix

    Args:
        matrix: a 2 dimensional list of integers

    Returns:
        A new matrix, same size as matrix, where each value is
        the square of the value at the same position in matrix.
        The original matrix is not modified.
    """
    new_matrix = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(value ** 2)
        new_matrix.append(new_row)
    return new_matrix
