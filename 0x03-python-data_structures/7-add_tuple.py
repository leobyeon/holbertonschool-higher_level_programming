#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = tuple_a[:]
    y = tuple_b[:]
    if len(tuple_b) == 0 or len(tuple_b) == 1:
        y = (0, 0)
    elif len(tuple_b) < 2:
        y = (tuple_b[0:2])
    return tuple(map(sum, zip(x, y)))
