def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add to tuple and return the result tuple.
    """
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    list_res = []
    for i in range(2):
        if len(list_a):
            a = list_a.pop(0)
        else:
            a = 0
        if len(list_b):
            b = list_b.pop(0)
        else:
            b = 0
        list_res.append(a + b)
    tuple_res = tuple(list_res)
    return tuple_res
