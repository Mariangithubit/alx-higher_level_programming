#!/usr/bin/python3
""" Class to JSON"""


def class_to_json(obj):
    """Retuns the dictionary description"""
    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
