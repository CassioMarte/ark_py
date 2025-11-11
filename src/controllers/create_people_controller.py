import re
from src.models.repositories.interfaces.people_repository_interface import PeopleRepositoryInterface
from src.utils.format_return import format_return
from src.controllers.interfaces.create_people_controller_interface import CreatePeopleControllerInterface


class CreatePeopleController(CreatePeopleControllerInterface): 
    def __init__(self, people_repository:PeopleRepositoryInterface)->None:
        self.__people_repository = people_repository
    

    def create(self, person_info:dict)-> dict:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age= person_info["age"]
        pet_uuid = person_info["pet_uuid"]

        self.__validate_data(first_name, last_name, age)

        self.__insert_people_in_db(first_name, last_name, age, pet_uuid)

        formated_response = self.__format_response(person_info)

        return formated_response
    
    def __validate_data(self, first_name:str, last_name:str, age:int)-> None:
        not_valid_str = re.compile(r'[^a-zA-Z]')
        
        if not_valid_str.search(first_name):
            raise Exception("Nome inválido") 
        
        if not_valid_str.search(last_name):
            raise Exception("Sobrenome inválido") 
        
        if not isinstance(age, int) or age <= 0:
            raise Exception("Idade inválida")
        
    def __insert_people_in_db(self, first_name:str, last_name:str, age:int , pet_uuid:str)-> None:
        self.__people_repository.create_people(first_name, last_name, age, pet_uuid)

    def __format_response(self, person_info: dict) -> dict:
        return format_return(type_route="post", type="Person", attributes=person_info)
        
       
        

