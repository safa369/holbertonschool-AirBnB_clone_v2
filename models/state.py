#!/usr/bin/python3
""" a class state"""

from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """state
    att:
    name: string name of state"""
    __tablename__ = "states"
    name = column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
