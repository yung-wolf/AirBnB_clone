#!/usr/bin/env python3

"""
Test case for City class
"""


import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):

    def test_attributes(self):
        """Test name attr of City class"""
        c1 = City()
        newyork_city = City()
        newyork_city.name = "New York City"

        self.assertTrue(hasattr(c1, 'name'))
        self.assertTrue(hasattr(c1, 'state_id'))
        self.assertTrue(hasattr(newyork_city, 'name'))
        self.assertEqual(newyork_city.name, 'New York City')
        self.assertIsInstance(c1.name, str)


if __name__ == "__main__":
    unittest.main()
