#!/usr/bin/python3
def read_file(filename=""):
    """opens and reads files"""
    with open(filename, mode="r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
