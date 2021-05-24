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
