#!/usr/bin/env python3

"""
module: base_model

Holds one class, BaseModel()
"""

import uuid
from models import storage
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize object"""

        self.id = str(uuid.uuid4())

        if not kwargs:
            storage.new(self)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'name' or key == 'my_number' or key == 'id':
                        self.key = value
                    else:  # format created_at/updated_at to datetime objs
                        self.key = datetime.fromisoformat(value)
                    self.__dict__[key] = self.key
            if 'key' in self.__dict__:  # removes the key `key` from dict
                del self.__dict__['key']

    def save(self):
        """Updates `updated_at` every time you change your object."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__

        # convert created_at & updated_at to string object in ISO format
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
