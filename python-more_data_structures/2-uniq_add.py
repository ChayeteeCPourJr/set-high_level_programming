#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list, only once for each integer

    Args:
        my_list: a list containing integers

    Returns:
        The sum of every distinct integer in my_list, each counted
        only once regardless of how many times it appears
    """
    seen = []
    total = 0
    for integer in my_list:
        if integer not in seen:
            seen.append(integer)
            total += integer
    return total
