#!/usr/bin/python3
"""Save json representation of python object in file.
"""


import json
def save_to_json_file(my_obj, filename):
    """Save json representation of python object in file.
    open file for write and write the json string to it. if doesn't exist
    create it.

    Args:
        my_obj (obj): python object
        filename (str): file name the json representation to be written to.
    """
    with open(filename, 'w') as file_write:
        json.dump(my_obj, file_write)
