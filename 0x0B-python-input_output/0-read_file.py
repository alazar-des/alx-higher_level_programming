#!/usr/bin/python3
"""A module contains a function reads a text file"""


def read_file(filename=""):
    """Read a text file.

    Args:
        filename (str): file name to be read.
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")
