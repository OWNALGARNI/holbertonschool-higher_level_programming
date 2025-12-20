#!/usr/bin/python3
"""
Defines a BaseGeometry class with an unimplemented
area method.
"""


class BaseGeometry:
    """Represents a base geometry class."""

    def area(self):
        """
        Raises an exception to indicate that the area
        method is not implemented.
        """
        raise Exception("area() is not implemented")
