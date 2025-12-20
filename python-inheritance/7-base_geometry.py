#!/usr/bin/python3
"""
Defines a BaseGeometry class with area and integer validation
methods.
"""


class BaseGeometry:
    """Represents a base geometry class."""

    def area(self):
        """
        Raises an exception to indicate that the area
        method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than zero.

        Args:
            name: The name of the value.
            value: The value to validate.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
