#!/usr/bin/python3
"""returns the dictionary description with simple data structure(list,
dictionary, string, integer and boolean) for JSON serialization of an object.
"""


def class_to_json(obj):
    """returns instance attributes.

    Args:
        obj (obj): python instance of a class

    Yields:
        dict represenataion of the object.
    """
    return (obj.__dict__)
