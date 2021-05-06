#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Search for search in a list and replace with replace in a list.
    """
    def if_equal_replace(x):
        if x == search:
            return replace
        else:
            return x
    return list(map(if_equal_replace, my_list))
