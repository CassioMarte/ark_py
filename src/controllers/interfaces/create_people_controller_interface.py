from abc import ABC, abstractmethod

class CreatePeopleController(ABC): 

    @abstractmethod
    def create(self, person_info:dict)-> dict:
        pass
       