#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specific position,
    without modifying the original list

    Args:
        my_list: the original list (left unmodified)
        idx: the index of the element to replace in the copy
        element: the new value to place at idx

    Returns:
        A new list, a copy of my_list with the element at idx
        replaced if idx is valid, or an unmodified copy if idx
        is negative or out of range
    """
    new_list = my_list[:]
    if idx < 0:
        return new_list
    if idx > len(new_list) - 1:
        return new_list
    new_list[idx] = element
    return new_list
