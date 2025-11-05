import pytest
from src.models.settings.sqlite.connection import db_connection_handler
from .people_repositories import PeopleRepository

db_connection_handler.connection_to_db()

@pytest.mark.skip(reason="Teste de criação de pessoa")
def test_create_people():
    first_name='first_name'
    last_name='last_name'
    age=1
    pet_uuid='550e8400-e29b-41d4-a716-446655440001'

    repo = PeopleRepository(db_connection_handler)

    repo.create_people(first_name, last_name, age, pet_uuid)

@pytest.mark.skip(reason="Teste busca de person com pet ")    
def test_get_person_and_pet():
    person_uuid= "030d4d23-422c-4f21-b140-84595ae5ccd4"

    repo = PeopleRepository(db_connection_handler)

    res = repo.get_person_and_pet(person_uuid)

    print("#######")
    print(res)
    print("#######")
