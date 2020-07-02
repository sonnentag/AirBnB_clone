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
        list_objs = dict(self.__objects)
        list_objs[obj] = dict([obj.to_dict()
                              for obj in list_objs])
        with open(self.__file_path,
                  mode="w", encoding="utf-8") as myFile:
            json.dump(list_objs, myFile)

    def reload(self):
        """ load_from_file """
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as jFile:
                insts = json.load(jFile)
                for inst in insts:
                    instances.append(self.to_dict(**inst))
        except FileNotFoundError:
            pass
