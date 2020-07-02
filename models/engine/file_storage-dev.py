#!/usr/bin/env python3

#!/usr/bin/python3
"""
    File Storage Engine, choo choo!
    HolbertonBnB
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review


class FileStorage():
    """ FileStorage class for command interpreter """

    def __init__(self):
        """ constructor for FS """
        self.__file_path = 'file.json'
        self.__objects = dict()

    def all(self):
        """ returns dict of __objects """
        return self.__objects

    def new(self, obj):
        """ new obj """
        self.__objects[str(type(obj).__name__) + "." +
                       str(obj.__dict__['id'])] = obj

    def save(self):
        """ saves/seralizes up in this motherfucker """
        e = dict(self.__objects)
        for key in list(e.keys()):
            e[key] = dict(e[key].to_dict())
        d = json.dumps(e)
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(d)

    def reload(self):
        """ deserializer, up in this bitch """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                s = f.read()
                l = json.loads(s)
                list_of_classes = ['BaseModel', 'User', 'State',
                                   'City', 'Amenity', 'Place', 'Review']
                for key in list(l.keys()):
                    for i in list_of_classes:
                        if i in key:
                            c = i + '(**l[key])'
                            self.__objects[key] = eval(c)
        except FileNotFoundError:
            pass


class FileStorage(self)

 a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances:

    Private class attributes:

        __file_path = cls.__name__ + '.json' 

        __objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)


    Public instance methods:

    def all(self):
        """load_from_file"""
        return (self.__objects)

    def new(self, obj):
        """create"""
        kcid = cls.__name__.id
        __objects.update(kcid)

        self.__objects[str(type(obj).__name__) + "." +
                       str(obj.__dict__['id'])] = obj

        save(self): serializes __objects to the JSON file (path: __file_path)
    @classmethod
    def save(self):
        """save_to_file"""
        jstr = []
        if not list_objs:
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            with open(__file_path,
                      mode="w", encoding='utf-8') as f:
                json.dump(jstr, f)
        else:
            jstr = cls.to_json_string([obj.to_dictionary()
                                      for obj in list_objs])
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            with open(cls.__name__ + '.json',
                      mode="w", encoding="utf-8") as myFile:
                myFile.write(jstr)

        e = dict(self.__objects)
        for key in list(e.keys()):
            e[key] = dict(e[key].to_dict())
        d = json.dumps(e)
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(d)

        reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
    def reload(self):
        """load_from_file"""
        instances = []
        try:
            with open(cls.__name__ + '.json',
                      mode="r", encoding="utf-8") as myFile:
                jfile = myFile.read()
                instances = cls.from_json_string(jfile)
            for instance in instances:
                instances.append(cls.create(**instance))
            return (instances)
        except FileNotFoundError:
            return (instances)

