#!/usr/bin/python3
def best_score(a_dictionary):
    """Return the key with the biggest integer value

    Args:
        a_dictionary: a dictionary whose values are all integers,
        assumed to all be different

    Returns:
        The key associated with the biggest value, or None if
        a_dictionary is empty or None
    """
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    best_key = None
    best_value = None
    for key in a_dictionary:
        if best_value is None or a_dictionary[key] > best_value:
            best_value = a_dictionary[key]
            best_key = key
    return best_key
