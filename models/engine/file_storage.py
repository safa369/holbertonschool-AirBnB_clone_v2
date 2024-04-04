#!/usr/bin/python3
"""model of storage """

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """a class that serializes instance to JSON file
    and deserializes JSON file to instance
        Privat attributes:
            __file_path: path to JSON file (string).
            __objects: dictionary will stored all objects.
            cl_dict: a dictionary of all classes
            """
    __file_path = "file.json"
    __objects = {}
    cl_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self, cls=None):
        """Returns a dictionary of models currently in the storage"""
        if not cls:
            return FileStorage.__objects
        else:
            newdict = {}
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    newdict[key] = value
            return newdict


    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        if obj:
            key = obj.__class__.__name__ + "." + str(obj.id)
            self.__objects[key] = obj

    def save(self):
        dict_obj = {}
        for key, val in self.__objects.items():
            dict_obj[key] = val.to_dict()
            with open(FileStorage.__file_path, "w", encoding="utf-8") as jf:
                json.dump(dict_obj, jf)

    def reload(self):
        try:
            with open(self.__file_path, "r",
                      encoding="utf-8") as fo:
                new_dict = json.load(fo)
                for key, val in new_dict.items():
                    class_name = val['__class__']
                    del val['__class__']
                    module = __import__('models.' + class_name.lower(),
                                        fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    self.__objects[key] = class_(**val)
        except FileNotFoundError:
            pass
    
    def delete(self, obj=None):
        """Delete obj from __objects"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

