#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Return the best score.
    """
    if a_dictionary is None or (not len(a_dictionary)):
        return
    keys = list(a_dictionary.keys())
    vals = list(a_dictionary.values())
    return keys[vals.index(max(vals))]
