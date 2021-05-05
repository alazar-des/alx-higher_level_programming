#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add to tuple and return the result tuple.
    """
    tuple_an = (tuple_a[0] if len(tuple_a) >= 1 else 0,
                tuple_a[1] if len(tuple_a) >= 2 else 0)
    tuple_bn = (tuple_b[0] if len(tuple_b) >= 1 else 0,
                tuple_b[1] if len(tuple_b) >= 2 else 0)
    tuple_res = (tuple_an[0] + tuple_bn[0], tuple_an[1] + tuple_bn[1])
    return tuple_res
