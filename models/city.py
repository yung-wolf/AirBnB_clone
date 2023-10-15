#!/usr/bin/env python3

"""
module: city

Holds one class, City() which inherits from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """Models a City."""

    state_id = ""  # = State.id
    name = ""
