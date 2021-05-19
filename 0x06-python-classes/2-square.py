#!/usr/bin/python3
"""
Define a Square class the define a square
"""


class Square:
    """
    A square class. And initialize size

    Args:
        size (int): size of square

    Attributes:
         size (int): size of square
    """

    def __init__(self, size=0):
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
