#!/usr/bin/python3
def multiple_returns(sentence):
    """Return the length of a string and its first character

    Args:
        sentence: the string to inspect

    Returns:
        A tuple (length, first_character). If sentence is empty,
        first_character is None.
    """
    if len(sentence) == 0:
        return (len(sentence), None)
    return (len(sentence), sentence[0])
