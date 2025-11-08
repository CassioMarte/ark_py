from typing import cast
import pytest
from src.models.repositories.people_repositories import PeopleRepository
from .create_people_controller import CreatePeopleController

class MockPeopleRepository:
    def create_people(self, first_name:str, last_name:str, age:int , pet_uuid:str)-> None:
        pass

def test_create_people_controller():
    mock = MockPeopleRepository()

    controller = CreatePeopleController(cast(PeopleRepository, mock))

    person_info = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "pet_uuid": "123e4567-e89b-12d3-a456-426614174000"
    }

    response = controller.create(person_info)

    expected_response = {
        "data": {
            "typeRoute": "post",
            "type": "Person",
            "count": 1,
            "attributes": person_info
        }
    }

    assert response["data"]["typeRoute"] == expected_response["data"]["typeRoute"]
    assert response["data"]["type"] == expected_response["data"]["type"]
    assert response["data"]["count"] == expected_response["data"]["count"]
    assert response["data"]["attributes"] == expected_response["data"]["attributes"]

    ''''
    Ou 
       assert response["data"]["type"] = "Person"
       aessert response["data"]["count"] = 1
       assert response["data"]["attributes"] = person_info
    '''


def test_create_name_error():
    mock = MockPeopleRepository()

    controller = CreatePeopleController(cast(PeopleRepository, mock))

    person_info = {
        "first_name": "John123",
        "last_name": "Doe",
        "age": 30,
        "pet_uuid": "123e4567-e89b-12d3-a456-426614174000"
    }

    with pytest.raises(Exception, match="Nome inválido"):
        controller.create(person_info)

def test_create_age_error( ):
    mock = MockPeopleRepository()

    controller = CreatePeopleController(cast(PeopleRepository, mock))

    person_info = {
        "first_name": "AgeError",
        "last_name": "Doe",
        "age": "5",
        "pet_uuid": "123e4567-e89b-12d3-a456-426614174000"
    }

    with pytest.raises(Exception, match="Idade inválida"):
        controller.create(person_info)
