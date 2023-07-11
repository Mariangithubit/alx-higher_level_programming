#!/usr/bin/python3
"""appends a string"""


def append_write(filename="", text=""):
    """Append to a file"""
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
