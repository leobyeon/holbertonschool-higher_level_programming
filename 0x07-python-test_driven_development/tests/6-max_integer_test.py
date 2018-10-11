#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max([1,2,100,55]), 100)

        self.assertEqual(max([1000, -1, -500, 500]), 1000)

        self.assertEqual(max([1]), 1)

        self.assertEqual(max([5, 4, 3, 2, 1]), 5)

if __name__ = "__main__":
    unittest.testmaxinteger()
