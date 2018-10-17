#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file and prints"""
    with open(filename, encoding="utf-8") as myFile:

        linenum = -1

        while True:
            line = myFile.readline()
            linenum += 1
            if not line:
                break
    myFile.close()

    with open(filename, encoding="utf-8") as myFile:

        print("{} : {}".format(nb_lines, linenum))

        if nb_lines <= 0 or nb_lines >= linenum:
            print(myFile.read(), end="")
        else:
            while nb_lines != 0:
                line = myFile.readline()
                print(line, end="")
                nb_lines -= 1
