#!/usr/bin/python3
"""define a square"""


class Square:
    '''represent a square'''

    def __init__(self, size):
        '''initialize a new square

        Args:
            size (int): the size of the square created
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
