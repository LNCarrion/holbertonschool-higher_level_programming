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

    def update(self, *args, **kwargs):
        """update square class"""
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) == 4:
            self.y = args[3]

    def to_dictionary(self):
        """creating a dictionary"""
        dict = {'id': self.id, 'x': self.x,
                'size': self.size, 'y': self.y}
        return dict
