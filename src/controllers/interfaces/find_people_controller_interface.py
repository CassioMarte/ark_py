from abc import ABC, abstractmethod
class FindPeopleController(ABC):
   
    @abstractmethod
    def find(self, person_uuid:str)-> dict:
     pass