#!/usr/bin/python3
"""Area of a square module"""


class Square:
     """ returns the current square area"""
     def __init__(self, size=0):
         if type(size) is not int:
             raise TypeError('size must be an integer')
         if size < 0:
             raise ValueError('size must be >= 0')
         self.__size = size

     def area(self):
         """calculate the area of square"""
         area = self.__size * self.__size
         return area
