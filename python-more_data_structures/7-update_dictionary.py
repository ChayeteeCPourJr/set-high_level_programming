#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replace or add a key/value pair in a dictionary

    Args:
        a_dictionary: the dictionary to modify
        key: the key to set (always a string)
        value: the value to associate with key (any type)

    Returns:
        a_dictionary, updated in place: the value at key is
        replaced if key already exists, or key is created
        with value if it doesn't
    """
    a_dictionary[key] = value
    return a_dictionary
