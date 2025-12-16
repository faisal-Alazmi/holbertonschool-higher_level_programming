#!/usr/bin/python3
"""Defines the BaseGeometry class with an unimplemented area method."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raise an Exception because area is not implemented."""
        raise Exception("area() is not implemented")
