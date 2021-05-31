#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""A subclass of Geometry class"""


class Rectangle(BaseGeometry):
    """A subclass of Geometry class"""
    def __init__(self, width, height):
        super.integer_validator("width", width)
        self.__width = width
        super.integer_validator("height", height)
        self.__height = height
