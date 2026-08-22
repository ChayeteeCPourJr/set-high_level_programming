#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list

    Args:
        my_list: a list containing only integers

    Returns:
        A new list of the same size as my_list, where each element
        is True if the integer at that position is a multiple of 2,
        and False otherwise
    """
    result = []
    for integer in my_list:
        result.append(integer % 2 == 0)
    return result
