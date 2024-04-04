#!/usr/bin/python3
""" a class user"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv

class User(BaseModel, Base):
    """Represents a user."""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade="all, delete", backref="user")
    places = relationship("Place", cascade="all, delete", backref="user")
    reviews = relationship("Review", backref="user", cascade="delete")
