#!/usr/bin/python3
"""Integer validator"""


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
        self.__integer_validator('width', width)
        self.__width = width
        self.__integer_validator('height ', height)
        self.__height = height

    def area(self):
        """implement area"""
        return self.__width * self.__height
    
    def __str__(self):
        """return str"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)


class SquareRectangle):
    """Class square"""
    def __init__(self, size):
        """Instantiation"""
        self.integer_validator('size', size)
        super().__init__('size', size)
        self.__size = size

