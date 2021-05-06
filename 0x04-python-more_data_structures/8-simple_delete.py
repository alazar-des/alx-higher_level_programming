#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Delete key in dictionary.
    """
    if (list(a_dictionary.keys()).count(key) != 0):
        del(a_dictionary[key])
    return a_dictionary
