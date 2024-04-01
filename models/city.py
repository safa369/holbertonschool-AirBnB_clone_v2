#!/usr/bin/python3
""" a class City"""

from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ a class city
        attr:
            state_id: id of city
            name: name of city"""
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(ForeignKey("state.id"), String(60), nullable=False)
    cities = relationship("City",
                          cascade="all, delete-orphan", backref="state")
