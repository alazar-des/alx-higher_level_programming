#!/usr/bin/python3
"""A class with no attribute which which only allowed an istance to be created
with a name = \"first_name\" only"""


class LockedClass:
    """ A class with no attributes """
    __slots__ = ['first_name']
