#!/usr/bin/python3
"""Module that defines a function to print indented text.

This module provides text_indentation, a function that prints a
text with 2 new lines after each '.', '?' and ':'.
"""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ".?:"
    sentence = ""
    for char in text:
        if char == " " and len(sentence) == 0:
            continue
        sentence += char
        if char in chars:
            print(sentence.strip())
            print()
            sentence = ""
    print(sentence.strip(), end="")
