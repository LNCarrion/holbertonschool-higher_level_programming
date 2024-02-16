#!/usr/bin/python3
"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """init class square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    """getter"""
    @property
    def size(self):
        return self.width

    """setter"""
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """return the info of the class"""
        string = f"[Square] ({self.id})"
        string += f" {self.x}/{self.y} - {self.width}"
        return string
