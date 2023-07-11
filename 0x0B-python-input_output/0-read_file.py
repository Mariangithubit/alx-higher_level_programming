#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Reads a text file"""
    with open(filename, 'r', encoding="UTF8") as f:
        read_data = f.read()
        print(read_data, end='')
