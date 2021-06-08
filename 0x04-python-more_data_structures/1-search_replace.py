#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Search for search in a list and replace with replace in a list.
    """
    def search(x):
        if x == search:
            return replace
        else:
            return x
    return list(map(search, my_list))
    #return list(map(lambda x: replace if x == search else x, my_list))
