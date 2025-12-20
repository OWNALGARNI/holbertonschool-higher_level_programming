#!/usr/bin/python3
"""
Defines a BaseGeometry class with an area method
and an integer validation method.
"""


class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Raises an exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than zero.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
