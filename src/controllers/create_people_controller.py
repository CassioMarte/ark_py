import re
from src.models.repositories.interfaces.people_repository_interface import PeopleRepositoryInterface

class CreatePeapleController:
    def __init__(self, people_repository:PeopleRepositoryInterface)->None:
        self.__people_repository = people_repository
    

    def create(self, person_info:dict)-> dict:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age= person_info["age"]
        pet_uuid = person_info["pet_uuid"]
    
    def __validate_data(self, first_name:str, last_name:str, age:int)-> None:
        not_valid_str = re.compile(r'[^a-zA-Z]')
        
        if not_valid_str.search(first_name):
            raise Exception("Nome inválido") 
        
        if not_valid_str.search(last_name):
            raise Exception("Sobrenome inválido")
        
       
        

# if not isinstance(age, int) or age <= 0:
#     raise Exception("Idade inválida")