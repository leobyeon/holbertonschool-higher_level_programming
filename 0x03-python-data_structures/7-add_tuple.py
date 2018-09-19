#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = tuple_a + (0, 0)
    y = tuple_b + (0, 0)
    x = x[0:2]
    y = y[0:2]
    return tuple(map(sum, zip(x, y)))
