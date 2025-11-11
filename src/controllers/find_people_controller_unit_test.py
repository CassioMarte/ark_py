from typing import cast
from unittest.mock import MagicMock
from src.models.repositories.people_repositories import PeopleRepository
from .find_people_controller import FindPeopleController

'''
Teste unitário para o FindPeopleController usando um mock simples, MagicMock

Aqui vamos ter vairias abordagens para criar mocks e testar o controller.
'''

class MockPeopleRepository:
    personData = [
        {
            "uuid": "valid-uuid",
            "first_name": "Jane",
            "last_name": "Doe",
            "age": 28,
            "pet_uuid": "pet-uuid-123",
            "pet_name": "Buddy",
            "pet_type": "Dog"
        }, 
        {
            "uuid": "another-uuid",
            "first_name": "Alice",
            "last_name": "Smith",
            "age": 34,
            "pet_uuid": "pet-uuid-456",
            "pet_name": "Whiskers",
            "pet_type": "Cat"
        }
    ]
    def get_person_and_pet(self, person_uuid: str):
        for person in self.personData:
            if person["uuid"] == person_uuid:
                return type('Person', (object,), person)()
        return None

def test_find_people_controller():
    mock = MockPeopleRepository()

    controller = FindPeopleController(cast(PeopleRepository, mock))

    response =  controller.find("valid-uuid")

    assert response["data"]["typeRoute"] == "post"
    assert response["data"]["type"] == "Person"
    assert response["data"]["attributes"] == {
        "first_name": "Jane",
        "last_name": "Doe",
        "pet_name": "Buddy",
        "pet_type": "Dog"
    }


# 🔹 Mock simples que simula o retorno de uma pessoa com seu pet
class MockPerson:
    def __init__(self, first_name, last_name, pet_name, pet_type):
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.pet_type = pet_type

def test_find_people_controller_with_magic_mock():
    # Cria um mock do repositório
    repo = MagicMock()
    
    # Define o retorno do método que o controller vai chamar
    repo.get_person_and_pet.return_value = MockPerson(
        "Jane", "Doe", "Buddy", "Dog"
    )

    # Injeta o mock no controller
    controller = FindPeopleController(repo)

    # Executa o método que queremos testar
    response = controller.find("valid-uuid")

    # Faz asserções (verificações)
    assert response["data"]["attributes"]["pet_name"] == "Buddy"
    assert response["data"]["attributes"]["first_name"] == "Jane"
    assert response["data"]["type"] == "Person"
