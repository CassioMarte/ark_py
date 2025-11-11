from abc import ABC, abstractmethod

class CreatePeopleControllerInterface(ABC): 

    @abstractmethod
    def create(self, person_info:dict)-> dict:
        pass
       