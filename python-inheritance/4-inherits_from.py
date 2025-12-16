#!/usr/bin/python3
"""
Defines a function that checks if an object is an instance of
a subclass of a specified class.
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a class that inherited
    from a_class, otherwise return False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
