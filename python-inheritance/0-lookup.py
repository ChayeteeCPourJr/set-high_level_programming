#!/usr/bin/python3
"""Module containing a function to list an object's attributes and methods."""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return dir(obj)
