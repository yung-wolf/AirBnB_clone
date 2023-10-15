#!/usr/bin/env python3

"""
module: amenity

Holds one class, Amenity() which inherits from BaseModel
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Models the amenities in an establishment."""

    name = ""
