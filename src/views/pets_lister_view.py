from .interface.view_interface import ViewInterface
from src.controllers.interfaces.pets_lister_controller_interface import PetListerControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class PetsListerView(ViewInterface):
    def __init__(self, pets_lister_controller: PetListerControllerInterface )-> None:
        self.__pets_lister_controller = pets_lister_controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pets = self.__pets_lister_controller.list_pets()

        return HttpResponse(status_code=200, body=pets)