#!/usr/bin/env python3

"""
Module: file_storage

file: models/engine/file_storage.py

Holds one class, FileStorage()
"""


import json


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file
    to instances.
    """
    __file_path = "objects_saveFile.json"
    __objects = dict()

    def all(self):
        """Returns the dictionary `__objects`."""
        return FileStorage.__objects

    def new(self, obj):
        """sets in `__objects` the `obj` with key <obj class name>.id"""
        dic_key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[dic_key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        s_objs = dict()
        for k, v in FileStorage.__objects.items():
            s_objs[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(s_objs, json_file)

    def get_class(self, class_name):
        """Returns class name if found"""
        from models.base_model import BaseModel
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.user import User

        classes = {
            'BaseModel': BaseModel,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review,
            'User': User
        }
        if class_name in classes:
            return classes.get(class_name)
        else:
            raise NameError

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists.
        """
        try:
            with open(FileStorage.__file_path, 'r') as json_file:
                s_objs = json.load(json_file)
                for k, v in s_objs.items():
                    class_name, obj_id = k.split('.')
                    cls = self.get_class(class_name)
                    if cls:
                        obj = cls(**v)
                        FileStorage.__objects[k] = obj
        except FileNotFoundError:
            pass
