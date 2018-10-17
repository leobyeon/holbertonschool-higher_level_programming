#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    writes a string to a text file and
    returns the number of characters written
    """
    charcount = 0

    if type(text) is not str:
        raise TypeError("your second input needs to be a string, son")
    with open(filename, mode="w", encoding="utf-8") as myFile:
        for i in text:
            charcount += 1
            myFile.write(i)
    myFile.close()
    return charcount
