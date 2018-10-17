#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file and prints"""
    with open(filename, encoding="utf-8") as myFile:

        linecount = 0

        for line in myFile:
            linecount += 1

    myFile.close()

    with open(filename, encoding="utf-8") as myFile:

        if nb_lines <= 0 or nb_lines >= linecount:
            print(myFile.read(), end="")
        else:
            while nb_lines != 0:
                line = myFile.readline()
                print(line, end="")
                nb_lines -= 1
