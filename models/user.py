#!/usr/bin/env python3

"""
module: models/user

holds User class.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Models a user. Inherits from BaseModel."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
