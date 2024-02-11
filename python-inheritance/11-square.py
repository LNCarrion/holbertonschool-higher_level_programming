#!/usr/bin/python3
"""
    class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """init the class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
