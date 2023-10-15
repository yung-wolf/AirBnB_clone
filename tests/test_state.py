#!/usr/bin/env python3

"""
Test State class
"""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        """Test set up State class"""
        self.s1 = State()
        self.newyork = State()
        self.newyork.name = "NewYork"

    def test_attr(self):
        """Test attributes"""
        self.assertTrue(hasattr(self.s1, 'name'))
        self.assertTrue(hasattr(self.newyork, 'name'))
        self.assertEqual(self.newyork.name, 'NewYork')
        self.assertIsInstance(self.s1.name, str)

        # attr from parent class
        self.assertTrue('updated_at' in self.s1.__dict__)
        self.assertTrue('created_at' in self.s1.__dict__)
        self.assertTrue('name' in self.newyork.__dict__)
        self.assertTrue('id' in self.s1.__dict__)

    def test_save(self):
        """ test save method"""
        self.s1.save()
        self.assertNotEqual(self.s1.created_at, self.s1.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        self.assertEqual('to_dict' in dir(self.s1), True)

    def test_inheritance(self):
        """Test if it inherits from BaseModel"""
        self.assertTrue(issubclass(self.s1.__class__, BaseModel), True)


if __name__ == "__main__":
    unittest.main()
