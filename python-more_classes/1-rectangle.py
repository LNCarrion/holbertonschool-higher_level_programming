#!/usr/bin/python3
"""define a rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        '''initialize a rectangle

        args:
            width (int): the width of the rectangle
            height (int): height of th rectangle
        '''
        self.width = width
        self.height = height

    @property
    def width(self, value):
        '''set the rectangle width'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''set rectangle height.'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
