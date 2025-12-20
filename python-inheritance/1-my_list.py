#!/usr/bin/python3
"""
Defines a class MyList that inherits from list and provides
a method to print the list in sorted order.
"""


class MyList(list):
    """Represents a list with a method to print it sorted."""

    def print_sorted(self):
        """Prints the list elements in ascending sorted order."""
        print(sorted(self))
