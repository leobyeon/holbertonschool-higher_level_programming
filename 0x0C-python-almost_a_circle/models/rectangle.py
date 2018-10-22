#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """define rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """return given width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """return given height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """return x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """return y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area"""
        return self.width * self.height

    def display(self):
        """
        prints in stdout the Rectangle instance
        with the char '#'
        """
        for i in range(self.y):
            print("")
        for j in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """override the default __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an arg to each attribute"""
        i = 0
        if isinstance(args, tuple) and len(args) > 0:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
                i += 1
        for k, v in kwargs.items():
            if k == "id":
                self.id = v
            if k == "width":
                self.width = v
            if k == "height":
                self.height = v
            if k == "x":
                self.x = v
            if k == "y":
                self.y = v

    def to_dictionary(self):
        """return the dict representation of a Rectangle"""
        rect = {}
        rect["id"] = self.id
        rect["width"] = self.width
        rect["height"] = self.height
        rect["x"] = self.x
        rect["y"] = self.y
        return rect
