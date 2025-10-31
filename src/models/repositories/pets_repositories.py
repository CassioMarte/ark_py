from sqlalchemy.exc import NoResultFound
from src.models.repositories.interfaces.pets_repositories_interface import PetsRepositoriesInterface
from src.models.settings.sqlite.connection import DBConnectionHandler
from src.models.entities.pets_table import PetsTable

class PetRepositories(PetsRepositoriesInterface):   # pylint: disable=too-few-public-methods
    def __init__(self, db_connection: DBConnectionHandler)-> None:
        self.__db_connection = db_connection

    def list_pets(self)->list:
        with self.__db_connection as database:
            try:
                pets = database.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []
            
