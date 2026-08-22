#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list, in reverse order, one per line

    Args:
        my_list: a list containing only integers

    Returns:
        None
    """
    if my_list is None:
        return
    for idx in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[idx]))
