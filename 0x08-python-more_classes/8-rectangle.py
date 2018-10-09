#!/usr/bin/python3
class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    """define class rectangle"""
    def __init__(self, width=0, height=0):
        """initialize"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """returns given width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns given height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return height x width"""
        return self.height * self.width

    def perimeter(self):
        """return height x 2 + width x 2"""
        if self.width is 0 or self.height is 0:
            return 0
        return self.height * 2 + self.width * 2

    def __str__(self):
        newstr = ""
        if self.area is 0:
            return newstr
        return "\n".join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """return the formatted str"""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """if deleted, print message"""
        print("Bye rectangle...")
        if type(self).number_of_instances > 0:
            type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1.area()
        return max(rect_1.area(), rect_2.area())
