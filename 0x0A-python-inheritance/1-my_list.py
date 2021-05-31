#!/usr/bin/python3
"""Prints list in sorted way."""


class MyList(list):
    """A subclass extends from list and add a function that prints a list
    in sorted way."""
    def print_sorted(self):
        """print list in ascending order."""
        print(sorted(self))
