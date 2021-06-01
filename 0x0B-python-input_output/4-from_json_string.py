#!/usr/bin/python3
import json
"""Return the json representation of an object"""


def from_json_string(my_str):
    """Return the python data structure from json representation.

    Args:
        my_str (json str):json string to be returned its equivalent python
            data structure.

    Yeilds:
        python object.
    """
    return json.loads(my_str)
