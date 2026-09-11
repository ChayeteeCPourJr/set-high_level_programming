#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Delete all keys with a specific value in a dictionary

    Args:
        a_dictionary: the dictionary to modify
        value: the value whose matching keys should be deleted

    Returns:
        a_dictionary, with every key that had value removed.
        Unmodified if value doesn't exist in a_dictionary.
    """
    keys_to_delete = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary
