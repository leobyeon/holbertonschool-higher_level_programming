#!/usr/bin/python3
def no_c(my_string):
    newstr = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        newstr += i
    return newstr
