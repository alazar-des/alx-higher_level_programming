#!/usr/bin/python3
"""Read json representation from file and return python object."""


import json
def load_from_json_file(filename):
    """Read json representation from file and return python object.

    Args:
        filename (str): file name where the json strings is .
    """
    with open(filename) as file_json:
        return json.load(file_json)
