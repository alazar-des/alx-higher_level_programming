#!/usr/bin/python3
"""Return the dict representation of instance attributes."""


class Student:
    """Student class. with first name, last name and age public attributes.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that retrieves a dictionary representation of a Student instance.
        """
        return (self.__dict__)
