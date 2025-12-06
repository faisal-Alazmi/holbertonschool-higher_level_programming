#!/usr/bin/python3
"""
Module for add_integer function.
Provides a function that adds two integers.
"""
DEf add_integer(a, b=98):
    """
    Add two integers or floats and return the result as an integer.

    Args:
        a (int or float): The first number.
        b (int or float): The second number (default = 98).

    Returns:
        int: The integer sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
