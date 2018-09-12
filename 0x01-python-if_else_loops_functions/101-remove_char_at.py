#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    for i in str:
        if n:
            copy += i
        n -= 1
    return copy
