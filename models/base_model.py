#!/usr/bin/python3
"""base class for all other subclasses"""


from uuid import uuid4
from datetime import datetime

class BaseModel():
    """
        attributes and functions for BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """
            instantiation of new BaseModel Class
        """
        if kwargs:
            self.__set_attributes(kwargs)
        else:
            self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def save(self):
        """
            updates attribute updated_at to current time
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """
            returns string type representation of object instance
        """
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

    def __set_attributes(self, attr_dict):
        """
            private: converts attr_dict values to python class attributes
        """
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if 'id' not in attr_dict:
            attr_dict['id'] = str(uuid4())
        for key, value in attr_dict.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(attr_dict["created_at"],
                                                        date_format)
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(attr_dict["updated_at"],
                                                        date_format)
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)