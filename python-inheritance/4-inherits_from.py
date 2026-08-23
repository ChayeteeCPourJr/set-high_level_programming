#!/usr/bin/python3
"""Module for checking class inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class."""
    return type(obj) is not a_class and isinstance(obj, a_class)
