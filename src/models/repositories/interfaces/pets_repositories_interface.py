from abc import ABC, abstractmethod

class PetsRepositoriesInterface(ABC): # pylint: disable=too-few-public-methods
    
    @abstractmethod
    def list_pets(self)->list: 
        pass



    
