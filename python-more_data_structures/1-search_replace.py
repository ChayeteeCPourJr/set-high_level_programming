#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list

    Args:
        my_list: the initial list
        search: the element to replace
        replace: the new element

    Returns:
        A new list, same size as my_list, with every occurrence of
        search replaced by replace. The original list is not
        modified.
    """
    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list
