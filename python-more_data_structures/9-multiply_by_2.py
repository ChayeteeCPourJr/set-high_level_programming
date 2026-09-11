#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multiplied by 2

    Args:
        a_dictionary: a dictionary whose values are all integers

    Returns:
        A new dictionary, same keys as a_dictionary, where each
        value is twice the value at the same key in a_dictionary.
        The original dictionary is not modified.
    """
    new_dictionary = {}
    for key in a_dictionary:
        new_dictionary[key] = a_dictionary[key] * 2
    return new_dictionary
