#!/usr/bin/env python3

"""
Test module for base_model
"""


import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Sets up test class"""
        self.bm1 = BaseModel()
        self.bm1.name = "My_First_Model"
        self.bm1.my_number = 89
        self.first_updated_at = self.bm1.updated_at
        self.bm2 = BaseModel()

    def test_uuid(self):
        """Test uuid of BaseModel objs"""
        self.assertIsInstance(self.bm1, BaseModel)
        self.assertNotEqual(self.bm1.id, self.bm2.id)
        self.assertIsInstance(self.bm1.id, str)

    def test_attributes(self):
        """ test that all attributes are present"""
        self.assertTrue(hasattr(self.bm1, "created_at"))
        self.assertTrue(hasattr(self.bm1, "updated_at"))
        self.assertTrue(hasattr(self.bm1, "name"))
        self.assertTrue(hasattr(self.bm1, "my_number"))
        self.assertTrue(hasattr(self.bm1, "id"))
        self.assertTrue(hasattr(self.bm2, "id"))

    def test_datetime_objs(self):
        """Test `created_at` and `updated_at` datetime objects"""
        self.assertIsInstance(self.bm1.created_at, datetime)
        self.assertIsInstance(self.bm2.created_at, datetime)
        self.assertIsInstance(self.bm1.updated_at, datetime)
        self.assertIsInstance(self.bm2.updated_at, datetime)
        self.assertNotEqual(self.bm1.created_at, self.bm1.updated_at)

    def test_save(self):
        """Test save method of BM"""
        self.bm1.save()
        self.assertNotEqual(self.first_updated_at, self.bm1.updated_at)

    def test_to_dic(self):
        """Test that to_dict method returns dictionary"""
        bm1_dict = self.bm1.to_dict()
        self.assertIsInstance(bm1_dict, dict)
        self.assertIsInstance(bm1_dict['created_at'], str)
        self.assertIsInstance(bm1_dict['updated_at'], str)
        # test `class_name` in dict
        self.assertEqual(bm1_dict['__class__'], 'BaseModel')

    def test_kwargs(self):
        """ create object from dict. Validate attr of object
        created from dict.
        """
        bm1_dict = self.bm1.to_dict()
        nb = BaseModel(**bm1_dict)

        self.assertEqual(self.bm1.id, nb.id)
        self.assertEqual(self.bm1.my_number, nb.my_number)
        self.assertEqual(self.bm1.name, nb.name)
        self.assertEqual(self.bm1.created_at, nb.created_at)
        self.assertEqual(self.bm1.updated_at, nb.updated_at)
        self.assertIsInstance(nb.created_at, datetime)
        self.assertIsInstance(nb.updated_at, datetime)

        # test that object created != original (bm1)
        self.assertFalse(self.bm1 is nb)

    def test_str_print(self):
        """Test the `str` print method"""


if __name__ == "__main__":
    unittest.main()
