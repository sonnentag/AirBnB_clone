#!/usr/bin/env python3
"""base module"""
import json
import uuid
from datetime import datetime


class BaseModel():
    """Base class"""

    def __class__(self):
        pass

    def __init__(self):
        """init"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """return object as printable string"""

        return ("[{}] ({}) {}".format(type(self).__name__,self.id,self.__dict__))

    def save(self):
        """save"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """return all k/v pairs as dict
        """
        self.__class__ = str(type(self).__name__)
        return dict(
            (key, value) if type(value) in ['int','str'] else (key, str(value))
            for (key, value) in self.__dict__.items()
            )
