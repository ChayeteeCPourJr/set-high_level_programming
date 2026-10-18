#!/usr/bin/python3
"""Temporary minimal Square, used only to test Base.draw."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square defined by a size, x and y."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
