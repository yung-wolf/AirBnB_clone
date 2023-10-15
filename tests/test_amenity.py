#!/usr/bin/env python3

"""
test Amenity class
"""


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_name(self):
        """Test name attr of Amenity class"""
        a1 = Amenity()
        pub = Amenity()
        pub.name = "Pub"

        self.assertTrue(hasattr(a1, 'name'))
        self.assertTrue(hasattr(pub, 'name'))
        self.assertEqual(pub.name, 'Pub')
        self.assertIsInstance(pub.name, str)
