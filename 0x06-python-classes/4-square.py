#!/usr/bin/python3
"""Access and update private attribute"""


class Square:
    """ defines a square by: (based on 3-square.py)"""

    def __init__(self, size=0):
        """init a new square.
        Args:
        size (int): size of new square.
        """
        self.size = size

    @property
    def size(self):
        """get/set the current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        area = self.__size * self.__size
        return area
