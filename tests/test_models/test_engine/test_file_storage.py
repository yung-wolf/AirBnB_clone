#!/usr/bin/env python3

"""
module: test_file_storage

unittest of FileStorage class
"""


import unittest
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test file_storage"""

    def setUp(self):
        """set up test class"""
        self.fs = FileStorage()
        self.objs_dict = self.fs.all()

    def test_all(self):
        """Test all method"""
        self.assertIsNotNone(self.objs_dict)
        self.assertEqual(type(self.objs_dict), dict)
        self.assertIs(self.objs_dict, self.fs._FileStorage__objects)


if __name__ == "__main__":
    unittest.main()
