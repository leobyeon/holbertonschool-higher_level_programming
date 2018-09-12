#!/usr/bin/python3
for i in range(122, 96, -1):
    num = i % 2
    print("{:s}".format(chr(i - num * 32)), end="")
