#!/usr/bin/python3
"""base module"""
import json
import csv


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
        with open("{}.json".format(
                cls.__name__), "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                f.write(cls.to_json_string(
                    [(cls.to_dictionary(obj)) for obj in list_objs]
                ))

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
        try:
            with open("{}.json".format(
                    cls.__name__), "r", encoding="utf-8") as f:
                ls_output = cls.from_json_string(f.read())
                for obj in ls_output:
                    list_objs.append(cls.create(**obj))
                return list_objs
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serialize list_objs in CSV"""
        list_dict = [cls.to_dictionary(obj) for obj in list_objs]
        with open("{}.csv".format(
                cls.__name__), "w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, list_dict[0].keys())
            writer.writeheader()
            writer.writerows(list_dict)

    @classmethod
    def load_from_file_csv(cls):
        """deserialize CSV"""
        list_objs = []
        with open("{}.csv".format(
                cls.__name__), "r", encoding="utf-8") as f:
            ls_output = csv.DictReader(f)
            for obj in ls_output:
                tmp = {}
                for k, v in dict(obj).items():
                    tmp[k] = int(v)
                list_objs.append(cls.create(**tmp))
        return list_objs
