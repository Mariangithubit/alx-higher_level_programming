#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """Returns True if obj an instance of a class"""
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
