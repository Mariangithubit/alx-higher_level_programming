#!/usr/bin/python3
"""Prevent user from creat new instance
"""


class LockedClass:
    """lock class from change"""
    __slots__ = ["first_name"]
