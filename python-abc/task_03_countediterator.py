#!/usr/bin/env python3
"""
Defines a CountedIterator that counts how many items
have been iterated over.
"""


class CountedIterator:
    """Iterator that keeps track of iteration count."""

    def __init__(self, iterable):
        """Initialize the iterator and counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Return the next item and increment the counter.
        Raises StopIteration when no items remain.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def __iter__(self):
        """Return the iterator object."""
        return self

    def get_count(self):
        """Return the number of iterated items."""
        return self.count
