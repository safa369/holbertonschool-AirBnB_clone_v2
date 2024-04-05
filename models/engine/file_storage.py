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
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

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
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass
    
    def delete(self, obj=None):
        """Delete obj from __objects"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()