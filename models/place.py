#!/usr/bin/python3
""" a class City"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship, backref
from os import getenv


class Place(BaseModel, Base):
    """Place class"""
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade="all, delete", backref="place")
    else:
        @property
        def reviews(self):
            """Getter attribute that returns the list of Review instances"""
            from models import storage
            from models.review import Review
            review_list = []
            reviews_dict = storage.all(Review)
            for review in reviews_dict.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list