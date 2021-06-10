#!/usr/bin/python3
"""A Rectangle module drived from a base class.
"""
from models.base import Base


class Rectangle(Base):
    """Rectangel class drived from base class. Contains private attrbutes that
    describes the size and position of the rectangle and methods that draws and
    calculate its area.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def __str__(self):
        return '[' + __class__.__name__ + '] ' + '(' + str(self.id) + ') '\
            + str(self.__x) + '/' + str(self.__y) + ' - '\
            + str(self.__width) + '/' + str(self.__height)

    def area(self):
        """Return area of rectangle.

        Yields:
            width times height.
        """
        return self.__width * self.__height

    def display(self):
        """Display rectangel using '#' character for height and width.
        And x,y as a position in space.
        """
        [print() for l in range(self.__y)]
        for h in range(self.__height):
            [print(" ", end="") for s in range(self.__x)]
            [print("#", end="") for w in range(self.__width)]
            print()

    def update(self, *args, **kwargs):
        """Update attributes of the instance.

        Args:
            args (tuple): no-keyword argument, update using order
            kwargs (dict): keyword argument, the attrbute to be updated is
                given as key and value pair
        """
        if args != ():
            for idx, arg in enumerate(args[:5]):
                self.__dict__.update({list(self.__dict__.keys())[idx]: arg})
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key in list(self.__dict__.keys()):
                    self.__dict__[key] = value
                elif '_' + __class__.__name__ + '__' + key \
                     in list(self.__dict__.keys()):
                    self.__dict__['_' + __class__.__name__ + '__' + key] = value

    def to_dictionary(self):
        """Return the dictionary representaion of instance attrbutes.
        """
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
