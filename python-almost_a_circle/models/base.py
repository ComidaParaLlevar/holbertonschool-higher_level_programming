#!/usr/bin/python3
""" script lng """

import json


class Base():
    """This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)"""

    __nb_objects = 0
    """private class attribute"""

    def __init__(self, id=None):
        """Class constructor

        Args: id(int)"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ takes list of dictionaries and return json"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json to file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                json_string =\
                    cls.to_json_string(
                        [obj.to_dictionary() for obj in list_objs])
                file.write(json_string)

    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with attributes already set"""
        if cls.__name__ == "Square":
            inst = cls(1)
        if cls.__name__ == "Rectangle":
            inst = cls(1, 1)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        filenamee = cls.__name__ + ".json"
        _list = []
        try:
            with open(filenamee, "r") as f:
                instances = cls.from_json_string(f.read())
            for i, dic in enumerate(instances):
                _list.append(cls.create(**instances[i]))
        except FileNotFoundError:
            pass
        return _list
