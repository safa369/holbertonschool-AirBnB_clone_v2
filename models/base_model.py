#!/usr/bin/python3
"""model that defines all common attributes/ methods of other classes"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from uuid import uuid4
from datetime import datetime
import models

Base = declarative_base()


class BaseModel:
    """a class base model that defines all common attributes/methods.
    Attributes:
            id: the id of each basemodel (string).
            created_at: the date and time when the instance is created.
            updated_at: the date and time when the instance is apdated."""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        if 'id' not in kwargs:
            self.id = str(uuid4())
        if 'created_at' not in kwargs:
            self.created_at = datetime.utcnow()
        if 'updated_at' not in kwargs:
            self.updated_at = datetime.utcnow()
        models.storage.new(self)

    def __str__(self):
        """return the infrmation n human readable"""
        return ("[{}] {} {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """save the current datetime of the updates """
        models.storage.save()

    def to_dict(self):
        """return a dictionary containig all key and value of the instance"""
        dict_f = {}
        dict_f["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dict_f[key] = value.isoformat()
            else:
                dict_f[key] = value
        return dict_f
