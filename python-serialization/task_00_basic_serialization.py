#!/usr/bin/env python3
"""Serializes a dictionary to JSON and deserializes it back."""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes data to JSON and saves it to filename, replacing it."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Loads a JSON file and returns the data as a Python object."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
