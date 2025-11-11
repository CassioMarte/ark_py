from src.models.repositories.interfaces.pets_repositories_interface import PetsRepositoriesInterface
from src.controllers.interfaces.pets_delet_controller_interface import PetDeletControllerInterface

class PetDeletController(PetDeletControllerInterface):
    def __init__(self, pet_repository:PetsRepositoriesInterface):
        self.__pet_repository = pet_repository

    def delet_pet(self, pet_uuid:str)-> None:
        self.__pet_repository.delete_pet(pet_uuid)