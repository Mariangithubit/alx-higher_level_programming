#!/usr/bin/python3
"""Printing a square"""


class Square:
    """ defines a square by: (based on 4-square.py)"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """get/set the cuurent square"""
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

    def my_print(self):
        for row in range(0, self.__size):
            for col in range(0, self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
