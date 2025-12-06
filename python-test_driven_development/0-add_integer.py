#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats casted to integers and return the result.

    Args:
        a: first number (int or float)
        b: second number (int or float, default is 98)

    Returns:
        int: the sum of a and b as an integer.

    Raises:
        TypeError: if a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
