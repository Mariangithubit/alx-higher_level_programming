#!/usr/bin/python3
"""String representation"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiation"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        self.__width = value
        try:
            assert type(self.__width) == int
        except:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")

   @property
    def height(self):
        """Retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        self.__height == value
        try:
            assert type(self.__height) == int
        except:
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__width):
            for k in range(self.__height):
                return ("\n".join(["".join(["#"])]))

    def __repr__(self):
        """representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """delet rectangle"""
        print ("Bye rectangle...")
