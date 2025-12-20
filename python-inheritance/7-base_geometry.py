#!/usr/bin/python3
"""
Defines BaseGeometry with an unimplemented area method
and an integer validation method.
"""


class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Raises an exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name="value", value=None):
        """
        Validates that value is an integer greater than zero.

        Args:
            name: The name of the value to validate.
            value: The value to validate.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
