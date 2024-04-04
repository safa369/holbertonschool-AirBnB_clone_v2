#!/usr/bin/python3
""" a class City"""
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import ForeignKey
from models.base_model import BaseModel, Base


class Place(BaseModel):
    """ a class model of place
    att:
        city_id:string
        user_id:string
        name:string
        description: string
        number_rooms: integer
        number_bathrooms: integer
        max_guest: integer
        price_by_night: integer
        latitude: float
        longitude: float
        amenity_ids: list
        """

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
