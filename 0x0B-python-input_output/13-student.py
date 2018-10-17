#!/usr/bin/python3
class Student:
    """class of student"""

    def __init__(self, first_name, last_name, age):
        """initialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dict def of student"""
        if attrs is not None:
            new_dict = {}
            for i in attrs:
                if i is "first_name":
                    new_dict[i] = self.first_name
                elif i is "last_name":
                    new_dict[i] = self.last_name
                elif i is "age":
                    new_dict[i] = self.age
                else:
                    pass
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attrs of student instance"""
        for k, v in json.items():
            self.__dict__[k] = v
