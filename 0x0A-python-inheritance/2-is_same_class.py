#!/usr/bin/python3
"""Exact same object"""


def is_same_class(obj, a_class):
    """ returns True if the obj an instance of class"""
    a = type(obj)
    if a == a_class:
        return True
    return False
