#!/usr/bin/env python3
"""base module"""
import uuid
from datetime import datetime


class BaseModel():
    """Base class"""

    def __class__(self):
        """ needed for todict """
        pass

    def __init__(self, *args, **kwargs):
        """init"""

        from models import storage
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k in kwargs:
                if k != '__class__':
                    if k in ['created_at', 'updated_at']:
                        var = datetime.fromisoformat(kwargs[k])
                    else:
                        var = kwargs[k]
                    setattr(self, k, var)
        else:
            storage.new(self)

    def __str__(self):
        """return object as printable string"""

        return ("[{}] ({}) {}".format(type(self).__name__,
                self.id, self.__dict__))

    def save(self):
        """save"""

        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """return all k/v pairs as dict
        """
        self.__class__ = str(type(self).__name__)
        return dict(
            (key, value) if type(value) in [int, str]
            else (key, datetime.isoformat(value))
            for (key, value) in self.__dict__.items()
            )
