#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Search for search in a list and replace with replace in a list.
    """
    return list(map(lambda x: replace if x == search else x, my_list))
