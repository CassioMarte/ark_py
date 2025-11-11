from abc import ABC, abstractmethod
class PetDeletController(ABC):
    @abstractmethod
    def delet_pet(self, pet_uuid:str)-> None:
        pass