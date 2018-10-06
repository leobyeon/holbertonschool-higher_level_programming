#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_maxint(self):
        self.assertEqual(max([1,2,100,55]), 100)

    def test_maxint2(self):
        self.assertEqual(max([1000, -1, -500, 500]), 1000)

    def test_maxint3(self):
        self.assertEqual(max([1]), 1)

    def test_maxint4(self):
        self.assertEqual(max([5, 4, 3, 2, 1]), 5)

if __name__ = "__main__":
    unittest.testmaxinteger()
