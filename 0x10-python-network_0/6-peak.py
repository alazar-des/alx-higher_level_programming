#!/usr/bin/python3
"""Find peak of a list.
"""


def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    peak = list_of_integers[0]
    for i in range(1, len(list_of_integers)):
        if list_of_integers[i] > peak:
            peak = list_of_integers[i]
    return peak
