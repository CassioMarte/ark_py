from abc import ABC, abstractmethod
class FindPeopleControllerInterface(ABC):
   
    @abstractmethod
    def find(self, person_uuid:str)-> dict:
     pass