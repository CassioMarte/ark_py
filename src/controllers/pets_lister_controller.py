from src.models.repositories.interfaces.pets_repositories_interface import PetsRepositoriesInterface
from src.models.entities.pets_table import PetsTable
from src.utils.format_return import format_return
from src.controllers.interfaces.pets_lister_controller_interface import PetListerControllerInterface


class PetListerController(PetListerControllerInterface):
    def __init__(self, pets_repository:PetsRepositoriesInterface):
        self.__pets_repository = pets_repository
    
    def list_pets(self)-> dict:
        pets = self.__get_list_of_pets()
        response = self.__format_response(pets)
        return response
    
    def __get_list_of_pets(self)-> list[PetsTable]:
        pets = self.__pets_repository.list_pets()
        return pets
   
    def __format_response(self, pets:list[PetsTable])-> dict:
        pets_res = []

        for pet in pets:
            pets_res.append({
                "uuid": pet.uuid,
                "name": pet.name,   
                "type": pet.type  
            })

        return format_return(type_route="get", type="Pets", count=len(pets), attributes=pets_res)