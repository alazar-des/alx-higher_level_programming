#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Add unique numbers in list.
    """
    return sum(x for x in set(my_list))
