#!/usr/bin/python3
"""
Module for add_integer function.
This module provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats and return the result as an integer.

    a and b must be integers or floats. If not, a TypeError is raised.

    Returns:
        int: The integer addition of a and b.
    """
    if not isinstance(a, (int, float)) or a != a:
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)) or b != b:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
