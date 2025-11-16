from src.controllers.interfaces.create_people_controller_interface import CreatePeopleControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.validators.person_creator_validator import person_creator_validator
from src.views.http_types.http_response import HttpResponse
from .interface.view_interface import ViewInterface

class CreatePeopleView(ViewInterface):
    def __init__(self, create_people_controller: CreatePeopleControllerInterface) -> None:
        self.__create_people_controller = create_people_controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_creator_validator(http_request)
        person_info = http_request.body
        create_person = self.__create_people_controller.create(person_info)

        return HttpResponse(status_code=201, body=create_person)