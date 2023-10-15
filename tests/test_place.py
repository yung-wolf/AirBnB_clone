#!/usr/bin/env python3

"""
Test Place class
"""


import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):

    def setUp(self):
        """setup test class"""
        self.s1 = Place()
        self.newyork = Place()
        self.newyork.name = "NewYork"

    def test_place(self):
        """Test attribute of Place class"""
        self.assertTrue(hasattr(self.s1, 'name'))
        self.assertTrue(hasattr(self.s1, 'city_id'))
        self.assertTrue(hasattr(self.s1, 'user_id'))
        self.assertTrue(hasattr(self.s1, 'description'))
        self.assertTrue(hasattr(self.s1, 'number_rooms'))
        self.assertTrue(hasattr(self.s1, 'number_bathrooms'))
        self.assertTrue(hasattr(self.s1, 'max_guest'))
        self.assertTrue(hasattr(self.s1, 'price_by_night'))
        self.assertTrue(hasattr(self.s1, 'latitude'))
        self.assertTrue(hasattr(self.s1, 'longitude'))
        self.assertTrue(hasattr(self.s1, 'amenity_ids'))
        self.assertEqual(self.newyork.name, 'NewYork')

    def test_instance_attr(self):
        """Test the class type of attributes"""
        self.assertIsInstance(self.s1.name, str)
        self.assertIsInstance(self.s1.city_id, str)
        self.assertIsInstance(self.s1.user_id, str)
        self.assertIsInstance(self.s1.description, str)
        self.assertIsInstance(self.s1.number_rooms, int)
        self.assertIsInstance(self.s1.number_bathrooms, int)
        self.assertIsInstance(self.s1.max_guest, int)
        self.assertIsInstance(self.s1.price_by_night, int)
        self.assertIsInstance(self.s1.latitude, float)
        self.assertIsInstance(self.s1.longitude, float)
        self.assertIsInstance(self.s1.amenity_ids, list)

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
