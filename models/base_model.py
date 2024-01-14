import datetime
import uuid
from models import storage

class BaseModel():
    def __init__(self, *args, **kwargs):
               
        if kwargs:
            for key, value in kwargs.items():
                #setattr(self,key,value)
                self.__dict__[key] = value
        
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
  
            

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        dictionary = {}
        for key, value in self.__dict__.items():
            dictionary.update({key: value})
        dictionary.update({"__class__": self.__class__.__name__})
        return dictionary

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"