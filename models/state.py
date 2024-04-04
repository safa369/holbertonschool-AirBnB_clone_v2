#!/usr/bin/python3
"""This module creates a User class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances"""
            from models import storage
            from models.city import City
            city_list = []
            cities_dict = storage.all(City)
            for city in cities_dict.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
