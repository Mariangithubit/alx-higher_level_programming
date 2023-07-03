#!/usr/bin/python3
"""Compare rectangles"""


class Rectangle:
    """Defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation"""
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

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

    @Static method
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else
        rect_2

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
        type(self).number_of_instances -= 1
        print ("Bye rectangle...")
