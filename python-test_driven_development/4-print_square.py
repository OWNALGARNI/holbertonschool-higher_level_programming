#!/usr/bin/python3
"""
This module provides a function that prints a square using '#'.
"""


def print_square(size):
    """
    Print a square with the character '#'.

    Args:
        size: The length of the square's sides.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is negative.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
