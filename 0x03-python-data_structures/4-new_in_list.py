#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = my_list.copy()
    if 0 <= idx <= len(newlist) - 1:
        newlist[idx] = element
        return newlist
    else:
        return my_list
