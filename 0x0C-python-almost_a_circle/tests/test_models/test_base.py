#!/usr/bin/python3
"""test module for base"""
import unittest
from models.base import Base


class BaseTests(unittest.TestCase):
    """define class for the tests"""

    def test_1arg(self):
        b = Base(2)
        self.assertEqual(2, b.id)

    def test_int(self):
        """test integer"""
        c = Base(666)
        self.assertEqual(666, c.id)

    def test_floats(self):
        """test floats"""
        d = Base(6.66)
        self.assertEqual(6.66, d.id)
        d = Base(-6.66)
        self.assertEqual(-6.66, d.id)

    def test_str(self):
        """test strings"""
        e = Base("6")
        self.assertEqual("6", e.id)
        e = Base("666")
        self.assertEqual("666", e.id)

    def test_class(self):
        """test class type"""
        f = Base()
        self.assertFalse(isinstance(type(f), Base))

    def test_none(self):
        """test none and empty"""
        g = Base(None)
        self.assertEqual(2, g.id)
        g = Base()
        self.assertEqual(3, g.id)
