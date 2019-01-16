#!/usr/bin/env python3
""" finds a peak in an unsorted list of integers """


def find_peak(list_of_integers):
    arr = list_of_integers
    if arr != []:
        arr.sort()
        return arr[-1]
    else:
        return None
