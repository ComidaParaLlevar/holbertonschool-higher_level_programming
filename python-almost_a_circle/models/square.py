#!/usr/bin/python3
"""
Module contains class Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    defines class Square; inherits from class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter size - sets width and height as size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        If args: set attributes in this order: id, width, height, x, y
        If no args given: set attributes according to kwargs
        """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.size = v
                elif k == 2:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
