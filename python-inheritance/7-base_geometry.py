#!/usr/bin/python3
"""creating a class"""


class BaseGeometry:
    '''
    public instance method
    '''
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        raise Exception("area() is not implemented")
