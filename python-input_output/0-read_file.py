#!/usr/bin/python3
"""Defines a function that reads and prints a UTF8 text file"""


def read_file(filename=""):
    """Read a text file (UTF8) and print its content to stdout

    Args:
        filename: the path of the file to read

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
