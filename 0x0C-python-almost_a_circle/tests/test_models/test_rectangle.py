#!/usr/bin/python3
"""test module for rectangle"""
import unittest
import json
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class RectangleTests(unittest.TestCase):
    """test cases for Rectangle class"""

    def setup(self):
        """set up"""
        self.r1 = Rectangle(1, 1)
        self.r2 = Rectangle(1, 2, 1, 2)
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput

    def breakdown(self):
        """break down"""
        sys.stdout = sys.__stdout__
        Base._Base__nb_objects = 0

    def value_error(self):
        """test to check value errors"""
        with self.assertRaises(TypeError):
            Rectangle(None, 6, 6, 6, 6)
            Rectangle(6, None, 6, 6, 6)
            Rectangle(6, 6, None, 6, 6)
            Rectangle(6, 6, 6, None, 6)
            Rectangle(6, 6, 6, 6, None)

    def type_error(self):
        """test to check type errors"""
        with self.assertRaises(ValueError):
            Rectangle(0, 6, 6, 6, 6)
            Rectangle(6, 0, 6, 6, 6)
            Rectangle(6, 6, 0, 6, 6)
            Rectangle(6, 6, 6, 0, 6)
            Rectangle(6, 6, 6, 6, 0)

        def error_messages(self):
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
