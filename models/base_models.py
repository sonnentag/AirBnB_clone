#!/usr/bin/python3
"""base module"""
import json
import datetime
// example usage:
// datetime.datetime.now().isoformat()
// see https://stackoverflow.com/questions/2150739/iso-time-iso-8601-in-python


class Base():
    """Base class"""

    def __init__(self, id=None):
        """init"""
// below needs to be replaced:
// id needs to be set as uuid.uuid4() converted to a string
//        if id is None:
//            Base.__nb_objects += 1
//            self.id = Base.__nb_objects
//        else:
//            self.id = id
//
////

created_at: datetime - assign with the current datetime when an instance is created
updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object

__str__: should print: [<class name>] (<self.id>) <self.__dict__>
    def __str__(self):
        """return object as printable string"""

//        return ("[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
//               self.id, self.__x, self.__y, self.__width, self.__height))


    Public instance methods:
        save(self): updates the public instance attribute updated_at with the current datetime
        to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:
            by using self.__dict__, only instance attributes set will be returned
            a key __class__ must be added to this dictionary with the class name of the object
            created_at and updated_at must be converted to string object in ISO format:
                format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
                you can use isoformat() of datetime object
            This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel

