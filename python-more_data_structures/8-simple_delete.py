#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary == key:
        del(a_dictionary[key])
    else:
        return a_dictionary
