from abc import ABC, abstractmethod

class PeopleRepositoryInterface(ABC): # pylint: disable=too-few-public-methods
    
    @abstractmethod
    def list_people(self)-> list: 
         pass

    @abstractmethod
    def delete_people(self, uuid:str)-> None:
      pass

    @abstractmethod
    def create_people(self, first_name:str, last_name:str, age: int, pet_uuid:str)-> None:
        pass
  
    @abstractmethod
    def get_person_and_pet(self, people_uuid:str):
        pass
        

