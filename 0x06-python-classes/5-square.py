#!/usr/bin/python3
class Square:
    """define Square
    """
    def __init__(self, size=0):
        """initialize
        """
        self.size = size

    @property
    def size(self):
        """return given size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set the size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """return size squared
        """
        return self.__size ** 2

    def my_print(self):
        """print to stdout the square with '#'
        """
        if self.size is 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end='')
                print()
