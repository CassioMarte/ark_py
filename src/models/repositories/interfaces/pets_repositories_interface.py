from abc import ABC, abstractmethod

class PetsRepositoriesInterface(ABC): # pylint: disable=too-few-public-methods
    
    @abstractmethod
    def list_pets(self)->list: 
        pass

    @abstractmethod
    def delete_pet(self, uuid:str)-> None:
        pass


    
