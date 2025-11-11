from src.models.repositories.interfaces.pets_repositories_interface import PetsRepositoriesInterface

class PetDeletController:
    def __init__(self, pet_repository:PetsRepositoriesInterface):
        self.__pet_repository = pet_repository

    def delet_pet(self, pet_uuid:str)-> None:
        self.__pet_repository.delete_pet(pet_uuid)