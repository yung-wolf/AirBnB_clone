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

    def test_new(self):
        """Test new method"""
        bm = BaseModel()
        bm_name = "Dummy Model"
        self.fs.new(bm)
        key = f"{bm.__class__.__name__}.{bm.id}"
        self.assertIsNotNone(self.objs_dict[key])

    def test_save(self):
        """Test save method"""
        e_storage = FileStorage()
        e_dict = e_storage.all()
        bm = BaseModel()
        bm_name = "Dummy Model-2"
        e_storage.new(bm)
        e_storage.save()
        self.assertEqual(self.objs_dict, e_dict)

    def test_reload(self):
        """test reload method"""
        try:
            os.remove("objects_saveFile.json")
        except:
            pass
        with open("objects_saveFile.json", "w") as file:
            file.write("hello")
        with open("objects_saveFile.json", "r") as file:
            for text in file:
                self.assertEqual(text, "hello")


if __name__ == "__main__":
    unittest.main()
