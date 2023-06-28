#!/usr/bin/python3
"""Coordinates of a square"""


class Square:
    """ defines a square by: (based on 5-square.py)"""
    def __init__(self, size=0, position=(0, 0)):
        """init a new square.

        Args:
        size (int): size of new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """get/set the current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter method"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """get/set the position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter position method"""
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for num in value:
            if type(num) is not int or num < 0:
                raise TypeError('position must be a tuple of 2 positive integers')
            self.__position = value

    def area(self):
        """return current square area"""
        area = self.__size * self.__size
        return area

    def my_print(self):
        """print the square"""
        if self.__size == 0:
            print()
        else:
            for v_offset in range(0, self.__position[1]):
                print()
            for row in range(0, self.__size):
                for h_offset in range(0, self.__position[0]):
                    print(" ", end="")
                for col in range(0, self.__size):
                    print("#", end="")
                print()
