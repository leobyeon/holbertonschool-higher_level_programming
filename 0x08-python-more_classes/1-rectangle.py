#!/usr/bin/python3
class Rectangle:
    """define class rectangle"""
    def __init__(self, width=0, height=0):
        """initialize"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """return given width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if type(value) is not int:
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """return given height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if value < 0:
            raise ValueError("height must be >= 0")
        if type(value) is not int:
            raise TypeError("height must be an integer")
        self.__height = value
