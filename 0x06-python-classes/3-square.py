#!/usr/bin/python3
"""Area of a square module"""


class Square:
     """ returns the current square area

     Args:
         size (int): length of side of square

     Attributes:
         __size (int): length one side of square

     Raises:
         TypeError: if size is not an integer
         ValueError: if size is less than 0

    """

     def __init__(self, size=0):
         """initialize a new square"""

         if type(size) is not int:
             raise TypeError('size must be an integer')
         if size < 0:
             raise ValueError('size must be >= 0')
         self.__size = size


     def area(self):
         """calculate the area of square

        Attributes:
             __size (int): length one side of square

        Returns:
            area (int): squared lenght of one side

        """
         area = self.__size * self.__size
         return area
