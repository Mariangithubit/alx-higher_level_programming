#!/usr/bin/python3
"""
 prevents the user from dynamically
 creating new instance
"""


class LockedClass:
    __slots__ = ['first_name']
