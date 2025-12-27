#!/usr/bin/env python3
"""Pickling custom classes: serialize and deserialize CustomObject instances."""


import pickle


class CustomObject:
    """Custom object that can be serialized/deserialized using pickle."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in the required format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current instance to a file using pickle.

        Returns:
            True if successful, otherwise None.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
            return True
        except (OSError, pickle.PickleError, AttributeError, TypeError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return a CustomObject instance from a pickle file.

        Returns:
            A CustomObject instance if successful, otherwise None.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except (OSError, EOFError, pickle.UnpicklingError, pickle.PickleError):
            return None
