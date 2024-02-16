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