#!/usr/bin/python3
""" a class state"""

from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """state
    att:
    name: string name of state"""
    name = ""
