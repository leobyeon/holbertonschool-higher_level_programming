#!/usr/bin/python3
def number_of_lines(filename=""):
    """returns the number of lines in a file"""
    with open(filename, encoding="utf-8") as myFile:

        linecount = 0

        for line in myFile:
            linecount += 1

        return linecount
