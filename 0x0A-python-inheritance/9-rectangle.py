#!/usr/bin/python3
"""Full rectangle"""


class BaseGeometry:
    """Public instance method"""

    def area(self):
        """Raise exception"""
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
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height

    def area(self):
        """implement area"""
        return self.__width * self.__height

    def __str__(self):
        """return str"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
