#!/usr/bin/python3
"""Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file"""
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
