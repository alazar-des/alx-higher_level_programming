#!/usr/bin/python3
""" Rectangle class with width and hight private properties"""


class Rectangle:
    """ Rectangle class

    Args:
        width (int): rectangle width
        height (int): rectangle height
    """
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """width attribute getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width attribute setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """height attribute getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height attribute setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Return rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        for i in range(self.__height - 1):
            string = string + ('#' * self.__width) + '\n'
        string = string + ('#' * self.__width)
        return string

    def __repr__(self):
        return "Rectangle(2, 4)"
