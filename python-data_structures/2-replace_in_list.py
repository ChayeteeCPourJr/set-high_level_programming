#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position, C-style

    Args:
        my_list: the list to modify
        idx: the index of the element to replace
        element: the new value to place at idx

    Returns:
        my_list, modified in place if idx is valid,
        unmodified if idx is negative or out of range
    """
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return my_list
    my_list[idx] = element
    return my_list
