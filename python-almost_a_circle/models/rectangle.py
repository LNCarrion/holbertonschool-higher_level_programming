#!/usr/bin/python3
"""rectangle class"""
from models.base import Base


class Rectangle(Base):
    """initiate rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    """getters"""
    @property
    def width(self):
        return self.__width

    """getters"""
    @property
    def height(self):
        return self.__height

    """getters"""
    @property
    def x(self):
        return self.__x

    """getters"""
    @property
    def y(self):
        return self.__y

    """ setters """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value


    """ setters """
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value


    """ setters """
    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value


    """ setters """
    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """returns the area of the rectangle"""
    def area(self):
        return self.__height * self.__width
