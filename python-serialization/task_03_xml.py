#!/usr/bin/env python3
"""Serializes a dictionary to XML and deserializes it back."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Writes a dictionary to filename as XML under a <data> root."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    ET.ElementTree(root).write(filename, encoding="utf-8")


def deserialize_from_xml(filename):
    """Reads an XML file written by serialize_to_xml and returns a dict."""
    root = ET.parse(filename).getroot()
    return {child.tag: child.text for child in root}
