#!/usr/bin/python3
""" a class user"""

from base_model import BaseModel

class User(BaseModel):
    """a class user inherits from Basemode
    attr:
        email: string email of user.
        password: password of user.
        first_name: first name of user
        last_name: last name of user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
