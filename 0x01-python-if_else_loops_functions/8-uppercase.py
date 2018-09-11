#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for i in range(len(str)):
        if ord(str[i]) >= 97:
            newstr += chr(ord(str[i]) - 32)
        else:
            newstr += str[i]
    print(newstr)
