#!/usr/bin/python3
"""Base class module
"""
import json
import csv


class Base:
    """A base class for a rectangle and other shapes. Contains class and static
    methods that apply for all drived classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert to json string.

        Args:
            list_dictionaries (list of dict): dictionary representations of
                attributes of an instance.

        Yeilds:
            The json string representaion of an instance attrbutes.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save the json string representaion of an instance in to a
        <class name>.json file.

        Args:
            list_objs (list of objects): list objects their json string to be
               saved.

        Yields:
            The number of characters written to the file.
        """
        list_objs_dict = [obj.to_dictionary() for obj in list_objs]
        filename = [obj.__class__.__name__ for obj in list_objs][0] + '.json'
        with open(filename, 'w') as fw:
            return fw.write(cls.to_json_string(list_objs_dict))

    @staticmethod
    def from_json_string(json_string):
        """Convert from json string into object dictionary representation.

        Args:
            json_string (str): json string representaion of an object.

        Yields:
            Dictionary representaion of an object.
        """
        if json_string == "" or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance.

        Args:
            dictionary (dict): dictionary representaion of an object.

        Yields:
            The object created.
        """
        if str(cls.__dict__['__module__']).find('rectangle') >= 0:
            from models.rectangle import Rectangle
            inst = Rectangle(1, 1)
        elif str(cls.__dict__['__module__']).find('square') >= 0:
            from models.square import Square
            inst = Square(1)
        else:
            return None
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """Load json representaion of an object from file <class name>.json and
        creates an object.

        Yields:
            The object created if file exist otherwise empty list.
        """
        if str(cls.__dict__['__module__']).find('rectangle') >= 0:
            from models.rectangle import Rectangle
            inst = Rectangle(1, 1)
        elif str(cls.__dict__['__module__']).find('square') >= 0:
            from models.square import Square
            inst = Square(1)
        else:
            return None
        inst.update(**dictionary)
        return inst
        if str(cls.__dict__['__module__']).find('rectangle') >= 0:
            filename = 'Rectangle.json'
        elif str(cls.__dict__['__module__']).find('square') >= 0:
            filename = 'Square.json'
        try:
            with open(filename, 'r') as fr:
                objs = cls.from_json_string(fr.read())
            return [cls.create(**obj) for obj in objs]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save the csv string representaion of an instance in to a
        <class name>.csv file.

        Args:
            list_objs (list of objects): list objects their csv string to be
               saved.

        Yields:
            The number of characters written to the file.
        """
        list_objs_dict = [obj.to_dictionary() for obj in list_objs]
        filename = [obj.__class__.__name__ for obj in list_objs][0] + '.csv'
        with open(filename, 'w') as fw:
            writer = csv.writer(fw)
            [writer.writerow(obj_dict.values()) for obj_dict in list_objs_dict]

    @classmethod
    def load_from_file_csv(cls):
        """Load csv representaion of an object from file <class name>.csv and
        creates an object.

        Yields:
            The object created if file exist otherwise empty list.
        """
        dicts = []
        if str(cls.__dict__['__module__']).find('rectangle') >= 0:
            keys = ['id', 'width', 'height', 'x', 'y']
            filename = 'Rectangle.csv'
            try:
                with open(filename, 'r') as fr:
                    reader = csv.reader(fr)
                    for values in reader:
                        diction = {}
                        for idx, value in enumerate(values):
                            diction[keys[idx]] = value
                        dicts.append(diction)
                return [cls.create(**dicn) for dicn in dicts]
            except FileNotFoundError:
                print(filename)
                return []
        elif str(cls.__dict__['__module__']).find('square') >= 0:
            keys = ['id', 'size', 'x', 'y']
            filename = 'Square.csv'
            try:
                with open(filename, 'r') as fr:
                    reader = csv.reader(fr)
                    for values in reader:
                        diction = {}
                        for idx, value in enumerate(values):
                            diction[keys[idx]] = value
                        dicts.append(diction)
                return [cls.create(**dicn) for dicn in dicts]
            except FileNotFoundError:
                return []
