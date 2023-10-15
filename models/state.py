#!/usr/bin/env python3

"""
module: state

Holds one class, State() which inherits from BaseModel
"""


from models.base_model import BaseModel


class State(BaseModel):
    """Models a State."""

    name = ""
