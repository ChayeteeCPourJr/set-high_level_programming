#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers, one row per line,
    values separated by a single space

    Args:
        matrix: a list of lists, each containing only integers

    Returns:
        None
    """
    for row in matrix:
        line = ""
        for idx in range(len(row)):
            if idx > 0:
                line += " "
            line += "{:d}".format(row[idx])
        print(line)
