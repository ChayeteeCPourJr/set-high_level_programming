#!/usr/bin/python3
def max_integer(my_list=[]):
    """Find the biggest integer of a list

    Args:
        my_list: a list containing only integers

    Returns:
        The biggest integer in my_list, or None if my_list is empty
    """
    if len(my_list) == 0:
        return None
    biggest = my_list[0]
    for integer in my_list:
        if integer > biggest:
            biggest = integer
    return biggest
