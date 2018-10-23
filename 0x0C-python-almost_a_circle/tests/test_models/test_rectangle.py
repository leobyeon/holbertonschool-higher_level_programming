#!/usr/bin/python3
"""test module for rectangle"""
import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class RectangleTests(unittest.TestCase):
    """test cases for Rectangle class"""

    def test_value_error(self):
        """test to check value errors"""
        with self.assertRaises(TypeError):
            test1 = Rectangle(None, 6, 6, 6, 6)
            test2 = Rectangle(6, None, 6, 6, 6)
            test3 = Rectangle(6, 6, None, 6, 6)
            test4 = Rectangle(6, 6, 6, None, 6)
            test5 = Rectangle(6, 6, 6, 6, None)

    def test_type_error(self):
        """test to check type errors"""
        with self.assertRaises(ValueError):
            test1 = Rectangle(0, 6, 6, 6, 6)
            test2 = Rectangle(6, 0, 6, 6, 6)
            test3 = Rectangle(6, 6, 0, 6, 6)
            test4 = Rectangle(6, 6, 6, 0, 6)
            test5 = Rectangle(6, 6, 6, 6, 0)

    def test_error_messages(self):
        """test to check correct error messages"""
        with self.assertRaises(TypeError) as e:
            Rectangle("satan's poop", 1)
            self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            Rectangle(666, None)
            self.assertEqual("height must be an integer", str(e.exception))

        with self.assertRaises(ValueError) as e:
            Rectangle(6, 6, -6)
            self.assertEqual("x must be >= 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            Rectangle(6, 6, 6, -6)
            self.assertEqual("y must be >= 0", str(e.exception))
