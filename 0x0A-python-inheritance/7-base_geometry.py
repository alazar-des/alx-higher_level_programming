#!/usr/bin/python3
"""A class with an area public function"""

import json
class BaseGeometry:
    """A class with an area public function"""
    def area(self):
        """ Raise an Exception with area() is not implemented message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value.

        Args:
            name (string): always string
            value (int): if not integer or less than zero raise exception
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
