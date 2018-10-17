#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    appends a string at the end of a text file
    and returns the number of chars added
    """
    charCount = 0

    with open(filename, "a+", encoding="utf-8") as myFile:
        for i in text:
            charCount += 1
            myFile.write(i)
    myFile.close()
    return charCount
