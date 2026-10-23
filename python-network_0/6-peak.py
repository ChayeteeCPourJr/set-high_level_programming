#!/usr/bin/python3
"""Module that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Return a peak of the list, or None if the list is empty.

    A peak is an element that is not smaller than its neighbors.
    Uses binary search, so it runs in O(log(n)).
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            # Rising slope: a peak exists to the right of mid
            low = mid + 1
        else:
            # Falling or flat: a peak exists at mid or to its left
            high = mid

    return list_of_integers[low]
