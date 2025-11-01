from unittest import mock
from typing import cast
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.entities.pets_table import PetsTable
from .pets_repositories import PetRepositories
from src.models.settings.sqlite.connection import DBConnectionHandler

class MockConnection:
    def __init__(self)->None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)], #query
                    [
                        PetsTable(name="dog_mock", type="dog"),
                        PetsTable(name="cat_mock", type="cat"),
                    ],  # resultado
                )
            ]
        )

    def __enter__(self): 
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def test_unitario_list():
    pass


def test_uni_list_pets():
    db_connection_mock = MockConnection()

    # repo = PetRepositories(db_connection_mock) -> assim aparece erro de tipagem da erro de pyLint
    repo = PetRepositories(cast(DBConnectionHandler, db_connection_mock))

    response = repo.list_pets()

    assert response[0].name == "dog_mock"


