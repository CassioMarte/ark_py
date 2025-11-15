from src.models.settings.sqlite.connection import db_connection_handler
from src.models.repositories.pets_repositories import PetRepositories
from src.controllers.pets_lister_controller import PetListerController
from src.views.pets_lister_view import PetsListerView
def pets_lister_composer():
    model =  PetRepositories( db_connection_handler)
    controller = PetListerController(model)
    view =PetsListerView(controller)

    return view