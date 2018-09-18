#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = tuple_a[:]
    y = tuple_b[:]
    if len(tuple_b) == 0:
        y = (0, 0)
    elif len(tuple_b) == 1:
        y = (tuple_b[0], 0)
    elif len(tuple_b) < 2:
        y = (tuple_b[0:2])
    if len(tuple_a) == 0:
        x = (0, 0)
    elif len(tuple_a) == 1:
        x = (tuple_a[0], 0)
    elif len(tuple_a) < 2:
        x = (tuple_a[0:2])
    return tuple(map(sum, zip(x, y)))
