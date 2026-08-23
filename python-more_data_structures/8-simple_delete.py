#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Delete a key in a dictionary

    Args:
        a_dictionary: the dictionary to modify
        key: the key to delete (always a string)

    Returns:
        a_dictionary, with key removed if it exists.
        Unmodified if key doesn't exist.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
