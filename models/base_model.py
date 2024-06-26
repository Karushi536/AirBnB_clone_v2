#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

""" changing the storage engine to use SQLAlchemy
creating Base, BaseModel does not inherit from Base
All other classes inherit from BaseModel to get common
values(id, created_at, updated_at),
Inheriting from Base will actually cause SQLAlchemy to map it to table
"""

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    # definingSQLAlchemy columns
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
<<<<<<< HEAD

        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
<<<<<<< HEAD
=======
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

>>>>>>> refs/remotes/origin/master
=======

>>>>>>> refs/remotes/origin/master
        if kwargs:
            for key, value in kwargs.items():
                # check if the class has an attribute matching key
                if hasattr(self, key):
                    setattr(self, key, value)

                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update(
                {'__class__': (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        # remove SQLAlchemy state if present
        try:
            del dictionary['_sa_instance_state']
        except KeyError:
            pass
        return dictionary

    def delete(self):
        """ delete the current instance from the storage"""
        from models import storage
        storage.delete(self)
