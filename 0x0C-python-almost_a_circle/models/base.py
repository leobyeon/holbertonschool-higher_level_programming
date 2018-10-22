#!/usr/bin/python3
"""base module"""
import json


class Base:
    """define base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON representation of list_dict"""
        if list_dictionaries is None or \
                len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write the JSON representation of list_objs to file"""
        list_dict = []
        for obj in list_objs:
            list_dict.append(cls.to_dictionary(obj))
        json_str = cls.to_json_string(list_dict)
        with open("{}.json".format(
                cls.__name__), mode="w", encoding="utf-8") as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """return the list of JSON str representation json_string"""
        if json_string is None or \
                len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attributes already set"""
        if cls.__name__ is "Rectangle":
            instance = cls(6, 66)
        if cls.__name__ is "Square":
            instance = cls(666)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        list_objs = []
        filename = str(cls.__name__) + ".json"
        if filename:
            with open(filename, "r", encoding="utf-8") as f:
                ls_output = cls.from_json_string(f.read())
                for obj in ls_output:
                    list_objs.append(cls.create(**obj))
                return list_objs
