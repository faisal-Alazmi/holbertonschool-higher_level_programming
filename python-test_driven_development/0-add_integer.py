#!/usr/bin/python3
"""
Module for add_integer function.
This module provides a simple function to add two integers.
"""

def add_integer(a, b=98):
    """
    Add two integers or floats and return the result as an integer.

    a and b must be integers or floats. If they are floats, they are casted to int.
    Raises TypeError if a or b is not an integer or float.

    Returns:
        int: The sum of a and b.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
