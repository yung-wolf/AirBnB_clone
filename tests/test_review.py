#!/usr/bin/env python3

"""
Test Review class
"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        """set up Review class"""
        self.s1 = Review()

    def test_attributes(self):
        """Test attributes of Review class"""
        self.assertTrue(hasattr(self.s1, 'place_id'))
        self.assertTrue(hasattr(self.s1, 'user_id'))
        self.assertTrue(hasattr(self.s1, 'text'))
        self.assertIsInstance(self.s1.place_id, str)
        self.assertIsInstance(self.s1.user_id, str)
        self.assertIsInstance(self.s1.text, str)
        self.assertTrue('created_at' in self.s1.__dict__)
        self.assertTrue('updated_at' in self.s1.__dict__)
        self.assertTrue('id' in self.s1.__dict__)

    def test_inheritance(self):
        """test parent class"""
        self.assertTrue(issubclass(self.s1.__class__, BaseModel), True)

    def test_save(self):
        """test save method"""
        self.s1.save()
        self.assertNotEqual(self.s1.created_at, self.s1.updated_at)

    def test_to_dict(self):
        """test to_dict method"""
        self.assertEqual('to_dict' in dir(self.s1), True)


if __name__ == "__main__":
    unittest.main()
