#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """ inherits BaseGeometry"""

    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        a = type(value)
        if a != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """class Rectangle BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation rectangle"""
        self.__integer_validator('width', width)
        self.__width = width
        self.__integer_validator('height ', height)
        self.__height = height
