#!/usr/bin/python3
class Square:
    """defines class of square
    """
    def __init__(self, size=0):
        """initialize self
        """
        self.size = size

    @property
    def size(self):
        """return given size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """return given size squared
        """
        return self.__size ** 2
