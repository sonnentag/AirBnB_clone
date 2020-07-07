#!/usr/bin/env python3
""" module specific init """

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity

rentalAttrs = {"BaseModel": BaseModel,
              "User": User,
              "City": City,
              "State": State,
              "Place": Place,
              "Amenity": Amenity,
              "Review": Review}

storage = FileStorage()
storage.reload()
