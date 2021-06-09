#!/usr/bin/python3
"""Test module for base module.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """A test class for all base class methods.
    """
    def test_assign_automatic_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
