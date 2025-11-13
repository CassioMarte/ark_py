from src.models.settings.sqlite.connection import db_connection_handler
from src.models.repositories.people_repositories import PeopleRepository
from src.controllers.find_people_controller import FindPeopleController
from src.views.find_people_view import FindPeopleView



def find_people_composer():
    model = PeopleRepository(db_connection_handler)
    controller = FindPeopleController(model)
    view = FindPeopleView(controller)

    return view