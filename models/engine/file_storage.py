#!/usr/bin/env python3
""" HBNB File Storage Engine """
import json
from models.base_model import BaseModel


class FileStorage():
    """ FileStorage class """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ all """
        return (self.__objects)

    def new(self, obj):
        """create"""
        self.__objects[str(type(obj).__name__) + "." +
                       str(obj.__dict__['id'])] = obj

    def save(self):
        """ save """
        pass

    def reload(self):
        """ load_from_file """
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as jFile:
                insts = json.load(jFile)
                for inst in insts:
                    instances.append(self.to_dict(**inst))
        except FileNotFoundError:
            pass
