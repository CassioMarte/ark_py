from src.models.settings.sqlite.connection import db_connection_handler
from src.models.repositories.pets_repositories import PetRepositories
from src.controllers.pets_delet_controller import PetDeletController
from src.views.pets_delet_view import PetsDeleteView
def pets_delet_composer():
    model =  PetRepositories( db_connection_handler)
    controller = PetDeletController(model)
    view = PetsDeleteView(controller)

    return view