#!/usr/bin/python3
""" a class City"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship, backref
from os import getenv


class Place(BaseModel, Base):
    if getenv("HBNB_TYPE_STORAGE") == "db":
        metadata = Base.metadata
        place_amenity = Table("place_amenity", metadata,
                              Column('place_id', String(60),
                                     ForeignKey('places.id'),
                                     nullable=False),
                              Column('amenity_id', String(60),
                                     ForeignKey('amenities.id'),
                                     nullable=False))

