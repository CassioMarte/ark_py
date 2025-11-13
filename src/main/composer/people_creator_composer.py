from src.models.settings.sqlite.connection import db_connection_handler
from src.models.repositories.people_repositories import PeopleRepository
from src.controllers.create_people_controller import CreatePeopleController
from src.views.create_people_view import CreatePeopleView


def people_creator_compose():
    model = PeopleRepository(db_connection_handler)
    controller= CreatePeopleController(model)
    view= CreatePeopleView(controller)

    return view