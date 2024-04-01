#!/usr/bin/python3
""" a class review"""

from base_model import BaseModel

class Review(BaseModel):
    """a class of review
        attr:
            place_id: string
            user_id: string
            text: string"""
    place_id = ""
    user_id = ""
    text = ""