from unittest import mock
from typing import cast
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.exc import NoResultFound
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

    # verificar se PetsTable foi chamado uma vez
    db_connection_mock.session.query.assert_called_once_with(PetsTable)

    # ver se all foi chamado  pets = database.session.query(PetsTable).all
    db_connection_mock.session.all.assert_called_once()

    # ver se não foi chamado o filter assert_not_called assert não ligou
    db_connection_mock.session.filter.assert_not_called()

    assert response[0].name == "dog_mock"

def test_ini_delet_pets():
    db_connection_mock = MockConnection()

    repo = PetRepositories(cast(DBConnectionHandler, db_connection_mock))

    repo.delete_pet("uuid-string")

    db_connection_mock.session.query.assert_called_once_with(PetsTable)

    db_connection_mock.session.filter.assert_called_once_with( PetsTable.uuid == "uuid-string")

    db_connection_mock.session.delete.assert_called_once()



## só para fim de estudo vou colocar class de erro aqui 

class MockConnectionNoResult:
    def __init__(self)-> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")
    
    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb): pass
