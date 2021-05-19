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
        self.__size = size

    @property
    def size(self):
        """Get size property"""
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Return the area of a square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print # area times in stdout.
        """
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
