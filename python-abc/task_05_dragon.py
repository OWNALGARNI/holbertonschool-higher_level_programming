#!/usr/bin/env python3
"""
Defines mixins and a Dragon class to demonstrate mixins usage.
"""


class SwimMixin:
    """Mixin that provides swimming behavior."""

    def swim(self):
        """Print swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying behavior."""

    def fly(self):
        """Print flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represents a dragon that can swim and fly."""

    def roar(self):
        """Print roaring action."""
        print("The dragon roars!")
