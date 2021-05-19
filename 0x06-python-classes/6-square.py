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

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if type(position) is not tuple or len(position) != 2:
            raise TypeError(
                    "position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError(
                    "position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError(
                    "position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """Get position property"""
        return self.__position

    @position.setter
    def position(self, a):
        self.__position = a

    def area(self):
        """
        Return the area of a square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print # area times in stdout.
        position[0] times space at the beginning of #.
        """
        if self.size == 0:
            print()
        else:
            for l in range(self.position[1]):
                print()
        for i in range(self.size):
            for k in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()
