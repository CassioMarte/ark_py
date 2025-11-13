from .interface.view_interface import ViewInterface
from src.controllers.interfaces.find_people_controller_interface import FindPeopleControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class FindPeopleView(ViewInterface):
    def __init__(self, find_people_controller: FindPeopleControllerInterface) -> None:
        self.__find_people_controller = find_people_controller
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_uuid = http_request.param["person_uuid"]
        person_data = self.__find_people_controller.find(person_uuid)

        return HttpResponse(status_code=200, body=person_data)