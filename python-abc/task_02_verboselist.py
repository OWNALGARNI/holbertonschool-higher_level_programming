#!/usr/bin/env python3
"""
Defines a VerboseList class that prints notifications
when the list is modified.
"""


class VerboseList(list):
    """Custom list that prints notifications on modifications."""

    def append(self, item):
        """Add an item to the list and print a message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list and print a message."""
        count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Remove an item from the list and print a message."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list and print a message."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
