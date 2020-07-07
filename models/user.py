#!/usr/bin/env python3
""" users """
from models.base_model import BaseModel


class User(BaseModel):
    """ users class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
