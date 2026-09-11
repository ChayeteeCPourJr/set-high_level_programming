#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete the item at a specific position in a list

    Args:
        my_list: the list to modify
        idx: the index of the item to delete

    Returns:
        my_list, with the item at idx removed if idx is valid.
        Unmodified if idx is negative or out of range.
    """
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return my_list
    del my_list[idx]
    return my_list
