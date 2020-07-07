#!/usr/bin/env python3
""" reviews """
from models.base_model import BaseModel


class Review(BaseModel):
    """ reviews class """

    place_id = ""
    user_id = ""
    text = ""
