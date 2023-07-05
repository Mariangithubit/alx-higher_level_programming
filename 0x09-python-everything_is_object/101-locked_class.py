#!/usr/bin/python3
"""Prevent user from creat new instance
"""


class LockedClass:
    __slots__= ['first_name']
