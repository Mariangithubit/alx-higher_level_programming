#!/usr/bin/python3
""" Same class or inherit"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance"""
    a = isinstance(obj), a_class
    if a:
        return True
    return False
