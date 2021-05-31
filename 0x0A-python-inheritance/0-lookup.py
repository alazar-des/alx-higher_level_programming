#!/usr/bin/python3
""" Return object attributes"""


def lookup(obj):
    """ Return obj attributes.

    Args:
        obj (instance): object

    Yields:
        obj attrbutes.
    """
    return dir(obj)
