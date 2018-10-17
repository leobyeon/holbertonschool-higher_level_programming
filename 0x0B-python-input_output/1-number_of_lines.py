#!/usr/bin/python3
def number_of_lines(filename=""):
    """returns the number of lines in a file"""
    with open(filename, encoding="utf-8") as myFile:

        linenum = -1

        while True:
            line = myFile.readline()
            linenum += 1
            if not line:
                break
        
        return linenum
