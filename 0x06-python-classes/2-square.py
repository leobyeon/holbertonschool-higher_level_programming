#!/usr/bin/python3
class Square:
    """define square
    """
    def __init__(self, size=0):
        """initialize with size param
           and create if/else loop
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
