#!/usr/bin/python3
"""check if class is subclass."""


def inherits_from(obj, a_class):
    """check if class is subclass.

    Args:
        obj (instance): object instance to be checked
        a_class (class): object instance to be checked against

    Yields:
        True or False
    """
    return issubclass(type(obj), a_class)
