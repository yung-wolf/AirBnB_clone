#!/usr/bin/env python3

"""
test Amenity class
"""


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test Amenity class"""

    def setUp(self):
        """set up test class"""
        self.a1 = Amenity()
        self.pub = Amenity()
        self.pub.name = "Pub"

    def test_attr(self):
        """Test name attr of Amenity class"""
        self.assertTrue(hasattr(self.a1, 'name'))
        self.assertTrue(hasattr(self.pub, 'name'))
        self.assertEqual(self.pub.name, 'Pub')
        self.assertIsInstance(self.pub.name, str)
        self.assertTrue('created_at' in self.a1.__dict__)
        self.assertTrue('updated_at' in self.a1.__dict__)
        self.assertTrue('name' in self.pub.__dict__)
        self.assertTrue('id' in self.a1.__dict__)

    def test_instance_attr(self):
        """Test type of attributes"""
        self.assertIsInstance(self.a1.name, str)

    def test_inheritance(self):
        """test parent class"""
        self.assertTrue(issubclass(self.a1.__class__, BaseModel), True)

    def save(self):
        """test save method"""
        self.a1.save()
        self.assertNotEqual(self.a1.created_at, self.a1.updated_at)

    def test_to_dict(self):
        """test to_dict method"""
        self.assertEqual('to_dict' in dir(self.a1), True)


if __name__ == "__main__":
    unittest.main()
