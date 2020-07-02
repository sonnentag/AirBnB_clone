#!/usr/bin/env python3

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string"""
        jstr = "[]"
        if list_dictionaries:
            jstr = json.dumps(list_dictionaries, sort_keys=True)
        return (jstr)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file"""
        jstr = []
        if not list_objs:
            with open(cls.__name__ + '.json',
                      mode="w", encoding='utf-8') as f:
                json.dump(jstr, f)
        else:
            jstr = cls.to_json_string([obj.to_dictionary()
                                      for obj in list_objs])
            with open(cls.__name__ + '.json',
                      mode="w", encoding="utf-8") as myFile:
                myFile.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """from_json_string"""
        rstr = []
        if json_string:
            rstr = json.loads(json_string)
        return (rstr)

    @classmethod
    def create(cls, **dictionary):
        """create"""
        retd = None
        if cls.__name__ == "Rectangle":
            retd = cls(1, 1)
        elif cls.__name__ == "Square":
            retd = cls(1)
        else:
            return (retd)
        retd.update(**dictionary)
        return (retd)

    @classmethod
    def load_from_file(cls):
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

