#!/usr/bin/python3
import unittest
from models.base import Base


class BaseTests(unittest.TestCase):
    """define class for the tests"""

  def test1(self):
      b = Base()
      self.assertEqual(1, b.id)

  def test2(self):
      c = Base(500)
      self.assertFalse(500, c.id)
