#!/usr/bin/env python3

"""
module: review

Holds one class, Review() which inherits from BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Models a review."""

    place_id = ""  # == Place.id
    user_id = ""  # == User.id
    text = ""
