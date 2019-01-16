#!/usr/bin/python3


def find_peak(list_of_integers):
    """finds a peak in an unsorted list of integers"""
    arr = list_of_integers
    if arr != []:
        arr.sort()
        return arr[-1]
    else:
        return None
