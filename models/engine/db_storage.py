#!/usr/bin/python3
from sqlalchemy import create_engine
from os import getenv

class DBStorage:
    """class database storage engine
    attributs:
        __engine
        __session"""
    __engine = None
    __session = None

    def __init__(self):
         self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")
        ), pool_pre_ping=True)