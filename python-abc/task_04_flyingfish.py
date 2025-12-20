#!/usr/bin/env python3
"""
Defines Fish, Bird, and FlyingFish classes to demonstrate
multiple inheritance and method overriding.
"""


class Fish:
    """Represents a fish."""

    def swim(self):
        """Print swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat of fish."""
        print("The fish lives in water")


class Bird:
    """Represents a bird."""

    def fly(self):
        """Print flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat of bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish using multiple inheritance."""

    def swim(self):
        """Override swim behavior."""
        print("The flying fish is swimming!")

    def fly(self):
        """Override fly behavior."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override habitat behavior."""
        print("The flying fish lives both in water and the sky!")
