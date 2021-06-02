#!/usr/bin/python3
"""Return the json representation of an object"""


import json
def to_json_string(my_obj):
    """Return the json representation of an object.

    Args:
        my_obj (obj): python object to be returned its equivalent json
            representation.

    Yeilds:
        json representation of python object.
    """
    return json.dumps(my_obj, sort_keys=True)
