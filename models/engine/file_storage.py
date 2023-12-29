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
        if cls is not None:
            object = []
            for i in self.__objects:
                if isinstance(i, cls):
                    object.append(i)
            return object
        return self.__objects

    def new(self, obj):
        if obj:
            key = obj.__class__.__name__ + "." + str(obj.id)
            self.__objects[key] = obj

    def save(self):
        dobj = {}
        for key, val in self.__class__.__objects.items():
            dobj[key] = val.to_dict()
            with open(FileStorage.__file_path, "w", encoding="utf-8") as jf:
                json.dump(dobj, jf)

    def reload(self):
        try:
            if os.path.exists(FileStorage.__file_path):
                with open(FileStorage.__file_path, "r",
                          encoding="utf-8") as fo:
                    new_dict = json.load(fo)
                for key, val in new_dict.items():
                    base = self.cl_dict[val["__class__"]](**val)
                    self.__objects[key] = base
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj is not None:
            for key, val in self.__objects.items():
                if val == obj:
                    del self.__objects[key]
