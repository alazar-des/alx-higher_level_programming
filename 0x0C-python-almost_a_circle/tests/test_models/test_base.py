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
    def test_instance_id(self):
        """Test for id. If id is not given and when it is given.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(10)
        self.assertEqual(b3.id, 10)

        b4 = Base()
        self.assertEqual(b4.id, 3)

        s1 = Square(4, 9, 4, 69)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary,
                         '[{"id": 69, "size": 4, "x": 9, "y": 4}]')

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary,
                         '[{"id": 4, "width": 10, "height": 7, "x": 2, "y": 8}]')

        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), '[Rectangle] (5) 1/0 - 3/5')

        s1 = Square(3, 5, 1)
        s1_dictionary = r1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s2), '[Square] (5) 1/0 - 3')
