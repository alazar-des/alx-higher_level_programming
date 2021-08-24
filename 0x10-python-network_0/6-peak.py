#!/usr/bin/python3
"""Find peak of a list.
"""


def find_peak(list_of_integers):
    """ Return the max number from a list.

    list_of_integers: list
    """
    if len(list_of_integers) == 0:
        return None
    peak = list_of_integers[0]
    for i in range(1, len(list_of_integers)):
        if list_of_integers[i] > peak:
            peak = list_of_integers[i]
    return peak
