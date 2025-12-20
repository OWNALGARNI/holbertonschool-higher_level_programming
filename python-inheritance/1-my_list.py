#!/usr/bin/python3
"""Defines MyList, a list subclass with a sorted print method."""


class MyList(list):
    """A custom list class."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
