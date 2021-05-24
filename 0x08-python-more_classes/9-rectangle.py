#!/usr/bin/python3
""" Rectangle class with width and hight private properties"""


class Rectangle:
    """ Rectangle class

    Args:
        width (int): rectangle width
        height (int): rectangle height
    """
    number_of_instances = 0
    print_symbol = "#"

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
        type(self).number_of_instances += 1

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
            string = string + str(self.print_symbol) * self.__width + '\n'
        string = string + str(self.print_symbol) * self.__width
        return string

    def __repr__(self):
        return "Rectangle(2, 4)"

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compare two rectangles of instance of Rectangle class and return
        rectangel with the largest area.

        Args:
            rect_1 (Rectangle): rectangle 1
            rect_2 (Rectangle): rectangle 2

        Yields:
            Rectangle with the largest area.
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ A class method which returns a new square with size.

        Args:
            size (int): size of square

        Yields:
            A new instance of a class
        """
        return Rectangle(size, size)
