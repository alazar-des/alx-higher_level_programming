#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return
    values = list(a_dictionary.values())
    if value in values:
        count = values.count(value)
        while count > 0:
            key = (list(a_dictionary.keys()))[
                 (list(a_dictionary.values())).index(value)
            ]
            a_dictionary.pop(key)
            count -= 1
    return a_dictionary
