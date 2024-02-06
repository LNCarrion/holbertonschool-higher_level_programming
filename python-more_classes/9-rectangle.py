#!/usr/bin/python3
"""
    define a rectangle
"""


class Rectangle:
    '''represent a rectangle in instance'''
    number_of_instances = 0

    '''print the symbol'''
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''initialize a rectangle

        args:
            width (int): the width of the rectangle
            height (int): height of th rectangle
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            return ""

        arr = ""
        for i in range(self.__height):
            for j in range(self.__width):
                arr += str(self.print_symbol)
            if i is not self.__height - 1:
                arr += "\n"
        return arr

    def __repr__(self):
        '''string representation of a rectangle'''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        '''print a message and delete the redctangle'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        '''check what rectangle is bigger'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
