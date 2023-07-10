#!/usr/bin/python3
"""My integer"""


class MyInt(int):
    """Inherits integer"""
    def __eq__(self, other):
        return int(str(self)) != other

    def __ne__(self, other):
        return int(str(self)) == other
