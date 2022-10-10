#!/usr/bin/python3

"""
Unittest for square
"""
import io
import os
import sys
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class SquareTest(unittest.TestCase):
    """Tests for square class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_00(self):
        """Test for square"""
        squar = Square(5)
        self.assertEqual(squar.id, 1)
        self.assertEqual(squar.width, 5)
        self.assertEqual(squar.height, 5)
        self.assertEqual(squar.x, 0)
        self.assertEqual(squar.y, 0)

    def test_01(self):
        """Test for square"""
        s = Square(10, 2)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 0)

    def test_02(self):
        """Test for square"""
        s = Square(3, 51, 96, 12)
        self.assertEqual(s.id, 12)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)
        self.assertEqual(s.x, 51)
        self.assertEqual(s.y, 96)

    def test_03(self):
        """Test for square"""
        with self.assertRaises(TypeError) as e:
            s = Square(None)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))

    def test_04(self):
        """Test for square"""
        with self.assertRaises(TypeError) as e:
            s = Square()
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'size'",
            str(e.exception))

    def test_05(self):
        """Test for square"""
        with self.assertRaises(TypeError) as e:
            s = Square(12, "3")
        self.assertEqual(
            "x must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            s = Square("12", 3)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            s = Square(12, 3, "98")
        self.assertEqual(
            "y must be an integer",
            str(e.exception))
        s = Square(10, 2, 0, "test")
        self.assertEqual(s.id, "test")

    def test_06(self):
        """Test for square"""
        with self.assertRaises(TypeError) as e:
            s = Square(11, [])
        self.assertEqual(
            "x must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            s = Square([1, 2, 3], 3)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            s = Square(13, 92, [[2, 4]])
        self.assertEqual(
            "y must be an integer",
            str(e.exception))
        s = Square(10, 98, 0, ["test"])
        self.assertEqual(s.id, ["test"])

    def test_07(self):
        """Test for square"""
        with self.assertRaises(ValueError) as e:
            s = Square(1, -5)
        self.assertEqual(
            "x must be >= 0",
            str(e.exception))
        with self.assertRaises(ValueError) as e:
            s = Square(-11, -21)
        self.assertEqual(
            "width must be > 0",
            str(e.exception))
        with self.assertRaises(ValueError) as e:
            s = Square(1, 2, -11)
        self.assertEqual(
            "y must be >= 0",
            str(e.exception))
        s = Square(1, 2, 54, -13)
        self.assertEqual(s.id, -13)

    def test_08(self):
        """Test for square"""
        s = Square(6, 0)
        self.assertEqual(s.x, 0)
        with self.assertRaises(ValueError) as e:
            s = Square(0, 2)
        self.assertEqual(
            "width must be > 0",
            str(e.exception))
        s = Square(1, 0, 0, 0)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 0)

    def test_09(self):
        """Test for square"""
        s = Square(4, 2)
        self.assertEqual(s.area(), 16)
        s = Square(2, 20, 1)
        self.assertEqual(s.area(), 4)
        s = Square(10, 5, 6, 2)
        self.assertEqual(s.area(), 100)
        s = Square(12, 7, 4, 6)
        self.assertEqual(s.area(), 144)
