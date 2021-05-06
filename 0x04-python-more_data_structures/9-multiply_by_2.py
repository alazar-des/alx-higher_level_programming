#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Multiplay values of dictionary by 2.
    """
    return dict(map((lambda item: (item[0], item[1] * 2)),
                    a_dictionary.items()))
