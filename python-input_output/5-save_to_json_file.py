#!/usr/bin/python3
"""
    writes an Object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """using JSON writes an Object to a text file"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
