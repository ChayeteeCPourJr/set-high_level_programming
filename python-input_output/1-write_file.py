#!/usr/bin/python3
"""Defines a function that writes a string to a UTF8 text file"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8), creating it if it
    doesn't exist or overwriting it if it does

    Args:
        filename: the path of the file to write to
        text: the string to write

    Returns:
        The number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
