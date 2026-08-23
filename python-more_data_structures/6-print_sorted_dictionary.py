#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys, one 'key: value' per line

    Args:
        a_dictionary: a dictionary whose keys are all strings

    Returns:
        None
    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
