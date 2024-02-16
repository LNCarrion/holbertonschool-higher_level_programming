#!/usr/bin/python3
"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """init class square"""
    def __init__(sel, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return the info of the class"""
        string = f"[Square] ({self.id})"
        string += f" {self.x}/{self.y} - {self.height}"
        return string
