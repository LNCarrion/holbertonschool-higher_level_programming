#!/usr/bin/python3
"""class base"""
import json


class Base():
    """private atribute"""
    __nb_objects = 0
    """init the class"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionary):
        """dic to json string"""
        if list_dictionary is None:
            return "[]"
        return json.dumps(list_dictionary)

    @classmethod
    def save_to_json_file(cls, list_objs):
        """json string to file"""
        if list_objs is None:
            list_objs = []
        list_dict = []
        with open(cls.__name__ + ".json", 'w') as file:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
            str_obj = cls.to_json_string(list_dict)
            file.write(str_obj)
