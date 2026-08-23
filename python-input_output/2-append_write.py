#!/usr/bin/python3
"""Defines a function that appends a string to a UTF8 text file"""


def append_write(filename="", text=""):
    """Append a string to the end of a text file (UTF8), creating
    the file if it doesn't exist

    Args:
        filename: the path of the file to append to
        text: the string to append

    Returns:
        The number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
