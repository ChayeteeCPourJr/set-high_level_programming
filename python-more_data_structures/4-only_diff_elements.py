#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one set

    Args:
        set_1: first set
        set_2: second set

    Returns:
        A new set containing every element that belongs to
        exactly one of set_1 or set_2, but not both
        (the symmetric difference)
    """
    return set_1 ^ set_2
