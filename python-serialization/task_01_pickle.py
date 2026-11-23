#!/usr/bin/env python3
"""Serializes and deserializes a custom object using pickle."""
import pickle


class CustomObject:
    """Represents an object with name, age and is_student attributes."""

    def __init__(self, name, age, is_student):
        """Initializes the object with its attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Saves the current instance to filename using pickle."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Loads and returns a CustomObject from filename, or None on error."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (OSError, pickle.UnpicklingError, EOFError, AttributeError):
            return None
