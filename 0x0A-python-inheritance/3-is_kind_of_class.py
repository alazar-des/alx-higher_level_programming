#!/usr/bin/python3
"""checks if instance is an instance of given class"""

import json
def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of a_class otherwise False.

    Args:
        obj (instance): an instance object to be checked

    Yields:
        True or False depending on the object is whether instance of the class
        or not.
    """
    return isinstance(obj, a_class)
