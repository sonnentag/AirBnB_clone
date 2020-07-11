#!/usr/bin/env python3
"""base module"""
import uuid
from datetime import datetime


class BaseModel():
    """Base class"""

    def __init__(self, *args, **kwargs):
        """init"""

        from models import storage
        if kwargs:
            for k in kwargs:
                if k != '__class__':
                    if k in ['created_at', 'updated_at']:
                        var = datetime.fromisoformat(kwargs[k])
                    else:
                        var = kwargs[k]
                    setattr(self, k, var)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
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
        """return all k/v pairs as dict"""

        this_dict = self.__dict__.copy()
        this_dict.update({'__class__': type(self).__name__})
        this_dict['created_at'] = self.created_at.isoformat()
        this_dict['updated_at'] = self.updated_at.isoformat()
        return this_dict
