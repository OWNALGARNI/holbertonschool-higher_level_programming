#!/usr/bin/python3
"""This module defines a Square class with size validation and area calculation."""


class Square:
    """This class defines a square."""

    def __init__(self, size=0):
        """Initialize a new Square with validated size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
