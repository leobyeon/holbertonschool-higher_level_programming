#!/usr/bin/python3
class Square(__import__('9-rectangle').Rectangle):
    """define class square"""

    def __init__(self, size):
        """initialize"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """return the area of square"""
        return self.__size * self.__size

    def __str__(self):
        """set print"""
        return "[Square] {}/{}".format(self.__size, self.__size)
