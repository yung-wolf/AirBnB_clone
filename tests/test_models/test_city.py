#!/usr/bin/env python3

"""
Test case for City class
"""


import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        """set up City class"""
        self.c1 = City()
        self.newyork_city = City()
        self.newyork_city.name = "New York City"

    def test_attributes(self):
        """Test name attr of City class"""
        self.assertTrue(hasattr(self.c1, 'name'))
        self.assertTrue(hasattr(self.c1, 'state_id'))
        self.assertTrue(hasattr(self.newyork_city, 'name'))
        self.assertEqual(self.newyork_city.name, 'New York City')
        self.assertIsInstance(self.c1.name, str)
        self.assertIsInstance(self.c1.state_id, str)
        self.assertTrue('created_at' in self.c1.__dict__)
        self.assertTrue('updated_at' in self.c1.__dict__)
        self.assertTrue('name' in self.newyork_city.__dict__)
        self.assertTrue('id' in self.c1.__dict__)

    def test_save(self):
        """test sve method"""
        self.c1.save()
        self.assertNotEqual(self.c1.created_at, self.c1.updated_at)

    def test_to_dict(self):
        """test to_dict method"""
        self.assertEqual('to_dict' in dir(self.c1), True)


if __name__ == "__main__":
    unittest.main()
