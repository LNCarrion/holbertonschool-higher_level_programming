#!/usr/bin/python3
"""
    define a rectangle
"""


class Rectangle:
    '''represent a rectangle'''

    def __init__(self, width=0, height=0):
        '''initialize a rectangle

        args:
            width (int): the width of the rectangle
            height (int): height of th rectangle
        '''
        self.width = width
        self.height = height

    '''width getter'''
    @property
    def width(self):
        
        return self.__width

    '''set the rectangle width'''
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    '''height getter'''
    @property
    def height(self):
        return self.__height

    '''set rectangle height.'''
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
