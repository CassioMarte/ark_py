from src.models.settings.sqlite.connection import db_connection_handler
from .people_repositories import PeopleRepository

db_connection_handler.connection_to_db()

def test_create_people():
    first_name='first_name'
    last_name='last_name'
    age=1
    pet_uuid='550e8400-e29b-41d4-a716-446655440001'

    repo = PeopleRepository(db_connection_handler)

    repo.create_people(first_name, last_name, age, pet_uuid)


