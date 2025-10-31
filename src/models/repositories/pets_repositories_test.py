from src.models.settings.sqlite.connection import db_connection_handler
from .pets_repositories import PetRepositories


db_connection_handler.connection_to_db()
def test_list_pets():
    repo = PetRepositories(db_connection_handler)
    pets = repo.list_pets()

    for pet in pets:
        print({
            "id": pet.id,
            "name": pet.name
        })
    assert len(pets) > 0  # Verifica se a lista de pets não
