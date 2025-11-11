from typing import cast
from src.models.repositories.interfaces.pets_repositories_interface import PetsRepositoriesInterface
from .pets_lister_controller import PetListerController
from src.models.entities.pets_table import PetsTable


class MockPet:
    def __init__(self, uuid, name, type):
        self.uuid = uuid
        self.name = name
        self.type = type


class MockPetsRepository:
    def list_pets(self):
        return [
            MockPet("123e4567-e89b-12d3-a456-426614174000", "Buddy", "Dog"),
            MockPet("123e4567-e89b-12d3-a456-426614174001", "Snaky", "Snake"),
            MockPet("123e4567-e89b-12d3-a456-426614174002", "Fishy", "Fish"),
        ]


def test_list_pets():
    mock = MockPetsRepository()

    controller = PetListerController(cast(PetsRepositoriesInterface, mock))

    response = controller.list_pets()

    print(response)

class MockPetsRepositoryWithTableEntities:
    def list_pets(self):
        return [
            PetsTable(uuid="123e4567-e89b-12d3-a456-426614174000", name="Buddy", type="Dog"),
            PetsTable(uuid="123e4567-e89b-12d3-a456-426614174001", name="Snaky", type="Snake"),
        ]


def test_list_pets_with_table_entities():
    mock = MockPetsRepositoryWithTableEntities()

    controller = PetListerController(cast(PetsRepositoriesInterface, mock))

    response = controller.list_pets()

    assert response == {
        "data": {
            "typeRoute": "get",
            "type": "Pets",
            "count": 2,
            "attributes": [
                {"uuid": "123e4567-e89b-12d3-a456-426614174000", "name": "Buddy", "type": "Dog"},
                {"uuid": "123e4567-e89b-12d3-a456-426614174001", "name": "Snaky", "type": "Snake"},
            ]
        }
    }