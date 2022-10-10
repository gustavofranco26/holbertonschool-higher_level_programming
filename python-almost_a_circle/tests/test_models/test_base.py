#!/usr/bin/python3

"""
Unittest for Base class
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Base tests"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_00(self):
        """Test for base"""
        base0 = Base()
        base1 = Base()
        self.assertEqual(base0.id, 1)
        self.assertEqual(base1.id, 2)

    def test_01(self):
        """Test for base"""
        base0 = Base(0)
        self.assertEqual(base0.id, 0)

    def test_02(self):
        """Test for base"""
        base0 = Base(12)
        self.assertEqual(base0.id, 12)

    def test_03(self):
        """Test for base"""
        base0 = Base("test")
        self.assertEqual(base0.id, "test")
