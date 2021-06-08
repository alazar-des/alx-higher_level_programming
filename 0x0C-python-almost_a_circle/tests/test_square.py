#!/usr/bin/python3
"""Test module for rectangle module.
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """A test class for all rectangle class methods.
    """
    def test_inherite_from_base(self):
        r1 = Square(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Square(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Square(10, 2, 0, 12)
        self.assertEqual(r3.id, 3)

    def test_validator(self):
        with self.assertRaises(TypeError):
            Square(10, "2")
        with self.assertRaises(TypeError):
            r = Square(10, 2)
            r.size = "2"
        with self.assertRaises(ValueError):
            r = Square(10, 2)
            r.size = -10
        with self.assertRaises(TypeError):
            r = Square(10, 2)
            r.x = {}
        with self.assertRaises(TypeError):
            r = Square(10, 2, {})
        with self.assertRaises(ValueError):
            Square(10, 2, -3)

    def test_area(self):
        r4 = Square(3, 2)
        self.assertEqual(r4.area(), 9)

        r5 = Square(2, 10)
        self.assertEqual(r5.area(), 4)

        r6 = Square(8, 7, 0, 12)
        self.assertEqual(r6.area(), 64)

    def test_display(self):
        s1 = Square(5)
        s1.display()

        s2 = Square(2, 2)
        s2.display()

        s3 = Square(3, 1, 3)
        s3.display()

    def test_str(self):
        s1 = Square(5)
        self.assertEqual(str(s1), '[Square] (5) 0/0 - 5')

    def test_update(self):
        s1 = Square(5)
        self.assertEqual(str(s1), '[Square] (6) 0/0 - 5')

        s1.update(10)
        self.assertEqual(str(s1), '[Square] (10) 0/0 - 5')

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), '[Square] (1) 3/4 - 2')

        s1.update(x=12)
        self.assertEqual(str(s1), '[Square] (1) 12/4 - 2')

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), '[Square] (1) 12/1 - 7')

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), '[Square] (89) 12/1 - 7')

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 1, 'x': 2, 'size': 10,
                                         'y': 1})
