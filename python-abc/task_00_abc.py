#!/usr/bin/env python3
"""
Defines an abstract Animal class and its subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Represents a dog."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Represents a cat."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"
