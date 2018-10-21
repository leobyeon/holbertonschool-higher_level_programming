#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """define Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """override the default str"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """return the size"""
        return self.width

    @size.setter
    def size(self, value):
        """set the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assign an arg to each attribute"""
        i = 0
        if isinstance(args, tuple) and len(args) > 0:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        for k, v in kwargs.items():
            if k == "id":
                self.id = v
            if k == "size":
                self.size = v
            if k == "x":
                self.x = v
            if k == "y":
                self.y = v

    def to_dictionary(self):
        """return the dict representation of a square"""
        sq = {}
        sq["id"] = self.id
        sq["size"] = self.size
        sq["x"] = self.x
        sq["y"] = self.y
        return sq
