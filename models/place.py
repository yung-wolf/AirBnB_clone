#!/usr/bin/env python3

"""
module: place

Holds one class, Place() which inherits from BaseModel
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """Models a Place in a City in a State."""

    city_id = ""  # == City.id
    user_id = ""  # == User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # == Amenity.id
