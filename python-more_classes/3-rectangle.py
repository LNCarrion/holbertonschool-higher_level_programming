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

    def area(self):
        '''return the area of the rectangle'''
        return (self.__height * self.__width)

    def perimeter(self):
        '''return the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        '''print the rectangle in the terminal with a # '''

        if self.__width == 0 or self.__height == 0:
            return ("")

        arr = ""
        for i in range(self.__height == 0):
            for j in range(self.__width):
                arr += "#"
            if i is not self.__height - 1:
                arr += "\n"
        return arr
