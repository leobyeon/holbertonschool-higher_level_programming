#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97:
            print("{:c}".format(ord(str[i]) - 32), end="")
        else:
            print("{:s}".format(str[i]), end="")
    print("")
