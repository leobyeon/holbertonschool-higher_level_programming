#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    results = {}
    for key in a_dictionary:
        a_dictionary[key] = a_dictionary[key] * 2
    return results
