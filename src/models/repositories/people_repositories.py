from sqlalchemy.exc import NoResultFound
from src.models.settings.sqlite.connection import DBConnectionHandler
from src.models.entities.people_table import PeopleTable
from .interfaces.people_repository_interface import PeopleRepositoryInterface

class PeopleRepository(PeopleRepositoryInterface):
    def __init__(self, db_connection:DBConnectionHandler)-> None:
        self.__db_connection = db_connection

    def list_people(self)-> list:
        with self.__db_connection as database:
            try:
                people = database.session.query(PeopleTable).all()
                return people   
            except NoResultFound:
                return []
    
    def delete_people(self, uuid:str)-> None:
        with self.__db_connection as database:
            try:
                (
                    database.session
                    .query(PeopleTable)
                    .filter(PeopleTable.uuid == uuid)
                    .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def create_people(self, first_name:str, last_name:str, age: int, pet_uuid:str)-> None:
        with self.__db_connection as database:
            try:
               people_data = PeopleTable(
                    first_name=first_name,
                    last_name=last_name,
                    age=age,
                    pet_uuid=pet_uuid
                )
               database.session.add(people_data)
               database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
