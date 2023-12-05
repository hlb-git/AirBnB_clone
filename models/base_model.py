#!/usr/bin/python3
"""base class for all other subclasses"""


from uuid import uuid4
from datetime import datetime

class BaseModel():
    """the base class"""

    def __init__(self):
        """the constructor method"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """return the official initialization of the class"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the updated_at attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns the dictionary representation of the instance"""
        instance_dict = self.__dict__.copy()
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        instance_dict["__class__"] = self.__class__.__name__
        return instance_dict
