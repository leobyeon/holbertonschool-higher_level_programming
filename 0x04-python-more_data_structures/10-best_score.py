#!/usr/bin/python3
def best_score(a_dictionary):
    d = a_dictionary
    if d:
        return sorted([(v, k) for k, v in d.items()], reverse=True)[0][1]
