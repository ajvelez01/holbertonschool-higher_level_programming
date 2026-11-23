#!/usr/bin/env python3
"""Converts a CSV file to a JSON file."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Reads a CSV file and writes its rows as JSON to data.json.

    Returns:
        bool: True on success, False if the file cannot be read.
    """
    try:
        with open(csv_filename, "r", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    except FileNotFoundError:
        return False
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(rows, f)
    return True
