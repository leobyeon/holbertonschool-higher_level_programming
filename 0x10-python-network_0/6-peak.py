#!/usr/bin/env python3
""" finds a peak in an unsorted list of integers """


def find_peak(list_of_integers):
    arr = list_of_integers
    lo = 0
    hi = len(arr) - 1
    while lo < hi:
        mid = int((lo + hi) / 2)
        if arr[mid - 1] <= arr[mid] and arr[mid + 1] <= arr[mid]:
            return arr[mid]
        elif arr[mid - 1] > arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
        if mid == lo:
            if arr[lo] > arr[hi]:
                return arr[lo]
            else:
                return arr[hi]
    return None
