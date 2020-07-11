#!/usr/bin/env python3
""" HBNB File Storage Engine """
import json
import models


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
        """ save 
        jdict = {}
        with open(self.__file_path, mode="w", encoding='utf-8') as f:
            for key, val in self.__objects.items():
                jdict.update({key: val.to_dict()})

            json.dump(jdict, f)
"""
        e = dict(self.__objects)
        for key in list(e.keys()):
            e[key] = dict(e[key].to_dict())
        d = json.dumps(e)
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(d)

    def reload(self):
        """ load_from_file """

        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as jFile:
                insts = json.load(jFile)
                for k, v in insts.items():
                    attr = models.rentalAttrs[v["__class__"]](**v)
                    self.__objects[k] = attr

        except FileNotFoundError:
            pass
