#!/usr/bin/env python3

"""
Module: tests/test_models/test_user
"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        """set up test class"""
        self.user1 = User()
        self.user1.first_name = "Eli"
        self.user1.last_name = "Yung"
        self.user1.email = "eliYung@alx.com"
        self.user1.password = "log1"

    def test_attributes(self):
        """Test attributes of User class"""
        self.assertTrue(hasattr(self.user1, 'first_name'))
        self.assertTrue(hasattr(self.user1, 'last_name'))
        self.assertTrue(hasattr(self.user1, 'email'))
        self.assertTrue(hasattr(self.user1, 'password'))
        self.assertTrue('created_at' in self.user1.__dict__)
        self.assertTrue('updated_at' in self.user1.__dict__)
        self.assertTrue('id' in self.user1.__dict__)

        self.assertEqual(self.user1.first_name, 'Eli')
        self.assertEqual(self.user1.last_name, 'Yung')
        self.assertEqual(self.user1.email, 'eliYung@alx.com')
        self.assertEqual(self.user1.password, 'log1')

    def test_instance_attr(self):
        """Test type of attributes"""
        self.assertIsInstance(self.user1.first_name, str)
        self.assertIsInstance(self.user1.last_name, str)
        self.assertIsInstance(self.user1.email, str)
        self.assertIsInstance(self.user1.password, str)

    def test_inheritance(self):
        """Test parent class"""
        self.assertTrue(issubclass(self.user1.__class__, BaseModel), True)

    def test_save(self):
        """test save method"""
        self.user1.save()
        self.assertNotEqual(self.user1.created_at, self.user1.updated_at)

    def test_to_dict(self):
        """test to_dict method"""
        self.assertEqual('to_dict' in dir(self.user1), True)


if __name__ == "__main__":
    unittest.main()
