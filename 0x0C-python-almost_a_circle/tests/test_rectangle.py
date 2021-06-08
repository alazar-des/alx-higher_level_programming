#!/usr/bin/python3
"""Test module for rectangle module.
"""
import unittest
unittest.TestLoader.sortTestMethodsUsing = None
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """A test class for all rectangle class methods.
    """
    def test_inherite_from_base(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 4)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 5)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_validator(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.width = "2"
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, {})
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        r4 = Rectangle(3, 2)
        self.assertEqual(r4.area(), 6)

        r5 = Rectangle(2, 10)
        self.assertEqual(r5.area(), 20)

        r6 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r6.area(), 56)

    def test_display(self):
        r7 = Rectangle(4, 6)
        r7.display()

        r8 = Rectangle(2, 2)
        r8.display()

        r9 = Rectangle(2, 3, 2, 2)
        r9.display()

        r10 = Rectangle(3, 2, 1, 0)
        r10.display()

    def test_str(self):
        r11 = Rectangle(4, 6, 2, 1, 12)
        test = str(r11)
        self.assertEqual(test, '[Rectangle] (12) 2/1 - 4/6')

    def test_update(self):
        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r), '[Rectangle] (1) 10/10 - 10/10')

        r.update(89)
        self.assertEqual(str(r), '[Rectangle] (89) 10/10 - 10/10')

        r.update(89, 2)
        self.assertEqual(str(r), '[Rectangle] (89) 10/10 - 2/10')

        r.update(89, 2, 3)
        self.assertEqual(str(r), '[Rectangle] (89) 10/10 - 2/3')

        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), '[Rectangle] (89) 4/10 - 2/3')

        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), '[Rectangle] (89) 4/5 - 2/3')

        r.update(height=1)
        self.assertEqual(str(r), '[Rectangle] (89) 4/5 - 2/1')

        r.update(width=1, x=2)
        self.assertEqual(str(r), '[Rectangle] (89) 2/5 - 1/1')

        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), '[Rectangle] (89) 3/1 - 2/1')

        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), '[Rectangle] (89) 1/3 - 4/2')

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary,
                         {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
