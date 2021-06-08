#!/usr/bin/python3
"""Test module for base module.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Monolithic(unittest.TestCase):
    """A test class for all base class methods.
    """
    def test_all(self):
        b1 = Base()
        self.assertAlmostEqual(b1.id, 1)

        b2 = Base()
        self.assertAlmostEqual(b2.id, 2)

        b3 = Base(10)
        self.assertAlmostEqual(b3.id, 10)

        b4 = Base()
        self.assertEqual(b4.id, 3)

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 4)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 5)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

        s1 = Square(10, 2)
        self.assertEqual(s1.id, 6)

        s2 = Square(2, 10)
        self.assertEqual(s2.id, 7)

        s3 = Square(10, 2, 0, 12)
        self.assertEqual(s3.id, 12)

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

        r4 = Rectangle(3, 2)
        self.assertEqual(r4.area(), 6)

        r5 = Rectangle(2, 10)
        self.assertEqual(r5.area(), 20)

        r6 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r6.area(), 56)

        r11 = Rectangle(4, 6, 2, 1, 12)
        test = str(r11)
        self.assertEqual(test, '[Rectangle] (12) 2/1 - 4/6')

        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r), '[Rectangle] (16) 10/10 - 10/10')

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

        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary,
                         {'x': 1, 'y': 9, 'id': 17, 'height': 2, 'width': 10})

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

        r4 = Square(3, 2)
        self.assertEqual(r4.area(), 9)

        r5 = Square(2, 10)
        self.assertEqual(r5.area(), 4)

        r6 = Square(8, 7, 0, 12)
        self.assertEqual(r6.area(), 64)

        s1 = Square(5)
        self.assertEqual(str(s1), '[Square] (26) 0/0 - 5')

        s1 = Square(5)
        self.assertEqual(str(s1), '[Square] (27) 0/0 - 5')

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

        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 28, 'x': 2, 'size': 10,
                                         'y': 1})

        s1 = Square(4, 9, 4, 69)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary,
                         '[{"id": 69, "size": 4, "x": 9, "y": 4}]')

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary,
                         '[{"id": 29, "width": 10, "height": 7, "x": 2, "y": 8}]')

        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), '[Rectangle] (30) 1/0 - 3/5')

        s1 = Square(3, 5, 1)
        s1_dictionary = r1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s2), '[Square] (30) 1/0 - 3')

if __name__ == '__main__':
    unittest.main()
