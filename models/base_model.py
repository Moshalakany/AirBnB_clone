#!/usr/bin/python3
"""import needed libraries."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """base model implemintation"""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
    
            Args:
                *args (any): not used.
                **kwargs (dict): of attributes.
        """
        date_time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        self.id = str(uuid4())
        if len(kwargs) != 0:
            for dic_key, item in kwargs.items():
                if dic_key == "created_at" or dic_key == "updated_at":
                    self.__dict__[dic_key] = datetime.strptime(item, tform)
                else:
                    self.__dict__[dic_key] = item
        else:
            models.storage.new(self)

    def save(self):
        """change updated_at value with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        tempname = self.__class__.__name__
        return "[{}] ({}) {}".format(tempname, self.id, self.__dict__)

    def to_dict(self):
        """Return the dictionary of the converted data of BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        inistdic = self.__dict__.copy()
        inistdic["created_at"] = self.created_at.isoformat()
        inistdic["updated_at"] = self.updated_at.isoformat()
        inistdic["__class__"] = self.__class__.__name__
        return inistdict

