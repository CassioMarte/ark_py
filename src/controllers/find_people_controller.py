from src.models.repositories.interfaces.people_repository_interface import PeopleRepositoryInterface
from src.utils.format_return import format_return

class FindPeopleController:
    def __init__(self, people_repository:PeopleRepositoryInterface)->None:
        self.__people_repository = people_repository

    def find(self, person_uuid:str)-> dict:
        person_data = self.__find_person_in_db(person_uuid)
        response = self.__format_response(person_data)
        return response

    def  __find_person_in_db(self, person_uuid:str):
        person = self.__people_repository.get_person_and_pet(person_uuid)

        if not person:
            raise Exception("Person not found")
    
        return person

    def __format_response(self, person)-> dict:
        return format_return(type_route="post", type="Person", attributes={
                    "first_name": person.first_name,
                    "last_name": person.last_name,
                    "pet_name": person.pet_name,
                    "pet_type": person.pet_type
                })