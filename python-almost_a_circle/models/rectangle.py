#!/usr/bin/python3
"""Temporary minimal Rectangle, used only to test Base.draw."""
from models.base import Base


class Rectangle(Base):
    """Rectangle with width, height, x and y."""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
