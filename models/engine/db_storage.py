#!/usr/bin/python3
"""Module DBstorage class"""
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage():
    """Class for database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes storage"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

    def all(self, cls=None):
        """returnds all object of class"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add object to db"""
        if not obj:
            return
        self.__session.add(obj)

    def save(self):
        """commit changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """Create all tables in the db"""

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)

        session_mak = sessionmaker(bind=self.__engine,
                                   expire_on_commit=False)
        Session = scoped_session(session_mak)
        self.__session = Session()

    def close(self):
        """close"""
        self.__session.close()
