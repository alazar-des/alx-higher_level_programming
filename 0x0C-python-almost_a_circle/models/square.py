#!/usr/bin/python3
"""Square module drived from rectangle class. Square is basically a rectangle.
it adds its own methods.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square module drived from rectangle class. And overwrites the update and
    the setter methods.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'\
            .format(self.id, self._Rectangle__x, self._Rectangle__y,
                    self._Rectangle__width)

    @property
    def size(self):
        return self._Rectangle__width

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self._Rectangle__width = size
        self._Rectangle__height = size

    def update(self, *args, **kwargs):
        """Update attributes of the instance.

        Args:
            args (tuple): no-keyword argument, update using order
            kwargs (dict): keyword argument, the attrbute to be updated is
                given as key and value pair
        """
        attrbs = self.__dict__
        if args != ():
            for idx, arg in enumerate(args[:4]):
                if idx == 0 or idx == 1:
                    attrbs[list(attrbs.keys())[idx]] = arg
                if idx >= 1:
                    attrbs[list(attrbs.keys())[idx+1]] = arg
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key in list(attrbs.keys()):
                    attrbs[key] = value
                elif key == 'size':
                    self._Rectangle__width = value
                    self._Rectangle__height = value
                elif '_Rectangle__' + key \
                     in list(attrbs.keys()):
                    attrbs['_Rectangle__' + key] = value

    def to_dictionary(self):
        """Return the dictionary representation of object attributes.
        """
        return {'id': self.id, 'size': self._Rectangle__width,
                'x': self._Rectangle__x,
                'y': self._Rectangle__y}
