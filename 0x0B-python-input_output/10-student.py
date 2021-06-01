#!/usr/bin/python3
"""Return the dict representation of instance attributes."""


class Student:
    """Student class. with first name, last name and age public attributes.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): a list of attributes that will be retrived

        Yields:
            If attrs is a list attributes with in the list, otherwise all
            the attributes of the instance.
        """
        if type(attrs) is list:
            self_dict = self.__dict__
            d = dict()
            for key in attrs:
                if key in self_dict:
                    d[key] = self_dict[key]
            return d
        return (self.__dict__)
