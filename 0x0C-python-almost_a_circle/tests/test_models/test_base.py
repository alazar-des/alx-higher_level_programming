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

        """
    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary,
                         {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})

        s1 = Square(4, 9, 4, 69)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictioanry,
                         {'x': 2, 'size': 10, 'id': 1, 'y': 8})

    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output,
                         [{'height': 4, 'width': 10, 'id': 89},
                          {'height': 7, 'width': 1, 'id': 7}])

    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), '[Rectangle] (1) 1/0 - 3/5')

    def load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()
        """
